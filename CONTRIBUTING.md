# Contributing

Ways to help, easiest first. Everyone who takes part follows the [code of conduct](CODE_OF_CONDUCT.md).

## 1. Share an eval result

Open the "Eval result" issue form. Wins and null results both count. Remove company-private details first. Results are added to the table in the README.

## 2. Add an example brief

Write a made-up brief for another kind of business. Copy the structure and length of `plugin/examples/company.md`. Use invented names that are not real brands, no real people, and settled decisions with the founder's reason quoted.

## 3. Add a country pack

Rules:

- An "as of" date at the top.
- Every figure cited to the adopted official text.
- Single-source items marked **(verify)**.
- Copy this line from `plugin/examples/tunisia/`: "General information, not legal, tax or financial advice. Check the official text and a licensed professional before relying on it."
- No personal data.

`plugin/examples/tunisia/` is the model. `plugin/staff/knowledge/templates/knowledge.md` is the template. Open the "Country pack" issue first to claim a country.

## 4. Add a craft knowledge file

Methods from free public sources or practice, each cited with its URL and its caveat. Put it in `plugin/staff/knowledge/`, and give the agent file one line that points to it.

## 5. Propose a new role

A new role needs at least 3 eval cases and a win over the `--pointer` baseline. See `evals/` and the "What made answers better" section of the README.

## 6. Propose a seat

- Public figure, public work only.
- The quote checker passes.
- The simulation label stays.
- No lines that state a person's religion or political views.
- List your sources. Sources must be free to read: no paywalled articles, paid newsletter posts, books, book excerpts, or quote or summary sites (`python3 -I tools/seat.py check` enforces the URL part).

## Writing a skill or an advisor file

Skill format: https://agentskills.io/specification. `.github/check-skills.py` checks it in CI.

- `name` is 1-64 characters (a-z, 0-9, single hyphens) and equals the folder name.
- `description` says what the skill does and when to use it. Put the use case first: the listing cuts the description at 1,536 characters. The hard limit is 1,024.
- Keep `SKILL.md` under 500 lines. Put details in `references/`.
- An advisor file in `plugin/staff/agents/` has a `name` equal to its file name and a non-empty `description`.
- A knowledge file starts from `plugin/staff/knowledge/templates/knowledge.md`.

## Bump the version

When you change anything a skill, an advisor or a seat, raise `version` in `plugin/.claude-plugin/plugin.json`. Installed copies update only when the version rises.

## Pull request process

- Open the "Country pack, Eval result or another" issue form first for new work, so two people do not start the same thing.
- One change per PR.
- Use a Conventional Commits title, for example `fix: ...` or `docs: ...`.
- By contributing you agree your work is MIT licensed.

## AI-assisted changes

AI help is fine. You must be able to explain the change yourself. Say in the PR which parts an AI wrote. Run the checks yourself, do not rely on the AI's word that they pass.

## Not accepted

- Promotion of a paid product.
- Real people's private data.
- Seat quotes that fail the checker.

## Run the checks

From the repo root:

```
python3 evals/test_run.py
python3 tools/test_check_quotes.py
python3 tools/check_index.py
python3 -I tools/seat.py check
bash -n install.sh
bash test_install.sh
python3 .github/check-skills.py plugin/skills/hire plugin/board --agents plugin/staff/agents/*.md
```

The same seven run on every push and pull request (`.github/workflows/checks.yml`).
