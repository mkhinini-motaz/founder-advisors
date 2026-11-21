# Frameworks: Werner Vogels

18 frameworks, roughly most-used first. Built from his blog posts and keynotes (2006 to 2026). "Sources" counts distinct sources where the idea is used. Guest-written bodies are credited to their authors. The How-to-score lines are scoring guidance for the council, not quotes.

---

## 1. Everything fails, so failure is the normal case
- **What it is:** The design starting point. At scale, rare events happen daily, so recovery is built in, not bolted on.
- **Parts:** assume failure; watch slow components, not only dead ones; keep working while a part is broken; make repair small and fast.
- **When to use:** Every design review. Ask what happens when this fails before "how does it work".
- **How to score:** 5 if each part's failure has a named, tested response; 3 if the answer is "we will fix it"; 1 if the plan assumes things stay up.
- **Quote:** "In large systems, failures are a norm, not an exception." (S040)
- **Sources:** 9 (S032, S040, S052, S063, S070, S074, S097, S098, S099). The Dynamo paper (S070) says the same: failure handling is the normal case.

## 2. Blast radius, cells and compartmentalization
- **What it is:** Hard boundaries so one fault touches the fewest customers. Zones share no low-level dependency; cells split a service into independent units.
- **Parts:** fault isolation ladder (cell, zone, region); never change more than one zone at a time; remove the whole zone when it misbehaves instead of hunting the cause; split hot partitions rather than growing them.
- **When to use:** Any shared component: a database, a queue, a config.
- **How to score:** 5 if a failure hits a small named share of users; 3 if one shared piece can hurt all; 1 if one bad customer or change can stop everyone.
- **Quote:** "Availability Zones draw a hard line around the scope and magnitude of those interruptions." (S043)
- **Sources:** 7 (S040, S043, S052, S097, S098, S099, S106). Shuffle sharding and per-volume tiny databases are the S097 examples (raw captions, no quote).

## 3. Tiers of criticality and the cost of nines
- **What it is:** Sort the system into what must always work, what matters, and what can go dark, then spend fault tolerance by tier.
- **Parts:** tier one (search, browse, cart, checkout, later reviews); tier two (recommendations); tier three (bestseller list). Tell the business what each extra nine costs; they decide.
- **When to use:** Before choosing any redundancy.
- **How to score:** 5 if tiers are written and each has a price; 3 if everything is "important"; 1 if one uptime figure is applied to all.
- **Quote:** "Oh, you want four nines behind your bestseller list? Well, that’s going to cost you so much." (S093)
- **Sources:** 5 (S093, S098, S104, S105, S094). Reviews moved up a tier once Amazon saw buyers leave when they were offline (S104).

## 4. Availability arithmetic and tiers of design
- **What it is:** Hard dependencies in series multiply down; redundancy multiplies up.
- **Parts:** two parts at four nines in series cap near 99.97; two redundant parts reach five nines. Rough ladder: one instance (two nines), two zones with failover (three), three zones with spare capacity (four), two regions active-active (five).
- **When to use:** Setting an uptime promise, or listing dependencies.
- **How to score:** 5 if the product of every hard dependency is computed and accepted; 1 if the promise exceeds its weakest dependency.
- **Quote:** "redundancy is a very important tool to create higher available systems" (S098)
- **Sources:** 1 (S098); related S065, S094.

## 5. Safe change: continuous configuration and staged rollout
- **What it is:** Treat configuration as code. Validate it, roll it to a few, watch alarms, undo on its own.
- **Parts:** store config apart from code; fetch at runtime; validate syntax and meaning; limit blast radius with small percentages; deploy zone by zone; feature toggles; blue/green; guardrails because stress makes people sloppy.
- **When to use:** Every release and every config edit.
- **How to score:** 5 if a bad change reaches under a small share of users and reverts without a human; 1 if all-at-once.
- **Quote:** "validation systems and guard rails help give you surgical precision when your hand is normally the shakiest." (S031)
- **Sources:** 4 (S031, S043, S098, S038).

## 6. The Frugal Architect (cost-aware design)
- **What it is:** Laws for cost-aware, sustainable systems in three groups: design, measure, optimize. He calls them observations, not legal laws.
- **Parts:** cost as a non-functional requirement; align cost with revenue; define your meter; cost per request over time; profile with flame graphs; turn off what is idle; cost-following pricing.
- **When to use:** Any new feature or architecture review, and any "unlimited" offer.
- **How to score:** 5 if cost tracks the revenue dimension and is on a dashboard; 3 if cost is reviewed after the bill; 1 if no one can name the cost of a request.
- **Quote:** "Define your meter, because if you can continue to look at this meter, it will change" (S104)
- **Sources:** 4 (S015, S052, S055, S104). Story: an unlimited plan, sold without matching cost to usage, "The company went out of business because of this" (S104).

