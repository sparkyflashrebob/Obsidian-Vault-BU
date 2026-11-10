---
tags:
  - notebooklm-import
notebook: "_Bee CLI Implementation Guide"
category: "research"
---

API - Bee
[Bee](https://docs.bee.computer/)
[Docs](https://docs.bee.computer/docs) [API](https://docs.bee.computer/docs/proxy) [Skill](https://docs.bee.computer/docs/skill) [MCP](https://docs.bee.computer/docs/mcp) 
[Skip to Content](https://docs.bee.computer/docs/proxy#nextra-skip-nav)
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
\* [Usage](https://docs.bee.computer/docs/proxy#usage)
\* [Options](https://docs.bee.computer/docs/proxy#options)
\* [Proxy Authentication](https://docs.bee.computer/docs/proxy#proxy-authentication)
\* [API Reference](https://docs.bee.computer/docs/proxy#api-reference)
\* [User](https://docs.bee.computer/docs/proxy#user)
\* [Changes](https://docs.bee.computer/docs/proxy#changes)
\* [Facts](https://docs.bee.computer/docs/proxy#facts)
\* [Todos](https://docs.bee.computer/docs/proxy#todos)
\* [Journals](https://docs.bee.computer/docs/proxy#journals)
\* [Conversations](https://docs.bee.computer/docs/proxy#conversations)
\* [Daily Summaries](https://docs.bee.computer/docs/proxy#daily-summaries)
\* [Search](https://docs.bee.computer/docs/proxy#search)
\* [Streaming](https://docs.bee.computer/docs/proxy#streaming)
\* [Direct API (No Proxy)](https://docs.bee.computer/docs/proxy#direct-api-no-proxy)
[Question? Give us feedback](https://github.com/shuding/nextra/issues/new?title=Feedback%20for%20%E2%80%9CAPI%E2%80%9D&labels=feedback) [Edit this page](https://github.com/shuding/nextra/content/proxy.mdx) Scroll to top
API
Copy page

### API

The bee proxy command starts a local HTTP API proxy server, allowing you to access your Bee data through standard HTTP requests. This is useful for building local applications, testing integrations, or accessing Bee data from tools that don't support the Bee protocol directly.
The proxy server is intended for local development only. Do not expose it to the public internet as it provides unauthenticated access to your Bee data.
You must authenticate first with bee login , then start bee proxy .

#### Usage

```
# TCP listener (defaults to port 8787, auto-picking the next free port if taken)
bee proxy
bee proxy --port 8787
```

This starts a local HTTP server bound to 127.0.0.1 , by default on port 8787 . If 8787 is in use, the proxy auto-picks the next free port (unless you pin one with --port ). Only paths under /v1/\* are forwarded; any other path returns 404 .

##### Options

| Flag | Description |
| --- | --- |
| --port N | Listen on TCP port N on 127.0.0.1 . Defaults to 8787 (auto-incrementing to the next free port when omitted). Cannot be combined with --socket . |
| --socket [path] | Listen on a Unix domain socket instead of TCP. Defaults to ~/.bee/proxy.sock when no path is given. Stale socket files are removed before listening. Cannot be combined with --port . |
| --idle-timeout SECONDS | Server idle request timeout. Defaults to 120 . Increase it for large exports, or pass 0 to disable the idle timeout entirely. |

```
# Unix socket listener (default path: ~/.bee/proxy.sock)
bee proxy --socket
bee proxy --socket /tmp/bee-proxy.sock
 
# Raise the idle timeout for long-running exports (or 0 to disable)
bee proxy --idle-timeout 300
bee proxy --idle-timeout 0
```

#### Proxy Authentication

When another trusted local process already handles Bee API authentication, point this CLI at it with bee login --proxy so requests are forwarded through that proxy instead of using a stored token directly:

```
# HTTP proxy
bee login --proxy http://127.0.0.1:8787
 
# Unix socket proxy
bee login --proxy ~/.bee/proxy.sock
```

This saves the proxy configuration to ~/.bee/proxy-{env}.json . When a proxy config exists, it **takes precedence** over stored token auth. Run bee logout to clear it before switching back to direct token auth.

#### API Reference

Once the proxy is running, you can access your Bee data through standard HTTP requests. The proxy forwards **any** /v1/\* path straight through to the Bee API, so the list below is a representative subset, not an exhaustive catalog — additional developer endpoints (for example insights , locations , photos , todoSuggestions , conversations/:id/related , search/conversations , journals , and todayBrief ) are forwarded the same way.

##### User

```
# Get user profile
GET /v1/me
```

##### Changes

```
# Get changed entity ids since cursor (or default window when cursor is omitted)
GET /v1/changes
```

##### Facts

```
# List all facts
GET /v1/facts
 
# Get a specific fact
GET /v1/facts/:id
 
# Create a new fact
POST /v1/facts
Content-Type: application/json
{"text": "Your fact here"}
 
# Update a fact
PUT /v1/facts/:id
Content-Type: application/json
{"text": "Updated fact", "confirmed": true}
 
# Delete a fact
DELETE /v1/facts/:id
```

##### Todos

```
# List all todos
GET /v1/todos
 
# Get a specific todo
GET /v1/todos/:id
 
# Create a new todo
POST /v1/todos
Content-Type: application/json
{"text": "New todo", "alarm_at": "2026-02-11T09:00:00Z"}
 
# Update a todo
PUT /v1/todos/:id
Content-Type: application/json
{"text": "Updated todo", "completed": true, "alarm_at": null}
 
# Delete a todo
DELETE /v1/todos/:id
```

alarm\_at is provided as an **ISO 8601 timestamp on input** (e.g. "2026-02-11T09:00:00Z" ), but is returned as **epoch milliseconds** in responses.

##### Journals

```
# List journals
GET /v1/journals
 
# Get a specific journal
GET /v1/journals/:id
```

##### Conversations

```
# List conversations
GET /v1/conversations
 
# Get a specific conversation
GET /v1/conversations/:id
```

##### Daily Summaries

```
# List daily summaries
GET /v1/daily
 
# Get a specific daily summary
GET /v1/daily/:id
```

##### Search

```
# BM25 keyword search
POST /v1/search/conversations
Content-Type: application/json
{"query": "project roadmap", "limit": 20, "cursor": null}
 
# Neural search
POST /v1/search/conversations/neural
Content-Type: application/json
{"query": "project roadmap", "limit": 20}
```

##### Streaming

```
# SSE stream (optional: ?types=new-utterance,todo-created)
GET /v1/stream
 
# Common event types:
# new-conversation, update-conversation, update-conversation-summary, delete-conversation
# new-utterance, todo-created, todo-updated, todo-deleted
# journal-created, journal-updated, journal-deleted, journal-text
```

#### Direct API (No Proxy)

If you want to call Bee API directly (without bee proxy ), use the same developer API endpoints ( /v1/\* ) and authenticate with a Bearer token.

```
curl --cacert ./bee-ca.pem \
  -H "Authorization: Bearer $BEE_TOKEN" \
  "$BEE_API_BASE/v1/me"
```

You must trust Bee's certificate in your client implementation. The Bee API uses a private CA (not a public CA), so standard system trust stores alone are not enough.
Certificate source used by Bee CLI:
\* <https://github.com/bee-computer/bee-cli/blob/97dfdb18e83c9e5151d8363de791e1f974aaacee/sources/certs.ts>
Last updated on June 7, 2026
[Full Sync](https://docs.bee.computer/docs/sync) [Skill](https://docs.bee.computer/docs/skill)
2026 © Bee Computer