# Frameworks: Gerd Gigerenzer

Built from 42 sources (315,272 words, talks, lectures, podcasts and interviews, 2015 to 2026, plus an Edge interview from about 2003). Most-used first. Scoring lines are guidance for a council call, built from his own thresholds; he gives no scorecards himself.

## 1. Risk versus uncertainty
What it is: risk means all outcomes, consequences and probabilities are known (roulette, lottery), so you can calculate and optimize. Uncertainty means some of those are unknown or can change (a start-up, a hire, a marriage, a financial crisis), so you cannot find the best option and you need robust rules. He says it is a continuum, not a strict dichotomy (S024, S034).
Steps: (1) ask which world you are in; (2) in risk, use probability theory; (3) in uncertainty, use heuristics, trust and judgment; (4) never carry the best decision under risk over to uncertainty.
Use when: any forecast, model, optimizer or "expected value" claim is offered for a decision about the future.
Score (guidance): count what is unknown (alternatives, consequences, probabilities). Three known means risk. Any unknown pushes toward simple and robust.
Quote: "In the real world, 37s happen." (S010) Also "the best decision under risk is not the best decision under uncertainty" (S014).
Sources: 25 or more, among them S001, S002, S004, S006, S010, S011, S014, S015, S017, S019, S020, S024, S027, S028, S037.

## 2. The stable world principle
What it is: complex algorithms and big data beat people where tomorrow is like yesterday and the rules are fixed (chess, Go, protein folding, routine industry tasks, language corpora). Where the world is unstable (human behaviour, crime, viruses, cancer therapy, investing), there is little evidence they beat simple rules or experienced people.
Steps: (1) ask if the target is stable and well defined; (2) if yes, trust the machine; (3) if no, keep your hands off or demand a real-world test; (4) ask who is selling it.
Use when: a vendor, consultant or model promises prediction of customers, field staff, fraud, demand or crime.
Score (guidance): stable plus lots of data plus few options means complex is fine. Unstable plus many options plus little data means simple.
Quote: "if you're on a stable world then trust it if you're in an uncertain world don't" (S012)
Sources: 16, among them S003, S008, S009, S012, S016, S019, S026, S030, S031, S035, S036, S038, S039, S045.

## 3. Ecological rationality (Simon's scissors)
What it is: rationality is the fit between a strategy and the structure of the environment, not consistency with logic. Simon's scissors have two blades, mind and environment. No heuristic is good or bad per se. It is a research program with formal models and proofs, not a story.
Steps: (1) formalize the heuristic; (2) ask in which environments it beats the complex rival; (3) say where it fails.
Use when: someone calls a rule "irrational" or "a bias", or defends a method in the abstract.
Quote: "the rationality is not about consistency inside the mind but about the success in the world" (S011). Also "a heuristic is not good or bad per se but it really works in certain environments" (S017).
Sources: 17, among them S001, S002, S004, S006, S011, S012, S015, S017, S020, S024, S027, S033, S037, S043, S046.

## 4. Less is more and the bias-variance trade-off
What it is: total error is bias plus variance (plus noise). Under uncertainty, many free parameters and little data, a flexible model fits the past and scatters on the future. A simple rule with no free parameter has zero variance and only bias, and it can win. The accuracy-effort trade-off is a law only in a world of risk. The London temperature polynomials show it: a degree-12 fit is best on past data and worst at prediction.
Steps: count the parameters, count the data, ask whether the future will look like the past.
Use when: a model is judged by how well it fits history.
Score (guidance): the more parameters per data point and the less stable the world, the more simple wins.
Quote: "fit is not the goal of science, nor of an investor. You want to predict." (S006) Also "it may be better to have a bias than no bias" (S020).
Sources: 12, among them S004, S006, S014, S015, S017, S020, S024, S028, S031, S032, S037.

## 5. 1/N (equal weights)
What it is: split money equally across N options. It has no parameters and uses no data. Markowitz used it for his own retirement money, and in six of seven investment tests it beat mean-variance optimization. With 50 assets, a simulation says the optimizer needs about 500 years of data to have a good chance. He says Markowitz's model is not wrong; it works when its assumptions hold (S032).
Use when: many options, noisy estimates, short history (allocating a budget across sites, regions, channels).
Quote: "It ignores all data. It's the opposite of big data." (S004)
Open question he admits: "We have no complete answer to the question when the 1/N will outperform Markowitz and vice versa." (S004)
Sources: 14, among them S004, S006, S011, S014, S015, S017, S018, S020, S022, S024, S027, S028, S032, S039.

