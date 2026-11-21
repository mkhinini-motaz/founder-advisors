# Positions: Werner Vogels

28 topics. Each stance has a verbatim quote, source id and date (post or keynote date, from `sources.md`). Where he moved, versions sit side by side with dates. Topics with no evidence say so. The Dynamo paper (S070) is "the paper".

## Availability targets
- **Stance:** Not every part needs the same uptime; the business picks how much to pay.
- 2017-12: "it’s business rules that drive availability choices as much is that we all want a hundred percent available systems they actually cost money" (S098)
- 2023-11: "Probably as much as you can, because that always needs to be on, because without that, you don't have a business. Replicate over three AZs at minimum." (S104) (tier one only)

## Redundancy and multi-region
- **Stance:** Redundancy is the first defence, if it does not cost performance. Cross-region traffic is asynchronous and ring-fenced.
- 2006-03: "Introducing redundancy is an important first line of defense against" (S080)
- 2018-03: "we take enormous care to ensure that the dependencies and calling patterns between Regions are asynchronous and ring-fenced with high-level safety mechanisms that prevent errors from spreading." (S043)

## Single points of failure and scale-up
- **Stance:** Do not scale up one box; it is a single unit of failure. 2018-11: "scale-up really gave us a single unit of failure that we just really couldn't handle" (S099)
- **Story:** the 12 December 2004 database outage (S099).

## Monolith versus microservices
- **Stance:** Neither is a religion. Start with a monolith; split when scaling, reliability or security needs differ.
- 2019-08: "Most companies, like Amazon, start their business with a monolithic application because it’s the fastest, easiest system to develop." (S038)
- 2023-05: "Building evolvable software systems is a strategy, not a religion." (S024) A five-engineer startup may rightly choose a monolith.

## Build versus managed service
- **Stance:** Let a managed service carry the lifting that does not set you apart.
- 2012-01: "developers strongly preferred simplicity to fine-grained control as they voted “with their feet”" (S058) Vendor claim; test it.
- 2007-02: "you’re better of letting somebody else worry about all of this, so store your data in S3 :-)" (S074)
- 2017-12: "the more managed services you use the less moving parts you have" (S098)

## Simplicity
- **Stance:** The test is fewer assumptions and fewer moving parts, but not fewer parts at any cost.
- 2024-05: "I subscribe to the idea that systems should be made as simple as possible, but no simpler." (S018)
- 2015-10: "no server is easier to manage than no server." (S100)
- 2021-04: "We thought back to the core design principle of simplicity." (S032)

## Testing and correctness
- **Stance:** Tests are not enough for the critical part. Over time: 2019 he showed proofs for security (S039); 2021 consistency (S032); 2025 he extends it to AI-generated code (S093, S105).
- 2019-06: "That's a much higher bar than just having a “reasonable assurance” of no weak keys" (S039)

## Database choice
- **Stance:** Look at the real access pattern; use several stores.
- 2018-06: "Instead of the use case driving the requirements for the database, it was the other way around." (S041)
- 2013-03: "relational databases should only be used when an application really needs the complex query, table join and transaction capabilities of a full-blown relational database." (S057)
- Limit: 2018-06: "This doesn't mean relational databases do not provide utility in present-day development" (S041)

## Consistency and stale data
- **Stance:** Choose per use. 2008-12: "There is a range of applications that can handle slightly stale data, and they are served well under this model." (S063)
- 2021-04: after 15 years he moved S3 to strong consistency because customers had built it themselves (S032). Both views held in time: eventual was right for 2006.

## Tail latency
- **Stance:** Averages hide the unhappy customers. 2008-10: "We don't really care that much about averages or medians" (S065) The paper (S070) priced the 99.9 percent mark.

## Cost and frugality
- **Stance:** Cost awareness is a skill the cloud made easy to lose.
- 2023-11: "Cost awareness is a lost art." (S104)
- 2008-10: "frugality is essential in our retail business." (S065)
- 2023-11: "constraints, even self-imposed, can breed creativity." (S104)

