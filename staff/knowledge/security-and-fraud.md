# Security and fraud: a checklist for a small marketplace

As of 3 Oct 2026. For the software architect (design and review) and the ops lead (incidents). Written for a typical small-team marketplace stack (a Laravel JSON API with several JWT-guarded surfaces, OTP login by SMS, a realtime relay, Next.js web apps, React Native apps, a single host, cash orders, and promotions, points, referrals and refunds); the checks carry over to other stacks.

**Why this file exists.** The incidents a small team meets are known-checklist misses, not exotic attacks: a key committed to a repo, a forgotten command that can text every customer, a logout that revokes nothing, passwords with no minimum length. A dedicated security advisor was considered on 3 Oct 2026 and rejected: the architect owns security design, and `/security-review` checks diffs. This file is the checklist the architect lacked.

**Sources and caveat.** Techniques were taken from a few skills in `mukul975/anthropic-cybersecurity-skills` (IDOR, mass assignment, JWT, WebSocket, rate limiting, secret scanning). That pack is mostly generic enterprise and pentest material and has nothing on Laravel, OTP pumping or marketplace fraud, so the stack wording and the fraud items are in-house. Check every framework API against the installed version's docs (`stack-pitfalls.md`).

## Abuse that costs money (design these before launch)

1. **SMS pumping is a bill, not a breach.** Limit OTP sends per phone (about 3 per 10 minutes), per IP and per device, and set a global daily SMS budget that alerts. Reject numbers outside the country's prefix unless intended.
2. **Key rate limits on the phone or account, not only the IP.** Carrier-grade NAT puts many mobile users behind one IP, so an IP-only limit both blocks real customers and misses a rotating attacker.
3. **OTP verification:** attempts capped per code (about 5), single use, expiry of 5 minutes or less, constant-time comparison, and a new code invalidates the old one. A "return the code in the response" convenience must be off by default and never gated on the environment name.
4. **Money races.** Promo redemption, points spend, referral reward, refund approval and cash settlement are each one transaction with `lockForUpdate()` or a unique constraint (promo + customer), plus an idempotency key on retries. Test each with two parallel requests.
5. **Promo and referral abuse.** Watch for one device, phone or address cluster redeeming several first-order offers, referral pairs that share a device or an address, and new-account-then-cancel loops. Cheap controls: OTP-verified phone, caps per address and per device, and rewards released only after the order is delivered and paid.
6. **Refund collusion.** Where there is no second approver, detection is the control: every full refund carries a reason code and its actor; a report flags repeated pairs (the same customer and seller refunded more than twice in 30 days; the same admin refunding the same field worker's orders); nobody approves a refund on their own order.
7. **Commands that can reach real people or money** (SMS, push, payouts) need a `--dry-run` default, an environment guard and a count confirmation before sending. A stray `dd()` is not a guard.

## Access control

8. **Guards cannot be crossed.** Pin the JWT algorithm, use a secret of at least 32 random bytes per environment, and test that each surface's token is refused by every other surface (a field-staff token on the admin API). Justify the token lifetime per surface; an admin surface deserves a shorter one.
9. **Revocation works.** Logout blacklists the token in a shared cache (clearing that cache un-revokes every token), and the realtime relay drops the account's sockets on logout.
10. **BOLA/IDOR.** Every route that takes an id scopes the query to the caller (customer, seller, area). Prove it with a two-account test per surface; scope an area manager to the area.
11. **Mass assignment.** No `$guarded = []` and no `$request->all()` into `create`/`update`. Price, discount, status, seller id, commission, role and points are never fillable from a client body.
12. **Realtime relay.** Verify the token on connect and on every channel join; a client joins only its own channels; allow-list the Origin; Redis stays on the internal network with a password.
13. **Outsiders see the minimum.** A field worker who is not staff sees the customer's number only while the order is active, and each reveal is logged.

## Secrets, apps and host

14. **Secrets.** Scan staged changes in pre-commit and the full history in CI. A key deleted from the tree is still in history: rotate it. A key shipped in a mobile app is public by definition, so restrict it by package name, signing fingerprint and API list in the provider's console.
15. **Mobile storage.** Tokens live in Keystore/Keychain, not AsyncStorage. Release builds: `allowBackup=false`, not debuggable, no cleartext HTTP.
16. **Host.** Only the reverse proxy publishes ports (80/443); the database and Redis sit on an internal network; containers run as non-root with `cap_drop: ALL` and pinned image versions; secrets come from env files outside git; the proxy sends HSTS and `nosniff`; production has debug off and error pages without stack traces.
17. **Supply chain.** Commit the lock files, run `composer audit` and `npm audit` in CI, review install scripts of new packages, and pin GitHub Actions to commit SHAs.
18. **Logs.** No OTP, token, password or full phone number in any log line.
19. **HTML from data.** Text that a seller, field worker or customer typed (product, option and seller names, notes, reviews) never reaches `dangerouslySetInnerHTML`, Blade's `{!! !!}` or an HTML string built on the server. Build the markup in JSX from the plain string; where HTML is truly needed, sanitise it on output with an allow-list. JSON-LD inside `<script>` escapes `<`. A seller who signed up on their own is an untrusted author.

## When something goes wrong

20. **A one-page runbook per trigger** (leaked key, stolen token, wrong mass message, abnormal refunds, exposed database): the first 30 minutes (revoke or rotate, stop ordering through the platform switch if needed), who is told, and when the data-protection authority must be notified (confirm the deadline with legal counsel against the country business-law file). Timestamp each action as it happens; the post-mortem is the timeline, root cause, impact, what worked, and fixes with an owner and a date.
21. **Pre-launch gate, run once and saved as a script:** the cross-guard token test, the two-account IDOR test per surface, the OTP throttle test, a history secret scan, one backup restored, debug off, database and Redis unreachable from outside, and strong passwords or two-step login on admin accounts.
