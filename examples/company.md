# Company brief: Mendly (made-up example)

<!--
This is a fictional company. Every name and number below is invented to show the
format. Copy this file to <your project>/.claude/company.md and replace it with your
own facts. Keep it short: every advisor reads all of it before every answer.
-->

## 1. What the company is

- **What it sells:** a phone app where people in one city book a vetted local tradesperson (plumber, electrician, handyman) for a small home repair, with a fixed price shown before booking.
- **To whom:** homeowners and renters who need a job done this week and do not know whom to call. On the other side, independent tradespeople who want more jobs without paying for ads.
- **Where:** one mid-sized city to start. A second city only after the first one breaks even (see Settled decisions).
- **Stage:** testing. The app works end to end; 12 tradespeople are signed; no paid marketing yet.
- **Money model:** 10% commission on each job, paid by the tradesperson, plus a 2.00 booking fee paid by the customer. Payment by card in the app; the tradesperson is paid weekly.
- **Cash:** enough for about 9 months at the current burn (plan, see Key numbers).
- **Founder's role:** one founder, who builds the product and runs the company. A part-time operations partner handles tradesperson onboarding on a fixed monthly retainer.
- **Registered:** yes, as a limited company. Tax regime and VAT status: see `docs/decisions/legal-form.md`.
- **Language rules:** the app and all customer messages are in English and Spanish. Prices always include tax and every fee.

## 2. Key numbers

Each line says whether it is a **plan** (a target or estimate) or a **record** (measured), with its date.

| Number | Value | Kind | Date |
|---|---|---|---|
| Cash in the bank | 48,000 | record | 1 Nov 2026 |
| Monthly fixed costs | 5,200 | record | Oct 2026 |
| Average job value | 110 | plan | |
| Jobs per week needed to break even | 70 | plan | |
| Jobs completed last week | 9 | record | week 44 |
| Tradespeople active in the last 30 days | 8 of 12 | record | 1 Nov 2026 |
| Repeat customers within 60 days | not measured yet | | |

## 3. Settled decisions

Closed unless new evidence appears. Each points to where it is recorded.

- **One city until break-even.** No second city before 70 jobs a week for four weeks in a row. Founder's reason: "Two half-run cities would teach us nothing about whether one can pay." `docs/decisions/one-city.md`
- **Tradespeople are independent contractors**, free to refuse jobs and to work elsewhere. No shifts, no fines. Founder's reason: "They are running their own businesses, and the contract has to match how they work." `docs/decisions/contractor-status.md`
- **No exclusivity** asked of tradespeople. Founder's reason: "We are not big enough to fill their week, so we cannot ask for all of it." `docs/decisions/no-exclusivity.md`
- **Fixed prices per job type**, set by the company and reviewed every quarter. Founder's reason: "Customers told us they book when they know the price before anyone comes to the door." `docs/decisions/pricing.md`
- **No investor money this year.** Founder's reason: "I want to prove the first city pays before I owe anyone a growth plan." `docs/decisions/funding.md`

## 4. Reading list by role

Advisors read the files listed for their role, and nothing else unless the question needs it.

- **All roles:** this brief; `GLOSSARY.md` if the project has one.
- **ceo:** `docs/decisions/`; the weekly scorecard in `docs/scorecard.md`.
- **cfo:** `docs/finance/model.md`; `<knowledge folder>/<country>-tax.md`; `<knowledge folder>/<country>-market.md`.
- **accountant:** `<knowledge folder>/<country>-tax.md`; `<knowledge folder>/<country>-business-law.md`.
- **legal-counsel:** `<knowledge folder>/<country>-business-law.md`; the contracts in `docs/contracts/`.
- **ops-lead:** `docs/ops/sops/`; `<knowledge folder>/<country>-market.md`.
- **marketer and sales-lead:** `docs/pitch.md`; `<knowledge folder>/<country>-market.md`.
- **product-designer:** `docs/design/`; `<knowledge folder>/<country>-tech.md`.
- **software-architect:** the project's `CLAUDE.md`; `docs/architecture.md`; `<knowledge folder>/<country>-tech.md`.
- **data-analyst:** `docs/metrics.md`; `<knowledge folder>/<country>-business-law.md` (data protection).

**Board notes:** `docs/board/`. **Seat index:** `<seat index path>` (rewrite its problem rows for this company before the first board).
