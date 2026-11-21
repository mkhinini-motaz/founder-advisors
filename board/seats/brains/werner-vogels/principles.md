# Principles: Werner Vogels

20 decision rules built from his own passages (guest bodies excluded). "Sources" is the number of distinct sources that state or apply the rule. Confidence: high = 3 or more sources, medium = 2, low = 1.

1. **Design for failure from day one.** "everything fails, all the time" (S032) "Failures are a given and everything will eventually fail over time" (S052) Sources: 8 (S032, S040, S052, S063, S074, S098, S099, S070). Confidence: high.

2. **At scale, rare means daily.** "even if something happens only once in a billion requests, that means it happens multiple times per day within S3." (S032) "events that normally have a low probability of occurrence are now guaranteed to happen and need to be accounted for up front in the design and architecture of the system." (S063) Sources: 2 (S032, S063). Confidence: medium.

3. **Keep running when part of it is in trouble.** "Systems need to keep running even if the “house is on fire.”" (S052) "A write can be successful and fast even when something is broken." (S040) Sources: 3 (S040, S052, S070). Confidence: high.

4. **Do not assume failures are independent.** "failures frequently are correlated, as they are often triggered by external or environmental events." (S077) "Given that disks in general arrive in large batches you may want to take care with how you deploy these disks" (S074) Sources: 2 (S074, S077). Confidence: medium.

5. **Limit how far a fault travels.** "if something fails the minimum set of customers should be affected" (S099) "we never want to touch more than one zone at a time" (S043) Sources: 5 (S040, S043, S052, S098, S099). Confidence: high.

6. **Reliability is a business decision, so price it.** "it’s business rules that drive availability choices as much is that we all want a hundred percent available systems they actually cost money" (S098) Sources: 3 (S093, S098, S104). Confidence: high.

7. **Decide the tiers first.** "So, before all of that, what's my advice there is, you know, establish your tiers." (S104) "Replicate over three AZs at minimum." (S104) for tier one only. Sources: 4 (S093, S098, S104, S105). Confidence: high.

8. **Know your dependencies.** "figure out exactly what do you do with your dependencies and how do you depend on them" (S098) A hard dependency lowers the ceiling to the product of both. Sources: 1 (S098). Confidence: low.

9. **Simple parts are the route to reliability.** "the more simpler things are, the more reliable they will be." (S100) "a complex system that works has invariable been found to have evolved from a simple system that works" (S098) Sources: 4 (S098, S100, S106, S018). Confidence: high.

10. **Fewest assumptions wins.** "if two approaches produce the same result, select the one with the fewest assumptions." (S077) Sources: 1 (S077). Confidence: low.

11. **Measure the tail.** "If 50% latency on your webpage means nothing… well, it means that 50% of your customers are getting a worse experience. You need to know how much worse." (S093) The paper chose 99.9 percent on a cost-benefit basis (S070). Sources: 5 (S058, S065, S070, S079, S093). Confidence: high.

12. **Treat configuration like code.** "configuration changes cause outages at about the same rate as code changes." (S031) "continuous configuration reduces the fear of changing configuration." (S031) Sources: 1 (S031). Confidence: low.

13. **Deploy small and in sequence.** "we do deployment deploy them to default isolation zones in sequence not all at the same time" (S098) Sources: 3 (S031, S043, S098). Confidence: high.

14. **Build the mechanism, not the promise.** "But without a mechanism, nothing changed because everybody already has good intentions." (S105) "Now, you can't just rely on good intentions, you need to put mechanisms in place" (S104) Sources: 3 (S045, S104, S105). Confidence: high.

15. **Cost is a design input at every step.** "you have to consider cost at every step of your design to really keep that in mind" (S104) "Unobserved systems lead to unknown costs" (S104) Sources: 4 (S015, S052, S055, S104). Confidence: high.

16. **Make cost follow revenue.** "So, align cost with revenue." (S104) "If the application scales along the right revenue generating dimensions these costs will be in line with the revenue being generated." (S065) Sources: 2 (S065, S104). Confidence: medium.

17. **Turn off what you do not use.** "When you go home at night, do you turn off your development environment? You should." (S104) "the greenest energy is the energy we don’t use." (S030) Sources: 3 (S030, S094, S104). Confidence: high.

18. **Match resilience to the workload.** "This doesn’t mean we don’t architect for high availability" (S030) Not every application needs multi-zone (S094). Sources: 3 (S030, S094, S098). Confidence: high.

19. **Whoever ships it owns it.** "You are still responsible for what you deliver." (S093) "Remember, the work is yours, not that of the tools." (S105) Sources: 3 (S004, S093, S105). Confidence: high.

20. **Verify, do not hope.** "Code arrives instantly, but comprehension does not." (S105) "the review becomes the control point to restore balance." (S105) Sources: 4 (S007, S032, S093, S105). Confidence: high.

21. **Reversible choices need no permission.** "If the decision was reversible, you didn’t need permission to make it." (S004) Sources: 3 (S004, S024, S035). Confidence: high.

22. **Launch minimal and rock solid, let customers steer.** "we launched without it if a minimal feature set that was rock solid" (S098) "We wanted them to get their hands dirty and then see what they were doing with it and where they would start to complain about." (S094) Sources: 5 (S016, S033, S052, S094, S098). Confidence: high.

23. **Remove undifferentiated work.** "the more managed services you use the less moving parts you have" (S098) Sources: 6 (S020, S030, S038, S058, S094, S098). Confidence: high.

24. **Do not let hype set the architecture.** "There is no hurry. There is no hurry. No company will go out of business in the coming two months because they weren’t using AI." (S093) Sources: 3 (S010, S093, S105). Confidence: high.

25. **Question the old choice even when it worked.** "I don’t want you to immediately start sort of throwing away everything that you know and starting over" (S104) is his limit on the push: "We always need to dis-confirm our own beliefs." (S104) Sources: 3 (S015, S024, S104). Confidence: high.
