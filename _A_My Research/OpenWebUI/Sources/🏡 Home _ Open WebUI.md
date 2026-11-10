---
tags:
  - notebooklm-import
notebook: "OpenWebUI"
category: "research"
---

🏡 Home / Open WebUI
[Skip to main content](https://docs.openwebui.com/#__docusaurus_skipToContent_fallback)
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
\* [❓ FAQ](https://docs.openwebui.com/faq)
\* [🛣 Roadmap](https://docs.openwebui.com/roadmap)
\* [🛡 Security Policy](https://docs.openwebui.com/security)
\* [🤝 Contributing](https://docs.openwebui.com/contributing)
\* [💖 Sponsorships](https://docs.openwebui.com/sponsorships)
\* [🎨 Brand Guidelines](https://docs.openwebui.com/brand)
\* [⚖ Open WebUI License](https://docs.openwebui.com/license)
\* [🎯 Our Mission](https://docs.openwebui.com/mission)
\* [👥 Our Team](https://docs.openwebui.com/team)
\* 🏡 Home
On this page

### Open WebUI

**Open WebUI is an extensible, feature-rich, and user-friendly self-hosted AI platform designed to operate entirely offline.** It supports **Ollama** and **OpenAI-compatible APIs** , making it a powerful, provider-agnostic solution for both local and cloud-based models.

#### Quick Start

```
*  Docker
*  pip
*  uv
*  Desktop
```

```
docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
```

Then open [http://localhost:3000](http://localhost:3000/).
For GPU support, Docker Compose, and more → [Full Docker guide](https://docs.openwebui.com/getting-started/quick-start)

```
pip install open-webui
open-webui serve
```

Then open [http://localhost:8080](http://localhost:8080/).

```
curl -LsSf https://astral.sh/uv/install.sh | sh
DATA_DIR=~/.open-webui uvx --python 3.11 open-webui@latest serve
```

Then open [http://localhost:8080](http://localhost:8080/).
Download the desktop app from [github.com/open-webui/desktop](https://github.com/open-webui/desktop). It runs Open WebUI natively on your system without Docker or manual setup.
Experimental
The desktop app is a **work in progress** and is not yet stable. For production use, install via **Docker** or **Python** .

#### Getting Started

```
*  [Quick Start](https://docs.openwebui.com/getting-started/quick-start) — Docker, Python, Kubernetes install options
*  [Connect a Provider](https://docs.openwebui.com/getting-started/quick-start/connect-a-provider) — Ollama, OpenAI, Anthropic, vLLM, and more
*  [Connect an Agent](https://docs.openwebui.com/getting-started/quick-start/connect-an-agent) — Hermes Agent, OpenClaw, and other autonomous AI agents
*  [Updating](https://docs.openwebui.com/getting-started/updating) — Keep your instance current
*  [Development Branch](https://docs.openwebui.com/getting-started/quick-start) — Help test the latest changes before stable release
*  [Advanced Topics](https://docs.openwebui.com/getting-started/advanced-topics) — Scaling, logging, and advanced configuration
```

#### Explore

```
*  [Features](https://docs.openwebui.com/features) — Discover what Open WebUI can do
*  [Tutorials](https://docs.openwebui.com/tutorials) — Step-by-step guides
*  [FAQ](https://docs.openwebui.com/faq) — Common questions answered
*  [Troubleshooting](https://docs.openwebui.com/troubleshooting) — Fix common issues
*  [Reference](https://docs.openwebui.com/reference) — Environment variables and API details
```

#### Enterprise

Need **custom branding** , **SLA support** , or **Long-Term Support (LTS)** versions? → [Learn about Enterprise plans](https://docs.openwebui.com/enterprise)

#### Get Involved

```
*  [Contributing](https://docs.openwebui.com/contributing) — Help build Open WebUI
*  [Development Setup](https://docs.openwebui.com/getting-started/advanced-topics/development) — Run the project locally from source
*  [Discord](https://discord.gg/5rJgQTnV4s) — Join the community
*  [GitHub](https://github.com/open-webui/open-webui) — Report issues, submit PRs
*  [Careers](https://careers.openwebui.com/) — Join our team
```

#### Sponsors

Emerald
Jade
[Open WebUI](https://openwebui.com/)
 [On a mission to build the best AI user interface.](https://openwebui.com/)

#### Acknowledgements

[A16z Open Source AI Grant 2025](https://a16z.com/advancing-open-source-ai-through-benchmarks-and-bold-experimentation/)
 [Mozilla Builders 2024](https://builders.mozilla.org/)
 [GitHub Accelerator 2024](https://github.com/accelerator)
[Edit this page](https://github.com/open-webui/docs/blob/main/docs/intro.mdx)
[Next 🚀 Getting Started](https://docs.openwebui.com/getting-started/)
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