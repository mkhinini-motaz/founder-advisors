# Founder Advisors

Founder Advisors gives Claude Code ten staff advisors for a small company: a CEO, a CFO, an accountant, legal counsel, a marketer, a sales lead, an ops lead, a product designer, a software architect and a data analyst. Each one reads your company brief before it answers, so its advice fits your company and not a generic one.

The plugin also holds a decision board of 52 seats. Each seat is a simulation built from one person's free public work, such as talks, interviews and essays, and every seat answer starts with a label that says it is a simulation. A `hire` skill walks you through building advisors of your own, with country files for tax, law and market.

## Install

Once the plugin is listed in the directory, run `/plugin install founder-advisors`. Before that, add the marketplace from GitHub with `/plugin marketplace add mkhinini-motaz/founder-advisors`, then install `founder-advisors@founder-advisors`.

## Start

Copy the example brief in the examples folder of this plugin to `.claude/company.md` in your project and rewrite it for your company. Then ask for an advisor by role, for example "ask the cfo whether we can afford a second hire". Without a brief, each advisor asks five questions first.

## More

The plugin holds only text. The eval runner and the tools that keep the board's seats up to date are in the repository, https://github.com/mkhinini-motaz/founder-advisors, along with a copy install script and the contribution guide. Licensed under MIT.
