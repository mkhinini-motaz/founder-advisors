#!/usr/bin/env python3
"""Fetch a persona's public sources into <build>/corpus/ (replaces roast-room's fetch.mjs).

  python3 -I fetch.py <build> --list urls.txt      fetch every URL not yet in sources.json
  python3 -I fetch.py <build> --add FILE --title T [--date YYYY-MM-DD] [--url U]
  python3 -I fetch.py <build> --manifest           counts, words, years
  python3 -I fetch.py <build> --drop S007 S012     exclude sources (wrong person, duplicate, mostly the host)
  python3 -I fetch.py <build> --batches [WORDS]    write batches.json (default 50000 words a batch)
  python3 -I fetch.py <build> --sources-md OUT --name "Full Name"
  python3 -I fetch.py --selftest

Pages are untrusted data: run with -I, from outside <build>. YouTube needs yt-dlp, PDFs pdftotext.
"""
import html, json, pathlib, re, subprocess, sys, tempfile
from html.parser import HTMLParser

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
SKIP = {"script", "style", "noscript", "svg", "nav", "header", "footer", "aside", "form", "button", "iframe", "template"}
BLOCK = {"p", "div", "br", "li", "h1", "h2", "h3", "h4", "h5", "h6", "tr", "section", "article", "blockquote", "pre", "dd", "dt", "figcaption"}
THIN = 400  # words; below this a page is a paywall, a JavaScript shell or a summary


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.skip = self.scope = 0
        self.in_title = False
        self.title, self.meta, self.all, self.scoped = "", {}, [], []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in SKIP:
            self.skip += 1
        elif tag == "title":
            self.in_title = True
        elif tag == "meta":
            k = (a.get("property") or a.get("name") or "").lower()
            if k and a.get("content"):
                self.meta.setdefault(k, a["content"])
        elif tag == "time" and a.get("datetime"):
            self.meta.setdefault("time", a["datetime"])
        if tag in ("article", "main"):
            self.scope += 1
        if tag in BLOCK:
            self.add("\n")

    def handle_endtag(self, tag):
        if tag in SKIP and self.skip:
            self.skip -= 1
        elif tag == "title":
            self.in_title = False
        if tag in ("article", "main") and self.scope:
            self.scope -= 1
        if tag in BLOCK:
            self.add("\n")

    def handle_data(self, d):
        if self.in_title:
            self.title += d
        elif not self.skip:
            self.add(d)

    def add(self, s):
        self.all.append(s)
        if self.scope:
            self.scoped.append(s)


def tidy(parts):
    lines = [re.sub(r"\s+", " ", l).strip() for l in "".join(parts).splitlines()]
    return "\n\n".join(l for l in lines if l)


def html_text(raw):
    p = Page()
    p.feed(raw)
    body = tidy(p.scoped)
    if len(body.split()) < 300:
        body = tidy(p.all)
    title = p.meta.get("og:title") or p.title.strip()
    date = (p.meta.get("article:published_time") or p.meta.get("date") or p.meta.get("time") or "")[:10]
    return title, date, body


def vtt_text(raw):
    out, recent = [], []
    for line in raw.splitlines():
        line = line.strip()
        if not line or line.startswith(("WEBVTT", "Kind:", "Language:", "NOTE", "STYLE")) or "-->" in line or line.isdigit():
            continue
        line = html.unescape(re.sub(r"<[^>]+>", "", line)).strip()
        if line and line not in recent:  # auto-captions repeat each line in the next cue
            out.append(line)
            recent = (recent + [line])[-3:]
    words = " ".join(out).split()
    return "\n\n".join(" ".join(words[i:i + 80]) for i in range(0, len(words), 80))


def run(cmd, timeout=300):
    return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)


def youtube(url, tmp):
    r = run(["yt-dlp", "--skip-download", "--write-subs", "--write-auto-subs", "--sub-langs", ",".join(LANGS + ["en-US", "en-GB", "en-orig"]),
             "--sub-format", "vtt", "--no-playlist", "--print-json", "-o", f"{tmp}/v.%(ext)s", url])
    meta = json.loads(r.stdout.strip().splitlines()[-1]) if r.stdout.strip() else {}
    orig = (meta.get("language") or "en").split("-")[0]  # the talk's own language first: a machine-translated track is not a source for quotes
    vtts = sorted(pathlib.Path(tmp).glob("v*.vtt"), key=lambda p: (not p.name.endswith((f".{orig}-orig.vtt", f".{orig}.vtt")), not p.name.endswith(f".{LANGS[0]}.vtt"), p.name))
    if not vtts:
        raise RuntimeError("YouTube refused captions (put an Apify token in ~/.apify_token)" + (": " + r.stderr.strip().splitlines()[-1] if r.stderr.strip() else ""))
    d = meta.get("upload_date", "")
    note = f"channel: {meta.get('channel', '')}; duration: {int(meta.get('duration') or 0) // 60} min"
    return meta.get("title", url), f"{d[:4]}-{d[4:6]}-{d[6:]}" if len(d) == 8 else "", vtt_text(vtts[0].read_text(errors="replace")), note


