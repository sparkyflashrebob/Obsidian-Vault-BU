---
tags:
  - notebooklm-import
notebook: "OpenWebUI"
category: "research"
---

Administration / Open WebUI
[Skip to main content](https://docs.openwebui.com/features/administration/#__docusaurus_skipToContent_fallback)
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
\* [Customizable Banners](https://docs.openwebui.com/features/administration/banners)
\* [Webhook Integrations](https://docs.openwebui.com/features/administration/webhooks)
\* [Analytics](https://docs.openwebui.com/features/administration/analytics/)
\* [Evaluation](https://docs.openwebui.com/features/administration/evaluation/)
\* [💬 Chat & Conversations](https://docs.openwebui.com/features/administration/)
\* [🧠 Workspace](https://docs.openwebui.com/features/administration/)
\* [📝 Notes](https://docs.openwebui.com/features/notes/)
\* [📢 Channels](https://docs.openwebui.com/features/channels/)
\* [💻 Open Terminal](https://docs.openwebui.com/features/open-terminal/)
\* [🔌 Plugins & Extensibility](https://docs.openwebui.com/features/extensibility/)
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
\* 🔧 Administration
On this page

### 🔧 Administration

**Monitor usage, evaluate model quality, and communicate with your users, all from the Admin Panel.**
Open WebUI gives administrators a full operational toolkit. Track which models your team uses and how much they cost. Run blind evaluations to find the best model for your workload. Push announcements to every user with customizable banners. Wire up webhooks to get notified when users sign up or when long-running tasks finish.

#### What's In This Section

|  |  |
| --- | --- |
| 📊 **Analytics** | Usage dashboards with message volume, token consumption, model breakdowns, and per-user activity |
| 🏆 **Evaluation** | Model arena, blind A/B testing, ELO-based leaderboards, and chat snapshots for fine-tuning |
| 📢 **Banners** | Customizable system-wide announcements with dismissible notifications |
| 🔔 **Webhooks** | Automated notifications for user sign-ups, chat completions, and external service integration |

#### Analytics

Get a bird's-eye view of how your instance is being used. The analytics dashboard shows message volume, token consumption, model popularity, and user activity, filterable by time period and user group.
**Use it for:** capacity planning, cost estimation, identifying popular models, tracking adoption trends, and per-department usage reporting.
[Learn about Analytics →](https://docs.openwebui.com/features/administration/analytics)

#### Evaluation

Not sure which model fits your team best? The evaluation system lets users rate model responses with thumbs up/down during normal conversations. Ratings feed into an ELO-based leaderboard, and rated chats are snapshotted for future model fine-tuning.
**Two evaluation modes:**
\* **Arena Mode** : Randomly selects models for blind comparison, removing bias
\* **Normal interaction** : Rate responses during regular use, then compare models by swapping them out
[Learn about Evaluation →](https://docs.openwebui.com/features/administration/evaluation)

#### Banners

Push high-visibility messages to every logged-in user. Use banners for maintenance windows, incident alerts, policy reminders, and feature announcements. Configure via the Admin Panel or the WEBUI\_BANNERS environment variable for GitOps workflows.

| Type | Color | Best for |
| --- | --- | --- |
| info | Blue | General announcements |
| success | Green | Resolved incidents, completed changes |
| warning | Yellow | Planned maintenance, partial degradation |
| error | Red | Active incidents, outages |

[Learn about Banners →](https://docs.openwebui.com/features/administration/banners)

#### Webhooks

Three types of webhook integrations keep your external services in sync:

| Webhook | Purpose |
| --- | --- |
| **Admin Webhook** | Notifies a Slack/Discord channel when a new user signs up |
| **User Webhook** | Notifies individual users when a long-running chat response is ready |
| **Channel Webhooks** | Let external services (CI/CD, monitoring, scripts) post messages into Open WebUI channels |

[Learn about Webhooks →](https://docs.openwebui.com/features/administration/webhooks)
[Edit this page](https://github.com/open-webui/docs/blob/main/docs/features/administration/index.mdx)
[Previous API Keys](https://docs.openwebui.com/features/authentication-access/api-keys)
[Next Customizable Banners](https://docs.openwebui.com/features/administration/banners)
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