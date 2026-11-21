"""Check references/seat-index.md against the roster.

Fails when a roster seat is missing from the index's area lists, when the index names a key the roster does not have,
or when a seat is never a lead, counterweight or wild card in the problems table. Run: python3 -I check_index.py [index path]
"""
import json
import pathlib
import re
import sys

SKILL = pathlib.Path(__file__).resolve().parent.parent
ROSTER = SKILL / "seats" / "roster.json"
INDEX = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else SKILL / "references" / "seat-index.md"  # optional path: an edited copy

keys = {s["key"] for s in json.loads(ROSTER.read_text())["seats"]}
text = INDEX.read_text()
listed = set(re.findall(r"^- ([a-z]+)", text, re.M))
in_table = set()
for line in text.splitlines():
    if line.startswith("| ") and not line.startswith("| Problem"):
        in_table |= set(re.findall(r"\b([a-z]+)\b", "|".join(line.split("|")[2:]))) & keys

errors = [f"missing from the area lists: {k}" for k in sorted(keys - listed)]
errors += [f"not in the roster: {k}" for k in sorted(listed - keys)]
errors += [f"in no problem row: {k}" for k in sorted(keys - in_table)]
print("\n".join(errors) or f"ok: {len(keys)} seats")
sys.exit(1 if errors else 0)
