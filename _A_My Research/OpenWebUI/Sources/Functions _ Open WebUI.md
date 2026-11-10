---
tags:
  - notebooklm-import
notebook: "OpenWebUI"
category: "research"
---

Functions / Open WebUI
[Skip to main content](https://docs.openwebui.com/features/extensibility/plugin/functions/#__docusaurus_skipToContent_fallback)
[Open WebUI](https://docs.openwebui.com/) [Blog](https://openwebui.com/blog)
[GitHub](https://github.com/open-webui/open-webui) [Discord](https://discord.com/invite/5rJgQTnV4s)

```

```

[Open WebUI](https://docs.openwebui.com/)
\* [Blog](https://openwebui.com/blog)
\* [GitHub](https://github.com/open-webui/open-webui)
\* [Discord](https://discord.com/invite/5rJgQTnV4s)
← Back to main menu
\* [🏡 Home](https://docs.openwebui.com/)
\* [🚀 Getting Started](https://docs.openwebui.com/getting-started/)
\* [📖 Reference](https://docs.openwebui.com/reference/)
\* [⭐ Features](https://docs.openwebui.com/features/)
\* [🔐 Authentication & Access](https://docs.openwebui.com/features/authentication-access/)
\* [🔧 Administration](https://docs.openwebui.com/features/administration/)
\* [💬 Chat & Conversations](https://docs.openwebui.com/features/extensibility/plugin/functions/)
\* [🧠 Workspace](https://docs.openwebui.com/features/extensibility/plugin/functions/)
\* [📝 Notes](https://docs.openwebui.com/features/notes/)
\* [📢 Channels](https://docs.openwebui.com/features/channels/)
\* [💻 Open Terminal](https://docs.openwebui.com/features/open-terminal/)
\* [🔌 Plugins & Extensibility](https://docs.openwebui.com/features/extensibility/)
\* [Tools & Functions (Plugins)](https://docs.openwebui.com/features/extensibility/plugin/)
\* [Tools](https://docs.openwebui.com/features/extensibility/plugin/tools/)
\* [Functions](https://docs.openwebui.com/features/extensibility/plugin/functions/)
\* [Action Function](https://docs.openwebui.com/features/extensibility/plugin/functions/action)
\* [Filter Function](https://docs.openwebui.com/features/extensibility/plugin/functions/filter)
\* [Pipe Function](https://docs.openwebui.com/features/extensibility/plugin/functions/pipe)
\* [Development](https://docs.openwebui.com/category/development)
\* [Migrating Tools & Functions: 0.4 to 0.5](https://docs.openwebui.com/features/extensibility/plugin/migration/)
\* [Model Context Protocol (MCP)](https://docs.openwebui.com/features/extensibility/mcp)
\* [Pipelines](https://docs.openwebui.com/features/extensibility/pipelines/)
\* [🛠 Troubleshooting](https://docs.openwebui.com/troubleshooting/)
\* [🏢 Open WebUI for Enterprise](https://docs.openwebui.com/enterprise/)
\* [🎓 Tutorials](https://docs.openwebui.com/tutorials/)
\* [❓ FAQ](https://docs.openwebui.com/faq)
\* [🛣 Roadmap](https://docs.openwebui.com/roadmap)
\* [🛡 Security Policy](https://docs.openwebui.com/security)
\* [🤝 Contributing](https://docs.openwebui.com/contributing)
\* [💖 Sponsorships](https://docs.openwebui.com/sponsorships)
\* [🎨 Brand Guidelines](https://docs.openwebui.com/brand)
\* [⚖ Open WebUI License](https://docs.openwebui.com/license)
\* [🎯 Our Mission](https://docs.openwebui.com/mission)
\* [👥 Our Team](https://docs.openwebui.com/team)
\* [⭐ Features](https://docs.openwebui.com/features/)
\* [🔌 Plugins & Extensibility](https://docs.openwebui.com/features/extensibility/)
\* [Tools & Functions (Plugins)](https://docs.openwebui.com/features/extensibility/plugin/)
\* Functions
On this page

### 🧩 Functions

⚠ Critical Security Warning
**Functions execute arbitrary Python code on your server.** Function creation is restricted to administrators only. Only install from trusted sources and review code before importing. A malicious Function could access your file system, exfiltrate data, or compromise your entire system. For full details, see the [Plugin Security Warning](https://docs.openwebui.com/features/extensibility/plugin/).
Functions are **modular Python plugins** that extend the capabilities of Open WebUI itself. While [Tools](https://docs.openwebui.com/features/extensibility/plugin/tools/) give LLMs the ability to call external APIs during inference, Functions change how the platform behaves at a deeper level. They can add entirely new "models" powered by any Python logic, intercept and transform every message flowing through the system, or place interactive buttons directly in the chat UI.
The possibilities are broad: connect a proprietary AI provider, build a smart home controller that responds to natural language, create a database query interface, add real-time translation to every conversation, enforce compliance policies, generate charts from data, or trigger external workflows with a button click. If you can write it in Python, you can turn it into a Function.
Functions are stored in the database as Python source code, dynamically loaded at runtime, and executed server-side. Administrators create and manage them; regular users interact with the results.

#### Function Types

Open WebUI supports three types of Functions. The type is **auto-detected** from the class name in your Python code, so you never need to configure it manually.

| Type | Class Name | What It Does | How Users See It |
| --- | --- | --- | --- |
| **Pipe** | class Pipe | Adds a custom model or agent | Appears as a selectable model in the chat sidebar |
| **Filter** | class Filter | Intercepts data flowing to/from models | Runs transparently as middleware on existing models |
| **Action** | class Action | Adds interactive buttons to messages | Appears as a clickable button on chat messages |

##### Pipe Functions

A Pipe registers itself as a new "model" in Open WebUI. When a user selects it and sends a message, the pipe() method handles the entire request with no LLM backend required. This makes Pipes incredibly versatile:
\* **Model providers** : Integrate APIs that don't follow the OpenAI protocol (Anthropic native, Google Vertex, custom inference servers).
\* **Agents & workflows** : Build multi-step agents that call tools, search the web, and reason across multiple turns.
\* **Non-LLM interfaces** : Create a smart home controller, a database query tool, a search engine, a calculator, or a code executor. Anything that takes user input and returns a response.
\* **Proxies & routers** : Route requests through your own logic, add caching, load balancing, or cost tracking.
A single Pipe can also expose **multiple models** (called a "manifold") by defining a pipes() method that returns a list of model identifiers.
→ **Pipe Function Guide**

##### Filter Functions

A Filter sits between the user and the model, intercepting data at three stages:
\* **inlet()** : Modifies the request **before** it reaches the model (add context, sanitize input, detect language, enforce rate limits, estimate token costs).
\* **stream()** : Intercepts **streamed chunks** from the model in real time (censor content, replace terms, track token usage).
\* **outlet()** : Processes the completed response **after** it's generated (log to observability platforms, format citations, append disclaimers, cache responses).
Filters enable powerful cross-cutting concerns like real-time translation, content moderation, prompt injection detection, A/B testing, compliance logging, and PII redaction, all without modifying the underlying model.
Filters can be applied globally (to all models) or attached to specific models. Toggleable filters let users enable/disable them per-chat.
→ **Filter Function Guide**

##### Action Functions

An Action adds a custom button to the chat message toolbar. When a user clicks it, the action() method runs with full access to the event system for real-time UI feedback, user prompts, and confirmations.
Actions can do anything Python can do: summarize or translate a message, copy formatted output, pin important messages, export conversations to external systems, trigger a CI/CD pipeline, send a Slack notification, generate a PDF report, run a code snippet, or kick off an external workflow.
→ **Action Function Guide**

#### How Functions Work

##### Type Detection

When you save a Function, Open WebUI scans the Python source code for a top-level class named Pipe , Filter , or Action . The first match determines the function type. You never need to manually set the type because it's inferred from the code.

```
# This is detected as a Pipe function:
class Pipe:
    def pipe(self, body: dict) -> str:
        return "Hello from my custom model!"
# This is detected as a Filter function:
class Filter:
    def inlet(self, body: dict) -> dict:
        return body
```

##### Module Loading & Caching

The Python source code is loaded via exec() into a temporary module namespace. Once loaded, the module is cached in memory ( request.app.state.FUNCTIONS ) and only reloaded when the source code changes. Import statements in your code are automatically rewritten to resolve within the Open WebUI package namespace.

##### Frontmatter

A triple-quoted docstring at the top of the file is parsed as YAML frontmatter for metadata:

```
"""
title: My Custom Function
author: your_name
author_url: https://github.com/your_name
version: 1.0.0
icon_url: https://example.com/icon.svg
required_open_webui_version: 0.4.0
requirements: requests, beautifulsoup4
"""
```

| Field | Purpose |
| --- | --- |
| title | Display name in the admin UI |
| author / author\_url | Attribution metadata |
| version | Version identifier |
| icon\_url | Icon displayed next to the function name (use a URL, not base64) |
| required\_open\_webui\_version | Minimum compatible Open WebUI version |
| requirements | Comma-separated list of pip packages to auto-install |

Automatic Dependency Installation
When requirements is specified in the frontmatter, Open WebUI automatically installs the listed packages via pip the first time the function loads. This is controlled by the PIP\_INSTALL\_FRONTMATTER\_REQUIREMENTS environment variable (enabled by default).

#### Installing Functions

##### From the Community Library

```
1. Browse the [Community Function Library](https://openwebui.com/search).
1. Click  **Get**  on the function you want.
1. Enter your Open WebUI instance URL (e.g., http://localhost:3000 ).
1. Click  **Import to Open WebUI** . You'll be redirected to the Function Editor.
1. Review the code, then click  **Save** .
```

warning
Always review the source code before importing. Community functions are user-contributed and **run directly on your server** .

##### From a URL

```
1. Go to  **Admin Panel → Functions** .
1. Click  **Import from URL**  and paste a link to the Python file.
*  GitHub URLs are automatically converted to raw file URLs.
1. Review and save.
```

##### Create Manually

```
1. Go to  **Admin Panel → Functions** .
1. Click  **Create** .
1. Enter an ID (alphanumeric and underscores only), name, and description.
1. Write your Python code in the editor.
1. Click  **Save** . The function type is auto-detected from your code.
```

#### Managing Functions

##### Admin Controls

Functions are managed from **Admin Panel → Functions** . Each function has the following controls:

| Control | Description |
| --- | --- |
| **Active toggle** | Enables or disables the function. Disabled functions are not loaded or executed. |
| **Global toggle** | When enabled, the function applies to **all models** automatically. Available for Filters and Actions. |
| **Valves** (⚙ gear icon) | Opens the admin-configurable settings for this function. |
| **Export / Delete** | Export the function as a file or remove it. |

##### Assigning Functions to Specific Models

Instead of making a Filter or Action global, you can attach it to specific models:
1. Go to **Workspace → Models** .
1. Edit the target model.
1. In the **Filters** or **Actions** section, select the functions you want to attach.
This allows different models to use different filters. For example, you might apply a content-moderation filter only on public-facing models.

##### Toggleable Filters

Filters can be made user-toggleable by setting self.toggle = True in **init** . When toggleable, users see an on/off switch in the chat input area and can enable or disable the filter per-conversation. Filters without self.toggle are always-on when active.

#### Valves & UserValves

Functions support a two-tier configuration system built on [Pydantic](https://docs.pydantic.dev/):

| Level | Class Name | Who Configures | Where |
| --- | --- | --- | --- |
| **Admin** | Valves | Administrators only | Admin Panel → Functions → ⚙ |
| **User** | UserValves | Any user | Chat interface, per-function |

**Valves** are ideal for API keys, model endpoints, and global behavior settings. **UserValves** let individual users customize behavior (e.g., their preferred language, output format, or personal API key).
Both are defined as nested Pydantic BaseModel classes inside your Pipe , Filter , or Action class. The admin-configured values are stored in the database and loaded automatically at runtime.
→ **Valves Development Guide**

#### Functions vs Tools: When to Use Which

| Use Case | Use a... | Why |
| --- | --- | --- |
| Give the LLM access to live data (weather, stocks, APIs) | **Tool** | Tools are called by the model during inference |
| Add a model provider with a non-OpenAI API | **Pipe Function** | Pipes register as models in the sidebar |
| Build a non-LLM interface (search, databases, smart home) | **Pipe Function** | Pipes handle the entire request without needing an LLM |
| Build a multi-step agent with custom logic | **Pipe Function** | Pipes control the full request/response cycle |
| Translate, moderate, or redact content in real time | **Filter Function** | Filters intercept every message transparently |
| Log requests to an observability platform | **Filter Function** | Inlet/outlet filters see all traffic |
| Rate-limit or enforce usage policies | **Filter Function** | Inlet filters can reject requests before the model |
| Add a button to export, summarize, or share messages | **Action Function** | Actions appear on the message toolbar |
| Trigger an external workflow from the chat UI | **Action Function** | Actions run arbitrary Python on click |

#### Development Resources

| Guide | Description |
| --- | --- |
| [Pipe Function Guide](https://docs.openwebui.com/features/extensibility/plugin/functions/pipe) | Build custom models, agents, and non-LLM interfaces |
| [Filter Function Guide](https://docs.openwebui.com/features/extensibility/plugin/functions/filter) | Intercept, translate, moderate, and log messages |
| [Action Function Guide](https://docs.openwebui.com/features/extensibility/plugin/functions/action) | Add buttons for export, workflows, and interactive tasks |
| [Valves](https://docs.openwebui.com/features/extensibility/plugin/development/valves) | Configure functions with admin and user settings |
| [Events](https://docs.openwebui.com/features/extensibility/plugin/development/events) | Send real-time updates to the UI |
| [Reserved Arguments](https://docs.openwebui.com/features/extensibility/plugin/development/reserved-args) | **user** , **event\_emitter** , **metadata** , and more |
| [Rich UI](https://docs.openwebui.com/features/extensibility/plugin/development/rich-ui) | Embed interactive HTML/JS content in responses |

[Edit this page](https://github.com/open-webui/docs/blob/main/docs/features/extensibility/plugin/functions/index.mdx)
[Previous FAQ](https://docs.openwebui.com/features/extensibility/plugin/tools/openapi-servers/faq)
[Next Action Function](https://docs.openwebui.com/features/extensibility/plugin/functions/action)
Docs
\* [Getting Started](https://docs.openwebui.com/getting-started)
\* [FAQ](https://docs.openwebui.com/faq)
\* [Help Improve The Docs](https://github.com/open-webui/docs)
Community
\* [GitHub](https://github.com/open-webui/open-webui)
\* [Discord](https://discord.gg/5rJgQTnV4s)
\* [Reddit](https://www.reddit.com/r/OpenWebUI/)
\* [𝕏](https://x.com/OpenWebUI)
More
\* [Release Notes](https://github.com/open-webui/open-webui/blob/main/CHANGELOG.md)
\* [About](https://openwebui.com/)
\* [Report a Vulnerability / Responsible Disclosure](https://github.com/open-webui/open-webui/security)