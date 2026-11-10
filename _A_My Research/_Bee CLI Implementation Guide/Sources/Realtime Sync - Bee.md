---
tags:
  - notebooklm-import
notebook: "_Bee CLI Implementation Guide"
category: "research"
---

Realtime Sync - Bee
[Bee](https://docs.bee.computer/)
[Docs](https://docs.bee.computer/docs) [API](https://docs.bee.computer/docs/proxy) [Skill](https://docs.bee.computer/docs/skill) [MCP](https://docs.bee.computer/docs/mcp) 
[Skip to Content](https://docs.bee.computer/docs/realtime#nextra-skip-nav)
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
\* [Basic Usage](https://docs.bee.computer/docs/realtime#basic-usage)
\* [Flags](https://docs.bee.computer/docs/realtime#flags)
\* [Event Types](https://docs.bee.computer/docs/realtime#event-types)
\* [Connection Events](https://docs.bee.computer/docs/realtime#connection-events)
\* [Conversation Events](https://docs.bee.computer/docs/realtime#conversation-events)
\* [Todo Events](https://docs.bee.computer/docs/realtime#todo-events)
\* [Journal Events](https://docs.bee.computer/docs/realtime#journal-events)
\* [Payload Shapes](https://docs.bee.computer/docs/realtime#payload-shapes)
\* [new-utterance](https://docs.bee.computer/docs/realtime#new-utterance)
\* [new-conversation](https://docs.bee.computer/docs/realtime#new-conversation)
\* [update-conversation](https://docs.bee.computer/docs/realtime#update-conversation)
\* [update-conversation-summary](https://docs.bee.computer/docs/realtime#update-conversation-summary)
\* [delete-conversation](https://docs.bee.computer/docs/realtime#delete-conversation)
\* [update-location](https://docs.bee.computer/docs/realtime#update-location)
\* [todo-created / todo-updated](https://docs.bee.computer/docs/realtime#todo-created--todo-updated)
\* [todo-deleted](https://docs.bee.computer/docs/realtime#todo-deleted)
\* [journal-created / journal-updated](https://docs.bee.computer/docs/realtime#journal-created--journal-updated)
\* [journal-deleted](https://docs.bee.computer/docs/realtime#journal-deleted)
\* [journal-text](https://docs.bee.computer/docs/realtime#journal-text)
\* [Output Modes](https://docs.bee.computer/docs/realtime#output-modes)
\* [Default mode ( bee stream )](https://docs.bee.computer/docs/realtime#default-mode-bee-stream)
\* [Agent mode ( bee stream --agent )](https://docs.bee.computer/docs/realtime#agent-mode-bee-stream---agent)
\* [JSON mode ( bee stream --json )](https://docs.bee.computer/docs/realtime#json-mode-bee-stream---json)
\* [Processing with jq](https://docs.bee.computer/docs/realtime#processing-with-jq)
\* [Webhooks](https://docs.bee.computer/docs/realtime#webhooks)
\* [Use Cases](https://docs.bee.computer/docs/realtime#use-cases)
\* [Real-Time Dashboard](https://docs.bee.computer/docs/realtime#real-time-dashboard)
\* [Integration with Other Tools](https://docs.bee.computer/docs/realtime#integration-with-other-tools)
\* [Live Notifications](https://docs.bee.computer/docs/realtime#live-notifications)
\* [Logging](https://docs.bee.computer/docs/realtime#logging)
\* [Running in the Background](https://docs.bee.computer/docs/realtime#running-in-the-background)
\* [Example: Building a Live Feed](https://docs.bee.computer/docs/realtime#example-building-a-live-feed)
[Question? Give us feedback](https://github.com/shuding/nextra/issues/new?title=Feedback%20for%20%E2%80%9CRealtime%20Sync%E2%80%9D&labels=feedback) [Edit this page](https://github.com/shuding/nextra/content/realtime.mdx) Scroll to top
Realtime Sync
Copy page

### Realtime Sync

The bee stream command provides real-time event streaming from your Bee device, allowing you to receive live updates as conversations happen and data changes. bee stream is real-time and does not guarantee delivery (at-most-once semantics). The stream requires an active internet connection, and events that occur while disconnected will not be received. If you need reliability/completeness, prefer a full bee sync snapshot.

#### Basic Usage

```
# Human-readable with colors (default)
bee stream
 
# Human-readable, token-optimized for inference (no colors)
bee stream --agent
 
# Structured JSON output
bee stream --json
 
# Filter to specific event types (comma-separated)
bee stream --types new-utterance,update-conversation
 
# Receive every event type explicitly
bee stream --types all
```

This starts a persistent connection that outputs events as they occur.

#### Flags

| Flag | Description |
| --- | --- |
| --types | Comma-separated event types to receive (e.g. new-utterance,todo-created ). Pass --types all to receive everything. When omitted, all events are streamed. |
| --json | Emit each event's raw JSON payload, one object per line, for programmatic parsing. |
| --agent | Single-line, token-efficient, color-free output optimized for inference. |
| --webhook-endpoint | POST each (filtered) event to this URL. Requires --webhook-body . |
| --webhook-body | Handlebars template for the webhook request body. Requires --webhook-endpoint . |

#### Event Types

The stream emits the following event types.

##### Connection Events

| Event | Description |
| --- | --- |
| connected | Successfully connected to the stream |

##### Conversation Events

| Event | Description |
| --- | --- |
| new-utterance | A new transcript snippet was captured |
| new-conversation | A new conversation started |
| update-conversation | An existing conversation was updated |
| update-conversation-summary | A conversation's short summary was updated |
| delete-conversation | A conversation was deleted |
| update-location | A conversation's location was updated |

##### Todo Events

| Event | Description |
| --- | --- |
| todo-created | A new todo was created |
| todo-updated | An existing todo was updated |
| todo-deleted | A todo was deleted |

##### Journal Events

| Event | Description |
| --- | --- |
| journal-created | A new journal entry was created |
| journal-updated | An existing journal entry was updated |
| journal-deleted | A journal entry was deleted |
| journal-text | Raw journal text streamed in (e.g. as a voice note is transcribed) |

#### Payload Shapes

In --json mode, bee stream prints the **raw event payload** — there is **no top-level event field** . Distinguish events by their structural keys (for example, a new-utterance has an utterance object; a new-conversation has a conversation object). Do **not** filter with jq 'select(.event == "...")' — that key does not exist in the JSON output and the filter will silently match nothing. Use bee stream --types

##### new-utterance

```
{
  "utterance": {
    "text": "Hello there",
    "speaker": "speaker_1"
  },
  "conversation_uuid": "uuid-string"
}
```

##### new-conversation

```
{
  "conversation": {
    "id": 123,
    "uuid": "uuid-string",
    "state": "processing",
    "title": "Optional title"
  }
}
```

id is a **number** , not a string.

##### update-conversation

```
{
  "conversation": {
    "id": 123,
    "state": "processed",
    "title": "Optional title",
    "short_summary": "Optional short summary"
  }
}
```

##### update-conversation-summary

```
{
  "conversation_id": 123,
  "short_summary": "Summary text"
}
```

##### delete-conversation

```
{
  "conversation": {
    "id": 123,
    "title": "Optional title"
  }
}
```

##### update-location

```
{
  "conversation_id": 123,
  "location": {
    "latitude": 37.77,
    "longitude": -122.41,
    "name": "Optional name"
  }
}
```

##### todo-created / todo-updated

```
{
  "todo": {
    "id": 10,
    "text": "Call dentist",
    "completed": false,
    "alarmAt": 1700000000000
  }
}
```

##### todo-deleted

```
{
  "todo": {
    "id": 10,
    "text": "Optional text"
  }
}
```

##### journal-created / journal-updated

```
{
  "journal": {
    "id": 55,
    "state": "processed",
    "text": "Optional raw text",
    "aiResponse": {
      "message": "Optional assistant message",
      "cleanedUpText": "Optional cleaned text",
      "followUp": "Optional follow up",
      "todos": ["Optional todo"]
    }
  }
}
```

##### journal-deleted

```
{
  "journalId": 55,
  "reason": "Optional reason"
}
```

##### journal-text

```
{
  "journalId": 55,
  "text": "Optional raw text"
}
```

#### Output Modes

##### Default mode ( bee stream )

Human-readable stream output with colors for terminal usage.

##### Agent mode ( bee stream --agent )

Human-readable output optimized for inference/token efficiency, with no color formatting. Each line looks like:

```
Event new-utterance: [speaker_1] "Hello there" conv=uuid-string
```

##### JSON mode ( bee stream --json )

The raw payload for each event, one JSON object per line, for programmatic parsing. Remember there is no top-level event field — see [Payload Shapes](https://docs.bee.computer/docs/realtime#payload-shapes).

#### Processing with jq

Because --json prints the raw payload, distinguish events by **structural keys** rather than an event field:

```
# Extract text from new utterances (only utterance events have .utterance)
bee stream --json | jq -r 'select(.utterance) | .utterance.text'
 
# Titles of newly created/updated conversations
bee stream --json | jq -r 'select(.conversation) | .conversation.title // empty'
 
# Conversation UUID attached to each utterance
bee stream --json | jq -r 'select(.conversation_uuid) | .conversation_uuid'
```

To filter by event type, prefer the server-side --types flag (it avoids fetching events you don't need):

```
# Only utterances
bee stream --types new-utterance --json | jq -r '.utterance.text'
 
# Only new conversations
bee stream --types new-conversation --json | jq -r '.conversation.title // empty'
```

#### Webhooks

Forward events to an external service without piping through a shell. The --webhook-body is a [Handlebars](https://handlebarsjs.com/) template; both --webhook-endpoint and --webhook-body are required together. Each matched event POSTs the rendered body to the endpoint.
Available template variables:

| Variable | Description |
| --- | --- |
| {{message}} / {{agentMessage}} | The agent-friendly single-line message (same as --agent ) |
| {{event}} | The event type name (e.g. new-utterance ) |
| {{timestamp}} | ISO timestamp of when the event was received |
| {{raw}} | The raw JSON payload string |
| {{data.\*}} | The parsed payload fields (e.g. {{data.utterance.text}} ) |

```
bee stream \
  --types new-utterance,new-conversation \
  --webhook-endpoint https://example.com/hooks/agent \
  --webhook-body '{"message":"{{message}}"}'
```

--types also scopes which events are delivered to the webhook.

#### Use Cases

##### Real-Time Dashboard

Pipe stream output to build live dashboards:

```
bee stream | while read event; do
  echo "$event" >> ~/bee-events.log
  # Process event...
done
```

##### Integration with Other Tools

Send events to external services. For a single integration, prefer --webhook-endpoint ; for ad-hoc forwarding you can pipe instead:

```
bee stream --json | while read event; do
  curl -X POST https://your-webhook.com/bee \
    -H "Content-Type: application/json" \
    -d "$event"
done
```

##### Live Notifications

Create desktop notifications for new conversations:

```
bee stream --types new-conversation --json \
  | jq -r '.conversation.title // empty' \
  | while read title; do
      osascript -e "display notification \"$title\" with title \"New Conversation\""
    done
```

##### Logging

Create a persistent log of all Bee activity:

```
bee stream >> ~/bee-activity-$(date +%Y-%m-%d).log
```

#### Running in the Background

Run the stream as a background process:

```
# Start in background
nohup bee stream >> ~/bee-events.log 2>&1 &
 
# Or use screen/tmux
screen -dmS bee-stream bee stream
```

#### Example: Building a Live Feed

Here's a complete example that creates a live feed of your conversations. It branches on structural keys, since the JSON payloads have no event field:

```
#!/bin/bash
 
echo "Starting Bee live feed..."
 
bee stream --json | while read -r line; do
  if echo "$line" | jq -e '.utterance' >/dev/null 2>&1; then
    speaker=$(echo "$line" | jq -r '.utterance.speaker')
    text=$(echo "$line" | jq -r '.utterance.text')
    echo "[$speaker]: $text"
  elif echo "$line" | jq -e '.conversation' >/dev/null 2>&1; then
    title=$(echo "$line" | jq -r '.conversation.title // "(untitled)"')
    echo "--- Conversation: $title ---"
  elif echo "$line" | jq -e '.todo' >/dev/null 2>&1; then
    todo=$(echo "$line" | jq -r '.todo.text // empty')
    [ -n "$todo" ] && echo "[Todo]: $todo"
  fi
done
```

Last updated on June 7, 2026
[Agentic Sync](https://docs.bee.computer/docs/agentic-sync) [Full Sync](https://docs.bee.computer/docs/sync)
2026 © Bee Computer