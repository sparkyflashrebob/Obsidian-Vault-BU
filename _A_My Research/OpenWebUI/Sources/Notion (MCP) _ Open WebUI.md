---
tags:
  - notebooklm-import
notebook: "OpenWebUI"
category: "research"
---

Notion (MCP) / Open WebUI
[Skip to main content](https://docs.openwebui.com/tutorials/integrations/mcp-notion#__docusaurus_skipToContent_fallback)
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
\* [LLM Providers](https://docs.openwebui.com/tutorials/integrations/mcp-notion)
\* [Monitoring](https://docs.openwebui.com/tutorials/integrations/mcp-notion)
\* [Dev Tools](https://docs.openwebui.com/tutorials/integrations/mcp-notion)
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
\* Notion MCP Integration
On this page

### Notion (MCP)

Community Contribution
This tutorial is a community contribution and is not supported by the Open WebUI team. It serves as a demonstration on how to customize Open WebUI for your specific use case. Want to contribute? Check out the [contributing tutorial](https://docs.openwebui.com/tutorials/contributing-tutorial/).
Notion hosts a remote MCP server at https://mcp.notion.com/mcp that Open WebUI connects to natively via **Streamable HTTP** . Authentication is handled through Notion's OAuth flow — no API tokens, no proxies, no extra containers.

#### Setup

Prerequisite: WEBUI\_SECRET\_KEY
You **MUST** set the WEBUI\_SECRET\_KEY environment variable to a persistent value. Without it, your OAuth session breaks every time the container restarts, forcing re-authentication. See the [MCP feature docs](https://docs.openwebui.com/features/extensibility/mcp) for details.

##### 1. Add the tool

Go to **Admin Panel → Settings → External Tools** and click **+** to add a new connection. Fill in the following:

| Field | Value |
| --- | --- |
| **Type** | MCP Streamable HTTP |
| **URL** | https://mcp.notion.com/mcp |
| **Auth** | OAuth 2.1 |
| **ID** | ntn |
| **Name** | Notion |

Click **Register Client** , then **Save** . Use OAuth 2.1 (Static) if you have pre-created OAuth client credentials.
Alternative: Import JSON
You can also click **Import** in the modal and paste this configuration:

```
[
  {
    "type": "mcp",
    "url": "https://mcp.notion.com/mcp",
    "spec_type": "url",
    "spec": "",
    "path": "openapi.json",
    "auth_type": "oauth_2.1",
    "key": "",
    "info": {
      "id": "ntn",
      "name": "Notion",
      "description": "Search, read, create, and manage Notion pages and databases."
    }
  }
]
```

##### 2. Authorize

In any chat, open **+ → Integrations → Tools** and toggle **Notion** on. You'll be redirected to Notion's OAuth flow — select your workspace and grant access.
OAuth 2.1 tools cannot be pre-enabled
Do **not** set this as a default tool on a model. OAuth 2.1 requires an interactive browser redirect that cannot happen mid-request. Users must enable it manually per-chat via the **+** button. See [MCP docs](https://docs.openwebui.com/features/extensibility/mcp) for details.
Re-authentication
Notion's OAuth session may expire after inactivity or container restarts. If you see Failed to connect to MCP server 'ntn' , re-toggle the tool in any chat to trigger the authorization flow again.

#### Rate limits

Standard [Notion API limits](https://developers.notion.com/reference/request-limits) apply:
\* **General:** 180 requests per minute
\* **Search:** 30 requests per minute

#### Troubleshooting

##### Failed to connect to MCP server 'ntn'

Your OAuth session has expired. Re-toggle the Notion tool in any chat ( **+** → **Integrations → Tools** ) to re-authorize.

##### OAuth callback failed: mismatching\_state

You're accessing Open WebUI via localhost , but WEBUI\_URL is set to a public domain. Access your instance using the **exact URL** from WEBUI\_URL and authorize again.

##### Object not found

The page hasn't been shared with the integration. During the OAuth flow, Notion asks which pages to grant access to — make sure the relevant pages are selected. You can update access anytime from your [Notion integrations settings](https://www.notion.so/profile/integrations).

##### missing\_property when creating a page

Notion requires a parent page or database. Tell the model: *"Search for my 'Notes' page first, then create the new page inside it."*
[Edit this page](https://github.com/open-webui/docs/blob/main/docs/tutorials/integrations/mcp-notion.mdx)
[Previous OneDrive & SharePoint](https://docs.openwebui.com/tutorials/integrations/onedrive-sharepoint)
[Next Redis Websocket Support](https://docs.openwebui.com/tutorials/integrations/redis)
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