## 7. Constant work and no modes
- **What it is:** Systems that do the same work whatever the load avoid a rarely used recovery path. The idea is Colm MacCárthaigh's; Vogels adopts it and republishes it.
- **Parts:** pay a cost once at boot, not under load; avoid modes; avoid heavy, seldom-run recovery code ("bimodal behavior"); size payloads to the maximum from day one.
- **When to use:** Config distribution, health checks, any "repair everything" loop.
- **How to score:** 5 if the failure path is the normal path; 1 if recovery is a special mode that is never exercised.
- **Quote:** "absorbing the cost once at boot rather than paying it continuously during operation" (S005)
- **Sources:** 4 (S005, S021, S093, S098). He admits it felt odd, "Because I’ve grown up in a time that you minimize the number of bytes on the wire." (S093).

## 8. One-way and two-way doors
- **What it is:** Reversible choices need no permission; irreversible ones get careful steps.
- **Parts:** classify the door; decide a two-way door fast; validate a one-way door in stages; remember there are few one-way doors.
- **When to use:** Before a language, vendor, schema or API commitment.
- **How to score:** 5 if the door type is stated and a one-way door has staged evidence; 1 if a one-way door is treated as a quick call or the reverse.
- **Quote:** "A one-way door decision is almost impossible to reverse, so you have to make it methodically, carefully, slowly, and with great deliberation and consultation." (S035)
- **Sources:** 3 (S004, S024, S035). Also "The cost of a wrong reversible decision is almost always lower than the cost of making that decision slowly." (S004)

## 9. Evolvable architecture (revisit at each order of magnitude)
- **What it is:** No design survives growth. Start small, let it grow, and re-examine at about every tenfold.
- **Parts:** start with a monolith if it is fastest; split by unique scaling and security needs, not by data ownership; merge services that always serve together and share one team; evaluate regularly; Gall's law (complex systems that work grew from simple ones that work).
- **When to use:** Growth planning, a rewrite debate.
- **How to score:** 5 if the next order of magnitude is named with a trigger; 1 if the design is meant to last forever.
- **Quote:** "My rule of thumb has been that with every order of magnitude of growth you should revisit your architecture" (S024)
- **Sources:** 7 (S024, S028, S038, S097, S098, S100, S106).

## 10. Mechanisms versus good intentions
- **What it is:** Intent does not change outcomes; a mechanism does. Build the thing that makes the right action automatic or the wrong one impossible.
- **Parts:** the Andon cord example; durability reviews that list every threat and its guardrail; mechanisms that stop an experiment that goes too far.
- **When to use:** After any incident or promise to "be careful".
- **How to score:** 5 if the lesson became a check or a button; 1 if it became a reminder.
- **Quote:** "There are mechanisms and there are good intentions. They're not the same." (S105)
- **Sources:** 3 (S045, S104, S105).

## 11. Cause of error: 5 Whys, no culprits, game days
- **What it is:** After a failure, restore service, find the cause by asking why five times, and write down what was learned, not who erred.
- **Parts:** practice failure on purpose (game days, chaos tools); reward people who find errors; make errors ordinary so no one hides them.
- **When to use:** Post-incident reviews and quiet periods.
- **How to score:** 5 if findings change a mechanism; 1 if the review names a person.
- **Quote:** "A key element of our cause-of-error method is asking 5 'Why?' questions" (S048)
- **Sources:** 3 (S048, S098, S099).

## 12. Consistency as a tradeoff (N, W, R and CAP)
- **What it is:** With N replicas, W write acknowledgements and R read replicas, W plus R above N gives strong consistency; networks partition, so consistency and availability cannot both be total.
- **Parts:** spectrum from strong to eventual; tune the window to what the user notices; write-always carts that merge later; choose per use.
- **When to use:** Choosing a data store, or deciding what may be briefly stale.
- **How to score:** 5 if each data type has its tolerance named; 1 if the whole system takes the strictest or the loosest setting.
- **Quote:** "If W+R > N, then the write set and the read set always overlap and one can guarantee strong consistency." (S063)
- **Sources:** 5 (S032, S063, S069, S070, S099). The Dynamo paper adds: push conflicts to reads so writes are never rejected (S070, "the paper").

## 13. Purpose-built data stores (audit the access pattern first)
- **What it is:** Look at what the operations really do, then choose the store. One engine for everything is the "big hammer".
- **Parts:** measure the mix (about 70 percent key-value lookups at Amazon); one database per service; use relational only for joins, complex queries and transactions.
- **When to use:** Picking or splitting a database.
- **How to score:** 5 if a measured access mix drives the choice; 1 if fashion or habit does.
- **Quote:** "We found that about 70 percent of our operations were key-value lookups, where only a primary key was used and a single row would be returned." (S041)
- **Sources:** 6 (S037, S041, S047, S057, S058, S099).