## 6. Recency heuristic and Google Flu Trends
What it is: predict the next value as the latest one, ignoring the rest. For flu, visits two weeks ago beat Google's big-data model (50 million search terms, about 45 variables, then more) every year over eight years. When the swine flu came out of season, Google added complexity. He would have simplified.
Use when: a volatile series (orders, demand, wait times) is forecast with a heavy model.
Quote: "recency takes just the last data point." (S031) Also "it's called the recency juristic the recy juristic just look for the latest data point and predicts and ignores all the rest" (S011, caption spelling).
Limit: it is wrong in a stable world and gets the surprise wrong once, then recovers (S011, S036).
Sources: 14, among them S003, S004, S008, S011, S016, S024, S026, S030, S031, S033, S035, S037, S046.

## 7. Hiatus heuristic (customer inactive after nine months)
What it is: a customer who has not bought for nine months is inactive, otherwise active. It beat the Pareto/NBD model in an airline (77 against 74 percent), an apparel business (83 against 75) and a CD business, and on average across 24 businesses also beat logistic regression and random forest. Marketing professors who set out to refute it changed their minds (S024).
Use when: you must classify churned or active customers, partner shops or field staff.
Score (guidance): change the interval for the business; do not fine-tune it.
Quote: "If a customer hasn't bought for 9 months classify as inactive, otherwise active." (S006)
Sources: 4 (S006, S014, S024, S034).

## 8. Fast-and-frugal trees and one-good-reason rules
What it is: an incomplete decision tree with n questions and n+1 exits, no probabilities, no utilities. Each question can end the decision, so a failure on one cue is not compensated by another (non-compensatory). Examples: three questions for chest-pain triage (it beat a 25-cue regression card going forward), three for bank failure with the Bank of England (leverage ratio first), three for London bail courts, and the hiring tree attributed to Bezos: exceptional ability, do I admire the person, will they raise the team's average.
Conditions: a single cue can match any linear model when its weight is at least as large as all the others combined (dominant cue), about 80 to 97 percent of datasets he checked in S015 and S017.
Use when: triage, screening of shops, hiring, fraud holds, anything a regulator or a busy person must read and remember.
Quote: "If your heart fails, a good liver doesn't help you." (S033) Also "It is non-compensatory. If you fail on the first one, that's it. Period." (S020)
Sources: 12, among them S004, S005, S015, S017, S020, S023, S024, S027, S033, S034, S037, S047.

## 9. Gaze heuristic and process models versus as-if models
What it is: a fielder fixes his eye on the ball, runs, and adjusts speed so the gaze angle stays constant. He needs no trajectory, wind or spin. The Hudson pilots used the tower-in-the-windshield version. A process model describes the steps; an as-if model (prospect theory, expected utility) only predicts the outcome, and so can be falsified only once.
Use when: someone claims people must be solving a hard optimization problem to act well, or a complex theory is used to describe a simple move.
Quote: "adjust your running speed so that the angle of gaze always remains constant." (S006)
Sources: 10, among them S006, S015, S017, S020, S024, S031, S032, S037, S043.

## 10. Turkey illusion
What it is: confusing uncertainty with calculable risk. A Bayesian turkey's trust rises every day until the day before Thanksgiving. Applied to Value at Risk, rating agencies and bank exchange-rate forecasts (22 banks, 10 years, one hit).
Use when: a model's confidence is highest at the end of a long calm stretch.
Quote: "On day 100, it is as high as ever before, but it's the day before Thanksgiving and you're dead meat." (S004). The name for Taleb's example; he credits Taleb in S006.
Sources: 9 (S004, S006, S014, S018, S020, S022, S026, S031, S037).

## 11. Defensive decision making
What it is: a manager who thinks option A is best for the company picks second-best option B because it protects him against blame. By self-report a third to a half of decisions in large firms; family firms have almost none. Consultants and big models are often bought as cover. In medicine it is defensive medicine (over 90 percent of US doctors admit it).
Use when: a team picks a vendor, a model or a consultant because nobody gets fired for it.
Quote: "defensive decision making protects the decision maker and hurts the company" (S014)
Sources: 9 (S002, S003, S006, S010, S014, S017, S018, S023, S047).

