---
tags:
  - notebooklm-import
notebook: "OpenWebUI"
category: "research"
---

LibreTranslate / Open WebUI
[Skip to main content](https://docs.openwebui.com/tutorials/integrations/libre-translate#__docusaurus_skipToContent_fallback)
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
\* [LLM Providers](https://docs.openwebui.com/tutorials/integrations/libre-translate)
\* [Monitoring](https://docs.openwebui.com/tutorials/integrations/libre-translate)
\* [Dev Tools](https://docs.openwebui.com/tutorials/integrations/libre-translate)
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
\* LibreTranslate
On this page

### LibreTranslate

warning
This tutorial is a community contribution and is not supported by the Open WebUI team. It serves only as a demonstration on how to customize Open WebUI for your specific use case. Want to contribute? Check out the contributing tutorial.

#### Overview

LibreTranslate is a free and open-source machine translation API that supports a wide range of languages. LibreTranslate is a self hosted, offline capable, and easy to setup, and unlike other APIs, it doesn't rely on proprietary providers such as Google or Azure to perform translations. Instead, its translation engine is powered by the open source [Argos Translate](https://github.com/argosopentech/argos-translate) library. You can integrate LibreTranslate with Open WebUI to leverage its machine translation capabilities. This documentation provides a step-by-step guide to setting up LibreTranslate in Docker and configuring the integration within Open WebUI.

#### Setting up LibreTranslate in Docker

To set up LibreTranslate in Docker, follow these steps:

##### Step 1: Create a Docker Compose File

Create a new file named docker-compose.yml in a directory of your choice. Add the following configuration to the file:

```
services:
  libretranslate:
    container_name: libretranslate
    image: libretranslate/libretranslate:v1.6.0
    restart: unless-stopped
    ports:
      - "5000:5000"
    env_file:
      - stack.env
    volumes:
      - libretranslate_api_keys:/app/db
      - libretranslate_models:/home/libretranslate/.local:rw
    tty: true
    stdin_open: true
    healthcheck:
      test: ['CMD-SHELL', './venv/bin/python scripts/healthcheck.py']

volumes:
  libretranslate_models:
  libretranslate_api_keys:
```

##### Step 2: Create a stack.env File

Create a new file named stack.env in the same directory as your docker-compose.yml file. Add the following configuration to the file:

```
# LibreTranslate
LT_DEBUG="false"
LT_UPDATE_MODELS="true"
LT_SSL="false"
LT_SUGGESTIONS="false"
LT_METRICS="false"
LT_HOST="0.0.0.0"

LT_API_KEYS="false"

LT_THREADS="12"
LT_FRONTEND_TIMEOUT="2000"
```

##### Step 3: Run the Docker Compose File

Run the following command to start the LibreTranslate service:

```
docker-compose up -d
```

This will start the LibreTranslate service in detached mode.

#### Configuring the Integration in Open WebUI

Once you have LibreTranslate up and running in Docker, you can configure the integration within Open WebUI. There are several community integrations available, including:
\* [LibreTranslate Filter Function](https://openwebui.com/f/iamg30/libretranslate_filter)
\* [LibreTranslate Action Function](https://openwebui.com/f/jthesse/libretranslate_action)
\* [MultiLanguage LibreTranslate Action Function](https://openwebui.com/f/iamg30/multilanguage_libretranslate_action)
\* [LibreTranslate Filter Pipeline](https://github.com/open-webui/pipelines/blob/main/examples/filters/libretranslate_filter_pipeline.py)
Choose the integration that best suits your needs and follow the instructions to configure it within Open WebUI.
Supported languages for the LibreTranslate pipeline & function: Really just all the languages that can be found within LibreTranslate, but here is the list:

```
Albanian, Arabic, Azerbaijani, Bengali, Bulgarian, Catalan, Valencian, Chinese, Czech, Danish, Dutch, English, Flemish, Esperanto, Estonian, Finnish, French, German, Greek, Hebrew, Hindi, Hungarian, Indonesian, Irish, Italian, Japanese, Korean, Latvian, Lithuanian, Malay, Persian, Polish, Portuguese, Romanian, Moldavian, Moldovan, Russian, Slovak, Slovenian, Spanish, Castilian, Swedish, Tagalog, Thai, Turkish, Ukrainian, Urdu
```

#### Troubleshooting

```
*  Make sure the LibreTranslate service is running and accessible.
*  Verify that the Docker configuration is correct.
*  Check the LibreTranslate logs for any errors.
```

#### Benefits of Integration

Integrating LibreTranslate with Open WebUI provides several benefits, including:
\* Machine translation capabilities for a wide range of languages.
\* Improved text analysis and processing.
\* Enhanced functionality for language-related tasks.

#### Conclusion

Integrating LibreTranslate with Open WebUI is a straightforward process that can enhance the functionality of your Open WebUI instance. By following the steps outlined in this documentation, you can set up LibreTranslate in Docker and configure the integration within Open WebUI.
[Edit this page](https://github.com/open-webui/docs/blob/main/docs/tutorials/integrations/libre-translate.md)
[Previous iTerm2](https://docs.openwebui.com/tutorials/integrations/dev-tools/iterm2)
[Next OneDrive & SharePoint](https://docs.openwebui.com/tutorials/integrations/onedrive-sharepoint)
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