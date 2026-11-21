# Brain spec: one seat on the board

Every seat has the same brain layout, so the seats differ only in content. The original seven follow this spec; new seats must too.

Folder: `${CLAUDE_PLUGIN_ROOT}/board/seats/brains/<slug>/`

## Files

| File | Budget (standard; `--quick` may run about half) | Contents |
|---|---|---|
| `_hot.md` | instructions, then a hot sheet of 600 to 800 words (the budget counts the hot sheet only) | Read on every council call. It opens with the frontmatter and `## Instructions` (the agent file written from `agent-template.md`), then `## Hot sheet`: who the seat is, the pillar and the question it owns, the corpus in one line, worldview in three sentences, the 8 rules they decide by (each with one short verbatim quote and source id), the 5 frameworks they reach for first, their decision loop (5 or 6 steps), signature questions they ask founders, a voice cheat sheet (5 lines), and **where this lens misfires**. |
| `frameworks.md` | 12 to 25 entries | Name (as they name it, or a short name marked *(unnamed)*), what it is, parts or steps, when to use it, how to score a decision with it (scoring guidance from their own thresholds, labeled as guidance), one verbatim quote with source id, and how many sources use it (with ids). Include the frameworks from their books. Most-used first. The file ends with a `## Books` section: one entry per book (title, year, core thesis, key frameworks in your own words, which sources teach it; never reproduce book text; if they have no books, say so in one line and list their major essays or series instead). |
| `principles.md` | 15 to 30 entries | Decision rules in one plain sentence, one or two verbatim quotes with source ids, number of supporting sources, confidence (high = 3+ sources, medium = 2, low = 1). |
| `positions.md` | 20 to 40 topics | Their stance on common founder questions: pricing, discounting, raising money, debt, first hire, firing, partners, equity, focus versus diversification, side projects, niche, content, paid ads, brand, AI, remote work, work hours, burnout, selling the company, culture, metrics, competition, timing. Verbatim quote, source id, and date. When they changed their mind, record both views side by side with dates. Topics with no evidence say "no recorded position"; never guess. |
| `voice.md` | 400 to 700 words | How they talk: sentence length, cadence, signature phrases (verbatim, with how many sources use them), go-to analogies, how they open and close an argument, how they disagree, words and moves they never use. Then 8 to 12 short verbatim voice anchors (under 45 words each, with source ids). |
| `stories.md` | 10 to 20 entries | The stories and case studies they reuse, one or two lines each with the lesson and source ids. |
| `sources.md` | all | Written by `fetch.py --sources-md`: a header with counts and total words, then `id | title | url | date | words` per source. |

Each file opens with a `# <File>: <Full Name>` heading and one line on what it was built from.

## Rules

- Sources must be free to read: no paywalled articles, paid newsletter posts, books, book excerpts, or quote or summary sites (`python3 -I board/scripts/seat.py check` enforces the URL part).
- Every quote is verbatim from the corpus and carries a source id from `sources.md`, like "..." (S014). Quotes stay under 45 words. `check_quotes.py` must pass on the whole folder.
- Quotation marks mean verbatim. Signature questions, paraphrases, and your own summaries go without them, so no agent later passes them off as the person's words.
- Never attribute a view without a source id. A line that is your reading of several sources says "inferred from S0xx, S0yy".
- Plain English. No em dashes. No filler.
- The brain describes how the person thinks so an agent can reason like them. It is not a biography and not a fan page: include where they are wrong, inconsistent, or out of their depth.
- **Where this lens misfires** is mandatory in `_hot.md`: the situations where this person's advice is known to fit badly (advice built for high-ticket services applied to SaaS, public-equity rules applied to a seed-stage startup, a solo creator's playbook applied to a 50-person company). Use what they say about their own limits first, then the shape of their experience.
- Prefer newer sources when views changed, and say so with dates.