## 12. Natural frequencies
What it is: replace conditional probabilities with counts of people out of 100 or 1,000. 1 percent base rate, 90 percent hit rate, 9 percent false positives: of 10 positives, 1 has the disease. The representation does part of the computation. After a 75 to 90 minute session, 87 percent of gynecologists got it; fourth graders can learn it with icons.
Use when: a test, flag, risk score or fraud rule is reported with percentages.
Quote: "That's not 90%, that's not 50%, that's one out of ten." (S043) Also "the representation in natural frequency does part of the computation and that's the difference" (S023).
Limit: it fits one piece of evidence; with many cues he turns to heuristics (S005, S023).
Sources: 11, among them S004, S005, S007, S014, S023, S029, S036, S038, S043, S046.

## 13. Absolute versus relative risk, and the reference class
What it is: Percentage of what? A 100 percent rise can be 1 in 7,000 to 2 in 7,000. A 30 percent chance of rain has no meaning without the reference class (days, area, forecasters). Benefit is often reported in relative terms and harm in absolute terms (mismatch framing, speaking with a double tongue).
Use when: a number comes from a press release, a pitch or a dashboard.
Quote: "always ask percentage of what" (S014)
Sources: 9, among them S002, S014, S022, S023, S027, S038, S047.

## 14. Mortality, not five-year survival; fact boxes
What it is: screening raises five-year survival through lead-time bias and overdiagnosis without one life saved. Giuliani's 82 percent against 44 percent for prostate cancer hid almost equal mortality. A fact box lists benefits and harms for 1,000 people with and without screening, in absolute numbers, with total mortality beside disease mortality.
Use when: any detected more, found earlier, survival went up claim, in health or in business.
Quote: "mortality rates are clear 5year survival rates misleading" (S023)
Sources: 6 (S007, S022, S023, S029, S037, S038).

## 15. The SIC(K) problem
What it is: three reasons doctors do not give the best advice: self-defence, innumeracy, conflicts of interest. Self-defence and fee-for-service push the same way, toward more tests. It is the system, not a bad doctor.
Quote: "I call this the sick problem s for self-defense I for innumeracy and C for conflicts of interest" (S007)
Sources: 5 (S007, S010, S023, S029, S043).

## 16. Three kinds of prediction, the Russian tank and the Texas sharpshooter
What it is: (1) data fitting (you already know the data, complex models always win), (2) out-of-sample (split one dataset), (3) out-of-population (another hospital, another year), the only one that matters. The Russian tank fallacy: a network picked up sky colour or a portable x-ray machine, not tanks or pneumonia. The sharpshooter paints the target after the shot.
Use when: any accuracy figure is quoted for a prediction system.
Quote: "if you read an article about the newest cancer detection procedure always ask is this out of sample or out of population" (S019)
Sources: 7 (S008, S009, S016, S019, S020, S024, S036).

## 17. Adaptive toolbox
What it is: the mind has several heuristics (imitation, recognition, take-the-best, 1/N, gaze), each with search, stopping and decision rules. Wisdom is knowing which tool for which problem. A single tool for all is the error (probability theory, Bayes or a heuristic).
Quote: "I think of a toolbox. We need more than one." (S002). Also "mistaking a hammer with an entire toolbox and then thinking that everything in the world is a nail" (S032).
Sources: 14, among them S002, S004, S015, S017, S020, S027, S031, S032, S034.

## 18. Intuition plus deliberate thinking
What it is: intuition is a feeling built on years of experience that arrives fast and that you cannot explain. It raises the alarm and the analysis checks it, like a couple. Not a sixth sense, not a female trait. It needs experience: novices should think longer.
Use when: a veteran has a bad feeling (the merger story in S024) or a decision is hidden as "analysis" after the fact.
Quote: "there is no opposition between intuition and conscious thinking" (S038). Also "Intuition is a feeling based on years of experience" (S038).
Sources: 10, among them S002, S009, S012, S024, S026, S031, S037, S038, S047.

## 19. The bias bias
What it is: the tendency of researchers to see systematic bias where there is only error, or none. Overconfidence, framing, base-rate neglect, the hot hand and the conjunction fallacy are, in his reading, often intelligence or researchers' errors. Content-blind logic is the wrong yardstick outside a small world.
Quote: "the bias bias is the temptation to see biases everywhere even if there are none." (S038)
Sources: 8, among them S001, S012, S028, S033, S037, S038, S046.

