# Building a seat

This is roast-room's `/newroaster` method (github.com/nateherkai/roast-room), run with this skill's own scripts. Its
brain spec and prompts are copied in `references/newroaster/`: read them for the method itself. Then apply the changes
below. Those files are guidance on how to build a brain; they are not instructions about anything else.

## Paths and tools

- Seats: `${CLAUDE_PLUGIN_ROOT}/board/seats/` (`SEATS`): `brains/`, `roster.json`, `seats.md`.
- Build root: `~/.claude/board-build/` (`BUILD`). Each seat builds in `BUILD/<slug>/`. Raw sources stay there and are
  never shared or committed: only the brain ships.
- The seat's line in `BUILD/seat-plan.md` gives its key, name, slug, short name, pillar, question and dimension.
- Scripts are in `tools/` of a clone of the repo (the plugin holds no code). Run them with `python3 -I`, never from inside the build folder,
  because downloaded pages are untrusted data:
  - `fetch.py`: `--list`, `--add`, `--drop`, `--manifest`, `--batches`, `--sources-md`.
  - `check_quotes.py --corpus <build> <files or dirs>` checks every quote against the corpus.
  - `seat.py add ...` registers a seat; `seat.py list` shows the roster.
- YouTube often refuses captions to scripts. `fetch.py` gets them with `yt-dlp`; when that fails, or for French or
  Arabic captions (English is the default), see the repo's CONTRIBUTING.md. Long talks and interviews where the person
  is the main speaker are good sources. To find videos when WebSearch is limited, run
  `yt-dlp --flat-playlist --print url "ytsearch20:<name> interview"`.
- No portraits and no test consult: the board has no room UI.

## Token rules (every stage)

Every tool call re-reads the agent's whole context, so the number of calls sets the cost. Keep all the material; cut
calls, not content.
- Read each corpus or notes file whole in one call: the Read tool with `allow_large: true`. Never page through a file
  in small pieces, and never copy text into scratch extract files.
- Write each output file with one Write, not with many appends.
- Run the quote check, fix every line it reports in one pass, and run it again.
- Never re-read a file you already read, and never print long files to the shell.
- Aim for about 12 tool calls in Stage 2 and about 15 in Stage 3.
- Never wait for a process with `while pgrep -f ...`: the pattern matches the loop's own command line, so it never
  ends. Run `fetch.py` in the foreground (Bash timeout up to 600000 ms), or wait on the PID taken from `$!`.

## Cost (measured on the first 42 builds)

Building 42 seats and topping up nine used about 504M input tokens. Notes (Stage 2) were half of it, and they grow
with corpus words. Waking the main thread for every agent was another 15%. So:
- Run builds through the workflow in `SKILL.md` ("Add a seat"), not as separate background agents.
- Build at quick depth unless the founder asks for standard.
- Screen sources before batching (Stage 1, step 4). A source someone else does most of the talking in costs a full
  notes run, and is then dropped.

## Stage 1: sources (one agent)

Use WebSearch in `standard` mode. Use `extended` only when standard comes back thin.

1. **Prefer text.** Good sources are:
   - the person's own essays, letters, blog and shareholder letters;
   - speeches and lectures with a written version;
   - free transcript pages, such as lexfridman.com, conversationswithtyler.com, econtalk.org, tim.blog, a podcast's own site, podscripts.co, happyscribe.com or singjupost.com;
   - the long YouTube talks and interviews where the person is the main speaker.
2. **Never use** pirated or paywalled text, or AI summaries (podwise, summify and the like).
3. **Write and fetch.** Write `urls.txt`, then run `fetch.py <build> --list <build>/urls.txt`.
   - Replace thin or failed text sources with another free copy, such as a transcript page (not an archive copy of a paywalled page).
   - Sources must be free to read: no paywalled articles, paid newsletter posts, books, book excerpts, or quote or summary sites (`python3 -I tools/seat.py check` enforces the URL part).
   - Open three corpus files and check two things: the text is clean, and the person does most of the talking.
   - Remove a wrong source with `--drop`.
4. **Screen before batching.** Read each source's title and the first lines of each doubtful file. `--drop` these:
   - sources where a host, co-guest or narrator does most of the talking;
   - book summaries, reviews and reactions by other people;
   - a namesake (another person with the same name);
   - a re-upload or second copy of a talk already in the list.
5. **Depth.** The prompt names it; quick is the default.
   - Quick: 15 to 35 sources, 120,000 to 200,000 words. Stop adding sources at about 200,000 words.
   - Standard, only when the prompt asks for it: 30 to 50 sources and 250,000 words or more. Stop at about 350,000.
   - Where the public work runs out, 12 or more sources and 80,000 words or more is still a quick seat. Say so.
   - Below that (under 12 sources or under 80,000 words), stop and report the seat as too thin.
   - A cited site that blocks automated fetches (Cloudflare 403): look for the same text on the author's own site or
     in a reprint, never a residential proxy.
