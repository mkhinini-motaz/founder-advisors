# Frameworks: David Heinemeier Hansson

Built from the extraction notes on 90 sources (interviews, his blog, REWORK podcast episodes, 2018 to 2026). Most-used first. "Score" lines are guidance inferred from his stated thresholds, not his own scoring system.

## 1. Omakase, convention over configuration
- **What:** ship the whole menu, with one chosen answer for each detail that does not matter, so the builder spends time on the decisions that do.
- **Parts:** pick defaults; keep substitutions possible; day one starts complete; the maker is the chef.
- **When:** choosing defaults for a product, a tool stack or an internal system.
- **Score (guidance):** each option you hand the customer is a decision you did not make. Count the knobs; fewer is better unless the knob defines the product.
- **Quote:** "I’m not just handing you a box of fucking Legos and asking you to build the Millennium Falcon. I’m giving you a finished toy." (S001)
- **Sources:** S001, S002, S005.

## 2. The majestic monolith (partition with modules, not networks)
- **What:** compress concepts until the whole system fits in one head. Start and stay with one integrated app; split only on evidence.
- **Parts:** stop digging; consolidate dependent paths first; leave isolated hotspots last; at most two backend languages; modules, not networks.
- **When:** any architecture choice for a small team.
- **Score (guidance):** he calls trouble past about half a million lines and 20 programmers. Basecamp and HEY are each just over 100,000 lines of Ruby (S001).
- **Quote:** "The vast majority of systems are much better served by starting and staying with a majestic monolith." (S072)
- **Sources:** S001, S072, S073, S051.

## 3. The one-person framework
- **What:** a toolkit strong enough that one person builds a modern app and a competitive business on it.
- **Parts:** conceptual compression (hide the physics you do not need); full stack in one box; delay specialist hiring as late as possible.
- **When:** judging whether a stack or a plan needs a big team.
- **Score (guidance):** if one programmer cannot take an idea to production, he says the setup is too complicated.
- **Quote:** "A toolkit so powerful that it allows a single individual to create modern applications upon which they might build a competitive business." (S107)
- **Sources:** S005, S107, S081, S001.

## 4. Default team of two, small as a destination
- **What:** one programmer, one designer, one feature. Basecamp and HEY were each defined by about three people before the rest joined.
- **Parts:** no roadmap or methodology to start; build, look, follow what the product tells you.
- **When:** staffing a new product or feature.
- **Score (guidance):** if a feature needs more than two builders, ask what is wrong with the scope.
- **Quote:** "our default team size is two. One programmer, one designer, one feature." (S001)
- **Sources:** S001, S008, S081.

## 5. As small as is not negligent
- **What:** stay the smallest company that still answers customers and ships. Complexity grows faster than headcount.
- **Parts:** cut products before hiring up; no full-time managers; remove needless words, paragraphs and process.
- **When:** any hiring or reorganisation decision.
- **Score (guidance):** he settled near 60 people after tests at 80 (S006, S033). Above that, ask which role a customer would miss.
- **Quote:** "So I want to be as small as is not negligent to be." (S003)
- **Sources:** S003, S004, S006, S033.

## 6. Buy the baseline, rent the spike (cloud exit test)
- **What:** compare the bill with what faster computers should cost. Own what you use steadily; rent only spiky or immaterial need.
- **Parts:** do your own math; rent cabinets and white-glove hands, not your own data centre; keep the exit trivial; sign multi-year terms only for storage.
- **When:** any rent-versus-own choice for infrastructure or tools.
- **Score (guidance):** his case: 3.2 million dollars a year at peak, seven apps moved in about six months, no extra hire, spend cut by a half to two thirds. He says cloud fits regular 5 to 10 times spikes or very early companies.
- **Quote:** "if you regularly do face 5-10x or higher spikes in demand over baseline, you may indeed be a good candidate for cloud." (S054)
- **Sources:** S001, S054, S062, S084, S097, S005.

## 7. Human cores, not CPU cores
- **What:** pick tools by the cost of human capacity to understand a system, not by raw machine speed.
- **Parts:** latency per request (target 100 ms, 300 ms at most) versus boxes; the economics of the bill.
- **When:** language, framework or vendor debates.
- **Score (guidance):** work out what share of the budget the technology line is. He found about 15% of operating budget in app servers, so doubling speed moved costs about seven points (S001).
- **Quote:** "it’s not CPU cores. It’s web cores, it’s human cores. It’s human capacity to understand and involve systems." (S001)
- **Sources:** S001, S005.

