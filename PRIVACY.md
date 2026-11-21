# Privacy

Last updated 21 November 2026. This covers the founder-advisors plugin and the scripts in this repository.

- The author runs no server and collects nothing. The plugin has no telemetry, no analytics and no account.
- What Claude reads while you use the plugin goes to Anthropic as part of your conversation, under your Claude plan's terms and [Anthropic's privacy policy](https://www.anthropic.com/legal/privacy).
- Advisors may read personal data in the files you point them to, such as names and emails in ledgers, invoices or exports. They use it only in the session and store none of it.
- Web searches and page fetches go out through Claude's built-in web tools. The search query is built from your question.
- Files the plugin writes stay on your machine: board briefs, seat answers, country files and your copy of the seat index.
- `/board add` and the scripts in `tools/` download public pages and YouTube captions about a public figure. They send nothing about you.
- If you put an Apify token in `~/.apify_token`, `tools/fetch.py` sends that token and the video address to Apify only.

Questions: open an issue at https://github.com/mkhinini-motaz/founder-advisors/issues.
