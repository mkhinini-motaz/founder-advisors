# AGENTS.md

Advisor subagents (`staff/agents/`), a decision board skill (`board/`), a `hire` skill (`skills/hire/`) and an eval runner (`evals/`) for Claude Code. They read a short company brief at `.claude/company.md` in the user's project.

- Install: `./install.sh` (`--dry-run` shows what it copies, `--force` overwrites on update). It is also a Claude Code plugin (`.claude-plugin/`). Markdown bodies use `${CLAUDE_PLUGIN_ROOT}/<repo path>` for shipped files and `${CLAUDE_PLUGIN_DATA}/<install path>` for files the user edits; `install.sh` fills both in with the installed `~/.claude` paths, so no `${CLAUDE_PLUGIN` text may be left in an installed file. Scripts find files from `__file__`.
- Checks: `claude plugin validate .` (run by hand, not in CI); `python3 evals/test_run.py` (prints `ok`), `python3 -I board/scripts/test_check_quotes.py`, `python3 -I board/scripts/check_index.py`, `bash -n install.sh`, `bash test_install.sh` (prints `ok`).
- Seat sources: Sources must be free to read: no paywalled articles, paid newsletter posts, books, book excerpts, or quote or summary sites (`python3 -I board/scripts/seat.py check` enforces the URL part).
- Evals: `python3 evals/run.py --model sonnet` asks each advisor its cases and grades the answers. Run it only after `./install.sh` and after writing `evals/cases.json`; it calls the model and costs tokens. `python3 evals/run.py --compare OLD NEW` compares two runs (exit 1 on a regression) and needs no model.