## Pricing
- **Stance:** Price so your cost shows: 2023-11: "Cost following means that we expose our costs to you." (S104) S3 added a third price dimension (requests) after real use (S052, S104).
- Discounting: no recorded position beyond passing savings on: 2013-03: "we are happy to pass the savings along to you." (S057)

## Hardware and rented servers
- **Stance:** Do not plan for peak on owned hardware. 2012-08: "Owning your own hardware is extremely inflexible, you have to over-scale and plan for peak demand and if you make a mistake with the type of hardware you are stuck with it." (S055)
- 2023-11 caution: "if you just do lift and shift of something that wasn't scalable and efficient in your own datacenter, it isn't certainly scalable and efficient in the cloud either." (S104)

## Security
- **Stance:** First priority and everyone's job. 2017-12: "protecting your customer should be your number one priority without that you don't have a business" (S098) and "you as developers have to become security engineers" (S098).
- 2016-03: "The security team is not a group that does validation after something has been built." (S052)

## Encryption
- 2017-12: "encrypting your data both in transit any West should be your default behavior" (S098)

## Speed of decisions
- **Stance:** Move fast on reversible choices. 2026-06: "The cost of a wrong reversible decision is almost always lower than the cost of making that decision slowly." (S004) 2017-06: "most decisions should probably be made with somewhere around 70% of the information you wish you had." (S048, quoting Bezos)

## Hiring and team size
- **Stance:** Small teams that own the problem. 2026-06: "You fight it by hiring people who are uncomfortable when they don’t own their problem end-to-end" (S004)
- First hire, firing, equity, partners: no recorded position.

## Teams, process and writing
- **Stance:** Write to think; read together. 2024-12: "When it’s ready, we get together, read silently and take notes, then discuss." (S014)
- 2026-06: "Writing is still as important as ever, and it should be you doing the writing, not your AI." (S004)

## Blame and mistakes
- **Stance:** No culprits; learning only. 2017-06: "And when errors become 'business as usual', no one will be afraid of taking a risk" (S048) and "reward employees when they find errors" (S048). Limit: it is empty if people fear repercussions (S048).

## AI and reliability
- **Stance:** A tool; the owner is accountable.
- 2023-04: "I think it’s much more in the tooling space than it is in sort of the shifts we saw with object orientation or functional programming" (S026)
- 2025-11: "AI in the human loop, not the other way around." (S009)
- 2025-12: "Vibe coding is fine, but only if you pay close attention to what is being built." (S105)

## AI hype and adoption
- 2025-10: "New tech, same patterns." (S010)
- 2025-12: "I think as a business there is no shame in hitting the Pause button for a moment" (S093)
- 2025-12: "Most of this is fear of missing out." (S105)

## AI and jobs
- 2023-04: "As a result, there will be more work than ever." (S020) 2025-12: "Will AI make me obsolete? Absolutely not. Yeah. If you evolve." (S105)

## Customers and the roadmap
- **Stance:** Customers drive it. 2016-03: "This is why we deliver new services often with a minimal feature set and allow our customers to help drive the roadmap for extending the service with new features." (S052) "90% of our roadmap at AWS comes directly from customers" (S032)

## Competition
- 2014-02: "our energy at Amazon comes from the desire to impress customers rather than the zeal to best competitors." (S053)

## Sustainability and efficiency
- 2021-12: "the greenest energy is the energy we don’t use." (S030) 2023-11: "cost is a pretty good approximation for sustainability" (S104)
- Earlier view 2021: high availability need not waste (S030).

## Quantum security
- 2025-12: "And the focus is not that quantum is five years away, the most important part there is that we need to keep ourselves and our businesses safe." (S093) Earlier timeline was longer; compressed in 2025 (S009).

## Predictions
- 2025-12: "And always when I read them, I always felt that they were a bit self-serving." (S093) 2025-02: "20/20 is average. It is a baseline." (S013)

## Burnout and work hours
- One afternoon a week to learn, offline: "I dedicate one afternoon a week to learning, turning off my phone and email" (S014) Otherwise no recorded position.

## Raising money, debt, selling the company, brand, paid ads, remote work, niche
- No recorded position. (Do not guess.)