## 8. Half a product, not a half-assed product
- **What:** cut scope, never quality. A half-ass thing needs its second half to work.
- **Parts:** fixed time and people; park ideas as V1.1; fidelity can drop, quality cannot (see the quote below).
- **When:** scoping a first release.
- **Score (guidance):** list what you left out; if the thing still works alone and is well built inside, it is a half. If it needs the missing piece, it is not.
- **Quote:** "the back of the cabinet has to be good too." (S008)
- **Sources:** S007, S008.

## 9. Launch before it feels ready (fidelity versus quality, criticality dial)
- **What:** the more novel the hook, the more table stakes you can skip. Set test depth by how much damage a bug can do.
- **Parts:** fidelity versus quality; process dial from zero (presentation tweaks) to long QA (data-mutating features); launch with a backpack.
- **When:** deciding when to ship and how much to test.
- **Score (guidance):** limit applies when competing against an established product: against a dominant email product, HEY needed over a year to add table stakes (S007).
- **Quote:** "If you’re not uncomfortable by the time you’re launching, it’s way too late." (S007)
- **Sources:** S007, S008.

## 10. Do not take other people's money (the VC steroid program)
- **What:** venture capital turns every business into one of ten bets and accepts losing most of them. Outside money installs time bombs against running a company for 20 years.
- **Parts:** profit pays for growth; compounding; owners keep decisions.
- **When:** any fundraising question.
- **Score (guidance):** he treats a 5 to 10 million dollar a year business as a success, which a Series A investor would call a failure (S011).
- **Quote:** "The logic of venture capital is to rush every business it touches through a steroid program that accepts a mortality rate of up to 90%." (S096)
- **Sources:** S001, S003, S005, S010, S011, S096.

## 11. Hedge, not investment (the secondary sale)
- **What:** sell a small non-control slice of founder shares to a strong investor, take the cash personally, put none into the company.
- **Parts:** proceeds go to founders; no board seat; the buyer endorses what you already do.
- **When:** founders who want security without the growth pressure.
- **Score (guidance):** only fits a company already profitable. He calls it a vaccine against taking larger venture checks.
- **Quote:** "Not put any of it into the company." (S003)
- **Sources:** S001, S003.

## 12. Managers of one, moonlighting managers
- **What:** hire people who do not need weekly one-on-ones; let senior individual contributors manage on the side.
- **Parts:** processes first (check-in questions, six-week cycles with two-week cool-downs, hill charts); each lead has one mentee.
- **When:** designing a team around 60 people or fewer.
- **Score (guidance):** he warns it would be hard at hundreds or thousands (S033). Tested the opposite twice and rejected it twice (S006).
- **Quote:** "We once more have no full-time managers whose sole function is to organize or direct the work of others." (S033)
- **Sources:** S001, S006, S033, S066.

## 13. Calm company: chart the course, set the pace, hold the line
- **What:** the three duties of an executive; calm is a method to reach ambition.
- **Parts:** 40 hours or fewer; no ASAP; long uninterrupted blocks; a hard end to the day; judge the work, not seat time.
- **When:** deciding a company's operating rhythm.
- **Score (guidance):** he asks whether the hours are good, not whether there are many.
- **Quote:** "Setting the pace isn't about demanding more hours, it's about demanding more from those hours." (S043)
- **Sources:** S001, S003, S004, S042, S043, S047.

## 14. The simplest thing that could possibly work, you aren't gonna need it
- **What:** the two mottos from Kent Beck that move all his programming. Do not build the general solution until the problem has appeared twice.
- **Parts:** extraction by pattern matching on the second sighting; remove moving parts as the platform improves.
- **When:** any design or scoping argument.
- **Score (guidance):** if a future need is imagined, not seen twice, leave it out.
- **Quote:** "To this day, these are the mottos that move all my programming work forward." (S082)
- **Sources:** S003, S041, S082.

## 15. Finished software and buy-once (ONCE)
- **What:** not all software must evolve forever; sell a product once, self-hosted, and let the customer own it.
- **Parts:** single-tenant, SQLite, one box; no forced upgrades; the maker is not a single point of failure.
- **When:** pricing and packaging a small business product.
- **Score (guidance):** he admits the marketing is unsolved: it sounds too good to be true (S046). Campfire sold 250,000 dollars in under a week (S046).
- **Quote:** "We've become so used to digital services being malleable that we've confused the possibility of software updates with their necessity." (S052)
- **Sources:** S046, S050, S052, S092.

