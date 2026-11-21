---
name: board
description: Persona council for a founder's decisions. Seats built from famous founders' and thinkers' public work challenge a decision, then the staff advisors check the facts. Use for /board, "ask <persona>", "what would <persona> say", or an advisor's `Board:` line. `/board add <name>` builds a new seat.
---

# Board

**Experimental.** The board is newer than the staff advisors and its value is not proven yet. See "Is the board worth it" at
the end, and count before you trust it.

A seat is a simulation built from a person's public work, not the person. Every seat answer starts with the simulation label from its `_hot.md`. Keep the label when you relay or quote an answer. Each seat has a brain at
`${CLAUDE_PLUGIN_ROOT}/board/seats/brains/<slug>/`. Its `_hot.md` holds the seat's instructions first (`## Instructions`) and its hot sheet after them (`## Hot sheet`).
The roster (key, name, pillar and question for every seat) prints with `python3 -I tools/seat.py list`. The plugin holds no code: the scripts are in the `tools/` folder of a clone of
https://github.com/mkhinini-motaz/founder-advisors, so run them from that clone, always with `python3 -I`.

**Seat index.** Read `${CLAUDE_PLUGIN_DATA}/skills/board/references/seat-index.md` if it exists, else the shipped
`${CLAUDE_PLUGIN_ROOT}/board/references/seat-index.md` (the `hire` skill copies the shipped one to the first path before it is edited).
**Plugin install only:** files this skill points to are read as plain text, so in them the placeholder `CLAUDE_PLUGIN_ROOT`
(written there with a dollar sign and braces) is the folder above `${CLAUDE_PLUGIN_ROOT}/board`. Staff advisors are named `founder-advisors:<name>` there.

**Session folder.** Briefs and answers go in `<project>/docs/board/<date>-<slug>/`, or in the folder the company brief
(`.claude/company.md`) names under "Board notes". Take the date from `date`.

The first test of persona seats against the staff advisors set these rules:

- **Seats challenge; the staff advisors hold the facts.** A seat's figures and its reading of a settled decision are
  checked before the founder sees them. In the test, seats used out-of-date figures that the advisors had already
  replaced.
- **The brief carries the founder's reason in their own words**, not only what they lean to. Leaving the reason out
  changed 6 of 8 calls in the test.
