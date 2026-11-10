---
tags:
  - notebooklm-import
notebook: "_Bee CLI Implementation Guide"
category: "research"
---

Agentic Sync - Bee
[Bee](https://docs.bee.computer/)
[Docs](https://docs.bee.computer/docs) [API](https://docs.bee.computer/docs/proxy) [Skill](https://docs.bee.computer/docs/skill) [MCP](https://docs.bee.computer/docs/mcp) 
[Skip to Content](https://docs.bee.computer/docs/agentic-sync#nextra-skip-nav)
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
\* [Usage](https://docs.bee.computer/docs/agentic-sync#usage)
\* [Agent Workflow](https://docs.bee.computer/docs/agentic-sync#agent-workflow)
\* [Example](https://docs.bee.computer/docs/agentic-sync#example)
[Question? Give us feedback](https://github.com/shuding/nextra/issues/new?title=Feedback%20for%20%E2%80%9CAgentic%20Sync%E2%80%9D&labels=feedback) [Edit this page](https://github.com/shuding/nextra/content/agentic-sync.mdx) Scroll to top
Agentic Sync
Copy page

### Agentic Sync

Use bee changed for agent-first incremental sync loops.
This mode is designed for assistants (OpenClaw and others) to reason about what changed since the last heartbeat and decide what to do next.
Use [Full Sync](https://docs.bee.computer/docs/sync) when you need a complete snapshot/backfill.

#### Usage

markdown json

##### markdown

```
# Get recent changes
bee changed
 
# Continue from a known cursor
bee changed --cursor
```

##### json

```
# Get recent changes
bee changed --json
 
# Continue from a known cursor
bee changed --cursor  --json
```

Without a cursor, bee changed is used as a bootstrap window (for example, last 10 hours) before cursor-based polling. The live example below is from a real local run.

#### Agent Workflow

```
1. Run bee changed on a heartbeat.
1. Let the assistant reason over changed facts/todos/conversations/dailies/journals.
1. Store the returned cursor.
1. Use that cursor in the next fetch with --cursor .
```

The cursor is returned in both formats:
\* Markdown output includes Next Cursor: ...
\* JSON output includes meta.next\_cursor

#### Example

markdown json

##### markdown

```
$ bee changed
 
# Changed
 
From: 2026-02-09 13:43 [1 day ago]
Until: 2026-02-10 13:43 [0 seconds ago]
Next Cursor: v1-1770759786297
 
# Confirmed Facts
 
- Prefers morning meetings
 
-----
 
# Pending Facts
 
- Steve is confused about where current AMIs come from in his deployment pipeline
- Steve needs cloud-init functionality to touch functions on the fly during deployment
- Steve is concerned about production AMIs being created months ago and potentially outdated
...
```

##### json

```
$ bee changed --json
```

```
{
  "meta": {
    "next_cursor": "v1-1770759786309",
    "since": 1770673386309,
    "until": 1770759786309,
    "updated": true,
    "timezone": "America/Los_Angeles"
  },
  "facts": [
    {
      "id": 8217328,
      "text": "Steve needs cloud-init functionality to touch functions on the fly during deployment",
      "confirmed": false,
      "timezone": "America/Los_Angeles"
    }
  ],
  "todos": [],
  "dailies": [],
  "conversations": [
    {
      "id": 6531525,
      "short_summary": "AMI and CloudInit troubleshooting",
      "state": "COMPLETED"
    }
  ],
  "journals": [
    {
      "id": "mvce1exyv1asjs2azspku59h",
      "state": "READY",
      "text": "Remember me to call lawyers about the car."
    }
  ]
}
```

Last updated on February 10, 2026
[Agentic Now](https://docs.bee.computer/docs/agentic-now) [Realtime Sync](https://docs.bee.computer/docs/realtime)
2026 © Bee Computer