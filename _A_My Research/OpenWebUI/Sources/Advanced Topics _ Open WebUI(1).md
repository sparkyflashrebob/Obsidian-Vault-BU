---
tags:
  - notebooklm-import
notebook: "OpenWebUI"
category: "research"
---

Advanced Topics / Open WebUI
[Skip to main content](https://docs.openwebui.com/getting-started/advanced-topics#__docusaurus_skipToContent_fallback)
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
\* [Sharing Open WebUI](https://docs.openwebui.com/getting-started/sharing)
\* [Updating Open WebUI](https://docs.openwebui.com/getting-started/updating)
\* [Advanced Topics](https://docs.openwebui.com/getting-started/advanced-topics/)
\* [Scaling Open WebUI](https://docs.openwebui.com/getting-started/advanced-topics/scaling)
\* [Hardening Open WebUI](https://docs.openwebui.com/getting-started/advanced-topics/hardening)
\* [Logging Open WebUI](https://docs.openwebui.com/getting-started/advanced-topics/logging)
\* [Developing Open WebUI](https://docs.openwebui.com/getting-started/advanced-topics/development)
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
\* Advanced Topics
On this page

### Advanced Topics

**Go beyond the defaults: scale, debug, and develop Open WebUI for production and contribution.**
Open WebUI works out of the box for personal use, but real-world deployments need more: production databases, horizontal scaling, structured logging, observability. This section covers everything between "it runs on my laptop" and "it serves my entire organization."

#### Why Advanced Topics?

##### Scale beyond a single container

The default SQLite database and single-worker setup top out at small-team usage. Learn how to swap in PostgreSQL, add Redis for shared state, run multiple replicas behind a load balancer, and choose an external vector database, all without re-architecting your deployment.

##### Debug with confidence

When something goes wrong at scale, the first question is always "what do the logs say?" Configure log levels, enable structured JSON output for log aggregators, and connect OpenTelemetry for end-to-end traces across your entire stack.

##### Contribute to the project

Set up a local development environment with hot-reloading frontend and backend, understand the contribution workflow, and start shipping pull requests.

#### What's Covered

|  |  |
| --- | --- |
| 🚀 **Scaling Open WebUI** | Move from SQLite to PostgreSQL, add Redis, run multiple replicas, configure external vector databases, and set up shared storage and observability |
| 🪵 **Logging Open WebUI** | Configure log levels, enable debug output, and switch to structured JSON logging for production log aggregators |
| 🛠 **Developing Open WebUI** | Clone the repo, run the frontend and backend side by side, test on other devices, and submit pull requests |
| 🔒 **Hardening Open WebUI** | Lock down authentication, secrets, CORS, security headers, audit logging, and network access for production deployments |

[Edit this page](https://github.com/open-webui/docs/blob/main/docs/getting-started/advanced-topics/index.md)
[Previous Updating Open WebUI](https://docs.openwebui.com/getting-started/updating)
[Next Scaling Open WebUI](https://docs.openwebui.com/getting-started/advanced-topics/scaling)
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