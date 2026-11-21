# Seat index

Use this file to pick seats. You do not need to read `roster.json` or `seats.md` to pick: this file holds the roster's
pillars and the natural tensions in short form, mapped to a company's problems. Read a seat's own tension line in
`seats.md` with `grep -n '^- <Short>' ${CLAUDE_PLUGIN_ROOT}/board/seats/seats.md` only when the reason for a pick needs it.

**This is an example index**, written for Mendly, the made-up tradesperson marketplace in `examples/company.md` (customers, tradespeople,
fixed prices, a second city). Rewrite the problem rows for your own company: keep the area lists, change the left column to the problems
your company actually has, and run `python3 ${CLAUDE_PLUGIN_ROOT}/board/scripts/check_index.py` until it prints `ok`. Keys are the roster keys (a seat's name in its `_hot.md` is `council-<key>`). (q) marks a quick-depth brain, which
has a thinner public record: when a quick seat and a standard seat fit equally, seat the standard one.

## Problems to seats

For each problem, the table gives the lead seats (the problem is their field), the counterweight (a seat with a natural
tension against the leads) and the wild card. Pick 3 to 5 seats: one or two leads, one counterweight, one wild card. For
law, tax and the figures, use the staff advisors (`legal-counsel`, `accountant`, `cfo`), not a seat.

| Problem | Lead | Counterweight | Wild card |
|---|---|---|---|
| Commission, booking fees, surcharges | gurley, goyal (q) | xu | - |
| Offers, discounts, promo codes, points | hormozi | gurley, michalowicz | cialdini (q) |
| Tradesperson supply: recruiting, pay, churn, no-shows | xu, goyal (q) | gurley | grant (q), taleb (q) |
| Scheduling, coverage, the job that must happen tomorrow | xu, goyal (q) | lutke (q), dhh | vogels |
| Tradespeople: onboarding, their tools, retention | lutke (q), xu | gurley | ulukaya (q) |
| Negotiating with a tradesperson or a partner | voss | hormozi | munger (q) |
| Franchising or licensing the model to another city | gerber (q), wickman | musk, xu | ghandour (q), munger (q) |
| Trust, vetting, payments and disputes | sheikha (q), tayebi (q) | michalowicz, buffett | yunus (q) |
| A new service line (cleaning, moving, installation) | sheikha (q), goyal (q) | gurley (liquidity per vertical) | chen, thiel |
| Launch, cold start, density in the first city | chen, xu | hormozi, garyvee | thiel, feynman (q) |
| A second city or country | ghandour (q), tayebi (q) | xu, goyal (q) | duke |
| Marketing, ads, campaigns, referral | sharp (q), garyvee | godin, kaushik | - |
| Brand and positioning | godin, blakely | sharp (q) | chesky |
| Retention, habits, notifications | eyal | norman | kaushik |
| Customer experience, refunds, support | chesky, xu | gurley, damodaran | norman |
| Screens, flows, accessibility | norman | musk | eyal |
| Software, architecture, infra, reliability | dhh, vogels | musk, graham | taleb (q) |
| Metrics, dashboards, experiments | kaushik, kozyrkov (q) | sharp (q) | feynman (q) |
| Cash, budget, runway, self-funding | michalowicz, buffett | sheikha (q), tayebi (q) | housel |
| Business plan, valuation, story against numbers | damodaran, buffett | chesky | munger (q) |
| Hiring, city managers, founder time | martell, leila | horowitz | grant (q), dhh |
| A hard call: close a city, stop a feature, part with someone | horowitz, duke | grant (q), voss | kahneman (q) |
| Fraud, ruin, single points of failure | taleb (q), goyal (q) | musk | munger (q), housel |
| Strategy, sequencing, big bets, reversibility | bezos, thiel | kahneman (q), munger (q) | naval |
| Build or buy (taking over a small agency, a ready product) | sanchez | graham, naval | buffett |
| The city, fair pay, tradespeople's livelihoods | ulukaya (q), yunus (q) | gurley, buffett | sheikha (q) |
| How a price or fee feels: fairness, surcharges, the reference price | thaler | hormozi, gurley | - |
| Word of mouth: what customers say, referral and sharing | berger | sharp (q), garyvee | cialdini (q) |
| Getting people to start and keep a habit (first booking, rebooking, tradesperson activity) | milkman, eyal | gigerenzer | thaler |
| Service catalogue size, too many options, defaults | schwartz | hormozi | norman |
| A simple rule against a model; showing a risk to people (arrival windows, fraud rules, forecasts) | gigerenzer | kozyrkov (q), kaushik | taleb (q) |
| Culture fit: partners from other cultures, feedback and trust | meyer (q) | voss, horowitz | ghandour |
| Speaking up and learning from failure (incidents, city managers, tradespeople) | edmondson | horowitz, martell | duke |

Any problem can take one judgment seat as its wild card: munger (q) for inversion, kahneman (q) for bias and the outside
view, duke for kill criteria, feynman (q) for self-deception, kozyrkov (q) for which decision the data changes, taleb (q)
for ruin, housel for the long run, or gigerenzer for whether a simple rule would do better.

## Seats by area

Delivery and super apps:
- xu: local delivery operations; every street, every night; all three sides must win.
- goyal (q): food delivery in emerging markets; contribution per order, fraud, courier churn, close a zone without density.
- sheikha (q): super apps in cash economies; earn trust, then let services ride on it. Thin brain.
- tayebi (q): Maghreb super app; daily need first, cash agents, payments later. The thinnest brain (mostly French and Arabic).
- ghandour (q): Arab-world logistics; own the standard, not the assets; local partners.

Marketplaces, merchants and franchise:
- gurley: take rate, liquidity, contribution after coupons.
- lutke (q): merchant platforms; remove the step where merchants give up.
- chen: network effects and cold start; the smallest network that works on its own.
- chesky: marketplace experience and trust between strangers.
- gerber (q): the franchise prototype; a written system a novice can run.
- wickman: operations and scaling; every process has an owner.

Money:
- buffett: cash, risk, long-term value.
- michalowicz: profit first, the bank balance.
- damodaran: valuation; does the story match the numbers.
- housel: money behaviour and the long run; room for error.
- naval: leverage and equity you own.
- sanchez: buy a business that already works.

Offers, marketing and influence:
- hormozi: offers, pricing and the close.
- garyvee: attention and underpriced platforms.
- sharp (q): evidence-based marketing; reach everyone in the category.
- godin: the smallest viable audience.
- blakely: consumer product and brand from zero, no outside money.
- cialdini (q): ethical influence; is the principle real and used honestly.
- voss: negotiation; a yes that holds.
- eyal: habits the user would choose.

Product, design and software:
- graham: what people want; do things that don't scale.
- norman: human-centered design; can an ordinary person use it.
- dhh: calm software; the simplest thing a tiny team can own.
- vogels: reliable systems; what happens when it fails.
- musk: first principles and speed; delete the step.
- kaushik: the one number that matters, and so what.
- kozyrkov (q): decision intelligence; which decision the data changes.

People and leadership:
- martell: hiring and founder time.
- leila: leadership and scaling teams (not the same seat as hormozi).
- horowitz: hard calls and wartime leadership.
- grant (q): rethinking and what motivates the people who carry it.
- edmondson: psychological safety; will people speak up early, and which kind of failure it is.
- meyer (q): culture and trust across cultures; how people give feedback, disagree and decide. Her written text is thin.

Psychology and behaviour:
- thaler: fair prices and mental accounting; which mental account the money comes from.
- berger: word of mouth; why people would talk about it, and what they would say.
- milkman: behaviour change; the barrier, then the moment and the nudge that start and keep it.
- gigerenzer: simple rules and risk literacy; the rule of thumb that beats the model.
- schwartz: choice overload; fewer options, a default, good enough.

Strategy and judgment:
- bezos: the right bet, and how reversible it is.
- thiel: monopoly and secrets; own a small market.
- munger (q): inversion and incentives.
- kahneman (q): bias and the outside view.
- duke: decision quality and kill criteria.
- taleb (q): fragility and ruin.
- feynman (q): scientific honesty.

Community:
- ulukaya (q): the town and the people who do the work.
- yunus (q): social business for people with little money.
