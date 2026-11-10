---
tags:
  - notebooklm-import
notebook: "OpenWebUI"
category: "research"
---

Sharing Open WebUI / Open WebUI
[Skip to main content](https://docs.openwebui.com/getting-started/sharing#__docusaurus_skipToContent_fallback)
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
\* Sharing Open WebUI
On this page

### Sharing Open WebUI

**Deploy once, give your entire team access.**
Open WebUI is built to be shared. A single instance can serve your whole organization. Users just open a browser and start chatting. No per-seat installs, no client-side dependencies, no fragmented data across machines.

#### Built for Teams

##### Frictionless Onboarding

End users don't need to install anything, manage Docker, or touch a terminal. They open a browser, navigate to your instance URL, and log in.

##### Collaborative Intelligence

A shared instance means shared knowledge.

|  |  |
| --- | --- |
| **Channels** | Persistent spaces where your team and AI models work together in real time |
| **Shared Chats** | Send an exact conversation snapshot to a colleague |
| **Global Prompts & Knowledge** | Build specialized agents and make them instantly available to everyone |

##### Shared Compute

When running local models, a single powerful server (or cluster) serves your entire team instead of requiring capable hardware on every desk.

##### Centralized Administration

Manage everything from one place: control which models users can access, configure [Role-Based Access Control (RBAC)](https://docs.openwebui.com/features/authentication-access/rbac), review audit logs, and restrict features as needed.

#### Opening Your Instance to the Team

To share your instance, you need to make it accessible over a network. There are three common approaches, from simple local access to production-grade public domains.

##### 1. Zero-Config LAN (Local Network)

If your team is on the same local network or VPN, they can reach Open WebUI using your machine's local IP address and port. http://192.168.1.100:3000

##### 2. Secure Private Networks (Recommended)

For remote teams that don't need public internet exposure. Overlay networks and secure tunnels provide encrypted access without opening firewall ports.

|  |  |
| --- | --- |
| **Tailscale** | Private mesh network with MagicDNS ( https://open-webui.tailnet-name.ts.net ) |
| **Cloudflare Tunnels** | Expose via Cloudflare's edge, protected by Cloudflare Access (Zero Trust) |
| **ngrok** | Quick temporary sharing for development or testing |

##### 3. Public HTTPS (Reverse Proxy)

For production deployments, place Open WebUI behind a reverse proxy for SSL/TLS termination on your own domain (e.g., ai.yourcompany.com ).

|  |  |
| --- | --- |
| **Nginx** | Industry standard web server and reverse proxy |
| **Caddy** | Automatic HTTPS with minimal configuration |
| **HAProxy** | High-performance load balancing and proxying |

#### Onboarding Your Team

Once your instance is network-accessible, you need to manage how users create accounts and log in.

##### The Pending Queue

The first user to register becomes the **Administrator** . All subsequent sign-ups are placed in a **Pending** state and cannot access models or use the platform until an admin approves their account from the Admin Panel.

##### Enterprise Single Sign-On (SSO)

For organizations where manual approval doesn't scale, Open WebUI integrates with your existing identity provider.

|  |  |
| --- | --- |
| **OAuth / OIDC** | Authenticate via **Google** , **Microsoft** , **Okta** , or **Keycloak** |
| **Group mapping** | Map IdP groups directly to Open WebUI groups |
| **SCIM 2.0** | Automated user and group provisioning and deprovisioning |

[Learn how to set up SSO →](https://docs.openwebui.com/features/authentication-access/auth/sso)
[Edit this page](https://github.com/open-webui/docs/blob/main/docs/getting-started/sharing.md)
[Previous Understanding Settings](https://docs.openwebui.com/getting-started/quick-start/settings)
[Next Updating Open WebUI](https://docs.openwebui.com/getting-started/updating)
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