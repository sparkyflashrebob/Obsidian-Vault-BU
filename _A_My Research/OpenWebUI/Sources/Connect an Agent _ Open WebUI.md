---
tags:
  - notebooklm-import
notebook: "OpenWebUI"
category: "research"
---

Connect an Agent / Open WebUI
[Skip to main content](https://docs.openwebui.com/getting-started/quick-start/connect-an-agent#__docusaurus_skipToContent_fallback)
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
\* [Quick Start](https://docs.openwebui.com/getting-started/quick-start/)
\* [Connect a Provider](https://docs.openwebui.com/getting-started/quick-start/connect-a-provider/)
\* [Connect an Agent](https://docs.openwebui.com/getting-started/quick-start/connect-an-agent/)
\* [Hermes Agent](https://docs.openwebui.com/getting-started/quick-start/connect-an-agent/hermes-agent)
\* [OpenClaw](https://docs.openwebui.com/getting-started/quick-start/connect-an-agent/openclaw)
\* [Understanding Settings](https://docs.openwebui.com/getting-started/quick-start/settings)
\* [Sharing Open WebUI](https://docs.openwebui.com/getting-started/sharing)
\* [Updating Open WebUI](https://docs.openwebui.com/getting-started/updating)
\* [Advanced Topics](https://docs.openwebui.com/getting-started/advanced-topics/)
\* [📖 Reference](https://docs.openwebui.com/reference/)
\* [⭐ Features](https://docs.openwebui.com/features/)
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
\* [🚀 Getting Started](https://docs.openwebui.com/getting-started/)
\* [Quick Start](https://docs.openwebui.com/getting-started/quick-start/)
\* Connect an Agent
On this page

### 🤖 Connect an Agent

**Use Open WebUI as the chat frontend for autonomous AI agents.**
AI agents go beyond simple model providers. They can execute terminal commands, read and write files, search the web, manage memory, and chain complex workflows. Because many agent frameworks expose an **OpenAI-compatible API** , Open WebUI can serve as a polished, full-featured chat interface for them with minimal setup.

#### How Is This Different from a Provider?

When you [connect a provider](https://docs.openwebui.com/getting-started/quick-start/connect-a-provider/starting-with-openai-compatible), you're connecting to a **model** . It receives your message and returns a response. That's it.
When you connect an **agent** , you're connecting to an autonomous system that can:
\* 🖥 **Run terminal commands** on your machine
\* 📁 **Read and write files** in your workspace
\* 🔍 **Search the web** for real-time information
\* 🧠 **Maintain memory** across conversations
\* 🧩 **Use skills and plugins** to extend its capabilities
\* 🔗 **Chain multiple tool calls** to solve complex tasks
The agent decides when and how to use these tools based on your message, and Open WebUI displays the results in a familiar chat interface.

#### Available Agents

| Agent | Description | Guide |
| --- | --- | --- |
| **Hermes Agent** | Autonomous agent by Nous Research with terminal, file ops, web search, memory, and extensible skills | [Set up Hermes Agent →](https://docs.openwebui.com/getting-started/quick-start/connect-an-agent/hermes-agent) |
| **OpenClaw** | Open-source self-hosted agent framework with shell access, file operations, web browsing, and messaging channel integrations | [Set up OpenClaw →](https://docs.openwebui.com/getting-started/quick-start/connect-an-agent/openclaw) |

#### How It Works

Regardless of which agent you connect, the architecture is the same:

```
┌──────────────┐         ┌──────────────────┐         ┌──────────────┐
│              │  HTTP    │                  │  Tools  │              │
│  Open WebUI  │────────▶│   Agent Gateway  │────────▶│  Terminal,   │
│  (frontend)  │◀────────│   (API server)   │◀────────│  Files, Web  │
│              │  Stream  │                  │  Results│              │
└──────────────┘         └──────────────────┘         └──────────────┘
```

```
1.  **You type a message**  in Open WebUI
1. Open WebUI sends it to the agent's API server (just like it would to OpenAI)
1. The agent  **decides which tools to use** , executes them, and reasons about the results
1. The final response  **streams back**  to Open WebUI with optional progress indicators
1. You see the response in the familiar chat interface, with full conversation history, user accounts, and all Open WebUI features
```

tip
Because agents speak the standard OpenAI Chat Completions protocol, adding one is as simple as adding the URL and API key in **Admin Settings → Connections → OpenAI** . No plugins, no pipes, no middleware required.
[Edit this page](https://github.com/open-webui/docs/blob/main/docs/getting-started/quick-start/connect-an-agent/index.md)
[Previous Open Responses](https://docs.openwebui.com/getting-started/quick-start/connect-a-provider/starting-with-open-responses)
[Next Hermes Agent](https://docs.openwebui.com/getting-started/quick-start/connect-an-agent/hermes-agent)
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