---
tags:
  - notebooklm-import
notebook: "_Bee CLI Implementation Guide"
category: "research"
---

Search - Bee
[Bee](https://docs.bee.computer/)
[Docs](https://docs.bee.computer/docs) [API](https://docs.bee.computer/docs/proxy) [Skill](https://docs.bee.computer/docs/skill) [MCP](https://docs.bee.computer/docs/mcp) 
[Skip to Content](https://docs.bee.computer/docs/search#nextra-skip-nav)
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
\* [Mode Comparison](https://docs.bee.computer/docs/search#mode-comparison)
\* [Usage](https://docs.bee.computer/docs/search#usage)
\* [Options](https://docs.bee.computer/docs/search#options)
\* [Filtering the keyword scope](https://docs.bee.computer/docs/search#filtering-the-keyword-scope)
\* [Bounding results by time](https://docs.bee.computer/docs/search#bounding-results-by-time)
\* [Recommendation](https://docs.bee.computer/docs/search#recommendation)
[Question? Give us feedback](https://github.com/shuding/nextra/issues/new?title=Feedback%20for%20%E2%80%9CSearch%E2%80%9D&labels=feedback) [Edit this page](https://github.com/shuding/nextra/content/search.mdx) Scroll to top
Search
Copy page

### Search

Bee supports two search modes:
1. **Keyword search (default, BM25)** — runs over your conversations, daily summaries, and facts.
1. **Neural semantic search** ( --neural ) — semantic recall over conversations only.
Neural search is significantly slower than keyword search. Use it only when keyword search misses relevant context.

#### Mode Comparison

| Mode | Access | Scope | Speed | Best for |
| --- | --- | --- | --- | --- |
| Keyword (BM25) | bee search --query " | Conversations, daily summaries, facts | Fast | Everyday lookup, exact terms, recent recall |
| Neural | bee search --query " | Conversations only | Slower | Semantic recall when wording differs |

By default, keyword search returns matches across **conversations, daily summaries, and facts** . Neural search is semantic and covers **conversations only** ; the keyword-only --filter and --sort flags do not apply when you pass --neural .
Todos and insights are not searchable here. Use bee todos list and bee insights for those.

#### Usage

```
bee search --query  [--limit N] [--since ] [--until ] [--json]
```

keyword (default) neural

##### keyword (default)

```
$ bee search --query "project roadmap"
$ bee search --query "project roadmap" --limit 20
$ bee search --query "project roadmap" --json
```

Keyword search returns BM25-ranked results across conversations, daily summaries, and facts.

##### neural

```
$ bee search --query "What do you know about me?" --neural
$ bee search --query "project roadmap" --neural --limit 20
$ bee search --query "project roadmap" --neural --json
```

Neural search returns semantically relevant conversations and is slower by design.

#### Options

| Option | Mode | Description |
| --- | --- | --- |
| --query | both | The search text (required). |
| --limit N | both | Maximum number of results (1–100, default 20). |
| --neural | — | Switch to neural semantic search (conversations only). |
| --filter conversations|daily|facts|all | keyword | Scope the keyword (BM25) search. Defaults to all . |
| --scope conversations|all | keyword | Alias for --filter ( conversations or all ). |
| --sort relevance|mostRecent | keyword | Order keyword results by relevance or recency. Defaults to relevance . |
| --since | both | Only return items at or after this time (epoch milliseconds). |
| --until | both | Only return items at or before this time (epoch milliseconds). |
| --json | both | Emit raw JSON instead of formatted markdown. |

##### Filtering the keyword scope

--filter scopes which record types the keyword index searches. --scope is an alias accepting conversations or all .

```
# Only search conversations
bee search --query "standup notes" --filter conversations
 
# Only search daily summaries
bee search --query "highlights" --filter daily
 
# Only search facts
bee search --query "coffee" --filter facts
 
# Order keyword matches by recency instead of relevance
bee search --query "release plan" --sort mostRecent
```

--filter , --scope , and --sort apply to keyword search only. They cannot be combined with --neural .

##### Bounding results by time

--since and --until accept **epoch milliseconds** and bound results in **both** keyword and neural modes.

```
# Keyword matches created on or after a timestamp
bee search --query "budget" --since 1704067200000
 
# Neural matches within a time window
bee search --query "what did I plan" --neural --since 1704067200000 --until 1706745600000
```

#### Recommendation

```
1. Start with keyword search for speed and broad coverage (conversations, daily summaries, facts).
1. Use neural search only when keyword results are insufficient.
1. Keep neural queries focused and use --limit to control latency.
1. Narrow either mode with --since / --until when you know the rough time window.
```

The same search is available to AI assistants through the bee\_search MCP tool, which mirrors these options ( query , limit , filter , sortBy , mode , plus since / until ). See [MCP](https://docs.bee.computer/docs/mcp).
Last updated on June 7, 2026
[MCP](https://docs.bee.computer/docs/mcp) [Agentic Now](https://docs.bee.computer/docs/agentic-now)
2026 © Bee Computer