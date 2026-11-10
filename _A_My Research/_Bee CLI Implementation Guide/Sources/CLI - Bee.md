---
tags:
  - notebooklm-import
notebook: "_Bee CLI Implementation Guide"
category: "research"
---

CLI - Bee
[Bee](https://docs.bee.computer/)
[Docs](https://docs.bee.computer/docs) [API](https://docs.bee.computer/docs/proxy) [Skill](https://docs.bee.computer/docs/skill) [MCP](https://docs.bee.computer/docs/mcp) 
[Skip to Content](https://docs.bee.computer/docs/cli#nextra-skip-nav)
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
\* [Authentication](https://docs.bee.computer/docs/cli#authentication)
\* [bee login](https://docs.bee.computer/docs/cli#bee-login)
\* [bee status](https://docs.bee.computer/docs/cli#bee-status)
\* [bee logout](https://docs.bee.computer/docs/cli#bee-logout)
\* [User Data](https://docs.bee.computer/docs/cli#user-data)
\* [bee me](https://docs.bee.computer/docs/cli#bee-me)
\* [Example output](https://docs.bee.computer/docs/cli#example-output)
\* [bee today](https://docs.bee.computer/docs/cli#bee-today)
\* [Example output](https://docs.bee.computer/docs/cli#example-output-1)
\* [bee now](https://docs.bee.computer/docs/cli#bee-now)
\* [Example output](https://docs.bee.computer/docs/cli#example-output-2)
\* [bee activity](https://docs.bee.computer/docs/cli#bee-activity)
\* [bee changed](https://docs.bee.computer/docs/cli#bee-changed)
\* [Example output](https://docs.bee.computer/docs/cli#example-output-3)
\* [Facts](https://docs.bee.computer/docs/cli#facts)
\* [bee facts list](https://docs.bee.computer/docs/cli#bee-facts-list)
\* [Example output](https://docs.bee.computer/docs/cli#example-output-4)
\* [bee facts get](https://docs.bee.computer/docs/cli#bee-facts-get)
\* [bee facts create](https://docs.bee.computer/docs/cli#bee-facts-create)
\* [Example output](https://docs.bee.computer/docs/cli#example-output-5)
\* [bee facts update](https://docs.bee.computer/docs/cli#bee-facts-update)
\* [Example output](https://docs.bee.computer/docs/cli#example-output-6)
\* [bee facts delete](https://docs.bee.computer/docs/cli#bee-facts-delete)
\* [Example output](https://docs.bee.computer/docs/cli#example-output-7)
\* [bee facts search](https://docs.bee.computer/docs/cli#bee-facts-search)
\* [Todos](https://docs.bee.computer/docs/cli#todos)
\* [bee todos list](https://docs.bee.computer/docs/cli#bee-todos-list)
\* [Example output](https://docs.bee.computer/docs/cli#example-output-8)
\* [bee todos get](https://docs.bee.computer/docs/cli#bee-todos-get)
\* [bee todos create](https://docs.bee.computer/docs/cli#bee-todos-create)
\* [Example output](https://docs.bee.computer/docs/cli#example-output-9)
\* [bee todos update](https://docs.bee.computer/docs/cli#bee-todos-update)
\* [Example output](https://docs.bee.computer/docs/cli#example-output-10)
\* [bee todos complete](https://docs.bee.computer/docs/cli#bee-todos-complete)
\* [bee todos delete](https://docs.bee.computer/docs/cli#bee-todos-delete)
\* [Example output](https://docs.bee.computer/docs/cli#example-output-11)
\* [bee todos suggestions](https://docs.bee.computer/docs/cli#bee-todos-suggestions)
\* [bee todos accept-suggestion](https://docs.bee.computer/docs/cli#bee-todos-accept-suggestion)
\* [bee todos dismiss-suggestion](https://docs.bee.computer/docs/cli#bee-todos-dismiss-suggestion)
\* [Conversations](https://docs.bee.computer/docs/cli#conversations)
\* [bee conversations list](https://docs.bee.computer/docs/cli#bee-conversations-list)
\* [bee conversations get](https://docs.bee.computer/docs/cli#bee-conversations-get)
\* [bee conversations transcript](https://docs.bee.computer/docs/cli#bee-conversations-transcript)
\* [bee conversations related](https://docs.bee.computer/docs/cli#bee-conversations-related)
\* [Daily Summaries](https://docs.bee.computer/docs/cli#daily-summaries)
\* [bee daily list](https://docs.bee.computer/docs/cli#bee-daily-list)
\* [bee daily get](https://docs.bee.computer/docs/cli#bee-daily-get)
\* [bee daily find](https://docs.bee.computer/docs/cli#bee-daily-find)
\* [Journals](https://docs.bee.computer/docs/cli#journals)
\* [bee journals list](https://docs.bee.computer/docs/cli#bee-journals-list)
\* [bee journals get](https://docs.bee.computer/docs/cli#bee-journals-get)
\* [bee journals search](https://docs.bee.computer/docs/cli#bee-journals-search)
\* [Insights](https://docs.bee.computer/docs/cli#insights)
\* [bee insights list](https://docs.bee.computer/docs/cli#bee-insights-list)
\* [bee insights get](https://docs.bee.computer/docs/cli#bee-insights-get)
\* [Locations](https://docs.bee.computer/docs/cli#locations)
\* [bee locations clusters](https://docs.bee.computer/docs/cli#bee-locations-clusters)
\* [bee locations recent](https://docs.bee.computer/docs/cli#bee-locations-recent)
\* [bee locations current](https://docs.bee.computer/docs/cli#bee-locations-current)
\* [Photos](https://docs.bee.computer/docs/cli#photos)
\* [bee photos list](https://docs.bee.computer/docs/cli#bee-photos-list)
\* [bee photos get](https://docs.bee.computer/docs/cli#bee-photos-get)
\* [Search](https://docs.bee.computer/docs/cli#search)
\* [bee search](https://docs.bee.computer/docs/cli#bee-search)
\* [Utility Commands](https://docs.bee.computer/docs/cli#utility-commands)
\* [bee sync](https://docs.bee.computer/docs/cli#bee-sync)
\* [bee stream](https://docs.bee.computer/docs/cli#bee-stream)
\* [bee proxy](https://docs.bee.computer/docs/cli#bee-proxy)
\* [bee mcp](https://docs.bee.computer/docs/cli#bee-mcp)
\* [bee ping](https://docs.bee.computer/docs/cli#bee-ping)
\* [bee version](https://docs.bee.computer/docs/cli#bee-version)
\* [Global Options](https://docs.bee.computer/docs/cli#global-options)
[Question? Give us feedback](https://github.com/shuding/nextra/issues/new?title=Feedback%20for%20%E2%80%9CCLI%E2%80%9D&labels=feedback) [Edit this page](https://github.com/shuding/nextra/content/cli.mdx) Scroll to top
CLI
Copy page

### CLI Reference

Install the CLI first if you have not set it up yet:
npm yarn

##### npm

```
npm install -g @beeai/cli
```

##### yarn

```
yarn global add @beeai/cli
```

Verify installation:

```
bee version
```

#### Authentication

##### bee login

Authenticate with your Bee account.

```
bee login
bee login --qr
bee login --no-wait
bee login --token 
bee login --token-stdin
bee login --proxy http://127.0.0.1:8787
bee login --proxy ~/.bee/proxy.sock
```

By default bee login prints an authentication link and then blocks, polling until you approve the connection (up to ~5 minutes). Use --no-wait to print the link and exit immediately without polling — useful for agents and automation: send the link to the user, then run bee status to confirm, or re-run bee login to resume the same (unexpired) session and finish.
Use --proxy  when another trusted local process handles Bee API authentication and this CLI should send requests through it. See [API documentation](https://docs.bee.computer/docs/proxy) for proxy details.

##### bee status

Check your authentication status.

```
bee status
```

##### bee logout

Clear your stored credentials.

```
bee logout
```

#### User Data

##### bee me

Fetch your user profile information.
markdown json

##### markdown

```
bee me
```

##### json

```
bee me --json
```

###### Example output

```
# Profile
 
- timezone: America/Los_Angeles
- first_name: Alex
- last_name: Rivera
```

##### bee today

Get today's brief including calendar events and emails. Use --context for Bee wearable context (daily summary, active todos, notes, conversations) instead.
markdown json

##### markdown

```
bee today
bee today --context
```

##### json

```
bee today --json
bee today --context --json
```

###### Example output

```
# Today Brief
 
- timezone: America/Los_Angeles
- calendar_events: (none)
- emails: (none)
```

##### bee now

Fetch recent conversations with utterances. See [Agentic Now](https://docs.bee.computer/docs/agentic-now) for agent-focused guidance.
markdown json

##### markdown

```
bee now
```

##### json

```
bee now --json
```

###### Example output

```
# Now
 
- timezone: America/Los_Angeles
 
## Conversation 987654
> To read the full conversation, run: `bee conversations get 987654`
 
- start_time: 2026-02-10 09:00 [3 hours ago]
- end_time: 2026-02-10 09:25 [2 hours ago]
- state: COMPLETED
 
Roadmap planning for Q1 milestones
 
Utterances
- Alex: Let's lock scope for the next sprint.
- Sam: I will draft the release checklist today.
```

##### bee activity

Show recent activity across conversations, summaries, notes, todos, and insights.
markdown json

##### markdown

```
bee activity
bee activity --limit 20
```

##### json

```
bee activity --json
bee activity --limit 20 --json
```

##### bee changed

Retrieve recently changed entities. See [Agentic Sync](https://docs.bee.computer/docs/agentic-sync) for details.
markdown json

##### markdown

```
bee changed
bee changed --cursor
```

##### json

```
bee changed --json
bee changed --cursor  --json
```

###### Example output

```
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
 
-----
 
# Conversations
- timezone: America/Los_Angeles
 
### Conversation 6531525
- start_time: 2026-02-10 10:14 [3 hours ago]
- end_time: 2026-02-10 10:54 [3 hours ago]
```

#### Facts

Manage your personal facts and preferences.

##### bee facts list

List your facts.
markdown json

##### markdown

```
bee facts list
bee facts list --limit 50
bee facts list --cursor 
bee facts list --unconfirmed
```

##### json

```
bee facts list --json
bee facts list --limit 50 --json
bee facts list --cursor  --json
bee facts list --unconfirmed --json
```

###### Example output

```
# Confirmed Facts
 
- User prefers morning standups.
- User keeps project notes in markdown.
 
-----
 
## Pagination
 
- next_cursor: v1-1762285321128-6777613
```

##### bee facts get

Retrieve a specific fact by ID.
markdown json

##### markdown

```
bee facts get
```

##### json

```
bee facts get  --json
```

##### bee facts create

Create a new fact.
markdown json

##### markdown

```
bee facts create --text "Prefers morning meetings"
```

##### json

```
bee facts create --text "Prefers morning meetings" --json
```

###### Example output

```
# Fact 9001
 
- timezone: America/Los_Angeles
- created_at: 2026-02-10 12:30 [just now]
- confirmed: false
- text: Prefers morning meetings
```

##### bee facts update

Update an existing fact.
markdown json

##### markdown

```
bee facts update  --text "Updated fact"
bee facts update  --text "Updated fact" --confirmed true
```

##### json

```
bee facts update  --text "Updated fact" --json
bee facts update  --text "Updated fact" --confirmed true --json
```

###### Example output

```
# Fact 9001
 
- timezone: America/Los_Angeles
- created_at: 2026-02-10 12:30 [5 minutes ago]
- confirmed: true
- text: Updated fact
```

##### bee facts delete

Delete a fact.
markdown json

##### markdown

```
bee facts delete
```

##### json

```
bee facts delete  --json
```

###### Example output

```
Deleted fact 9001.
```

##### bee facts search

Search your saved facts by text query.
markdown json

##### markdown

```
bee facts search --query "morning meetings"
bee facts search --query "morning meetings" --limit 20
```

##### json

```
bee facts search --query "morning meetings" --json
bee facts search --query "morning meetings" --limit 20 --json
```

#### Todos

Manage your todos.

##### bee todos list

List your todos.
markdown json

##### markdown

```
bee todos list
bee todos list --limit 50
bee todos list --cursor
```

##### json

```
bee todos list --json
bee todos list --limit 50 --json
bee todos list --cursor  --json
```

###### Example output

```
# Todos
 
## Open
 
### Todo 1001
- timezone: America/Los_Angeles
- created_at: 2026-02-10 08:30 [4 hours ago]
- alarm_at: n/a
- completed: false
- text: Draft release notes
 
## Completed
- (none)
```

##### bee todos get

Retrieve a specific todo by ID.
markdown json

##### markdown

```
bee todos get
```

##### json

```
bee todos get  --json
```

##### bee todos create

Create a new todo.
markdown json

##### markdown

```
bee todos create --text "Review the roadmap"
bee todos create --text "Review the roadmap" --alarm-at 2026-02-11T09:00:00Z
```

##### json

```
bee todos create --text "Review the roadmap" --json
bee todos create --text "Review the roadmap" --alarm-at 2026-02-11T09:00:00Z --json
```

###### Example output

```
# Todo 1002
 
- timezone: America/Los_Angeles
- created_at: 2026-02-10 12:40 [just now]
- alarm_at: 2026-02-11 01:00 [in 12 hours]
- completed: false
- text: Review the roadmap
```

##### bee todos update

Update an existing todo.
markdown json

##### markdown

```
bee todos update  --text "Updated todo"
bee todos update  --completed true
bee todos update  --alarm-at 2026-02-11T09:00:00Z
bee todos update  --clear-alarm
```

##### json

```
bee todos update  --text "Updated todo" --json
bee todos update  --completed true --json
bee todos update  --alarm-at 2026-02-11T09:00:00Z --json
bee todos update  --clear-alarm --json
```

###### Example output

```
# Todo 1002
 
- timezone: America/Los_Angeles
- created_at: 2026-02-10 12:40 [10 minutes ago]
- alarm_at: n/a
- completed: true
- text: Updated todo
```

##### bee todos complete

Mark a todo complete. A shortcut for bee todos update

##### markdown

```
bee todos complete
```

##### json

```
bee todos complete  --json
```

##### bee todos delete

Delete a todo.
markdown json

##### markdown

```
bee todos delete
```

##### json

```
bee todos delete  --json
```

###### Example output

```
Deleted todo 1002.
```

##### bee todos suggestions

List pending Bee-suggested todos. These are action items Bee proposed from your conversations that you have not yet accepted or dismissed.
markdown json

##### markdown

```
bee todos suggestions
bee todos suggestions --limit 20
```

##### json

```
bee todos suggestions --json
bee todos suggestions --limit 20 --json
```

##### bee todos accept-suggestion

Accept a suggested todo, turning it into a real todo.
markdown json

##### markdown

```
bee todos accept-suggestion
```

##### json

```
bee todos accept-suggestion  --json
```

##### bee todos dismiss-suggestion

Dismiss a suggested todo.
markdown json

##### markdown

```
bee todos dismiss-suggestion
```

##### json

```
bee todos dismiss-suggestion  --json
```

#### Conversations

Access your conversation history.

##### bee conversations list

List conversations.
markdown json

##### markdown

```
bee conversations list
bee conversations list --limit 20
bee conversations list --cursor
```

##### json

```
bee conversations list --json
bee conversations list --limit 20 --json
bee conversations list --cursor  --json
```

##### bee conversations get

Retrieve a specific conversation by ID, including its full transcript.
markdown json

##### markdown

```
bee conversations get
```

##### json

```
bee conversations get  --json
```

##### bee conversations transcript

Retrieve just the transcript utterances for a conversation.
markdown json

##### markdown

```
bee conversations transcript
```

##### json

```
bee conversations transcript  --json
```

##### bee conversations related

Find conversations related to a given conversation.
markdown json

##### markdown

```
bee conversations related 
bee conversations related  --limit 10
```

##### json

```
bee conversations related  --json
bee conversations related  --limit 10 --json
```

#### Daily Summaries

Access daily summaries.

##### bee daily list

List daily summaries.
markdown json

##### markdown

```
bee daily list
bee daily list --limit 20
bee daily list --cursor
```

##### json

```
bee daily list --json
bee daily list --limit 20 --json
bee daily list --cursor  --json
```

##### bee daily get

Retrieve a specific daily summary by ID.
markdown json

##### markdown

```
bee daily get
```

##### json

```
bee daily get  --json
```

##### bee daily find

Find the daily summary for a specific date ( YYYY-MM-DD ).
markdown json

##### markdown

```
bee daily find 2026-02-10
```

##### json

```
bee daily find 2026-02-10 --json
```

#### Journals

Access your journals.

##### bee journals list

List journals.
markdown json

##### markdown

```
bee journals list
bee journals list --limit 20
bee journals list --cursor
```

##### json

```
bee journals list --json
bee journals list --limit 20 --json
bee journals list --cursor  --json
```

##### bee journals get

Retrieve a specific journal by ID.
markdown json

##### markdown

```
bee journals get
```

##### json

```
bee journals get  --json
```

##### bee journals search

Search your voice notes and journal entries by text query.
markdown json

##### markdown

```
bee journals search --query "car"
bee journals search --query "car" --limit 20
```

##### json

```
bee journals search --query "car" --json
bee journals search --query "car" --limit 20 --json
```

#### Insights

Access Bee's insights about you.

##### bee insights list

List recent insights.
markdown json

##### markdown

```
bee insights list
bee insights list --limit 20
bee insights list --cursor
```

##### json

```
bee insights list --json
bee insights list --limit 20 --json
bee insights list --cursor  --json
```

##### bee insights get

Retrieve a specific insight by ID.
markdown json

##### markdown

```
bee insights get
```

##### json

```
bee insights get  --json
```

#### Locations

Access where you have been.

##### bee locations clusters

Show places grouped by visit frequency.
markdown json

##### markdown

```
bee locations clusters
bee locations clusters --limit 20
bee locations clusters --min-visits 3
bee locations clusters --visits
```

##### json

```
bee locations clusters --json
bee locations clusters --min-visits 3 --json
bee locations clusters --visits --json
```

Use --min-visits N to only include places visited at least N times, and --visits to include the individual visits within each cluster.

##### bee locations recent

Show recent individual visits.
markdown json

##### markdown

```
bee locations recent
bee locations recent --limit 20
bee locations recent --from 2026-02-01 --to 2026-02-10
```

##### json

```
bee locations recent --json
bee locations recent --from 2026-02-01 --to 2026-02-10 --json
```

Bound the window with --from

##### bee locations current

Show your latest known location.
markdown json

##### markdown

```
bee locations current
```

##### json

```
bee locations current --json
```

#### Photos

Access photos synced from your photo gallery. Photos are imported from your phone's photo library, not captured by the device.

##### bee photos list

List photos, newest first. Filter by daily summary or date.
markdown json

##### markdown

```
bee photos list
bee photos list --limit 20
bee photos list --daily-id 100
bee photos list --date 2026-02-10
```

##### json

```
bee photos list --json
bee photos list --daily-id 100 --json
bee photos list --date 2026-02-10 --json
```

##### bee photos get

Download one photo by ID. Use --output

##### markdown

```
bee photos get 
bee photos get  --output ~/Downloads/photo.jpg
```

##### json

```
bee photos get  --json
```

#### Search

Search your Bee data. See [Search](https://docs.bee.computer/docs/search) for default vs neural guidance.

##### bee search

Keyword search (default) runs a BM25 index across conversations, daily summaries, and facts. Scope it with --filter conversations|daily|facts|all and order it with --sort relevance|mostRecent . Use --neural for semantic conversation search (conversations only; --filter and --sort do not apply). Bound either mode by time with --since / --until (epoch milliseconds).
markdown json

##### markdown

```
bee search --query "project roadmap"
bee search --query "project roadmap" --limit 20
bee search --query "project roadmap" --filter conversations
bee search --query "project roadmap" --filter daily --sort mostRecent
bee search --query "project roadmap" --since 1770700000000 --until 1770759786297
bee search --query "What do you know about me?" --neural
bee search --query "project roadmap" --neural --limit 10
```

##### json

```
bee search --query "project roadmap" --json
bee search --query "project roadmap" --limit 20 --json
bee search --query "project roadmap" --filter facts --json
bee search --query "project roadmap" --sort mostRecent --json
bee search --query "project roadmap" --since 1770700000000 --until 1770759786297 --json
bee search --query "What do you know about me?" --neural --json
bee search --query "project roadmap" --neural --limit 10 --json
```

| Option | Applies to | Description |
| --- | --- | --- |
| --query | both | The search query (required). |
| --limit N | both | Maximum number of results (1–100). |
| --neural | — | Use semantic conversation search instead of keyword search. |
| --filter conversations|daily|facts|all | keyword | Scope which entity types are searched. Defaults to all . |
| --scope conversations|all | keyword | Alias for --filter ( conversations or all ). |
| --sort relevance|mostRecent | keyword | Order results by relevance or recency. Defaults to relevance . |
| --since | both | Only return items at or after this time (epoch milliseconds). |
| --until | both | Only return items at or before this time (epoch milliseconds). |
| --json | both | Print raw JSON instead of markdown. |

#### Utility Commands

##### bee sync

Export your Bee data to local markdown files. Re-runs into the same output directory are incremental by default — only daily summaries and conversations that changed since the last run are re-fetched (facts and todos are always synced in full). See [Full Sync](https://docs.bee.computer/docs/sync) for details.

```
bee sync
bee sync --output ~/my-bee-data
bee sync --only facts,todos
bee sync --recent-days 7
bee sync --full
bee sync --since 1770700000000
```

| Option | Default | Description |
| --- | --- | --- |
| --output | bee-sync | Output directory for synced files. |
| --recent-days N | all | Limit daily summaries and conversations to the last N days. Applies to full syncs only; ignored on an incremental run. |
| --only | all | Comma-separated list to limit the sync: facts , todos , daily , conversations (or all ). |
| --full | off | Force a complete re-sync, ignoring the saved manifest, and rewrite it with fresh cursors. |
| --since | — | Advanced/recovery: override the saved incremental cursor with an explicit epoch-milliseconds timestamp. |

##### bee stream

Stream real-time events from Bee. See [Realtime Sync](https://docs.bee.computer/docs/realtime) for details.

```
# Human-readable with colors (default)
bee stream
 
# Human-readable, token-optimized for inference (no colors)
bee stream --agent
 
# Structured JSON output
bee stream --json
 
# Optional event filtering
bee stream --types new-utterance,update-conversation --agent
bee stream --types new-utterance,update-conversation --json
```

##### bee proxy

Start a local Bee API proxy. See [API documentation](https://docs.bee.computer/docs/proxy) for details. Authenticate with bee login before starting it.

```
# TCP listener (default auto-picks from 8787)
bee proxy
bee proxy --port 8787
bee proxy --idle-timeout 300
 
# Unix socket listener (default: ~/.bee/proxy.sock)
bee proxy --socket
bee proxy --socket /tmp/bee-proxy.sock
```

| Option | Default | Description |
| --- | --- | --- |
| --port N | auto from 8787 | TCP port to listen on. |
| --socket [path] | ~/.bee/proxy.sock | Listen on a Unix socket instead of TCP. Optionally provide a path. |
| --idle-timeout SECONDS | 120 | Server idle timeout. Use 0 to disable idle request timeouts (helpful for large exports). |

##### bee mcp

Run or connect the CLI as a [Model Context Protocol](https://modelcontextprotocol.io/) server so assistants like Claude and Codex can read your Bee context. See [MCP](https://docs.bee.computer/docs/mcp) for the full guide, the serve-http security model, and the tool catalog.

```
bee mcp connect claude          # Claude Desktop (one-click install)
bee mcp connect claude-code     # Claude Code (CLI)
bee mcp connect codex           # Codex
bee mcp status                  # show what's connected
bee mcp disconnect claude-code  # remove a connection
 
bee mcp serve                   # stdio JSON-RPC (what the connectors launch)
bee mcp serve-http --token               # local HTTP on 127.0.0.1:8790 (default port), bearer-token auth
bee mcp serve-http --port 9000 --token   # ...or choose a port with --port
```

The connectors authenticate with your existing Bee login (run bee login first); there is no extra token to manage for the stdio transport. serve-http requires an auth token of at least 32 characters via --token or the BEE\_MCP\_HTTP\_TOKEN environment variable, binds to 127.0.0.1 only, and clients send it as Authorization: Bearer

##### bee ping

Check connectivity to Bee servers.

```
bee ping
bee ping --count 5
```

##### bee version

Display the CLI version.
markdown json

##### markdown

```
bee version
```

##### json

```
bee version --json
```

#### Global Options

These options are available at the top-level command:

| Option | Description |
| --- | --- |
| --help | Show help |
| --version | Show version number |

Run bee