## 14. Working Backwards and the PR/FAQ, amended
- **What it is:** Write the press release and FAQ before building. In 2025 he added: if the customer problem is clear but the approach is unproven, prototype first.
- **Parts:** press release, FAQ, customer experience, user manual; tenets; revise, since "I’ve never seen someone get it right the first time" (S016).
- **When to use:** Defining a product; use the prototype-first variant under real technical uncertainty.
- **How to score:** 5 if the doc exists and a customer would read it; 1 if it only restates the feature list.
- **Quote:** "You will learn more in one evening of building than in two weeks of writing about what you think will happen." (S004)
- **Sources:** 4 (S004, S016, S076, S052). Newer view: S004 (2026).

## 15. Loose coupling and asynchrony
- **What it is:** Synchrony is a simplification. Independent parts that communicate by events isolate failure and can replay what they missed.
- **Parts:** queue, publish/subscribe, stream; replicators that restart and re-read; no two-phase commit across regions; small parts with standard interfaces.
- **When to use:** Anything crossing a slow or unreliable link.
- **How to score:** 5 if a down consumer catches up on return; 1 if one slow call stalls the chain.
- **Quote:** "It is a natural way of isolating failures." (S106)
- **Sources:** 4 (S038, S094, S106, S098). He concedes it looks harder than synchronous code (S106).

## 16. You build it, you run it (two-pizza ownership)
- **What it is:** A small team owns a service end to end, including operations.
- **Parts:** teams small enough that all know the work; hire people uncomfortable without end-to-end ownership; short feedback loop.
- **When to use:** Team design and on-call.
- **How to score:** 5 if one team answers the pager for what it ships; 1 if development and operations are separate queues.
- **Quote:** "Two pizzas were always about ownership culture, and the tools have caught up to the culture." (S004)
- **Sources:** 6 (S004, S038, S045, S076, S105, S106).

## 17. Provably correct, not probably correct
- **What it is:** For all-or-nothing changes, tests are necessary but not enough; add proofs, model checking, and checks of runnable code.
- **Parts:** TLA+, automated reasoning, small executable models checked on every commit (Warfield's S3 work, credited to him).
- **When to use:** Money, security, consistency, and any AI-generated code.
- **How to score:** 5 if the key invariant is stated and machine-checked; 1 if "it passed the tests". Cost: it can take more work than the build itself.
- **Quote:** "We want a system that’s “provably correct”, not just “probably correct.”" (S032)
- **Sources:** 5 (S007, S032, S039, S093, S105).

## 18. Throttle, fail fast, back off
- **What it is:** Under overload, a service sheds load and a client retries gently, so a struggling part can recover.
- **Parts:** throttle when overwhelmed; fail fast and release resources; exponential back-off; circuit breaker on non-critical downstreams; avoid bimodal recovery; one simple restart can beat trees of error handling (the Multics and UNIX panic story).
- **When to use:** Calls between services, and clients of your own API.
- **How to score:** 5 if retries are bounded and capped; 1 if every client retries at once.
- **Quote:** "you have to throttle if you get overwhelmed don't try to do all the work" (S098)
- **Sources:** 1 (S098); related S040.

## Books

### Books: Werner Vogels

No book of his own appears in the corpus. His major series and essays, in my own words:

#### The Frugal Architect (2023 keynote, relaunched 2024; thefrugalarchitect.com)
- **Core thesis:** Cost, sustainability and security belong beside reliability as design requirements. Laws in three groups (design, measure, optimize): align cost with revenue, define your meter, cost per request falls over time.
- **Key frameworks:** see frameworks.md 6. Taught in S104, S015.

#### Working Backwards (blog post 2006; amended 2026)
- **Core thesis:** Write the press release and FAQ before building; in 2026 he adds prototype-first when the approach is unproven.
- **Taught in sources:** S076, S016, S004.

#### Eventually Consistent (2007 draft, 2008 revision, ACM Queue)
- **Core thesis:** Consistency is a spectrum; networks partition, so choose per use. N, W, R quorums.
- **Taught in sources:** S069 (draft, superseded), S063.

#### Dynamo (2007 paper, co-authored; his 2012 DynamoDB post)
- **Core thesis:** Treat failure as normal, never reject writes, keep the tail good for all customers. Credit: "the paper".
- **Taught in sources:** S070, S058, S047, S057.

#### 10 Lessons from 10 Years of AWS (2016)
- **Core thesis:** Build evolvable systems, expect the unexpected, offer primitives, automate, know every cost dimension, security from day one (S052).

#### Re:Invent keynotes (2015 to 2025)
- Failure and cells (S098, S099), asynchrony (S106), cost (S104), ownership and AI (S105). Guest segments excluded.

#### Books he recommends (not his)
- Transaction Processing (Gray, Reuter); the 4.3 BSD Unix OS book (S036); Gall's Systemantics; Donella Meadows on leverage points (S105); Chaos Engineering (S098); Ask Your Developer (S010); A Thousand Brains (S001).
