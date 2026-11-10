---
tags:
  - notebooklm-import
notebook: "OpenWebUI"
category: "research"
---

Browser Search Engine / Open WebUI
[Skip to main content](https://docs.openwebui.com/tutorials/integrations/dev-tools/browser-search-engine#__docusaurus_skipToContent_fallback)
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
\* [LLM Providers](https://docs.openwebui.com/tutorials/integrations/dev-tools/browser-search-engine)
\* [Monitoring](https://docs.openwebui.com/tutorials/integrations/dev-tools/browser-search-engine)
\* [Dev Tools](https://docs.openwebui.com/tutorials/integrations/dev-tools/browser-search-engine)
\* [Continue.dev](https://docs.openwebui.com/tutorials/integrations/dev-tools/continue-dev)
\* [Jupyter Notebooks](https://docs.openwebui.com/tutorials/integrations/dev-tools/jupyter)
\* [Firefox Sidebar](https://docs.openwebui.com/tutorials/integrations/dev-tools/firefox-sidebar)
\* [Browser Search Engine](https://docs.openwebui.com/tutorials/integrations/dev-tools/browser-search-engine)
\* [iTerm2](https://docs.openwebui.com/tutorials/integrations/dev-tools/iterm2)
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
\* Dev Tools
\* Browser Search Engine
On this page

### Browser Search Engine Integration

warning
This tutorial is a community contribution and is not supported by the Open WebUI team. It serves only as a demonstration on how to customize Open WebUI for your specific use case. Want to contribute? Check out the contributing tutorial.
Open WebUI allows you to integrate directly into your web browser. This tutorial will guide you through the process of setting up Open WebUI as a custom search engine, enabling you to execute queries easily from your browser's address bar.

#### Setting Up Open WebUI as a Search Engine

##### Prerequisites

Before you begin, ensure that:
\* You have Chrome or another supported browser installed.
\* The WEBUI\_URL environment variable is set correctly, either using Docker environment variables or in the .env file as specified in the [Getting Started](https://docs.openwebui.com/reference/env-configuration) guide.

##### Step 1: Set the WEBUI\_URL Environment Variable

Setting the WEBUI\_URL environment variable ensures your browser knows where to direct queries.

###### Using Docker Environment Variables

If you are running Open WebUI using Docker, you can set the environment variable in your docker run command:

```
docker run -d \
  -p 3000:8080 \
  --add-host=host.docker.internal:host-gateway \
  -v open-webui:/app/backend/data \
  --name open-webui \
  --restart always \
  -e WEBUI_URL="https://" \
  ghcr.io/open-webui/open-webui:main
```

Alternatively, you can add the variable to your .env file:

```
WEBUI_URL=https://
```

##### Step 2: Add Open WebUI as a Custom Search Engine

##### For Chrome

```
1. Open Chrome and navigate to  **Settings** .
1. Select  **Search engine**  from the sidebar, then click on  **Manage search engines** .
1. Click  **Add**  to create a new search engine.
1. Fill in the details as follows:
*   **Search engine** : Open WebUI Search
    *   **Keyword** : webui (or any keyword you prefer)
    *   **URL with %s in place of query** :
```

```
https:///?q=%s
```

```
1. Click  **Add**  to save the configuration.
```

##### For Firefox

```
1. Go to Open WebUI in Firefox.
1. Expand the address bar by clicking on it.
1. Click the plus icon that is enclosed in a green circle at the bottom of the expanded address bar. This adds Open WebUI's search to the search engines in your preferences.
```

Alternatively:
1. Go to Open WebUI in Firefox.
1. Right-click on the address bar.
1. Select "Add Open WebUI" (or similar) from the context menu.

##### Optional: Using Specific Models

If you wish to utilize a specific model for your search, modify the URL format to include the model ID:

```
https:///?models=&q=%s
```

note
**Note:** The model ID will need to be URL-encoded. Special characters like spaces or slashes need to be encoded (e.g., my model becomes my%20model ).

#### Example Usage

Once the search engine is set up, you can perform searches directly from the address bar. Simply type your chosen keyword followed by your query:

```
webui your search query
```

This command will redirect you to the Open WebUI interface with your search results.

#### Troubleshooting

If you encounter any issues, check the following:
\* Ensure the WEBUI\_URL is correctly configured and points to a valid Open WebUI instance.
\* Double-check that the search engine URL format is correctly entered in your browser settings.
\* Confirm your internet connection is active and that the Open WebUI service is running smoothly.
[Edit this page](https://github.com/open-webui/docs/blob/main/docs/tutorials/integrations/dev-tools/browser-search-engine.md)
[Previous Firefox Sidebar](https://docs.openwebui.com/tutorials/integrations/dev-tools/firefox-sidebar)
[Next iTerm2](https://docs.openwebui.com/tutorials/integrations/dev-tools/iterm2)
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