## 16. Price at what you would pay yourself
- **What:** build the v1 you need, price it where you would buy, and never hassle a customer who cancels.
- **Parts:** cap enterprise pricing (Basecamp at 299 dollars a month for unlimited users); do not A/B test core values; easy cancellation.
- **When:** setting prices, cancellation flows and growth experiments.
- **Score (guidance):** an easy metric that wins by a dark pattern is rejected, however well it converts.
- **Quote:** "I can't in good conscience sell software at prices where I'd never pay." (S068)
- **Sources:** S011, S068, S089, S046.

## 17. Test the opposite
- **What:** a conviction untested for too long gets run in reverse as an experiment.
- **Parts:** pick the belief; run its opposite for a bounded time; keep what is weathered.
- **When:** a policy has gone unchallenged for years.
- **Score (guidance):** he hired engineering managers twice and dropped them twice, and says he is glad he tried.
- **Quote:** "Whatever we’re doing, could the opposite be better?" (S006)
- **Sources:** S001, S006.

## 18. Take 1, 2, 3, 4 (make it work, right, beautiful, simple)
- **What:** repeated passes on the same work. The first draft is bad; pride comes from refining.
- **Parts:** work, right, beautiful, simplify.
- **When:** reviewing code, copy or a product before release.
- **Score (guidance):** ask which pass the work is on. Shipping take 1 is fine for low-criticality work.
- **Quote:** "Okay, take 2; let’s make this right. Okay, take 3; let’s make this beautiful. Okay, take 4; let’s simplify this." (S003)
- **Sources:** S003, S002.

## 19. Whoever cares most; stop talking and start making
- **What:** settle a dispute by conceding to whoever does the work or cares most, then try the smallest disprovable test.
- **Parts:** disagree and commit; trust each other's area; do not co-found with someone who does your exact job.
- **When:** partner or team disagreement.
- **Score (guidance):** if the test costs less than the meeting, run the test.
- **Quote:** "stop talking and start making." (S004)
- **Sources:** S001, S004.

## 20. Be vague first, then use it; pick from three
- **What:** nobody knows what software should do until they use it. Write a little, use it, steer. With agents, ask for three options and let taste choose.
- **Parts:** do not specify upfront; one differently sourced model reviews the first; tell the agent to make it simpler.
- **When:** early product work and agent-assisted building (newer view, 2026).
- **Score (guidance):** he cut a long, over-prescriptive instruction file by 80% when a newer model arrived (S002).
- **Quote:** "Be as vague as you can to manifest something, then interact with the something." (S002)
- **Sources:** S002.

## 21. Know the scale you are at
- **What:** do not borrow the tools or rules of a giant. Modelling your stack on Netflix is a siren song for the other 99.99%.
- **Parts:** check whether your facts are out of date; match the tool to the problem's size.
- **When:** someone cites Google, Amazon or Meta as precedent.
- **Score (guidance):** ask how many programmers and requests the cited firm has versus you.
- **Quote:** "you don’t, I don’t know, use your Pagani to go pick up groceries at Costco." (S001)
- **Sources:** S001, S051, S107.

## Books

### Books: David Heinemeier Hansson

Built from 90 sources. Summaries are in my own words. Never reproduce book text.

- **Getting Real (37signals, 2006).** Build less software and treat small as an advantage. Taught in S001.
- **REWORK (37signals).** Short, jargon-free essays that give entrepreneurs permission to stay small, run calm, and skip the hockey stick. Halved in the last edit, 87 essays, over a million copies (S047). The REWORK Revisited episodes (S007 to S010) walk its chapters; his favourite essay is "Inspiration is perishable" (S001). Co-written with Jason Fried: attribute only lines the notes give to him.
- **Remote: Office Not Required (2013).** A decade early; the case for distributed work (S011).
- **It Doesn't Have to Be Crazy at Work (2018).** 40 hours is enough if you do not waste it in meetings (S001).
- **Shape Up (37signals method).** Six-week budgets with a cool-down, fixed time and variable scope (S008).
- Books he draws on, not his own: Patterns of Enterprise Application Architecture (Fowler) for ActiveRecord (S001); The Innovator's Dilemma (Christensen) on mature firms avoiding the big call (S105); Bullshit Jobs (Graeber) on pointless work (S002, S104); Drive (Pink) on motivation (S003, S108); Maverick (Semler) on a radical company design (S003); The E-Myth Revisited (Gerber), which he now rejects: the baker should run the bakery (S009).
- No book on Rails is covered in the sources beyond the above.
