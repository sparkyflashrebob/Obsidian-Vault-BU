---
tags:
  - notebooklm-import
notebook: "_Bee CLI Implementation Guide"
category: "research"
---

Full Sync - Bee
[Bee](https://docs.bee.computer/)
[Docs](https://docs.bee.computer/docs) [API](https://docs.bee.computer/docs/proxy) [Skill](https://docs.bee.computer/docs/skill) [MCP](https://docs.bee.computer/docs/mcp) 
[Skip to Content](https://docs.bee.computer/docs/sync#nextra-skip-nav)
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
\* [Usage](https://docs.bee.computer/docs/sync#usage)
\* [Incremental by Default](https://docs.bee.computer/docs/sync#incremental-by-default)
\* [Options](https://docs.bee.computer/docs/sync#options)
\* [--output](https://docs.bee.computer/docs/sync#--output-directory) 
\* [--only](https://docs.bee.computer/docs/sync#--only-target) 
\* [--recent-days](https://docs.bee.computer/docs/sync#--recent-days-n) 
\* [--full](https://docs.bee.computer/docs/sync#--full)
\* [--since](https://docs.bee.computer/docs/sync#--since-epochms) 
\* [Output Structure](https://docs.bee.computer/docs/sync#output-structure)
\* [File Formats](https://docs.bee.computer/docs/sync#file-formats)
\* [facts.md](https://docs.bee.computer/docs/sync#factsmd)
\* [todos.md](https://docs.bee.computer/docs/sync#todosmd)
\* [daily/YYYY-MM-DD/summary.md](https://docs.bee.computer/docs/sync#dailyyyyy-mm-ddsummarymd)
\* [conversations/YYYY-MM-DD/ID.md](https://docs.bee.computer/docs/sync#conversationsyyyy-mm-ddidmd)
\* [Notes](https://docs.bee.computer/docs/sync#notes)
\* [Automation](https://docs.bee.computer/docs/sync#automation)
[Question? Give us feedback](https://github.com/shuding/nextra/issues/new?title=Feedback%20for%20%E2%80%9CFull%20Sync%E2%80%9D&labels=feedback) [Edit this page](https://github.com/shuding/nextra/content/sync.mdx) Scroll to top
Full Sync
Copy page

### Full Sync Command

The bee sync command exports your Bee data to local markdown files, creating a portable backup of your conversations, facts, todos, and daily summaries for use with AI agents.
For incremental polling of recent changes as a feed instead of a file snapshot, see [Agentic Sync](https://docs.bee.computer/docs/agentic-sync).

#### Usage

```
bee sync [--output ] [--recent-days N] [--only ] [--full] [--since ]
```

This creates a bee-sync/ directory in your current location with all your data.

#### Incremental by Default

After a first sync, re-running bee sync into the **same output directory** is **incremental** : it re-fetches only the daily summaries and conversations that have changed since the last run. Facts and todos are always re-fetched in full, since they are small.
Sync state is tracked in a .bee-sync.json manifest inside the output directory (it stores per-target changefeed cursors). Delete the manifest — or the entire output directory — to force a full re-sync.
Deletes are not reconciled. A local file for an item that is later deleted on the server remains on disk until you do a --full re-sync into a fresh directory.

#### Options

##### --output

Specify a custom output directory (default bee-sync ):

```
bee sync --output ~/my-bee-data
```

##### --only

Limit sync to a comma-separated list of data types ( facts , todos , daily , conversations , or all ):

```
# Only sync facts
bee sync --only facts
 
# Sync facts and todos
bee sync --only facts,todos
 
# Only sync conversations
bee sync --only conversations
 
# Only sync daily summaries
bee sync --only daily
```

##### --recent-days

Limit daily summaries and conversations to the last N days (facts and todos are always synced in full):

```
bee sync --recent-days 7
```

--recent-days applies to **full syncs only** . It is ignored on an incremental run, where the set of items to fetch is driven by the changefeed cursor.

##### --full

Force a complete re-sync, ignoring the saved manifest and rewriting it with fresh cursors:

```
bee sync --full
```

##### --since

Advanced/recovery option: override the saved incremental cursor with an explicit epoch-milliseconds timestamp for the changefeed-driven targets (daily summaries and conversations). Most users never need this — prefer the default incremental behavior or --full .

```
bee sync --since 1704067200000
```

#### Output Structure

After running bee sync , your data is organized as follows. Conversations live in a **separate top-level conversations/ tree** (one folder per day), parallel to daily/ — they are not nested under daily summaries.
\* bee-sync
\* .bee-sync.json
\* facts.md
\* todos.md
\* daily
\* 2024-01-15
\* summary.md
\* 2024-01-14
\* conversations
\* 2024-01-15
\* 123.md
\* 124.md
\* 2024-01-14

#### File Formats

All timestamps are written in ISO 8601 format (UTC).

##### facts.md

All facts, organized by confirmation status. Each line is - text [tags] (ISO timestamp, id N) ; tags are omitted when empty.

```
# Facts
 
## Confirmed
 
- Fact text here [tag1, tag2] (2024-01-15T10:30:00.000Z, id 42)
- Another fact (2024-01-14T08:00:00.000Z, id 41)
 
## Pending
 
- Unconfirmed fact (2024-01-16T12:00:00.000Z, id 43)
```

##### todos.md

All todos, organized by completion status. Each line is - text (id N, created ISO, alarm ISO) ; the alarm clause is omitted when no alarm is set. There are no checkboxes.

```
# Todos
 
## Open
 
- Buy groceries (id 10, created 2024-01-15T09:00:00.000Z, alarm 2024-01-16T18:00:00.000Z)
- Call dentist (id 11, created 2024-01-15T10:00:00.000Z)
 
## Completed
 
- Finish report (id 9, created 2024-01-14T08:00:00.000Z)
```

##### daily/YYYY-MM-DD/summary.md

Daily summary with metadata bullets followed by section headings. Optional sections (Summary, Email Summary, Calendar Summary) appear only when present.

```
# Daily Summary — 2024-01-15
 
- id: 100
- date_time: 2024-01-15T00:00:00.000Z
- created_at: 2024-01-16T02:00:00.000Z
- conversations_count: 5
 
## Short Summary
 
Brief overview of the day's activities.
 
## Summary
 
Detailed summary of conversations and events.
 
## Email Summary
 
Summary of email activity (if available).
 
## Calendar Summary
 
Summary of calendar events (if available).
 
## Locations
 
- 123 Main St, City (37.77490, -122.41940)
- Coffee Shop (37.78500, -122.40900)
 
## Conversations
 
- 123 (2024-01-15T09:00:00.000Z - 2024-01-15T09:30:00.000Z) — Meeting with team
- 124 (2024-01-15T14:00:00.000Z - 2024-01-15T14:15:00.000Z) — Quick chat
```

##### conversations/YYYY-MM-DD/ID.md

Individual conversation transcripts with full details: metadata bullets, summaries, primary location, suggested links, and transcriptions grouped under ### Transcription

```
# Conversation 123
 
- start_time: 2024-01-15T09:00:00.000Z
- end_time: 2024-01-15T09:30:00.000Z
- device_type: ios
- state: processed
- created_at: 2024-01-15T09:00:00.000Z
- updated_at: 2024-01-15T10:00:00.000Z
 
## Short Summary
 
Brief description of the conversation.
 
## Summary
 
Detailed summary of what was discussed.
 
## Primary Location
 
- 123 Main St, City (37.77490, -122.41940)
- created_at: 2024-01-15T09:00:00.000Z
 
## Suggested Links
 
- https://example.com/resource (2024-01-15T09:15:00.000Z)
 
## Transcriptions
 
### Transcription 456
- realtime: false
 
- Speaker 1: Hello, how are you?
- Speaker 2: I'm doing well, thanks!
```

#### Notes

```
*  The first sync (or any --full run) fetches everything; facts and todos are always re-fetched in full.
*  Re-runs are incremental: only daily summaries and conversations that changed since the last run are re-fetched, tracked via the .bee-sync.json manifest in the output directory.
*  Conversations and daily summaries are fetched concurrently for faster syncing.
*  All timestamps are in ISO 8601 format (UTC).
*  The output directory is created if it doesn't exist.
*  Existing files for changed items are overwritten in place; deletes are not reconciled, so a local file for an item later deleted on the server remains until a --full re-sync into a fresh directory.
```

#### Automation

You can automate sync with a cron job:

```
# Add to crontab (runs daily at midnight); incremental re-runs keep this cheap
0 0 * * * cd ~/bee-backup && bee sync
```

Or use a shell alias for quick syncing:

```
# Add to ~/.bashrc or ~/.zshrc
alias bee-backup="bee sync --output ~/Dropbox/bee-backup"
```

Last updated on February 10, 2026
[Realtime Sync](https://docs.bee.computer/docs/realtime) [API](https://docs.bee.computer/docs/proxy)
2026 © Bee Computer