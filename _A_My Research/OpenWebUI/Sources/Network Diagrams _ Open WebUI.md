---
tags:
  - notebooklm-import
notebook: "OpenWebUI"
category: "research"
---

Network Diagrams / Open WebUI
[Skip to main content](https://docs.openwebui.com/reference/network-diagrams#__docusaurus_skipToContent_fallback)
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
\* [Environment Variable Configuration](https://docs.openwebui.com/reference/env-configuration)
\* [HTTPS & Reverse Proxies](https://docs.openwebui.com/reference/https/)
\* [Monitoring](https://docs.openwebui.com/reference/monitoring/)
\* [Backend-Controlled API Flow](https://docs.openwebui.com/reference/api-flow)
\* [Database Schema](https://docs.openwebui.com/reference/database-schema)
\* [Network Diagrams](https://docs.openwebui.com/reference/network-diagrams)
\* [API Endpoints](https://docs.openwebui.com/reference/api-endpoints)
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
\* [📖 Reference](https://docs.openwebui.com/reference/)
\* Network Diagrams
On this page

### Network Diagrams

Visual C4 diagrams for common deployment topologies showing how Open WebUI, Ollama, and Docker communicate. Use these to debug connectivity issues or plan your architecture.
\* macOS / Windows
\* Linux
\* Host Ollama
\* Compose Stack
\* Separate Networks
\* Host Network

###### Ollama on Host, Open WebUI in Container

Ollama runs directly on the host machine while Open WebUI operates within a Docker container.
<> User <> Ollama [Listening on port 11434] <> Open WebUI [Listening on port 8080] Docker Desktop's Linux VM [system] Hosting Machine - Mac OS/Windows [system] Makes API calls via Docker proxy [http://host.docker.internal:11434] Makes requests via exposed port -p 3000:8080 [http://localhost:3000]

###### Ollama and Open WebUI in Compose Stack

Both Ollama and Open WebUI are configured within the same Docker Compose stack, simplifying network communications.
<> User <> Open WebUI [Listening on port 8080] <> Ollama [Listening on port 11434] Compose Stack [system] Docker Desktop's Linux VM [system] Hosting Machine - Mac OS/Windows [system] Makes API calls via inter-container networking [http://ollama:11434] Makes requests via exposed port -p 3000:8080 [http://localhost:3000]

###### Ollama and Open WebUI, Separate Networks

Ollama and Open WebUI are deployed in separate Docker networks. This leads to connectivity issues.
<> User <> Open WebUI [Listening on port 8080] Network A [system] <> Ollama [Listening on port 11434] Network B [system] Docker Desktop's Linux VM [system] Hosting Machine - Mac OS/Windows [system] Unable to connect Makes requests via exposed port -p 3000:8080 [http://localhost:3000]

###### Open WebUI in Host Network

Open WebUI utilizes the host network, which impacts its ability to connect in certain environments.
<> User <> Open WebUI [Listening on port 8080] Docker Desktop's Linux VM [system] Hosting Machine - Mac OS/Windows [system] Unable to connect, host network is the VM's network
\* Host Ollama
\* Compose Stack
\* Separate Networks
\* Host Network

###### Ollama on Host, Open WebUI in Container

Ollama runs on the host and Open WebUI is deployed inside a Docker container.
<> User <> Ollama [Listening on port 11434] <> Open WebUI [Listening on port 8080] Container Network [system] Hosting Machine - Linux [system] Makes API calls via Docker proxy [http://host.docker.internal:11434] Makes requests via exposed port -p 3000:8080 [http://localhost:3000]

###### Ollama and Open WebUI in Compose Stack

Both Ollama and Open WebUI reside within the same Docker Compose stack, allowing for straightforward networking.
<> User <> Open WebUI [Listening on port 8080] <> Ollama [Listening on port 11434] Compose Stack [system] Container Network [system] Hosting Machine - Linux [system] Makes API calls via inter-container networking [http://ollama:11434] Makes requests via exposed port -p 3000:8080 [http://localhost:3000]

###### Ollama and Open WebUI, Separate Networks

Ollama and Open WebUI are in different Docker networks, which can hinder connectivity.
<> User <> Open WebUI [Listening on port 8080] Container Network A [system] <> Ollama [Listening on port 11434] Container Network B [system] Hosting Machine - Linux [system] Unable to connect Makes requests via exposed port -p 3000:8080 [http://localhost:3000]

###### Open WebUI in Host Network, Ollama on Host

Both Open WebUI and Ollama use the host's network, enabling seamless interaction.
<> User <> Open WebUI [Listening on port 8080] <> Ollama [Listening on port 11434] Hosting Machine - Linux [system] Makes API calls via localhost [http://localhost:11434] Makes requests via listening port [http://localhost:8080]
[Edit this page](https://github.com/open-webui/docs/blob/main/docs/reference/network-diagrams.mdx)
[Previous Database Schema](https://docs.openwebui.com/reference/database-schema)
[Next API Endpoints](https://docs.openwebui.com/reference/api-endpoints)
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