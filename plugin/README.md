# Founder Advisors

Founder Advisors gives Claude Code ten staff advisors for a small company: a CEO, a CFO, an accountant, legal counsel, a marketer, a sales lead, an ops lead, a product designer, a software architect and a data analyst. Each one reads your company brief before it answers, so its advice fits your company and not a generic one.

The plugin also holds a decision board of 52 seats. Each seat is a simulation built from one person's free public work, such as talks, interviews and essays, and every seat answer starts with a label that says it is a simulation. A `hire` skill walks you through building advisors of your own, with country files for tax, law and market.

## Install

Once the plugin is listed in the directory, run `/plugin install founder-advisors`. Before that, add the marketplace from GitHub with `/plugin marketplace add mkhinini-motaz/founder-advisors`, then install `founder-advisors@founder-advisors`.

## Start

Copy the example brief in the examples folder of this plugin to `.claude/company.md` in your project and rewrite it for your company. Then ask for an advisor by role, for example "ask the cfo whether we can afford a second hire". Without a brief, each advisor asks five questions first.

## Where it works

Claude Code and Cowork load the advisors, the board and the `hire` skill. Chat on claude.ai skips plugin agents, so it cannot run the advisors or the board's seats there.

## What it runs and sends

- Advisors read your company brief and the project files a question needs.
- Those files can hold personal data, such as names and emails in ledgers, invoices, exports or contracts. Advisors use it only in the session and store none of it.
- Advisors can search the web and open pages with Claude's built-in web tools to check facts and sources. The search queries are built from your question.
- The CFO, the accountant, the data analyst and the software architect can run shell commands, for example to compute a figure or read a data export.
- The product designer can use Playwright browser tools if you have them installed. It opens the pages you ask it to review.
- Advisors advise only. They never send, post, file, pay or sign anything, and never edit project files.
- The board writes its briefs and seat answers as new files in `docs/board/<date>-<slug>/` in your project, or in the folder your company brief names.
- `/board add <name>` builds a new seat with the repository's scripts and writes it into the plugin folder.
- Those scripts download public pages and YouTube captions about that person into a build folder at `~/.claude/board-build/`.
- The `hire` skill and the board keep your own files (country files, your copy of the seat index) in the plugin's data folder.
- The plugin has no server and no telemetry. Nothing goes to its author.

## Not professional advice

The advisors are not lawyers, accountants or financial advisers. Have a licensed professional check any legal, tax or financial decision before you act on it. Each board seat is a simulation built from one person's public work, not that person, and every seat answer says so.

## Examples

- "Ask the cfo whether we can afford a second hire with eight months of runway."
- "Ask legal-counsel what our supplier contract must say about late delivery."
- "/board Should we raise our prices by 10% before the holiday season?"
- "Hire an advisor for logistics in Morocco." (the `hire` skill)

## Troubleshooting

- **An advisor asks five questions first.** It found no brief at `.claude/company.md`. Copy the example brief and fill it in.
- **No advisors in the list.** Check that you are in Claude Code or Cowork, then run `/agents` to see the ten advisors.
- **Quote checking or building a new seat does not work.** Those tools are scripts, so they live in the repository, not the plugin. Clone it and run them from there.

## More

The plugin holds only text. The eval runner and the tools that keep the board's seats up to date are in the repository, https://github.com/mkhinini-motaz/founder-advisors, along with a copy install script and the contribution guide. Licensed under MIT.

## Support

Questions and bugs: open an issue at https://github.com/mkhinini-motaz/founder-advisors/issues. Security problems: report them privately from the repository's Security tab (private vulnerability reporting), not in a public issue.
