---
tags:
  - notebooklm-import
notebook: "_Bee CLI Implementation Guide"
category: "research"
---

Agentic Now - Bee
[Bee](https://docs.bee.computer/)
[Docs](https://docs.bee.computer/docs) [API](https://docs.bee.computer/docs/proxy) [Skill](https://docs.bee.computer/docs/skill) [MCP](https://docs.bee.computer/docs/mcp) 
[Skip to Content](https://docs.bee.computer/docs/agentic-now#nextra-skip-nav)
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
\* [Usage](https://docs.bee.computer/docs/agentic-now#usage)
\* [Agent Workflow](https://docs.bee.computer/docs/agentic-now#agent-workflow)
\* [Example](https://docs.bee.computer/docs/agentic-now#example)
[Question? Give us feedback](https://github.com/shuding/nextra/issues/new?title=Feedback%20for%20%E2%80%9CAgentic%20Now%E2%80%9D&labels=feedback) [Edit this page](https://github.com/shuding/nextra/content/agentic-now.mdx) Scroll to top
Agentic Now
Copy page

### Agentic Now

Use bee now to get a point-in-time “what is happening right now” snapshot that is suitable for agent reasoning. bee now is a snapshot, not a durable stream. For live events use [Realtime Sync](https://docs.bee.computer/docs/realtime). For reliable backfill/completeness use [Full Sync](https://docs.bee.computer/docs/sync) and [Agentic Sync](https://docs.bee.computer/docs/agentic-sync).

#### Usage

markdown json

##### markdown

```
# Human-readable snapshot
bee now
```

##### json

```
# Machine-readable snapshot
bee now --json
```

#### Agent Workflow

```
1. Run bee now on demand when an assistant needs immediate context.
1. Let the assistant reason over conversation summaries and utterances.
1. Use bee conversations get  for deep drill-down.
1. Combine with [Agentic Sync](https://docs.bee.computer/docs/agentic-sync) for incremental follow-ups.
```

#### Example

markdown json

##### markdown

```
$ bee now
 
# Now
 
- timezone: America/Los_Angeles
 
## Conversation 6531525
> To read the full conversation, run: `bee conversations get 6531525`
 
- start_time: 2026-02-10 10:14 [4 hours ago]
- end_time: 2026-02-10 10:54 [3 hours ago]
- state: COMPLETED
 
AMI and CloudInit troubleshooting
 
Utterances
 
- Unknown: And so I think being able to like get shared
- Unknown: And then my buddy draws that one on the conversation.
- Unknown: And so I have that.
...
```

##### json

```
$ bee now --json
```

```
{
  "since": 1770723943081,
  "until": 1770759943081,
  "timezone": "America/Los_Angeles",
  "conversations": [
    {
      "id": 6531525,
      "start_time": 1770747298995,
      "end_time": 1770749653042,
      "state": "COMPLETED",
      "short_summary": "AMI and CloudInit troubleshooting",
      "utterances": [
        {
          "speaker": "Unknown",
          "text": "And so I think being able to like get shared"
        },
        {
          "speaker": "Unknown",
          "text": "And I'm number one."
        },
        {
          "speaker": "Unknown",
          "text": "But my brother, he's a senior official, so why don't we get to work?"
        }
      ]
    }
  ]
}
```

Last updated on February 10, 2026
[Search](https://docs.bee.computer/docs/search) [Agentic Sync](https://docs.bee.computer/docs/agentic-sync)
2026 © Bee Computer