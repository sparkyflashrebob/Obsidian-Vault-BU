---
tags:
  - notebooklm-import
notebook: "_Bee CLI Implementation Guide"
category: "research"
---

Getting Started - Bee
[Bee](https://docs.bee.computer/)
[Docs](https://docs.bee.computer/docs) [API](https://docs.bee.computer/docs/proxy) [Skill](https://docs.bee.computer/docs/skill) [MCP](https://docs.bee.computer/docs/mcp) 
[Skip to Content](https://docs.bee.computer/docs#nextra-skip-nav)
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
\* [Two Ways to Work with Bee](https://docs.bee.computer/docs#two-ways-to-work-with-bee)
\* [Prerequisites](https://docs.bee.computer/docs#prerequisites)
\* [Installation](https://docs.bee.computer/docs#installation)
\* [Output Modes](https://docs.bee.computer/docs#output-modes)
\* [Authentication](https://docs.bee.computer/docs#authentication)
\* [Login to your Bee account](https://docs.bee.computer/docs#login-to-your-bee-account)
\* [Verify your connection](https://docs.bee.computer/docs#verify-your-connection)
\* [Test the connection](https://docs.bee.computer/docs#test-the-connection)
\* [Your First Commands](https://docs.bee.computer/docs#your-first-commands)
\* [Syncing Your Data](https://docs.bee.computer/docs#syncing-your-data)
\* [Logging Out](https://docs.bee.computer/docs#logging-out)
\* [Next Steps](https://docs.bee.computer/docs#next-steps)
[Question? Give us feedback](https://github.com/shuding/nextra/issues/new?title=Feedback%20for%20%E2%80%9CGetting%20Started%E2%80%9D&labels=feedback) [Edit this page](https://github.com/shuding/nextra/content/index.mdx) Scroll to top
Getting Started
Copy page

### Getting Started with Bee CLI

Bee CLI is the command-line interface for interacting with your Bee data. It allows you to export your conversations, facts, todos, and more to local markdown files.

#### Two Ways to Work with Bee

You can work with Bee in two ways:
1. **CLI** : Use bee commands directly in your terminal. This is usually the best option for AI agents because it provides markdown output by default, supports JSON when needed, and works well with local automation.
1. **API** : Start a local HTTP API with bee proxy and call Bee over HTTP from your app or service. See [API documentation](https://docs.bee.computer/docs/proxy).
Prefer to wire Bee directly into an AI assistant? Connect it over [MCP](https://docs.bee.computer/docs/mcp) to give tools like Claude, Claude Code, or Codex live access to your Bee context.
This guide continues with the CLI workflow.

#### Prerequisites

To use the Bee CLI, you must have the **Bee iOS app** installed and Developer Mode unlocked by tapping app **Version** 5 times. See the [Developer Mode guide](https://docs.bee.computer/docs/developer-mode).

#### Installation

npm yarn

##### npm

```
npm install -g @beeai/cli
```

##### yarn

```
yarn global add @beeai/cli
```

Verify the installation:

```
bee version
```

#### Output Modes

Data commands render markdown by default. Add --json when you need machine-readable output.
markdown json

##### markdown

```
bee me
```

##### json

```
bee me --json
```

#### Authentication

##### Login to your Bee account

Run the login command:

```
bee login
```

##### Verify your connection

Check that you're authenticated:

```
bee status
```

##### Test the connection

Ping the Bee servers:

```
bee ping
```

#### Your First Commands

Once authenticated, try these commands to explore your data:
markdown json

##### markdown

```
# Get your user profile
bee me
 
# See your daily brief (calendar events, emails)
bee today
 
# View recent conversations from the last 10 hours
bee now
 
# List your facts
bee facts list
 
# List your todos
bee todos list
 
# Search your data (fast default mode)
bee search --query "project roadmap"
 
# Semantic search (slower neural mode)
bee search --query "What do you know about me?" --neural
```

##### json

```
# Get your user profile
bee me --json
 
# See your daily brief (calendar events, emails)
bee today --json
 
# View recent conversations from the last 10 hours
bee now --json
 
# List your facts
bee facts list --json
 
# List your todos
bee todos list --json
 
# Search your data (fast default mode)
bee search --query "project roadmap" --json
 
# Semantic search (slower neural mode)
bee search --query "What do you know about me?" --neural --json
```

#### Syncing Your Data

The most powerful feature of Bee CLI is the ability to sync your data to local markdown files:

```
bee sync
```

This creates a bee-sync/ directory with all your data organized in markdown format. See the [Full Sync documentation](https://docs.bee.computer/docs/sync) for more details.

#### Logging Out

To clear your credentials:

```
bee logout
```

#### Next Steps

```
*  Learn about all available [CLI commands](https://docs.bee.computer/docs/cli)
*  Learn how to use [Search](https://docs.bee.computer/docs/search) (default and neural modes)
*  Set up automatic [Full Sync](https://docs.bee.computer/docs/sync) for your data
*  Use [Realtime Sync](https://docs.bee.computer/docs/realtime) for real-time events
*  Run a local [API](https://docs.bee.computer/docs/proxy) server
*  Connect your AI assistant with [MCP](https://docs.bee.computer/docs/mcp)
```

Last updated on February 10, 2026
[Developer Mode](https://docs.bee.computer/docs/developer-mode)
2026 © Bee Computer