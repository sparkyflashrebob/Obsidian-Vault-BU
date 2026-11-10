---
tags:
  - notebooklm-import
notebook: "OpenWebUI"
category: "research"
---

Intel GPU (IPEX-LLM) / Open WebUI
[Skip to main content](https://docs.openwebui.com/tutorials/integrations/llm-providers/ipex_llm#__docusaurus_skipToContent_fallback)
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
\* [🛠 Troubleshooting](https://docs.openwebui.com/troubleshooting/)
\* [🏢 Open WebUI for Enterprise](https://docs.openwebui.com/enterprise/)
\* [🎓 Tutorials](https://docs.openwebui.com/tutorials/)
\* [Community Guides](https://docs.openwebui.com/tutorials/community/)
\* [Authentication & SSO](https://docs.openwebui.com/tutorials/auth-sso/)
\* [Integrations](https://docs.openwebui.com/tutorials/integrations/)
\* [LLM Providers](https://docs.openwebui.com/tutorials/integrations/llm-providers/ipex_llm)
\* [Azure OpenAI with EntraID](https://docs.openwebui.com/tutorials/integrations/llm-providers/azure-openai/)
\* [DeepSeek R1 Dynamic](https://docs.openwebui.com/tutorials/integrations/llm-providers/deepseekr1-dynamic)
\* [Intel GPU (IPEX-LLM)](https://docs.openwebui.com/tutorials/integrations/llm-providers/ipex_llm)
\* [Monitoring](https://docs.openwebui.com/tutorials/integrations/llm-providers/ipex_llm)
\* [Dev Tools](https://docs.openwebui.com/tutorials/integrations/llm-providers/ipex_llm)
\* [LibreTranslate](https://docs.openwebui.com/tutorials/integrations/libre-translate)
\* [OneDrive & SharePoint](https://docs.openwebui.com/tutorials/integrations/onedrive-sharepoint)
\* [Notion MCP Integration](https://docs.openwebui.com/tutorials/integrations/mcp-notion)
\* [Redis Websocket Support](https://docs.openwebui.com/tutorials/integrations/redis)
\* [Maintenance](https://docs.openwebui.com/tutorials/maintenance/)
\* [Contributing to Docs](https://docs.openwebui.com/tutorials/contributing-tutorial)
\* [❓ FAQ](https://docs.openwebui.com/faq)
\* [🛣 Roadmap](https://docs.openwebui.com/roadmap)
\* [🛡 Security Policy](https://docs.openwebui.com/security)
\* [🤝 Contributing](https://docs.openwebui.com/contributing)
\* [💖 Sponsorships](https://docs.openwebui.com/sponsorships)
\* [🎨 Brand Guidelines](https://docs.openwebui.com/brand)
\* [⚖ Open WebUI License](https://docs.openwebui.com/license)
\* [🎯 Our Mission](https://docs.openwebui.com/mission)
\* [👥 Our Team](https://docs.openwebui.com/team)
\* [🎓 Tutorials](https://docs.openwebui.com/tutorials/)
\* [Integrations](https://docs.openwebui.com/tutorials/integrations/)
\* LLM Providers
\* Intel GPU (IPEX-LLM)
On this page

### Intel GPU (IPEX-LLM)

warning
This tutorial is a community contribution and is not supported by the Open WebUI team. It serves only as a demonstration on how to customize Open WebUI for your specific use case. Want to contribute? Check out the [contributing tutorial](https://docs.openwebui.com/contributing).
note
This guide is verified with Open WebUI setup through [Manual Installation](https://docs.openwebui.com/getting-started/).

#### Local LLM Setup with IPEX-LLM on Intel GPU

info
[IPEX-LLM](https://github.com/intel-analytics/ipex-llm) is a PyTorch library for running LLM on Intel CPU and GPU (e.g., local PC with iGPU, discrete GPU such as Arc A-Series, Flex and Max) with very low latency.
This tutorial demonstrates how to setup Open WebUI with **IPEX-LLM accelerated Ollama backend hosted on Intel GPU** . By following this guide, you will be able to setup Open WebUI even on a low-cost PC (i.e. only with integrated GPU) with a smooth experience.

#### Start Ollama Serve on Intel GPU

Refer to [this guide](https://ipex-llm.readthedocs.io/en/latest/doc/LLM/Quickstart/ollama_quickstart.html) from IPEX-LLM official documentation about how to install and run Ollama serve accelerated by IPEX-LLM on Intel GPU.
tip
If you would like to reach the Ollama service from another machine, make sure you set or export the environment variable OLLAMA\_HOST=0.0.0.0 before executing the command ollama serve .

#### Configure Open WebUI

Access the Ollama settings through **Settings -> Connections** in the menu. By default, the **Ollama Base URL** is preset to [https://localhost:11434](https://localhost:11434/), as illustrated in the snapshot below. To verify the status of the Ollama service connection, click the **Refresh button** located next to the textbox. If the WebUI is unable to establish a connection with the Ollama server, you will see an error message stating, WebUI could not connect to Ollama .
If the connection is successful, you will see a message stating Service Connection Verified , as illustrated below.
tip
If you want to use an Ollama server hosted at a different URL, simply update the **Ollama Base URL** to the new URL and press the **Refresh** button to re-confirm the connection to Ollama.
[Edit this page](https://github.com/open-webui/docs/blob/main/docs/tutorials/integrations/llm-providers/ipex_llm.md)
[Previous DeepSeek R1 Dynamic](https://docs.openwebui.com/tutorials/integrations/llm-providers/deepseekr1-dynamic)
[Next Helicone](https://docs.openwebui.com/tutorials/integrations/monitoring/helicone)
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