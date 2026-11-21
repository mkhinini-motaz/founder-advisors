#!/usr/bin/env python3
"""Register a built seat in the board roster (replaces roast-room's add_seat.mjs).

  python3 -I seat.py add --key K --name "Full Name" --short S --slug first-last --pillar P --question Q --dimension D
  python3 -I seat.py list
  python3 -I seat.py check    # every sources.md row has a free-to-read URL (no known paid domain); CI runs it

Refuses when any of the seven brain files is missing, when `_hot.md` lacks its "## Instructions" or "## Hot sheet" part, or when the key is taken.
"""
import colorsys, json, pathlib, re, sys, zlib

SEATS = pathlib.Path(__file__).resolve().parent.parent / "plugin" / "board" / "seats"
ROSTER = SEATS / "roster.json"
BRAIN = ["_hot.md", "frameworks.md", "principles.md", "positions.md", "voice.md", "stories.md", "sources.md"]


# Sources must be free to read: no books, excerpts, quote or summary sites, paywalled news or archive copies of them.
PAID = ("goodreads.com books.google.com amazon.com amazon.co.uk audible.com shortform.com blinkist.com getabstract.com supersummary.com brainyquote.com "
        "azquotes.com quotefancy.com web.archive.org archive.org nytimes.com wsj.com ft.com economist.com hbr.org newyorker.com "
        "bloomberg.com businessinsider.com spectator.co.uk spectator.com").split()


def paid(url):
    h = re.sub(r"^https?://([^/]*).*", r"\1", url)
    return any(h == d or h.endswith("." + d) for d in PAID)


def check():
    bad = []
    for f in sorted((SEATS / "brains").glob("*/sources.md")):
        for line in f.read_text().splitlines():
            if line.startswith("| S"):
                m = re.search(r"\| (https?://\S+) \|", line)
                if not m or paid(m.group(1)):
                    bad.append(f"{f.parent.name}: {line.split('|')[1].strip()} {m.group(1) if m else 'no URL'}")
    n = len(json.loads(ROSTER.read_text())["seats"])
    sys.exit("paid or missing source URLs:\n" + "\n".join(bad)) if bad else print(f"ok: {n} seats, every source has a free URL")


def add(o):
    roster = json.loads(ROSTER.read_text())
    if any(s["key"] == o["key"] for s in roster["seats"]):
        sys.exit(f"key {o['key']} already in the roster")
    missing = [str(p) for p in [SEATS / "brains" / o["slug"] / f for f in BRAIN] if not p.exists()]
    if missing:
        sys.exit("missing: " + ", ".join(missing))
    hot = (SEATS / "brains" / o["slug"] / "_hot.md").read_text()
    if "\n## Instructions\n" not in hot or "\n## Hot sheet\n" not in hot:
        sys.exit('_hot.md needs a "## Instructions" part (the old council file) and a "## Hot sheet" part')
    r, g, b = colorsys.hls_to_rgb((zlib.crc32(o["key"].encode()) % 360) / 360, 0.55, 0.6)
    roster["seats"].append({"key": o["key"], "name": o["name"], "short": o["short"],
                            "initials": (o["name"].split()[0][0] + o["name"].split()[-1][0]).upper(),
                            "slug": o["slug"], "pillar": o["pillar"], "question": o["question"], "dimension": o["dimension"],
                            "color": "#%02x%02x%02x" % (int(r * 255), int(g * 255), int(b * 255))})
    ROSTER.write_text(json.dumps(roster, indent=2, ensure_ascii=False) + "\n")
    print("added", o["key"], "-", len(roster["seats"]), "seats")


if __name__ == "__main__":
    a = sys.argv[1:]
    if a[:1] == ["list"]:
        for s in json.loads(ROSTER.read_text())["seats"]:
            print(f"{s['key']:12} {s['name']:28} {s['pillar']} | {s['question']}")
    elif a[:1] == ["check"]:
        check()
    elif a[:1] == ["add"]:
        o = {a[i][2:]: a[i + 1] for i in range(1, len(a) - 1, 2)}
        need = {"key", "name", "short", "slug", "pillar", "question", "dimension"}
        if need - o.keys():
            sys.exit("missing flags: " + ", ".join(sorted(need - o.keys())))
        add(o)
    else:
        sys.exit(__doc__)
