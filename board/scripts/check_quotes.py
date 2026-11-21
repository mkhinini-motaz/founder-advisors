#!/usr/bin/env python3
"""Check that every quote is verbatim (replaces roast-room's check_quotes scripts).

  python3 -I check_quotes.py --corpus <build> FILE_OR_DIR...   a quote must be in the source it cites (S012)
  python3 -I check_quotes.py --brain <brain dir> FILE...       a quote must be somewhere in that brain
  python3 -I check_quotes.py --selftest

A quote is text in straight or curly double quotes or « guillemets », 20 to 400 characters, on one line. Its source id is the
nearest S### after it on the same line (or before it). "..." and [inserted words] split a quote into parts;
each part of three words or more must match. Exit 1 when a quote is missing or cites the wrong source.
"""
import pathlib, re, sys, unicodedata

# Match every quote, short ones too, so a short quote cannot pair its closing mark with the next opening one
# (16 Nov 2026: "Supply side is 👑." made the text between two quotes read as a quote). Short ones are skipped below.
QUOTE = re.compile(r"[\"“«]([^\"“”«»\n]{1,400})[\"”»]")
SID = re.compile(r"\bS\d{3}\b")


# Arabic short vowels, tatweel and Quranic marks: captions and notes write them inconsistently.
AR_MARKS = re.compile(r"[\u0610-\u061a\u064b-\u065f\u0670\u0640\u06d6-\u06ed]")


def norm(s):
    # Letters of every script count (Arabic, accented French), so non-Latin quotes are checked too.
    s = unicodedata.normalize("NFKC", s).casefold().replace("’", "'").replace("‘", "'")
    return re.sub(r"\s+", " ", re.sub(r"[^\w']+|_", " ", AR_MARKS.sub("", s))).strip()


def parts(q):
    return [n for n in (norm(p) for p in re.split(r"\.\.\.|…|\[[^\]]*\]", q)) if len(n.split()) >= 3]


def quotes(text):
    for line in text.splitlines():
        for m in QUOTE.finditer(line):
            if len(m.group(1)) < 20:
                continue
            after = SID.search(line, m.end(), m.end() + 80)
            before = [x for x in SID.finditer(line, max(0, m.start() - 80), m.start())]
            sid = after.group() if after else (before[-1].group() if before else None)
            yield m.group(1), sid


def files(targets):
    for t in map(pathlib.Path, targets):
        yield from (sorted(t.rglob("*.md")) if t.is_dir() else [t])


def found(q, hay):
    ps = parts(q)
    return bool(ps) and all(p in hay for p in ps)


def check(targets, by_id=None, everything=""):
    bad = n = 0
    for f in files(targets):
        for q, sid in quotes(f.read_text(errors="replace")):
            if not parts(q):
                continue
            n += 1
            if by_id is not None:
                if sid and sid in by_id and found(q, by_id[sid]):
                    continue
                other = next((k for k, v in by_id.items() if found(q, v)), None)
                why = f"wrong id {sid}, found in {other}" if other else f"missing (cites {sid})"
            else:
                if found(q, everything):
                    continue
                why = "not in brain"
            bad += 1
            print(f"{f.name}: {why}: \"{q[:90]}\"")
    print(f"{n} quotes checked, {bad} bad")
    return bad


def corpus(build):
    return {f.name[:4]: norm(f.read_text(errors="replace")) for f in (pathlib.Path(build).expanduser() / "corpus").glob("S[0-9][0-9][0-9]-*.md")}


def selftest():
    by_id = {"S001": norm("He said: the best code is no code at all, and he meant it."), "S002": norm("Cash is king.")}
    assert check_text('"the best code is no code at all" (S001)', by_id) == 0
    assert check_text('"the best code ... at all, and he meant it" (S001)', by_id) == 0
    assert check_text('"the best code is no code at all" (S002)', by_id) == 1
    assert check_text('"the best code is some code at all" (S001)', by_id) == 1
    assert norm("It’s first-principles!") == "it's first principles"
    # Arabic and accented French are checked, not stripped (16 Nov 2026: Arabic quotes had been skipped).
    assert norm("الكاش هو الملك") == "الكاش هو الملك" and norm("كَاشٌ") == "كاش"
    assert check_text('"نبدأ من الصفر في كل بلد عربي" (S001)', {"S001": norm("قال: نبدأ من الصفر في كل بلد عربي.")}) == 0
    assert check_text('« le cash reste roi au Maghreb » (S001)', {"S001": norm("Pour lui, le cash reste roi au Maghreb.")}) == 0
    assert check_text('« le cash reste roi en Europe » (S001)', {"S001": norm("Le cash reste roi au Maghreb.")}) == 1
    print("selftest ok")


def check_text(text, by_id):
    import tempfile
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as t:
        t.write(text)
    return check([t.name], by_id)


if __name__ == "__main__":
    a = sys.argv[1:]
    if a == ["--selftest"]:
        selftest()
    elif len(a) >= 3 and a[0] == "--corpus":
        sys.exit(1 if check(a[2:], by_id=corpus(a[1])) else 0)
    elif len(a) >= 3 and a[0] == "--brain":
        sys.exit(1 if check(a[2:], everything=" ".join(norm(f.read_text()) for f in files([a[1]]))) else 0)
    else:
        sys.exit(__doc__)
