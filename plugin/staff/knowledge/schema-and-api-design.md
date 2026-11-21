# Schema and API design

Durable design rules for a MySQL schema and its JSON API. Every point rests on free official documentation: the MySQL 8.0 Reference Manual and the IETF RFCs, each opened on 21 Nov 2026. Read for a schema, migration, query, endpoint or database-operations question. Version-specific framework behaviour is in `stack-pitfalls.md`; where the two disagree, the installed version's docs decide.

## Schema and query rules

Each bullet: the symptom to spot, what the manual says, our fix. The manual states the behaviour; the fix and the Laravel notes are our reasoning.

- **Binary floats for money.** The manual: floating-point numbers "are approximate and not stored as exact values", and FLOAT and DOUBLE are subject to this [1]. It says DECIMAL operations use 65 digits of precision, which "should solve most common inaccuracy problems" [1]. Our fix: `DECIMAL`, or an integer count of the smallest unit, for any amount. Ratings and GPS may stay float.
- **Missing foreign keys.** The manual: foreign key constraints "help keep the related data consistent", with `ON DELETE` and `ON UPDATE` actions (CASCADE, SET NULL, RESTRICT, NO ACTION) [2]. Symptom: `unsignedBigInteger('x_id')` with no `foreign()`. Our fix: declare the key and choose the action on purpose; the cost is small next to orphaned order or cash rows. Our caveat: Laravel's polymorphic `morphs()` columns cannot carry a foreign key, so use them for write-once logs and use real keys where integrity or joins matter.
- **ENUM for a changing list.** The manual lists the traps [3]: values sort by their index number, a number stored into an ENUM is read as an index, and an invalid value becomes an empty string unless strict mode raises an error. It also says "We strongly recommend that you do not use numbers as enumeration values." Our fix: a lookup table with a key when admins edit the list; ENUM only for sets that never change.
- **Selecting a column that is not grouped.** With `ONLY_FULL_GROUP_BY` (the default) MySQL "rejects queries for which the select list, HAVING condition, or ORDER BY list refer to nonaggregated columns" [4]. Without the mode, the server "is free to choose any value from each group" [4]. The manual's way out without turning the mode off: `ANY_VALUE()`. Our fix: group by every selected column, aggregate it, or use a window function; do not disable the mode.
- **Passwords on the command line.** The manual: a password given with `-p` on the command line is visible to `ps`; the safest ways are the prompt or a protected option file, or `mysql_config_editor` [5].
- **utf8mb4.** The manual: utf8mb4 supports supplementary characters in up to four bytes, which utf8mb3 cannot store [6]. Our line: use it for non-Latin scripts and emoji, and check each table and connection.

## HTTP API rules

- **Bearer tokens go in the `Authorization` header.** RFC 6750 makes the `Bearer` header the way to send an access token; it says the query-string method is "not recommended, due to its security deficiencies", mainly that the URL is likely to be logged [7]. Use HTTPS only (ours).
- **One error shape, machine-readable.** RFC 9457 defines problem details: `type`, `title`, `status`, `detail`, `instance`, in the media type `application/problem+json`, and says consumers "SHOULD NOT parse the "detail" member for information" [8]. Our line: the app matches the stable `type` or an app error code, never the message text. Keep one error shape across every app, because an app that reads one field name breaks on a middleware that sends another.

## Reviewing a change that crosses surfaces (as of 6 Oct 2026)

Our own review practice, not sourced from a document.

In a platform with several apps, one API change reaches every app, any realtime relay, and old builds still installed on phones. Before approving one:

- **A new status, type or enum value:** grep every sibling value (the constant names and the bare integers) across all repos and read each hit: app status maps, labels and translation keys; every API query, scope or `whereIn` list that names statuses (active orders, dispatch, reports, monitoring, exports); what is published to Redis. A list that names statuses drops the new one without an error, and a `default` branch gives it the wrong label.
- **Installed builds get the new value before any update ships.** Each app shows an unknown status as something neutral and never crashes or goes blank. If an old build would mishandle it, hold the value back until the builds that understand it are out.
- **Errors keep one shape.** A new error path answers in the shape the apps already parse. One admin app read `{ message }` while a middleware sent `{ messages: [...] }`, so every refusal from that middleware arrived as undefined.
- **A removed or renamed field** stays beside its replacement until the oldest supported build stops reading it. Builds lag in the stores, so old clients live for months.

