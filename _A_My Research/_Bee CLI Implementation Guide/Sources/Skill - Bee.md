---
tags:
  - notebooklm-import
notebook: "_Bee CLI Implementation Guide"
category: "research"
---

Skill - Bee
[Bee](https://docs.bee.computer/)
[Docs](https://docs.bee.computer/docs) [API](https://docs.bee.computer/docs/proxy) [Skill](https://docs.bee.computer/docs/skill) [MCP](https://docs.bee.computer/docs/mcp) 
[Skip to Content](https://docs.bee.computer/docs/skill#nextra-skip-nav)
\* [Getting Started](https://docs.bee.computer/docs)
\* [Developer Mode](https://docs.bee.computer/docs/developer-mode)
\* [CLI](https://docs.bee.computer/docs/cli)
\* [MCP](https://docs.bee.computer/docs/mcp)
\* [Search](https://docs.bee.computer/docs/search)
\* [Agentic Now](https://docs.bee.computer/docs/agentic-now)
\* [Agentic Sync](https://docs.bee.computer/docs/agentic-sync)
\* [Realtime Sync](https://docs.bee.computer/docs/realtime)
\* [Full Sync](https://docs.bee.computer/docs/sync)
\* [API](https://docs.bee.computer/docs/proxy)
\* [Skill](https://docs.bee.computer/docs/skill)
\* [Getting Started](https://docs.bee.computer/docs)
\* [Developer Mode](https://docs.bee.computer/docs/developer-mode)
\* [CLI](https://docs.bee.computer/docs/cli)
\* [MCP](https://docs.bee.computer/docs/mcp)
\* [Search](https://docs.bee.computer/docs/search)
\* [Agentic Now](https://docs.bee.computer/docs/agentic-now)
\* [Agentic Sync](https://docs.bee.computer/docs/agentic-sync)
\* [Realtime Sync](https://docs.bee.computer/docs/realtime)
\* [Full Sync](https://docs.bee.computer/docs/sync)
\* [API](https://docs.bee.computer/docs/proxy)
\* [Skill](https://docs.bee.computer/docs/skill)
On This Page
\* [What It Enables](https://docs.bee.computer/docs/skill#what-it-enables)
\* [Example Prompts for Your Agent](https://docs.bee.computer/docs/skill#example-prompts-for-your-agent)
\* [Personal Context](https://docs.bee.computer/docs/skill#personal-context)
\* [Planning and Execution](https://docs.bee.computer/docs/skill#planning-and-execution)
\* [Memory-Aware Writing](https://docs.bee.computer/docs/skill#memory-aware-writing)
\* [Agentic Monitoring](https://docs.bee.computer/docs/skill#agentic-monitoring)
[Question? Give us feedback](https://github.com/shuding/nextra/issues/new?title=Feedback%20for%20%E2%80%9CSkill%E2%80%9D&labels=feedback) [Edit this page](https://github.com/shuding/nextra/content/skill.mdx) Scroll to top
Skill
Copy page

### Bee Skill

Install Bee Skill from GitHub:

```
npx skills add bee-computer/bee-skill
```

Repository: [github.com/bee-computer/bee-skill](https://github.com/bee-computer/bee-skill)
Prefer a direct tool connection? Assistants can also read your Bee context over [MCP](https://docs.bee.computer/docs/mcp) — connect Claude, Claude Code, or Codex in one command.
Bee Skill requires Bee app Developer Mode. See [Developer Mode](https://docs.bee.computer/docs/developer-mode). After install, the skill can complete its own authentication flow automatically (no separate manual bee login step is required).

#### What It Enables

Bee Skill lets your agent use Bee as live personal context:
\* Read your profile, facts, todos, conversations, journals, and daily summaries.
\* Search your history (default and neural modes).
\* Use realtime updates when needed and sync snapshots for reliability.
\* Ground responses in your actual captured context instead of generic guesses.

#### Example Prompts for Your Agent

Use these as copy-paste starting points.

##### Personal Context

```
What do you know about me? Give me:
1) confirmed facts
2) likely but unconfirmed facts
3) missing information you need from me
```

```
Summarize the last 24 hours from my Bee context in 8 bullets.
Include people, projects, decisions, and open questions.
```

##### Planning and Execution

```
Review my current todos and recent conversations.
Propose a prioritized plan for today (top 5 actions) with rationale.
```

```
Find anything I said I would do but did not convert into a todo.
Create a suggested todo list with due-time suggestions.
```

##### Memory-Aware Writing

```
Draft a weekly update email based on my Bee context.
Tone: concise, executive.
Include: shipped work, blockers, next week focus.
```

```
Prepare talking points for my next 1:1 with  using relevant context from recent conversations.
```

##### Agentic Monitoring

```
Run as a heartbeat assistant:
1) do a full sync once
2) poll incrementally
3) notify me only on meaningful changes (new commitments, urgent tasks, high-impact decisions)
```

```
Watch for contradictions in my recent notes/facts.
When you find one, show evidence and propose a corrected fact update.
```

Last updated on June 7, 2026
[API](https://docs.bee.computer/docs/proxy)
2026 © Bee Computer