TOKEN = pathlib.Path.home() / ".apify_token"
ACTOR = "johnvc~YoutubeTranscripts"  # about $0.0055 a video with upload date; captions only
LANGS = __import__("os").environ.get("FETCH_LANGS", "en").split(",")  # e.g. FETCH_LANGS=fr,ar,en for a French speaker


def apify_youtube(urls):
    """YouTube often refuses captions to scripts without a PO token, so transcripts come through Apify."""
    import urllib.request
    out = {}
    for i in range(0, len(urls), 100):  # the actor takes 100 URLs a run
        req = urllib.request.Request(
            f"https://api.apify.com/v2/acts/{ACTOR}/run-sync-get-dataset-items?clean=true&maxTotalChargeUsd=1",
            data=json.dumps({"youtube_url": urls[i:i + 100], "languages": LANGS, "include_metadata": True, "include_extended_metadata": True}).encode(),
            headers={"Authorization": "Bearer " + TOKEN.read_text().strip(), "Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=600) as r:
            for item in json.loads(r.read()):
                out[item.get("url") or item.get("video_id")] = item
    return out


def youtube_id(url):
    m = re.search(r"(?:v=|youtu\.be/|/live/|/shorts/)([\w-]{11})", url)
    return m.group(1) if m else url


def web(url, tmp):
    f = pathlib.Path(tmp) / "page"
    r = run(["curl", "-sSL", "--max-time", "60", "--max-filesize", "30000000", "-A", UA, "-o", str(f), "-w", "%{content_type}", url], 90)
    if r.returncode or not f.exists():
        raise RuntimeError(r.stderr.strip() or f"curl exit {r.returncode}")
    if "pdf" in r.stdout or url.lower().split("?")[0].endswith(".pdf") or f.read_bytes()[:5] == b"%PDF-":
        t = run(["pdftotext", "-q", str(f), "-"])
        return pathlib.Path(url.split("?")[0]).name, "", tidy([t.stdout]), "pdf"
    title, date, body = html_text(f.read_bytes().decode("utf-8", errors="replace"))
    return title or url, date, body, ""


def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:60] or "source"


class Build:
    def __init__(self, path):
        self.dir = pathlib.Path(path).expanduser()
        self.corpus = self.dir / "corpus"
        self.corpus.mkdir(parents=True, exist_ok=True)
        self.log = self.dir / "sources.json"
        self.sources = json.loads(self.log.read_text()) if self.log.exists() else []

    def next_id(self):
        return f"S{max([int(s['id'][1:]) for s in self.sources] or [0]) + 1:03d}"

    def save(self, url, title, date, text, note=""):
        sid = self.next_id()
        words = len(text.split())
        status = "ok" if words >= THIN else "thin"
        name = f"{sid}-{slugify(title)}.md"
        (self.corpus / name).write_text(f"# {title}\n\nurl: {url}\ndate: {date}\n{note}\n\n{text}\n")
        self.sources.append({"id": sid, "title": title, "url": url, "date": date, "file": name, "words": words, "status": status})
        self.log.write_text(json.dumps(self.sources, indent=1, ensure_ascii=False))
        return sid, status, words

    def fail(self, url, why):
        self.sources.append({"id": self.next_id(), "title": "", "url": url, "date": "", "file": "", "words": 0, "status": "fail", "why": why[:200]})
        self.log.write_text(json.dumps(self.sources, indent=1, ensure_ascii=False))

    def fetch_list(self, listfile):
        seen = {s["url"] for s in self.sources if s["status"] != "fail"}  # failures may be retried
        urls = [u for u in dict.fromkeys(l.strip() for l in pathlib.Path(listfile).read_text().splitlines()) if u and not u.startswith("#")]
        for u in urls:
            if u in seen:
                print("skip", u)
        urls = [u for u in urls if u not in seen]
        self.sources = [s for s in self.sources if not (s["status"] == "fail" and s["url"] in urls)]
        yt = [u for u in urls if re.search(r"(youtube\.com/(watch|live|shorts)|youtu\.be/)", u)]
        if yt and TOKEN.exists():
            try:
                got = {youtube_id(k): v for k, v in apify_youtube(yt).items()}
            except Exception as e:
                got = {}
                print("apify failed:", str(e)[:200])
            for u in yt:
                item = got.get(youtube_id(u))
                text = (item or {}).get("non_timestamped") or ""
                if not item or not item.get("success", True) or not text:
                    self.fail(u, "no English captions via Apify")
                    print("fail", u, "no captions")
                    continue
                words = text.split()
                text = "\n\n".join(" ".join(words[i:i + 80]) for i in range(0, len(words), 80))
                note = f"channel: {item.get('channel_name', '')}; duration: {int(item.get('video_duration_seconds') or 0) // 60} min"
                d = re.sub(r"\D", "", str(item.get("upload_date") or ""))[:8]
                sid, status, n = self.save(u, item.get("title") or u, f"{d[:4]}-{d[4:6]}-{d[6:]}" if len(d) == 8 else "", text, note)
                print(status, sid, n, "words", (item.get("title") or "")[:70])
            urls = [u for u in urls if u not in yt]
        for url in urls:
            with tempfile.TemporaryDirectory() as tmp:
                try:
                    is_yt = url in yt
                    title, date, text, note = (youtube if is_yt else web)(url, tmp)
                    sid, status, words = self.save(url, title, date, text, note)
                    print(status, sid, words, "words", title[:70])
                except Exception as e:
                    self.fail(url, str(e))
                    print("fail", url, str(e)[:120])
        self.manifest()

    def ok(self):
        return [s for s in self.sources if s["status"] == "ok"]

    def manifest(self):
        ok = self.ok()
        years = sorted(s["date"][:4] for s in ok if s["date"][:4].isdigit())
        print(f"manifest: {len(ok)} ok, {sum(s['words'] for s in ok)} words, "
              f"{sum(s['status'] == 'thin' for s in self.sources)} thin, {sum(s['status'] == 'fail' for s in self.sources)} fail, "
              f"years {years[0] + '-' + years[-1] if years else 'unknown'}")

    def batches(self, size=50000):
        out, cur = [], []
        for s in self.ok():
            if cur and sum(x["words"] for x in cur) + s["words"] > size:
                out.append(cur)
                cur = []
            cur.append(s)
        if cur:
            out.append(cur)
        data = [{"batch": f"{i + 1:02d}", "ids": [s["id"] for s in b], "files": [str(self.corpus / s["file"]) for s in b],
                 "words": sum(s["words"] for s in b)} for i, b in enumerate(out)]
        (self.dir / "batches.json").write_text(json.dumps(data, indent=1))
        for b in data:
            print(b["batch"], len(b["ids"]), "sources", b["words"], "words")

    def sources_md(self, out, name):
        ok = self.ok()
        rows = "\n".join(f"| {s['id']} | {s['title'].replace('|', '/')} | {s['url']} | {s['date']} | {s['file']} |" for s in ok)
        pathlib.Path(out).write_text(f"# Sources: {name}\n\n{len(ok)} sources, {sum(s['words'] for s in ok):,} words. "
                                     f"Raw text lives in `build/{self.dir.name}/corpus/` (gitignored).\n\n"
                                     f"| id | title | url | date | file |\n|---|---|---|---|---|\n{rows}\n")


def selftest():
    t, d, b = html_text('<html><head><title>T</title><meta property="article:published_time" content="2021-05-04T00:00"></head>'
                        '<body><nav>menu</nav><article><p>' + "word " * 320 + '</p><script>x()</script></article><footer>f</footer></body></html>')
    assert t == "T" and d == "2021-05-04" and "menu" not in b and "x()" not in b and len(b.split()) == 320
    v = vtt_text("WEBVTT\nKind: captions\n\n00:00.000 --> 00:01.000\nhello <c>there</c>\n\n00:01.000 --> 00:02.000\nhello there\nnew line\n")
    assert v == "hello there new line", v
    print("selftest ok")


if __name__ == "__main__":
    a = sys.argv[1:]
    if a == ["--selftest"]:
        selftest()
        sys.exit()
    if len(a) < 2:
        sys.exit(__doc__)
    b, flag = Build(a[0]), a[1]
    opt = lambda k, default="": a[a.index(k) + 1] if k in a else default
    if flag == "--list":
        b.fetch_list(a[2])
    elif flag == "--add":
        src = pathlib.Path(a[2])
        text = src.read_text(errors="replace")
        print(*b.save(opt("--url", f"local:{src.name}"), opt("--title", src.stem), opt("--date"), text))
        b.manifest()
    elif flag == "--drop":  # a source that is not by this person, or a duplicate
        for s in b.sources:
            if s["id"] in a[2:]:
                s["status"] = "dropped"
        b.log.write_text(json.dumps(b.sources, indent=1, ensure_ascii=False))
        b.manifest()
    elif flag == "--manifest":
        b.manifest()
    elif flag == "--batches":
        b.batches(int(a[2]) if len(a) > 2 else 50000)
    elif flag == "--sources-md":
        b.sources_md(a[2], opt("--name", b.dir.name))
    else:
        sys.exit(__doc__)
