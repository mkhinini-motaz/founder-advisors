# Prompt: write my company brief

Paste everything below the line into your coding agent, in your project folder.

---

You will write a company brief for this project. Every advisor or agent that works here will read it before answering, so it must be short and true.

**Step 1: read the repo.** Read the README, the package or manifest files, and the docs folder. Fill in what they tell you. Do not guess the rest.

**Step 2: ask me questions.** Ask at most 10 questions, one at a time. Wait for my answer before the next one. Ask only for what the repo cannot tell you:

- who the customers are, and what they pay
- decisions that are settled, each with the reason in my own words
- constraints (cash, time, people, rules)
- the country or countries we operate in
- which files each role should read (CEO, CFO, legal, sales, design, architecture, data)

Skip a question if the repo already answers it.

**Step 3: write `.claude/company.md`.** Use exactly these four sections, the same as `examples/company.md` in the founder-advisors repo:

1. What the company is
2. Key numbers (each marked plan or record, with a date)
3. Settled decisions (each with my reason, quoted, and where it is recorded)
4. Reading list by role

Rules:

- Mark every unknown as **ASK**. Never invent a number, a name or a reason.
- Keep it under two pages.
- Use plain English and short sentences.

**Step 4: add the pointer.** Add this line to `CLAUDE.md` (Claude Code) or `AGENTS.md` (other agents). Create the file if it does not exist.

`Before answering, read the company brief at .claude/company.md and the files it lists for this question.`

Then show me the brief and list every **ASK** so I can fill them in.
