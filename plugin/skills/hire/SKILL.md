---
name: hire
description: Build your own staff advisors for your project, step by step. Use when someone wants advisor subagents for their company, wants to add or remove an advisor role, or asks how to adapt the shipped advisors to their business and country.
---

# Hire your own advisors

The shipped advisors were written for one small company. Yours should fit your company. Build them in this order, because each step makes the next one cheaper, and stop as soon as the advisors stop beating plain Claude.

## 1. Write the company brief first

Every advisor reads `<project>/.claude/company.md` before answering. In tests, the brief and the knowledge files explained every case where an advisor beat plain Claude; the persona did not. So the brief comes before any agent.

To have your agent interview you and write it, paste `prompts/write-brief.md` (in your clone of founder-advisors) into any agent. Or start from `examples/company.md` in that clone. It has four sections:

1. **What the company is:** what it sells, to whom, where; the stage; the cash; the founder's role; registered or not; language rules for customer text.
2. **Key numbers,** each labelled plan or record, with a date.
3. **Settled decisions,** each with a pointer to where it is recorded. Advisors treat these as closed unless they bring new evidence.
4. **Reading list by role:** which files each advisor reads. Name your country files here.

Keep it under two pages. Every advisor reads all of it on every question.

## 2. Pick two or three roles by recurring work

List the questions you asked in the last month, or expect to ask every week for the next three months. Group them. A group with at least one question a week earns a role; a group you asked once does not.

Start with two or three roles. The ten in `staff/agents/` are a menu; you do not have to install all of them.

Each role owns a list of decisions and names the roles that own the neighbouring ones ("You do not own pricing (the CFO)"). Without that line, two advisors answer the same question differently and nobody breaks the tie.

Reject a role when its work already has an owner, or when it has no recurring work before launch. The original build left out HR, investor relations, a product manager, a security advisor, QA, customer support, accessibility, incident response and growth for one of those two reasons. Security became a knowledge file for the architect instead.

Reject a role built on a personality ("a ruthless VC", "a famous founder"). Personalities belong on the board (step 5), where they challenge a decision. Advisors hold the facts and the method.

To adapt a shipped advisor, copy it to a new name (`install.sh --force` saves a changed file as `.bak`, but a new name is safer) and change three parts: the "What you own" list, the beliefs that do not hold in your business, and the reads in "First". Keep the file short. When three rounds of added bullets made the original CEO, sales and marketing files worse, trimming them back to the goal and a few beliefs fixed it.

Where things go:

- A method or a belief that does not change goes in the agent file.
- A fact that changes (a rate, a law, a price, a deadline) goes in a knowledge file, never in the agent file. A copy in the agent file drifts when someone corrects the knowledge file.
- A fact about one company goes in that company's brief.

## 3. Write the knowledge files your roles read

Two kinds, both under `${CLAUDE_PLUGIN_DATA}/staff/knowledge/` (the knowledge folder; create it if missing, and write its full path in the brief's reading list):

- **Country files:** tax, business law, market and tech for each country you operate in. Copy `${CLAUDE_PLUGIN_ROOT}/staff/knowledge/templates/knowledge.md` into the knowledge folder for each one, or use `examples/tunisia/*.md` in your clone as the model country pack.
- **Craft files:** methods from free sources and practice, each with its caveat. Eight ship in `staff/knowledge/`.

In a country file, every fact cites its URL and the date you opened it, and anything unconfirmed is marked **(verify)**. Put an "as of" date at the top. Update the tax and law files every year when the budget law changes.

Add a source to a craft file only if it is free to read and you have opened it. Give the agent file one line that points to the section, never the content again.

Write the country files with the advisor that will read them: ask it what it needs to know, then research and cite each item yourself or with a research agent. An advisor answering from memory about tax in your country is the failure this step exists to prevent.

## 4. Test each role with three cases against plain Claude

In your clone, copy `evals/cases.example.json` to `evals/cases.json` (git-ignored; the plugin holds no code, so run `run.py` from your clone) and write three cases per role from questions you have asked. Each case has:

- `question`: asked in your words.
- `cwd`: the project folder that holds `.claude/company.md`.
- `must`: what a good answer does, stated positively. The runner refuses a `must` item that starts with "does not", "never" or "no".
- `must_not`: what a wrong answer does.

Then run each role twice:

```
python3 evals/run.py --model opus cfo             # the advisor
python3 evals/run.py --model opus --baseline --pointer cfo  # plain Claude, told to read the brief first
```

If you installed the advisors as a plugin, put `ADVISOR_PREFIX=founder-advisors:` before the first command, because the plugin names them `founder-advisors:<role>`. The `--pointer` baseline is the fair one: without it, plain Claude may never open your brief, and the advisor wins only because it was told to. Use the model the advisor is installed with in `--model` (`opus` unless you installed with `--model`), so both runs use the same one. Keep a role only if it passes a case that this baseline fails.

A role that ties the baseline costs tokens for nothing: one consultation starts at about 13–16k tokens of context and reads 0.3–2.8M input tokens in all, because every tool call re-reads the context. Run important cases with `--trials 3`, since one good answer can be luck. To try a cheaper advisor model on the same cases, add `--model sonnet`. `python3 evals/test_run.py` checks the grading logic without calling any model.

When an advisor gets something wrong in real use, add the question as a case before you fix the file, so the fix is tested.

## 5. Add the board last

The board is a set of persona seats, each built from one founder's or thinker's public work (`board/`). Seats challenge a decision that is hard to undo; advisors hold the facts. Add the board only after the advisors pass their cases, because a seat is only as useful as the brief it reads.

1. Copy `${CLAUDE_PLUGIN_ROOT}/board/references/seat-index.md` to `${CLAUDE_PLUGIN_DATA}/skills/board/references/seat-index.md` if that is missing (create its folder), then rewrite the problem rows of the copy for your company; a plugin update replaces the plugin folder but not the copy. The shipped index is an example for Mendly, the made-up company in `examples/company.md`. Run `python3 ${CLAUDE_PLUGIN_ROOT}/board/scripts/check_index.py ${CLAUDE_PLUGIN_DATA}/skills/board/references/seat-index.md` until it prints `ok`.
2. Add `**Seat index:**` (the path of the copy) and `**Board notes:**` lines to your company brief. The advisors then end a costly-to-reverse answer with a `Board:` line naming the seats to ask.
3. Ask one seat to confirm one advisor's call before you run a full board. A confirmation costs about 66–69k tokens; a full board costs about 2M.
4. After ten confirmations or a month, count how many changed your call. If none did, stop using the board.

## Keep them honest

- Read each advisor's memory folder (`~/.claude/agent-memory/<agent>/`; only a copy install with `install.sh` gives advisors memory, a plugin install has none) now and then. An advisor records what it takes for your habits, and a wrong note there shapes every later answer.
- When an advisor says a knowledge file is wrong, fix the file and cite the source.
- Re-check any knowledge file older than six months before relying on an exact figure from it.
