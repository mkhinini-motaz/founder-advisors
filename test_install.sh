#!/usr/bin/env bash
# Scripted check for install.sh: add a role, --force backup, uninstall. Uses a scratch CLAUDE_HOME.
set -euo pipefail
cd "$(dirname "$0")"
H=$(mktemp -d); trap 'rm -rf "$H"' EXIT
export CLAUDE_HOME="$H"
./install.sh ceo cfo >/dev/null
./install.sh legal-counsel software-architect >/dev/null  # adding roles: no clash
[ -f "$H/agents/staff/legal-counsel.md" ]
! grep -rqF '${CLAUDE_PLUGIN' "$H"                          # plugin variables are filled in
grep -q "$H/staff/operating-rules.md" "$H/agents/staff/cfo.md"
[ "$(sed -n '/^model:/{n;N;N;p;}' "$H/agents/staff/cfo.md" | tr '\n' ' ')" = "memory: user omitClaudeMd: true color: green " ]   # copy-only settings
[ "$(sed -n '/^model:/{n;N;p;}' "$H/agents/staff/software-architect.md" | tr '\n' ' ')" = "memory: user color: blue " ]   # the architect reads CLAUDE.md
echo "# mine" >> "$H/agents/staff/cfo.md"
! ./install.sh >/dev/null 2>&1                            # an edited file still blocks a plain install
out=$(./install.sh --force)
grep -q "backup: $H/agents/staff/cfo.md.bak" <<<"$out"
grep -q "# mine" "$H/agents/staff/cfo.md.bak"
rm -r "$H/staff" "$H/skills/board" "$H/skills/hire" "$H/agents/staff"
echo ok