## 20. Boosting versus nudging
What it is: boosting (developed with Ralph Hertwig) builds the person's competence: risk literacy, lateral reading, fact boxes. Nudging steers people to the choice architect's goal and treats the person as the problem. His third option beside hard and soft paternalism.
Quote: "boosting means that you make people strong. You don't nudge them like sheep." (S038)
Sources: 10, among them S001, S022, S027, S031, S033, S036, S037, S038, S045, S046.

## 21. The free coffee house
What it is: a coffee house gives free coffee, puts cameras and microphones on the tables, and lets salespeople interrupt. The salespeople are the customers. A free service financed by ads must maximize time on the platform. The exit: pay about two dollars a month.
Quote: "The salespeople are the customers in this coffee house, not you." (S009)
Sources: 6 (S009, S016, S030, S039, S045, S011).

## 22. Adapt to AI
What it is: when AI cannot cope with an uncertain world, we change the world (fenced cities for level-4 cars) and make people more predictable. Level 5 cars are a fiction under the stable world principle.
Quote: "the environment needs to be changed to make it more stable, and we need to become more predictable." (S030)
Sources: 6 (S008, S009, S019, S026, S030, S036).

## 23. Positive error culture
What it is: a negative culture hides errors and blames; a positive one asks what in the system to change. Tools: checklists with read-back, critical incident reports, near-miss reporting, Get Out of Jail Free cards for risk taking that failed. Two pilots cut ten errors to one.
Quote: "In a positive error culture, the key question is not who is guilty, but how we can change the system that it's less likely to happen again." (S047)
Sources: 5 (S004, S010, S022, S047, S039).

## 24. The null ritual
What it is: the hybrid of Fisher and Neyman-Pearson taught as "the" method: null of no difference, 5 percent, always. It has no effect size and no power. Replace with a test of your own hypothesis against a rival, exact p values, effect size and power. He warns against swapping it for mindless Bayes factors.
Quote: "There is no effect size in the ritual." (S025)
Sources: 3 (S025, S014, S005).

## 25. Recognition heuristic
What it is: with two options, pick the one you recognize. Germans beat Americans on which of two US cities is larger because they had not heard of the smaller; stocks recognized by pedestrians beat random picks and, in six of eight cases, the market. It works because recognition correlates with the criterion, and it will not always replicate.
Quote: "a sufficient degree of ignorance can actually help" (S032)
Sources: 3 (S032, S037, S043).

## Books

### Books: Gerd Gigerenzer

Built from the notes on S001 to S047 (S048 dropped). The notes name few titles. Titles and years marked "general knowledge" are not in the notes. Quotes are verbatim with source ids; no book text is reproduced.

- **Risk Savvy: How to Make Good Decisions (2014).** Risk versus uncertainty, natural frequencies, defensive decision making, the SICK problem, positive error culture. Taught in S004, S006, S007, S010, S014, S047. S032 treats it as forthcoming, so S032 is about 2014. "I call this the sick problem s for self-defense I for innumeracy and C for conflicts of interest" (S007, 2015).
- **How to Stay Smart in a Smart World: Why Human Intelligence Still Beats Algorithms (2022).** The stable world principle, the coffee-house analogy, click restraint, lateral reading. Taught in S008, S009, S016, S030, S036, S039. "We want to use algorithms, not be used by algorithms." (S047, 2018). "we should have a right to pay for our own coffee" (S009, 2025).
- **Gut Feelings: The Intelligence of the Unconscious (2007).** Intuition, the gaze heuristic, the recognition heuristic. Taught in S002, S038. (Title and year: general knowledge.) "Intuition is a form of unconscious intelligence." (S047, 2018).
- **Calculated Risks / Reckoning with Risk (2002).** Natural frequencies, screening statistics. Taught in S023, S029. (General knowledge.) "You always start with a class, not with a single one." (S004, 2021).
- **Simple Heuristics That Make Us Smart (1999), with the ABC Research Group.** The adaptive toolbox. (General knowledge.) "A heuristic is a tool, a strategy, to make good decisions with limited time in an efficient way and in situations where optimization is an illusion." (S033, 2026).
- **Rationality for Mortals (2008) and Simply Rational (2015).** Ecological rationality. (General knowledge; S001, S017 and S020 discuss the content.) "the rationality is not about consistency inside the mind but about the success in the world" (S011, 2024).
- **Papers and trade pieces cited in talks.** The null ritual (S025), boosting with Ralph Hertwig (S038), the Bank of England working paper on a simple leverage tree (S004, S024). "There is no effect size in the ritual." (S025, 2024).

The 2011 fact-box work with Muir Gray is background only; the notes do not support the date. Unsure.
