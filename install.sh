#!/usr/bin/env bash
# Copy the advisors, the board and the hire skill into ~/.claude.
# (To use them as a Claude Code plugin instead, see the README; this script is the copy install.)
# The files use ${CLAUDE_PLUGIN_ROOT} and ${CLAUDE_PLUGIN_DATA} paths; the copy fills in the installed paths.
#   ./install.sh --dry-run   show what would be copied
#   ./install.sh --model sonnet   set the staff advisors' model (opus, sonnet or haiku); board seats run on opus, set in plugin/board/SKILL.md
#   ./install.sh ceo cfo     install only these advisors (the shared files, the board and the hire skill always go in)
#   ./install.sh             copy; stops before copying anything if a target file exists and differs
#                            (identical files are skipped, so adding a role to an existing install works)
#   ./install.sh --force     overwrite the files this repo installs (use after a git pull); other files are left alone;
#                            a changed file you edited is first saved as <file>.bak
# Uninstall: rm -r ~/.claude/staff ~/.claude/skills/board ~/.claude/skills/hire ~/.claude/agents/staff
#   (one advisor: rm ~/.claude/agents/staff/<role>.md)
# CLAUDE_HOME is for testing: the installed files name the folder they were copied to, so a real install belongs in ~/.claude.
set -euo pipefail
cd "$(dirname "$0")"
DEST="${CLAUDE_HOME:-$HOME/.claude}"
DRY=0; FORCE=0; MODEL=; ROLES=" "
while [ $# -gt 0 ]; do
  case "$1" in
    --dry-run) DRY=1 ;;
    --force) FORCE=1 ;;
    --model) shift; MODEL="${1:-}"
      case "$MODEL" in opus|sonnet|haiku) ;; *) echo "--model takes opus, sonnet or haiku"; exit 2 ;; esac ;;
    -*) echo "unknown option: $1"; exit 2 ;;
    *) [ -f "plugin/staff/agents/$1.md" ] || { echo "no such advisor: $1"; exit 2; }; ROLES="$ROLES$1 " ;;
  esac
  shift
done

# source folder -> target folder
MAP="plugin/staff/operating-rules.md staff/operating-rules.md
plugin/staff/knowledge staff/knowledge
plugin/staff/agents agents/staff
evals staff/evals
plugin/board skills/board
plugin/skills/hire skills/hire"

pairs=()
while read -r src dst; do
  if [ -f "$src" ]; then pairs+=("$src|$DEST/$dst"); continue; fi
  while IFS= read -r f; do
    if [[ "$f" == plugin/staff/agents/*.md && "$ROLES" != " " ]]; then b="${f##*/}"; [[ "$ROLES" == *" ${b%.md} "* ]] || continue; fi
    pairs+=("$f|$DEST/$dst/${f#"$src"/}"); done \
    < <(find "$src" -type f ! -name .DS_Store ! -path '*/__pycache__/*' ! -path '*/runs/*' | sort)
done <<< "$MAP"

# what a source file becomes at its target: plugin variables filled in with the installed paths
# (each ${CLAUDE_PLUGIN_ROOT}/<repo path> becomes its MAP target, ${CLAUDE_PLUGIN_DATA} becomes $DEST),
# and the model line rewritten for advisors
SUBS=()
while read -r src dst; do SUBS+=(-e "s|\${CLAUDE_PLUGIN_ROOT}/${src#plugin/}|$DEST/$dst|g"); done <<< "$MAP"
SUBS+=(-e "s|\${CLAUDE_PLUGIN_DATA}|$DEST|g")
render() {
  if [ -n "$MODEL" ] && [[ "$1" == plugin/staff/agents/*.md ]]; then sed "${SUBS[@]}" -e "1,/^---\$/{s/^model:.*/model: $MODEL/;}" "$1"; else sed "${SUBS[@]}" "$1"; fi
}
same() { render "$1" | cmp -s - "$2"; }
clash=0
[ $FORCE = 1 ] || for p in "${pairs[@]}"; do
  d="${p#*|}"; [ -e "$d" ] && ! same "${p%%|*}" "$d" && { echo "exists: $d"; clash=1; }
done
[ $clash = 1 ] && { echo "Nothing copied. Move those files aside or merge them by hand."; exit 1; }

for p in "${pairs[@]}"; do
  src="${p%%|*}"; dst="${p#*|}"
  set_model=; [ -n "$MODEL" ] && [[ "$src" == plugin/staff/agents/*.md ]] && set_model=1
  if [ $DRY = 1 ]; then echo "$src -> $dst${set_model:+ (model: $MODEL)}"
  else
    mkdir -p "$(dirname "$dst")"
    if [ -e "$dst" ] && same "$src" "$dst"; then continue; fi
    if [ $FORCE = 1 ] && [ -e "$dst" ]; then cp "$dst" "$dst.bak"; echo "backup: $dst.bak"; fi
    render "$src" > "$dst"
  fi
done
echo "${#pairs[@]} files $([ $DRY = 1 ] && echo 'would be copied' || echo copied) to $DEST"
[ $DRY = 1 ] || echo "Next: copy plugin/examples/company.md to <your project>/.claude/company.md and rewrite it."
