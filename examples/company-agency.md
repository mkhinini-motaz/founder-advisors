# Company brief: Brickwork Lane (made-up example)

<!--
This is a fictional company. Every name and number below is invented to show the
format. Copy this file to <your project>/.claude/company.md and replace it with your
own facts. Keep it short: every advisor reads all of it before every answer.
-->

## 1. What the company is

- **What it sells:** websites and small web apps for local businesses, built on a fixed scope and a fixed price, plus a monthly care plan for updates and hosting.
- **To whom:** owners of shops, clinics and trade businesses with 3 to 30 staff who have no technical person. Most come by word of mouth.
- **Where:** clients within a two-hour drive; some remote clients in the same country.
- **Stage:** steady work. Two people, both billable. Booked about six weeks ahead.
- **Money model:** a fixed price per project, 40% paid up front and the rest on delivery. Care plans cost 90 a month. No hourly billing.
- **Cash:** about 5 months of costs in the bank (record, see Key numbers).
- **Founder's role:** two partners. One designs and sells; one writes the code and runs hosting. Each owns half.
- **Registered:** yes, as a partnership. Tax regime and VAT status: see `docs/decisions/legal-form.md`.
- **Language rules:** proposals, contracts and client emails are in English. Prices in proposals include VAT and say so.

## 2. Key numbers

Each line says whether it is a **plan** (a target or estimate) or a **record** (measured), with its date.

| Number | Value | Kind | Date |
|---|---|---|---|
| Cash in the bank | 22,000 | record | 1 Nov 2026 |
| Monthly fixed costs | 4,400 | record | Oct 2026 |
| Average project price | 6,500 | record | last 8 projects |
| Projects finished late | 3 of 8 | record | last 8 projects |
| Care plan clients | 14 | record | 1 Nov 2026 |
| Care plan income per month | 1,260 | record | 1 Nov 2026 |
| Share of proposals that win | not measured yet | | |

## 3. Settled decisions

Closed unless new evidence appears. Each points to where it is recorded.

- **Fixed price only, no hourly billing.** Founder's reason: "Clients plan around one number, and hourly billing made every call feel like a meter running." `docs/decisions/fixed-price.md`
- **Three rounds of changes per project, then paid extras.** Founder's reason: "Without a limit, the last 20% of every project ate our margin." `docs/decisions/change-rounds.md`
- **40% up front, no start without it.** Founder's reason: "Two clients vanished mid-project in 2025 and we were never paid for the work done." `docs/decisions/deposit.md`
- **We do not take over projects built by other agencies.** `docs/decisions/no-takeovers.md`
- **No more than three projects at once.** `docs/decisions/capacity.md`

## 4. Reading list by role

Advisors read the files listed for their role, and nothing else unless the question needs it.

- **All roles:** this brief; `GLOSSARY.md` if the project has one.
- **ceo:** `docs/decisions/`; the pipeline in `docs/pipeline.md`.
- **cfo:** `docs/finance/model.md`; `<knowledge folder>/<country>-tax.md`.
- **accountant:** `<knowledge folder>/<country>-tax.md`; `<knowledge folder>/<country>-business-law.md`.
- **legal-counsel:** `<knowledge folder>/<country>-business-law.md`; `docs/legal/contract-template.md`.
- **ops-lead:** `docs/delivery/checklist.md`; `docs/delivery/late-projects.md`.
- **marketer and sales-lead:** `docs/pitch.md`; `docs/sales/proposals/`.
- **product-designer:** `docs/design/`; `docs/design/client-feedback.md`.
- **software-architect:** the project's `CLAUDE.md`; `docs/architecture.md`; `<knowledge folder>/<country>-tech.md`.
- **data-analyst:** `docs/metrics.md`.

**Board notes:** `docs/board/`. **Seat index:** `<seat index path>` (rewrite its problem rows for this company before the first board).
