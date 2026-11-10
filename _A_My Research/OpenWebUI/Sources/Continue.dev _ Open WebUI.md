---
tags:
  - notebooklm-import
notebook: "OpenWebUI"
category: "research"
---

Continue.dev / Open WebUI
[Skip to main content](https://docs.openwebui.com/tutorials/integrations/dev-tools/continue-dev#__docusaurus_skipToContent_fallback)
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
\* [LLM Providers](https://docs.openwebui.com/tutorials/integrations/dev-tools/continue-dev)
\* [Monitoring](https://docs.openwebui.com/tutorials/integrations/dev-tools/continue-dev)
\* [Dev Tools](https://docs.openwebui.com/tutorials/integrations/dev-tools/continue-dev)
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
\* Continue.dev
On this page

### Integrating Continue.dev VS Code Extension with Open WebUI

warning
This tutorial is a community contribution and is not supported by the Open WebUI team. It serves only as a demonstration on how to customize Open WebUI for your specific use case. Want to contribute? Check out the [contributing tutorial](https://docs.openwebui.com/contributing).

#### Download Extension

You can download the VS Code extension on the [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=Continue.continue) or directly via the EXTENSION:MARKETPLACE within VS Code by searching for continue . Once installed, you can access the application via the continue tab in the side bar of VS Code.
**VS Code side bar icon:**

#### Setup

Click on the assistant selector to the right of the main chat input. Then hover over Local Assistant and click on the settings icon (⚙). This will open the config.yaml file in your editor. Here you can change the settings of your Local Assistant .
info
Currently the ollama provider does not support authentication so we cannot use this provider with Open WebUI. However Ollama and Open WebUI both have compatibility with OpenAI API spec. Read more about the specification in the [Ollama blog post on OpenAI compatibility](https://ollama.com/blog/openai-compatibility). We can still setup continue.dev to use the openai provider which will allow us to use Open WebUI's authentication token.

##### Example config

Below you find an example config for Llama3 as the model with a local Open WebUI setup.

```
name: Local Assistant
version: 1.0.0
schema: v1
models:
  - name: LLama3
    provider: openai
    model: Meta-Llama-3-8B-Instruct-Q4_K_M.gguf
    env:
      useLegacyCompletionsEndpoint: false
    apiBase: http://localhost:3000/api
    apiKey: YOUR_OPEN_WEBUI_API_KEY
    roles:
      - chat
      - edit
context:
  - provider: code
  - provider: docs
  - provider: diff
  - provider: terminal
  - provider: problems
  - provider: folder
  - provider: codebase
```

##### Miscellaneous Configuration Settings

These values are needed by the extension to work properly. Find more information in the [official config guide](https://docs.continue.dev/reference).

```
name: Local Assistant
version: 1.0.0
schema: v1
```

The context section provides additional information to the models. Find more information in the [official config guide](https://docs.continue.dev/reference#context) and in the [context provider guide](https://docs.continue.dev/customize/custom-providers).

```
context:
  - provider: code
  - provider: docs
  - provider: diff
  - provider: terminal
  - provider: problems
  - provider: folder
  - provider: codebase
```

##### Models

The models section is where you specify all models you want to add. Find more information in the [official models guide](https://docs.continue.dev/reference#models).

```
models:
  - ...
```

##### Name

Sets the name for the model you want to use. This will be displayed within the chat input of the extension.

```
name: LLama3
```

##### Provider

Specifies the method used to communicate with the API, which in our case is the OpenAI API endpoint provided by Open WebUI.

```
provider: openai
```

##### Model

This is the actual name of your model in Open WebUI. Navigate to Admin Panel > Settings > Models , and then click on your preferred LLM. Below the user-given name, you'll find the actual model name.

```
model: Meta-Llama-3-8B-Instruct-Q4_K_M.gguf
```

##### Legacy completions endpoint

This setting is not needed for Open WebUI, though more information is available in the [original guide](https://platform.openai.com/docs/guides/completions/completions-api-legacy).

```
env:
  useLegacyCompletionsEndpoint: false
```

##### APIBase

This is a crucial step: you need to direct the continue.dev extension requests to your Open WebUI instance. Either use an actual domain name if the instance is hosted somewhere (e.g., https://example.com/api ) or your localhost setup (e.g., http://localhost:3000/api ). You can find more information about the URLs in the [API Endpoints guide](https://docs.openwebui.com/reference/api-endpoints).

```
apiBase: http://localhost:3000/api
```

##### API Key

To authenticate with your Open WebUI instance, you'll need to generate an API key. Follow the instructions in the [API Endpoints guide](https://docs.openwebui.com/reference/api-endpoints) to create it.

```
apiKey: YOUR_OPEN_WEBUI_API_KEY
```

##### Roles

The roles will allow your model to be used by the extension for certain tasks. For the beginning you can choose chat and edit . You can find more information about roles in the [official roles guide](https://docs.continue.dev/customize/model-roles/intro).

```
roles:
  - chat
  - edit
```

The setup is now completed and you can interact with your model(s) via the chat input. Find more information about the features and usage of the continue.dev plugin in the [official documentation](https://docs.continue.dev/getting-started/overview).
[Edit this page](https://github.com/open-webui/docs/blob/main/docs/tutorials/integrations/dev-tools/continue-dev.md)
[Previous Langfuse ⚠](https://docs.openwebui.com/tutorials/integrations/monitoring/langfuse)
[Next Jupyter Notebooks](https://docs.openwebui.com/tutorials/integrations/dev-tools/jupyter)
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