## MySQL 8 operations

A managed database such as RDS removes installing, hand-written `my.cnf` and building replication.

- **Point-in-time recovery.** The manual: the source for point-in-time recovery is the binary logs written after the full backup; replaying them with `mysqlbinlog` re-executes the changes, and it can select a time or position range [9]. On RDS, a point-in-time restore goes into a NEW instance, which gets the default security group and subnet group unless told otherwise (AWS CLI docs, opened 21 Nov 2026) [12]; repoint `DB_HOST`, never restore in place. Our line: before launch, restore a snapshot to a throwaway instance, time it, check order counts, delete it. A backup counts only after a restore.
- **Slow query log.** The manual: it is off by default; `long_query_time` defaults to 10 seconds; queries not using indexes are logged only if `log_queries_not_using_indexes` is on; `mysqldumpslow` summarises the file [10]. On RDS, enable it in the parameter group and read it weekly after launch. Index from real queries.
- **Schema changes.** The manual shows `ALTER TABLE` taking `ALGORITHM=` and `LOCK=` clauses, and a statement that cannot run with the requested algorithm fails with an error instead of falling back [11]. Our line: when orders and the queue share one database, a blocking `ALTER` stalls ordering. Migrate off-peak and name both clauses on big tables.
- **Privileges.** Our line: give the app a schema-only account (`SELECT, INSERT, UPDATE, DELETE`) and a separate migration account, not the RDS master user.

## Sources

All opened on 21 Nov 2026 unless stated.

1. MySQL 8.0 Reference Manual, "Problems with Floating-Point Values": https://dev.mysql.com/doc/refman/8.0/en/problems-with-float.html
2. MySQL 8.0 Reference Manual, "FOREIGN KEY Constraints": https://dev.mysql.com/doc/refman/8.0/en/create-table-foreign-keys.html
3. MySQL 8.0 Reference Manual, "The ENUM Type": https://dev.mysql.com/doc/refman/8.0/en/enum.html
4. MySQL 8.0 Reference Manual, "MySQL Handling of GROUP BY": https://dev.mysql.com/doc/refman/8.0/en/group-by-handling.html
5. MySQL 8.0 Reference Manual, "End-User Guidelines for Password Security": https://dev.mysql.com/doc/refman/8.0/en/password-security-user.html
6. MySQL 8.0 Reference Manual, "The utf8mb4 Character Set": https://dev.mysql.com/doc/refman/8.0/en/charset-unicode-utf8mb4.html
7. RFC 6750, "The OAuth 2.0 Authorization Framework: Bearer Token Usage": https://www.rfc-editor.org/rfc/rfc6750.html
8. RFC 9457, "Problem Details for HTTP APIs": https://www.rfc-editor.org/rfc/rfc9457.html
9. MySQL 8.0 Reference Manual, "Point-in-Time (Incremental) Recovery": https://dev.mysql.com/doc/refman/8.0/en/point-in-time-recovery-binlog.html
10. MySQL 8.0 Reference Manual, "The Slow Query Log": https://dev.mysql.com/doc/refman/8.0/en/slow-query-log.html
11. MySQL 8.0 Reference Manual, "Online DDL Operations": https://dev.mysql.com/doc/refman/8.0/en/innodb-online-ddl-operations.html
12. AWS CLI, `restore-db-instance-to-point-in-time`, opened 21 Nov 2026: https://docs.aws.amazon.com/cli/latest/reference/rds/restore-db-instance-to-point-in-time.html

Further reading, not used as a source: Karwin, *SQL Antipatterns*; Sturgeon, *Build APIs You Won't Hate*.
