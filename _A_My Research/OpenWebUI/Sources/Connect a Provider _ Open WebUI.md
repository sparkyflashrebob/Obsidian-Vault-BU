---
tags:
  - notebooklm-import
notebook: "OpenWebUI"
category: "research"
---

Connect a Provider / Open WebUI
[Skip to main content](https://docs.openwebui.com/getting-started/quick-start/connect-a-provider#__docusaurus_skipToContent_fallback)
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
\* [Ollama](https://docs.openwebui.com/getting-started/quick-start/connect-a-provider/starting-with-ollama)
\* [OpenAI](https://docs.openwebui.com/getting-started/quick-start/connect-a-provider/starting-with-openai)
\* [Anthropic (Claude)](https://docs.openwebui.com/getting-started/quick-start/connect-a-provider/starting-with-anthropic)
\* [Llama.cpp](https://docs.openwebui.com/getting-started/quick-start/connect-a-provider/starting-with-llama-cpp)
\* [vLLM](https://docs.openwebui.com/getting-started/quick-start/connect-a-provider/starting-with-vllm)
\* [OpenAI-Compatible](https://docs.openwebui.com/getting-started/quick-start/connect-a-provider/starting-with-openai-compatible)
\* [Functions](https://docs.openwebui.com/getting-started/quick-start/connect-a-provider/starting-with-functions)
\* [Open Responses](https://docs.openwebui.com/getting-started/quick-start/connect-a-provider/starting-with-open-responses)
\* [Connect an Agent](https://docs.openwebui.com/getting-started/quick-start/connect-an-agent/)
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
\* Connect a Provider
On this page

### 🔌 Connect a Provider

**Connect Open WebUI to any model provider and start chatting in minutes.**
Open WebUI supports multiple connection protocols, including **Ollama** , **OpenAI-compatible APIs** , and **Open Responses** . Any cloud API or local server that speaks one of these protocols works out of the box. Just add a URL and API key, and your models appear in the dropdown.

#### How It Works

```
┌──────────────┐         ┌──────────────────┐         ┌──────────────┐
│              │  HTTP    │                  │  Inference│             │
│  Open WebUI  │────────▶│  Provider API    │────────▶ │    Model     │
│  (frontend)  │◀────────│  (cloud/local)   │◀──────── │  (LLM/VLM)  │
│              │  Stream  │                  │  Tokens  │             │
└──────────────┘         └──────────────────┘         └──────────────┘
```

```
1.  **You type a message**  in Open WebUI
1. Open WebUI sends it to your provider's API endpoint
1. The provider runs inference on the selected model
1. Tokens  **stream back**  to Open WebUI in real time
1. You see the response in the chat interface
```

tip
Adding a provider is as simple as entering a URL and API key in **Admin Settings → Connections** . Open WebUI auto-detects available models from most providers.

#### Cloud Providers

Hosted APIs that require an account and API key. No hardware needed.

| Provider | Models | Guide |
| --- | --- | --- |
| **Ollama** | Llama, Mistral, Gemma, Phi, and thousands more (local) | [Starting with Ollama →](https://docs.openwebui.com/getting-started/quick-start/connect-a-provider/starting-with-ollama) |
| **OpenAI** | GPT-4o, GPT-4.1, o3, o4-mini | [Starting with OpenAI →](https://docs.openwebui.com/getting-started/quick-start/connect-a-provider/starting-with-openai) |
| **Anthropic** | Claude Opus, Sonnet, Haiku | [Starting with Anthropic →](https://docs.openwebui.com/getting-started/quick-start/connect-a-provider/starting-with-anthropic) |
| **OpenAI-Compatible** | Google Gemini, DeepSeek, Mistral, Groq, OpenRouter, Amazon Bedrock, Azure, and more | [OpenAI-Compatible Providers →](https://docs.openwebui.com/getting-started/quick-start/connect-a-provider/starting-with-openai-compatible) |

#### Local Servers

Run models on your own hardware. No API keys, no cloud dependency.

| Server | Description | Guide |
| --- | --- | --- |
| **llama.cpp** | Efficient GGUF model inference with OpenAI-compatible API | [Starting with llama.cpp →](https://docs.openwebui.com/getting-started/quick-start/connect-a-provider/starting-with-llama-cpp) |
| **vLLM** | High-throughput inference engine for production workloads | [Starting with vLLM →](https://docs.openwebui.com/getting-started/quick-start/connect-a-provider/starting-with-vllm) |

More local servers (LM Studio, LocalAI, Docker Model Runner, Lemonade) are covered in the [OpenAI-Compatible Providers](https://docs.openwebui.com/getting-started/quick-start/connect-a-provider/starting-with-openai-compatible#local-servers) guide.

#### Other Connection Methods

| Feature | Description | Guide |
| --- | --- | --- |
| **Open Responses** | Connect providers using the Open Responses specification | [Starting with Open Responses →](https://docs.openwebui.com/getting-started/quick-start/connect-a-provider/starting-with-open-responses) |
| **Functions** | Extend Open WebUI with custom pipe functions for any backend | [Starting with Functions →](https://docs.openwebui.com/getting-started/quick-start/connect-a-provider/starting-with-functions) |

#### Looking for Agents?

If you want to connect an autonomous AI agent (with terminal access, file operations, web search, and more) instead of a plain model provider, see [Connect an Agent](https://docs.openwebui.com/getting-started/quick-start/connect-an-agent).
[Edit this page](https://github.com/open-webui/docs/blob/main/docs/getting-started/quick-start/connect-a-provider/index.md)
[Previous Quick Start](https://docs.openwebui.com/getting-started/quick-start/)
[Next Ollama](https://docs.openwebui.com/getting-started/quick-start/connect-a-provider/starting-with-ollama)
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