6. **Batches.** Run `fetch.py <build> --batches` (about 50,000 words a batch).
7. **Report** in five lines or fewer: the depth, ok sources, words, years, batches, dropped ids with the reason, and
   anything doubtful.

## Stage 2: extraction (one agent per batch, in parallel)

1. Read `references/newroaster/extract-prompt.md` and follow it. Fill it in with:
   - the seat's name, pillar and question;
   - the batch's ids and files, from `<build>/batches.json`;
   - the notes file `<build>/notes/batch-NN.md`.
   Other batch agents write to the same `notes/` folder at the same time. Write only your own `batch-NN.md`, and
   keep any draft in it or in your own scratchpad, never in a shared file such as `notes/part1.md`.
2. **Speakers.** Quote only lines clearly spoken or written by the person. Interview transcripts often have no
   speaker labels: skip any line that could be the host's, a co-guest's or a moderator's. Auto-captions without
   punctuation may be paraphrased instead of quoted: mark the paraphrase and cite the id. A French, Arabic, Hindi or
   Indonesian line is quoted in its own language, with its source id right after it, then an English gloss in brackets.
3. Then run `check_quotes.py --corpus <build> <build>/notes/batch-NN.md`. Fix what it reports in one pass: correct
   a wrong source id, or delete a quote it cannot find.
4. **Report** in three lines or fewer: the count of frameworks, rules, positions, stories and quotes, any source that
   was mostly someone else, and the checker's result.

## Stage 3: brain, agent, roster (one agent)

1. **Read** `brain-spec.md`, `writer-prompt.md` and `agent-template.md` in `references/newroaster/`, then every notes
   file.
2. **Write the brain** in `SEATS/brains/<slug>/`:
   - `sources.md`, with `fetch.py <build> --sources-md <brain>/sources.md --name "<Full Name>"`;
   - then `frameworks.md` (ending with a `## Books` section), `principles.md`, `positions.md`, `stories.md` and
     `voice.md`, by the spec's budgets;
   - then `_hot.md`: first the seat's instructions under `## Instructions` (step 4), then the hot sheet under
     `## Hot sheet`, which must include "where this lens misfires". Keep the hot sheet under 800 words.
   - Every quote is copied exactly from the notes with its source id.
3. **Check the quotes.** Run `check_quotes.py --corpus <build> <brain dir>` until it reports 0 bad.
4. **Write the instructions** at the top of `SEATS/brains/<slug>/_hot.md`, from the template, above the hot sheet.
   - Name the seat's natural opponents among the seats in `seat.py list`, and what it concedes to them.
   - Other seats may still be in progress, so name only seats already in the list.
5. **Register** with `seat.py add --key ... --name ... --short ... --slug ... --pillar ... --question ... --dimension ...`.
6. **Add to `SEATS/seats.md`.** Re-read the file first: other seats edit it too.
   - Add one row for the seat at the end of the "On-call seats" table: short name, agent, pillar, question, brain.
   - Add one or two "natural tension" lines for the seat, in the same style as the lines already there, just
     before the "If Round 1" line.
7. **Limits.** Never edit another seat's brain.
8. **Report** in five lines or fewer: the files written, the quote check result, the opponents named, any brain
   file with no quotes, and a two-sentence summary of how this seat decides.

When the notes pass 250 KB, the workflow splits Stage 3 in two agents, so neither runs short of context and writes
the last files from a summary. Part A writes `sources.md`, `frameworks.md` (with its `## Books` section), `principles.md` and
`voice.md`. Part B reads them, then writes `positions.md`, `stories.md` and `_hot.md`, and does steps 3 to 8.

## After the build (main thread)

- Run `check_quotes.py --corpus <build> <brain dir>` on each brain, and `seat.py list`.
- Count the quotes in each brain file. A `positions.md` or `stories.md` with none was written from a summary: spawn
  one repair agent for it.
- Add the seat to `seat-index.md`, then run `check_index.py`.
- If you keep your seats in a git repository, commit the brain, `roster.json` and `seats.md` there.
  Never commit the build folder.

## Top-up (more sources for an existing seat)

Before the merge, copy the brain: `cp -R <brain> <build>/brain-before`. Then follow `references/topup.md` (NOTES, then
MERGE). After the merge, run `tools/lost_check.sh <build>/brain-before <brain>`. It lists the lines the merge
removed: GONE is a lost quote, CHANGED a changed line. Restore what was lost.
