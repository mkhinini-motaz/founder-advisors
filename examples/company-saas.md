# Company brief: Tallybird (made-up example)

<!--
This is a fictional company. Every name and number below is invented to show the
format. Copy this file to <your project>/.claude/company.md and replace it with your
own facts. Keep it short: every advisor reads all of it before every answer.
-->

## 1. What the company is

- **What it sells:** a web tool that matches supplier invoices to purchase orders and flags the ones that do not agree, so a small finance team stops checking them by hand.
- **To whom:** finance leads at companies with 20 to 200 staff that pay 100 to 500 supplier invoices a month. Buyers are the finance lead and the owner.
- **Where:** sold online in one country. Customers in two neighbouring countries have signed up on their own.
- **Stage:** early revenue. 31 paying accounts; one founder does sales calls; no outbound team.
- **Money model:** monthly subscription by invoice volume: 49 for up to 100 invoices, 129 for up to 500. Annual plans get two months free. No setup fee.
- **Cash:** about 14 months at the current burn (plan, see Key numbers).
- **Founder's role:** two co-founders. One builds the product; one handles sales, support and the books.
- **Registered:** yes, as a limited company. VAT status: see `docs/decisions/vat.md`.
- **Language rules:** the product and all customer messages are in English. Prices on the site exclude VAT and say so.

## 2. Key numbers

Each line says whether it is a **plan** (a target or estimate) or a **record** (measured), with its date.

| Number | Value | Kind | Date |
|---|---|---|---|
| Monthly recurring revenue | 3,100 | record | 1 Nov 2026 |
| Cash in the bank | 61,000 | record | 1 Nov 2026 |
| Monthly fixed costs | 4,300 | record | Oct 2026 |
| Accounts lost in the last 90 days | 3 of 34 | record | 1 Nov 2026 |
| Trial to paid conversion | 18% | record | Q3 2026 |
| Accounts needed to cover two salaries | 90 | plan | |
| Support hours per week | not measured yet | | |

## 3. Settled decisions

Closed unless new evidence appears. Each points to where it is recorded.

- **No free plan.** A 14-day trial only. Founder's reason: "Free users cost us support time and never told us what they would pay for." `docs/decisions/no-free-plan.md`
- **No custom work for one customer.** Founder's reason: "Every custom request we said yes to in 2025 became a feature nobody else used." `docs/decisions/no-custom-work.md`
- **Price by invoice volume, not by seat.** Founder's reason: "Our value is invoices checked, and a small team with many invoices should pay more than a big team with few." `docs/decisions/pricing.md`
- **No outside funding before 100 accounts.** Founder's reason: "We want to learn who buys before we sell part of the company." `docs/decisions/funding.md`
- **One accounting package integration at a time.** `docs/decisions/integrations.md`

## 4. Reading list by role

Advisors read the files listed for their role, and nothing else unless the question needs it.

- **All roles:** this brief; `GLOSSARY.md` if the project has one.
- **ceo:** `docs/decisions/`; the monthly review in `docs/review.md`.
- **cfo:** `docs/finance/model.md`; `<knowledge folder>/<country>-tax.md`.
- **accountant:** `<knowledge folder>/<country>-tax.md`; `<knowledge folder>/<country>-business-law.md`.
- **legal-counsel:** `<knowledge folder>/<country>-business-law.md`; `docs/legal/terms.md`; `docs/legal/dpa.md`.
- **ops-lead:** `docs/support/playbook.md`.
- **marketer and sales-lead:** `docs/pitch.md`; `docs/sales/lost-deals.md`.
- **product-designer:** `docs/design/`; `docs/research/interviews.md`.
- **software-architect:** the project's `CLAUDE.md`; `docs/architecture.md`; `<knowledge folder>/<country>-tech.md`.
- **data-analyst:** `docs/metrics.md`; `<knowledge folder>/<country>-business-law.md` (data protection).

**Board notes:** `docs/board/`. **Seat index:** `<seat index path>` (rewrite its problem rows for this company before the first board).