- **No options in the first round.** A list of options steers the answer. Ask open first, then score.
- **Flag rule clashes; do not adopt them.** Seats push against settled rules (for example "the founder does no field
  sales"). Report each clash as a clash.
- **Reuse before asking.** Before you start any seat, run `grep -ril <word> <session folder parent>`. If that seat
  answered the same question in the last 30 days and no new fact has come in since, relay that answer.

## The brief

Write it to `<session folder>/brief.md`. Put in:

- the question, in the founder's words;
- their reason or purpose, quoted;
- the settled decisions and constraints that bear on it, from `.claude/company.md` and the project's decision records;
- the newest figures, and the files that hold them (absolute paths);
- no options.

## The seat prompt

Spawn `general-purpose` with `model: "opus"`. Give it this prompt, with the brackets filled in:

> Read [brain dir]/_hot.md and follow it as your instructions for this task. It is your first file; your brain is
> [brain dir], so then read what you need. Then read the brief at [brief path] and the files it lists.
> Answer as if you ran [the company, in one line from the brief] in the founder's place. [Round instructions.] You may
> call one settled decision wrong: name it and say why. Quote only your brain, with source ids. Write your answer to
> [answer path] and no other file. Reply with the path and a five-line summary.

Run the quote check on each answer before using it:
`python3 -I tools/check_quotes.py --brain <brain dir> <answer>`, run from a clone of the repo. Without a clone, check the quotes against the brain files by reading them. Drop any quote you cannot find, and say so.

## Ask one seat

Use this when the founder asks what one seat would say.

**A small question gets a quick read, not a seat run.** Small means they want a view, not a confirmation of a decision
that is hard to undo. Read the seat's `_hot.md`, and its `positions.md` only when the hot sheet does not cover the
question. Answer in that seat's frame, quoting at most two lines copied exactly from those files with their source ids.
Head the answer "Quick read from <name>'s hot sheet, not a seat run". Offer a seat run in one line when the answer will
drive a decision. A quick read costs about 1 to 4k tokens, a full seat run 160 to 200k, and a confirmation seat about
66 to 69k (measured on Opus: 5 calls, under a minute).

For a decision:

1. Match their words to a seat by key, name or short name. When they name a problem and no seat, take the first lead
   seat in its row of the seat index.
2. Write the brief.
3. Spawn the seat. The round instructions are: "Answer the question: your call, your reasons, and what would change
   your mind."
4. Relay the call, the reasons, any settled decision it calls wrong, and any rule clash.

## Confirm an advisor's call

When a call is hard to undo, a staff advisor ends its answer with `Board: <keys>, <question>` (operating rules § 5 in
`${CLAUDE_PLUGIN_ROOT}/staff/operating-rules.md`). The advisors are the staff and the seats are the board: staff ask the board to
confirm such a call. Run the seats without asking the founder. A good answer comes first; spend tokens only where they
buy one:

- **The seats the question needs.** Usually one; more when the call spans fields or needs another tension. When several
  advisors name seats, merge the lists and drop duplicates. Every seat must bring an angle the others do not. Before
  three or more seats at once, give one cost line; past five, wait for the founder's go-ahead.
- **Skip a seat** when the founder has already decided the point, or when the reuse rule above finds its answer.
- **Rounds follow the debate.** One round, unless the founder argues with the answer, adds a fact or asks the seats
  again. Then continue the same seats with SendMessage: a continued seat keeps what it has read, and a fresh one reads
  it all again. Start a fresh seat only for one not yet asked.
- **No advisor re-check.** The advisor already holds the facts. Check the seats' figures against the advisor's answer
  yourself, and drop any figure that is in neither the answer nor the seat's brain.

1. Write `brief.md` in the session folder: the founder's question and their reason, in their own words, then the
   advisor's answer as it came. List no other files.
2. Spawn each seat with "The seat prompt", changed in two places; several seats go in one message. First change: it
   reads only `_hot.md`, `positions.md` and the brief, in one turn, not "the files it lists". Second
   change: it replies in text and writes no file, so drop "Write your answer to [answer path]". The round instructions are: "Say whether you agree with the advisor's call. Give your strongest
   reason, and the fact or number that would change your mind. 250 words at most."
3. Save the reply beside the brief as `confirm-<key>.md`, with the first line `Verdict: agrees` or
   `Verdict: challenges`. Run `check_quotes.py --brain` on it.
4. Under the advisor's answer, add one line: `Board (<name>): agrees|challenges: <reason>; would change on <gate>.`
   The founder decides.
5. When the founder has decided, add the line `Changed the call: yes` or `no` to the file.

## Run a board (`/board <decision>`)

1. **Brief.** Write it as above.
2. **Seats.** Pick 3 to 5 from the decision's row in the seat index. Do not read `roster.json` or
   `seats/seats.md` to pick; the index holds both in short form.
   - the seats whose field it is (lead);
   - one seat with a natural tension against them (counterweight);
   - one wild card.

   Name them to the founder in one line. Do not ask, unless they named seats themselves.
3. **Round 1, open.** All seats at once, blind to each other. The round instructions are:
   - invent 4 to 6 options, and mark NEW any option not in the files;
   - score each option /10, and pick one;
   - give the gate: the fact or number that would make you change your pick.
4. **Round 2, score.** Merge every option without duplicates, and add any option the founder or an advisor proposed.
   - Continue each seat with SendMessage; do not start a fresh one.
   - The round instructions are: score the merged list /10, and keep or change your pick, saying why.
5. **Fact check.** Spawn the staff advisor whose field the decision is (its name is `founder-advisors:<name>` when installed as a plugin, e.g. `founder-advisors:cfo`): `cfo` for money, `ceo` for strategy,
   `legal-counsel` for law, `ops-lead`, `marketer`, `software-architect`, and so on. Give it the brief and the answers.
   It checks every figure against the files and flags every clash with a settled decision or a rule.
6. **Report** to the founder:
   - where the seats converge;
   - the NEW options;
   - each pick with its gate;
   - any settled decision called wrong;
   - the rule clashes;
   - the figures the advisor corrected;
   - what is left for them to decide.

Keep the brief, answers and report in the session folder.

**Cost:** one seat answer was about 160k to 200k tokens in the test. Five seats over two rounds plus one advisor is
about 2M tokens. Use a board for decisions that are hard to undo, not for routine ones.

## Add a seat (`/board add <name>`)

1. Add the person's line to `~/.claude/board-build/seat-plan.md` (create it if missing): key, name, slug, short name, pillar, question and
   dimension. Sharpen the pillar against the existing seats.
2. Build all the seats asked for in one Workflow run. This skill's instruction is the opt-in for it. Run it with
   `scriptPath` set to the absolute path of `tools/seat-build.js` in a clone of the repo and
   `args: {home: "<absolute home folder>", board: "${CLAUDE_PLUGIN_ROOT}/board", seats: [{key, slug}, ...]}`. Add `depth: "standard"` only when the founder asks for it.
   - The main thread wakes once, at the end. Separate background agents woke it twice per agent, which was 15% of the
     cost of the first builds.
   - Start a build of more than three seats in a fresh session, so each call re-reads less context.
   - The stage rules are in `references/build-seat.md`; the workflow's agents read them there.
3. Do "After the build" in `references/build-seat.md`.
4. Add the seat to the seat index (copy it to the DATA path first if the shipped one is the only one): one line under its area, and its key in the rows of the problems it leads.
   Then run `python3 -I tools/check_index.py <seat index path>` from a clone; it must print `ok`.

Plugin install: a new seat is written into the plugin folder, which an update replaces. Copy new seats and the roster out before updating, or use `install.sh` if you add seats.

For more sources on an existing seat, use "Top-up" in `references/build-seat.md`.

## Is the board worth it

Keep the `Changed the call: yes|no` lines. After ten confirmations, or a month, count them. If no seat changed a call,
stop confirmations and keep the board for open questions only. Record the count where the project keeps its decisions.
