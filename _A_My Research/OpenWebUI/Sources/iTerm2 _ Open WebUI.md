---
tags:
  - notebooklm-import
notebook: "OpenWebUI"
category: "research"
---

iTerm2 / Open WebUI
[Skip to main content](https://docs.openwebui.com/tutorials/integrations/dev-tools/iterm2#__docusaurus_skipToContent_fallback)
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
\* [LLM Providers](https://docs.openwebui.com/tutorials/integrations/dev-tools/iterm2)
\* [Monitoring](https://docs.openwebui.com/tutorials/integrations/dev-tools/iterm2)
\* [Dev Tools](https://docs.openwebui.com/tutorials/integrations/dev-tools/iterm2)
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
\* iTerm2
On this page

### Use your Open WebUI models with Iterm2

warning
This tutorial is a community contribution and is not supported by the Open WebUI team. It serves only as a demonstration on how to customize Open WebUI for your specific use case. Want to contribute? Check out the [contributing tutorial](https://docs.openwebui.com/contributing).
You can use your Open WebUI models within the Iterm2 AI plugin. This guide shows you how to set up the necessary configuration.

#### Why use the Iterm2 AI plugin?

Whenever you forget a command or need a quick bash script for a repetitive task, you likely already use AI responses. To streamline this workflow, the Iterm2 AI plugin allows you to send requests to your specified AI provider or your Open WebUI.

#### Why connect to your Open WebUI instance?

Open WebUI provides a simple and straightforward way to interact with your LLMs via its [API Endpoints](https://docs.openwebui.com/reference/api-endpoints). This is particularly beneficial if you are running your own LLMs locally. Furthermore, you can leverage all your implemented features, monitoring, and other capabilities.

#### Prerequisites

##### 1. Download the iTerm2 AI plugin

If you haven't already installed the iTerm2 AI plugin, you'll need to download it first from [their page](https://iterm2.com/ai-plugin.html). Unzip the file and move the application into your **Applications** folder.

##### 2. Generate your Open WebUI API key

To authenticate with your Open WebUI instance, you'll need to generate an API key. Follow the instructions in the [API Endpoints guide](https://docs.openwebui.com/reference/api-endpoints) to create it.

#### Configuration

Open your iTerm2 terminal and navigate to **Settings** (⌘,) from the **iTerm2** menu, then select the **AI** tab.

##### Verify the installed plugin

Once the iTerm2 AI plugin is installed, verify that the **Plugin** section shows Plugin installed and working ✅ .

##### Give consent for generative AI features

Under the **Consent** section, check the box for Enable generative AI features to agree.

##### Set API key

Enter your previously created Open WebUI API token into the **API Key** field.

##### Optional: customize your prompt

If you want a specialized prompt sent to your LLM, feel free to edit the Prompt template .
**Original prompt example:**

```
Return commands suitable for copy/pasting into \(shell) on \(uname). Do
NOT include commentary NOR Markdown triple-backtick code blocks as your
whole response will be copied into my terminal automatically.

The script should do this: \(ai.prompt)
```

You can read more about the Iterm2 prompt in the [Iterm2 documentation](https://gitlab.com/gnachman/iterm2/-/wikis/AI-Prompt).

##### Select Your LLM

Since the iTerm2 AI plugin does not automatically list your custom models, you'll need to add your preferred one manually. In your Open WebUI instance, navigate to Admin Panel > Settings > Models , and then click on your preferred LLM. Below the user-given name, you'll find the actual model name that you need to enter into iTerm2 (e.g., name: Gemma3 - model name: /models/gemma3-27b-it-Q4\_K\_M.gguf ).

##### Adjust the Tokens

Set your preferred amount of tokens here. Typically, your inference tool will already have a limitation set.

##### Adjust the URL

This is a crucial step: you need to direct the iTerm2 AI plugin requests to your Open WebUI instance. Either use an actual domain name if the instance is hosted somewhere (e.g., https://example.com/api/chat/completions ) or your localhost setup (e.g., http://localhost:8080/api/chat/completions ). You can find more information about the URLs in the [API Endpoints guide](https://docs.openwebui.com/reference/api-endpoints).

##### Legacy Completions API

This setting is not needed for Open WebUI, though more information is available in the [original guide](https://platform.openai.com/docs/guides/completions/completions-api-legacy).
After setup, the **AI** section will look like this:

#### Usage

Within your terminal session, open the prompt input field by pressing **command + y** (⌘y). Write your prompt and send it by clicking the **OK** button or by using **shift + enter** (⇧⌤).
This will lead you back to the terminal with an additional window bound to the session frame. The result of your query will be displayed within this overlay. To send the command to your terminal, move your cursor to the target line and use **shift + enter** (⇧⌤).
info
There can be more than one line of response. If so, you can navigate with the arrow keys to edit the commands as needed.
[Edit this page](https://github.com/open-webui/docs/blob/main/docs/tutorials/integrations/dev-tools/iterm2.md)
[Previous Browser Search Engine](https://docs.openwebui.com/tutorials/integrations/dev-tools/browser-search-engine)
[Next LibreTranslate](https://docs.openwebui.com/tutorials/integrations/libre-translate)
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