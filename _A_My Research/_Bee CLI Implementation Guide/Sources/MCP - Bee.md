---
tags:
  - notebooklm-import
notebook: "_Bee CLI Implementation Guide"
category: "research"
---

MCP - Bee
[Bee](https://docs.bee.computer/)
[Docs](https://docs.bee.computer/docs) [API](https://docs.bee.computer/docs/proxy) [Skill](https://docs.bee.computer/docs/skill) [MCP](https://docs.bee.computer/docs/mcp) 
[Skip to Content](https://docs.bee.computer/docs/mcp#nextra-skip-nav)
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
\* [Connect quickly to Claude, Claude Code, or Codex](https://docs.bee.computer/docs/mcp#connect-quickly-to-claude-claude-code-or-codex)
\* [What this is](https://docs.bee.computer/docs/mcp#what-this-is)
\* [Connectors](https://docs.bee.computer/docs/mcp#connectors)
\* [Transports](https://docs.bee.computer/docs/mcp#transports)
\* [Tool catalog](https://docs.bee.computer/docs/mcp#tool-catalog)
\* [See also](https://docs.bee.computer/docs/mcp#see-also)
[Question? Give us feedback](https://github.com/shuding/nextra/issues/new?title=Feedback%20for%20%E2%80%9CMCP%E2%80%9D&labels=feedback) [Edit this page](https://github.com/shuding/nextra/content/mcp.mdx) Scroll to top
MCP
Copy page

### MCP

#### Connect quickly to Claude, Claude Code, or Codex

Already logged in ( bee login )? Connect your assistant in one command:

```
bee mcp connect claude          # Claude Desktop (one-click install)
bee mcp connect claude-code     # Claude Code (CLI)
bee mcp connect codex           # Codex
```

That's it — your assistant can now read your Bee context (conversations, facts, todos, daily summaries) directly from this computer. Check or undo with bee mcp status / bee mcp disconnect

#### What this is

The Bee CLI is also a [Model Context Protocol](https://modelcontextprotocol.io/) server, so assistants like Claude and Codex can read your Bee context — search conversations, look up facts and todos, fetch daily summaries — directly, with your data staying on your machine.
The server authenticates with your existing Bee login, so there is **no extra token to manage** for the connector path (stdio). The connected client launches the local Bee CLI, which signs in with your stored Bee credentials.

#### Connectors

Wire Bee into a specific assistant. connect claude generates a Claude **Desktop** one-click install package and opens it in Claude (click **Install** to finish); claude-code and codex register Bee directly with those clients.

```
bee mcp connect claude          # Claude Desktop (one-click install)
bee mcp connect claude-code     # Claude Code (CLI)
bee mcp connect codex           # Codex
 
bee mcp status                  # show what's connected
bee mcp disconnect claude       # remove (claude | claude-code | codex)
```

bee mcp status reports the launch command and which clients are connected. bee mcp disconnect

#### Transports

To run the server yourself — for another MCP client, or to debug — use one of the transports directly.
stdio HTTP

##### stdio

```
bee mcp serve
```

Stdio JSON-RPC 2.0. This is what the connectors launch under the hood; it uses your stored Bee login, so no token is required.

##### HTTP

```
bee mcp serve-http --token "$(openssl rand -hex 32)"
bee mcp serve-http --port 8790 --token "$(openssl rand -hex 32)"
```

Local HTTP JSON-RPC over POST /mcp , bound to 127.0.0.1 only. A health check is available at GET /health . An auth token is **required** (see below).
**serve-http security.** The HTTP transport requires an auth token:
\* **Required** , and at least **32 characters** long.
\* Supplied with --token

#### Tool catalog

Every read, search, and manage capability in the CLI is exposed as an MCP tool, so the CLI and your assistant work from the same data. The tools map closely to their CLI equivalents:

| MCP tool | CLI equivalent |
| --- | --- |
| bee\_status | bee status |
| bee\_search | bee search |
| bee\_search\_facts | bee facts search |
| bee\_list\_facts | bee facts list |
| bee\_get\_fact | bee facts get |
| bee\_create\_fact | bee facts create |
| bee\_update\_fact | bee facts update |
| bee\_delete\_fact | bee facts delete |
| bee\_get\_recent\_activity | bee activity |
| bee\_get\_today | bee today |
| bee\_list\_conversations | bee conversations list |
| bee\_get\_conversation | bee conversations get |
| bee\_get\_conversation\_transcript | bee conversations transcript |
| bee\_get\_related\_conversations | bee conversations related |
| bee\_get\_daily\_summary | bee daily get / bee daily find |
| bee\_list\_daily\_summaries | bee daily list |
| bee\_list\_voice\_notes | bee journals list |
| bee\_search\_voice\_notes | bee journals search |
| bee\_get\_voice\_note | bee journals get |
| bee\_list\_todos | bee todos list |
| bee\_create\_todo | bee todos create |
| bee\_update\_todo | bee todos update |
| bee\_complete\_todo | bee todos complete |
| bee\_delete\_todo | bee todos delete |
| bee\_get\_todo\_suggestions | bee todos suggestions |
| bee\_accept\_todo\_suggestion | bee todos accept-suggestion |
| bee\_dismiss\_todo\_suggestion | bee todos dismiss-suggestion |
| bee\_get\_insights | bee insights list |
| bee\_get\_insight | bee insights get |
| bee\_get\_location\_clusters | bee locations clusters |
| bee\_get\_recent\_visits | bee locations recent |
| bee\_get\_current\_location | bee locations current |
| bee\_get\_photos | bee photos list |
| bee\_get\_photo | bee photos get |

#### See also

For a packaged, prompt-driven integration that bundles these capabilities for your agent, see the [Bee Skill](https://docs.bee.computer/docs/skill).
Last updated on June 7, 2026
[CLI](https://docs.bee.computer/docs/cli) [Search](https://docs.bee.computer/docs/search)
2026 © Bee Computer