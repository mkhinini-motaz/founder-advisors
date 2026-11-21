# Stack pitfalls: Laravel, Next.js, React Native

Framework behaviour that changes a design or a review verdict and is easy to get wrong from memory. Checked on 1 Oct 2026 against Laravel 13 and Next.js 16.3.

**Before a verdict depends on an API named here, read the installed version's docs.** For Laravel, `laravel.com/docs/<major>.x`. For Next.js, the docs are in `node_modules/next/dist/docs/`; a Pages Router app reads `02-pages/`. For React Native, read `reactnative.dev` for the installed version.

**Caveat.** The Laravel points come mostly from Laravel's own best-practice rules, which ship with Laravel Boost. The queue points were checked against the Laravel 13 queue docs. The Next.js points come from Next's guide for AI agents. The community skills on skills.laravel.cloud were mostly copies of one another and added nothing beyond these sources. Behaviour changes between versions.

## Laravel

### Side effects inside a transaction

- **A side effect inside `DB::transaction()` escapes the transaction.** This covers a Redis publish, an SMS, a push and an HTTP call. Each goes out even when the transaction rolls back. It can also reach whoever reacts before the row is visible to them, such as a websocket relay that then fetches the order. Fix it with one of these:
  - Wrap the side effect in `DB::afterCommit()`.
  - Mark events `ShouldDispatchAfterCommit`.
  - Call `afterCommit()` on queued jobs and notifications dispatched inside a transaction.
- **The queue driver changes this risk.** The `database` queue on the default connection writes the job row inside the same transaction. A rollback removes the job, and no worker sees it early. A Redis or SQS queue gives no such guarantee: a worker can run the job before the commit, as the Laravel docs warn. Moving to Redis (for Horizon, say) therefore needs one of two changes:
  - `after_commit => true` on the queue connection;
  - `afterCommit()` at every dispatch.

  Name this in any plan that changes the queue driver.
- **Locks do not replace the database constraint.**
  - `lockForUpdate()` locks rows only inside a transaction.
  - `Cache::lock()` serialises work across processes only when every process uses one shared store that supports locks (Redis, the database or Memcached).
  - Neither replaces a unique index or an idempotency key. The constraint is the last line of defence.

### Queues

- **A job's timeout must be shorter than `retry_after`, by several seconds.** That covers the worker's `--timeout` and any job's `$timeout`. When the two are equal, or the timeout is longer, a slow job's reservation expires while it still runs. A second worker then runs it again: a second SMS, or a second payout line.
- **`ShouldBeUnique` stops duplicate dispatch, not duplicate processing.** It is a cache lock, so the handler must still be idempotent. It does not apply to jobs inside a batch.
- **`failed()` runs on a new job instance.** State set during `handle()` is gone by then. Use `failed()` to mark the domain record as failed or to alert someone, not only to log.
- **Retry only transient failures, with backoff** (`$backoff = [1, 5, 10]`). Fail a validation or business-rule error at once.
- **A batch is not a transaction.** When one job in a batch fails, finished jobs are not undone.
- **`defer()` runs after the response, in the same process.** It never retries, and the work is lost if the process dies. It suits a log line. It does not suit money or a message the user must receive.

### Scheduler

- **Put `withoutOverlapping()` on any task whose run time varies.** Its argument is the lock's expiry in minutes, not a timeout. A crash leaves the lock in place until it expires: 24 hours by default, or until `schedule:clear-cache` runs.
- **Add `onOneServer()` once two instances run the scheduler.** All instances need one shared cache store that supports locks. Without it, a second app server runs every task twice.
- **The scheduler does not stop a task at a deadline.** Bound the work inside the command itself.

### Migrations on live tables

- **A required or unique column on a populated table takes several deploys:**
  1. Add the column as nullable.
  2. Ship code that handles rows with and without it.
  3. Backfill it in chunks, from a command you can restart.
  4. Add the constraint.
- **Never edit a migration that has run in production;** add a new one.
- **A `down()` that drops a populated column destroys data.** Prefer a forward fix.
- **Rolling back the image does not roll back the schema.** When the API container migrates on start, deploying the previous image tag runs the old code on the new schema. A release whose migration renames, drops or tightens something the previous tag reads cannot be rolled back by tag. Split it: expand in this release, contract in a later one, so the previous tag always runs on the current schema, and say in the release note when a release cannot be rolled back by tag.
- **Index the queries you have measured.** A composite index's column order must match `WHERE … ORDER BY`. Confirm it with `EXPLAIN` on realistic data. Check first whether a foreign key already created the index.

### Queries

- **Catch N+1 queries in development** with `Model::preventLazyLoading()` or `Model::shouldBeStrict()`. Every N+1 then throws an exception.
- **Use `chunkById()` when the loop updates a column that the query filters on.** Plain `chunk()` pages by offset and skips rows.
- **Read settings through `config()`.** Once config is cached, `env()` returns null everywhere outside the config files.
- **A query without `ORDER BY` returns rows in no fixed order.** Paginate with a unique tie-breaker.
- **Use `mb_*` functions or `Str::` for Arabic and other UTF-8 text.** `strlen()` counts bytes, not characters.

### Cache

- **`Cache::remember()` does not stop a stampede.** When a hot key expires, every concurrent request recomputes it. Use a lock, or `Cache::flexible()` to serve the stale value while one request refreshes it.
- **Cache tags do not work on the `file`, `database` or `dynamodb` stores.**

## Next.js 16

- **Read the bundled docs before judging a design.** Next.js ships docs matching the installed version in `node_modules/next/dist/docs/`, in three folders: `01-app/`, `02-pages/` and `03-architecture/`. Next 16 changed APIs after most training data. Read the matching page before judging a rendering, caching or routing design.
- **`next dev` (16.3 and later) maintains a marked block of agent rules.** It writes the block into `AGENTS.md` when that file exists, otherwise into an existing `CLAUDE.md`, and keeps everything outside the markers. It creates both files only when neither exists. Setting `agentRules: false` in `next.config` turns this off. Claude Code reads `CLAUDE.md`, not `AGENTS.md`. The block reaches Claude only inline or through an `@AGENTS.md` import line, and an import written inside backticks is not followed.
- **Some features are App Router only:** Cache Components, `"use cache"`, Partial Prefetching and `instant()` tests. A Pages Router app cannot use them.

## React Native

General React Native coding rules are out of scope here. These four change a design or a review verdict:

- **Virtualise any list that can grow,** such as orders, menus or history. Use FlashList, or FlatList with stable keys and memoised rows. Never render it as a mapped `ScrollView`.
- **Prefer native stack navigation, native modals and native menus** to JavaScript ones.
- **Animate only `transform` and `opacity`.**
- **`{count && <View/>}` crashes when `count` is `0`.** The 0 is rendered as bare text outside `<Text>`. Use a ternary or `count > 0`.

## Sources

- Laravel Boost, `laravel-best-practices` rules (queues, caching, architecture, database performance, events, migrations, scheduling), read 1 Oct 2026: https://github.com/laravel/boost/tree/main/.ai/laravel/skill/laravel-best-practices/rules
- Laravel 13 queue docs (timeout and `retry_after`, jobs and database transactions, unique jobs): https://laravel.com/docs/13.x/queues
- Next.js, "How to set up your Next.js project for AI coding agents" (16.3, updated 7 Sept 2026): https://nextjs.org/docs/app/guides/ai-agents
- Vercel, React Native skills: https://github.com/vercel-labs/agent-skills
- Directory surveyed: https://skills.laravel.cloud/ (1,241 skills, 1 Oct 2026)
