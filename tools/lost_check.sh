#!/bin/zsh
# Usage: lost_check.sh <brain-before> <brain-after>
# Before a top-up merge, copy the brain: cp -R <brain> <build>/brain-before. After the merge, run this.
# Prints quoted lines the merge removed that no longer appear anywhere in the brain (GONE),
# and removed unquoted lines whose first 40 characters no longer appear (CHANGED). Ends with the word count of the hot-sheet part of _hot.md (from "## Hot sheet" on; the instructions above it do not count).
OLD=$1 NEW=$2
[ -d "$OLD" ] && [ -d "$NEW" ] || { echo "usage: lost_check.sh <brain-before> <brain-after>"; exit 1; }
for f in _hot frameworks principles positions stories voice; do
  diff -U0 -- $OLD/$f.md $NEW/$f.md | grep -E '^-' | grep -v '^--- ' | while IFS= read -r l; do
    q=$(printf '%s' "$l" | sed -E 's/^[^"]*"([^"]{20,60}).*/\1/')
    if [ "$q" = "$l" ]; then k=$(printf '%s' "${l:1}" | cut -c1-40); [ -z "${k// }" ] && continue
      grep -rqF -- "$k" $NEW || echo "CHANGED $f: ${l:1:160}"
    else grep -rqF -- "$q" $NEW || echo "GONE $f: ${l:1:200}"; fi
  done
done
sed -n '/^## Hot sheet$/,$p' $NEW/_hot.md | wc -w
