---
tags:
  - notebooklm-import
notebook: "OpenWebUI"
category: "research"
---

Langfuse ⚠ / Open WebUI
[Skip to main content](https://docs.openwebui.com/tutorials/integrations/monitoring/langfuse#__docusaurus_skipToContent_fallback)
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
\* [LLM Providers](https://docs.openwebui.com/tutorials/integrations/monitoring/langfuse)
\* [Monitoring](https://docs.openwebui.com/tutorials/integrations/monitoring/langfuse)
\* [Helicone](https://docs.openwebui.com/tutorials/integrations/monitoring/helicone)
\* [Langfuse ⚠](https://docs.openwebui.com/tutorials/integrations/monitoring/langfuse)
\* [Dev Tools](https://docs.openwebui.com/tutorials/integrations/monitoring/langfuse)
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
\* Monitoring
\* Langfuse ⚠
On this page

### Langfuse ⚠

warning
This tutorial is a community contribution and is not supported by the Open WebUI team. It serves only as a demonstration on how to customize Open WebUI for your specific use case. Want to contribute? Check out the contributing tutorial.
danger
This tutorial was reported as **OUTDATED** / stale. It might not work anymore with newer versions of Open WebUI or Langfuse.
Feel free to contribute to make it up to date again, by submitting a PR: <https://github.com/open-webui/docs>

#### Langfuse Integration with Open WebUI

[Langfuse](https://langfuse.com/) ( [GitHub](https://github.com/langfuse/langfuse)) offers open source observability and evaluations for Open WebUI. By enabling the Langfuse integration, you can trace your application data with Langfuse to develop, monitor, and improve the use of Open WebUI, including:
\* Application [traces](https://langfuse.com/docs/tracing)
\* Usage patterns
\* Cost data by user and model
\* Replay sessions to debug issues
\* [Evaluations](https://langfuse.com/docs/scores/overview)

#### How to integrate Langfuse with Open WebUI

*Langfuse integration steps*
[Pipelines](https://github.com/open-webui/pipelines/) in Open WebUI is an UI-agnostic framework for OpenAI API plugins. It enables the injection of plugins that intercept, process, and forward user prompts to the final LLM, allowing for enhanced control and customization of prompt handling.
To trace your application data with Langfuse, you can use the [Langfuse pipeline](https://github.com/open-webui/pipelines/blob/039f9c54f8e9f9bcbabde02c2c853e80d25c79e4/examples/filters/langfuse_v3_filter_pipeline.py), which enables real-time monitoring and analysis of message interactions.

#### Quick Start Guide

##### Step 1: Setup Open WebUI

Make sure to have Open WebUI running. To do so, have a look at the [Open WebUI documentation](https://docs.openwebui.com/).

##### Step 2: Set Up Pipelines

Launch [Pipelines](https://github.com/open-webui/pipelines/) by using Docker. Use the following command to start Pipelines:

```
docker run -p 9099:9099 --add-host=host.docker.internal:host-gateway -v pipelines:/app/pipelines --name pipelines --restart always ghcr.io/open-webui/pipelines:main
```

##### Step 3: Connecting Open WebUI with Pipelines

In the *Admin Settings* , create and save a new connection of type OpenAI API with the following details:
\* **URL:** [http://host.docker.internal:9099](http://host.docker.internal:9099/) (this is where the previously launched Docker container is running).
\* **Password:** 0p3n-w3bu! (standard password)

##### Step 4: Adding the Langfuse Filter Pipeline

Next, navigate to *Admin Settings* -> *Pipelines* and add the Langfuse Filter Pipeline. Specify that Pipelines is listening on [http://host.docker.internal:9099](http://host.docker.internal:9099/) (as configured earlier) and install the [Langfuse Filter Pipeline](https://github.com/open-webui/pipelines/blob/039f9c54f8e9f9bcbabde02c2c853e80d25c79e4/examples/filters/langfuse_v3_filter_pipeline.py) by using the *Install from Github URL* option with the following URL:

```
https://github.com/open-webui/pipelines/blob/main/examples/filters/langfuse_v3_filter_pipeline.py
```

Now, add your Langfuse API keys below. If you haven't signed up to Langfuse yet, you can get your API keys by creating an account [here](https://cloud.langfuse.com/).
note
*Note: Capture usage (token counts) for OpenAi models while streaming is enabled, you have to navigate to the model settings in Open WebUI and check the "Usage" box below Capabilities.*

##### Step 5: See your traces in Langfuse

You can now interact with your Open WebUI application and see the traces in Langfuse.
[Example trace](https://cloud.langfuse.com/project/cloramnkj0002jz088vzn1ja4/traces/904a8c1f-4974-4f8f-8a2f-129ae78d99c5?observation=fe5b127b-e71c-45ab-8ee5-439d4c0edc28) in the Langfuse UI:

#### Learn more

For a comprehensive guide on Open WebUI Pipelines, visit [this post](https://ikasten.io/2024/06/03/getting-started-with-openwebui-pipelines/).
[Edit this page](https://github.com/open-webui/docs/blob/main/docs/tutorials/integrations/monitoring/langfuse.md)
[Previous Helicone](https://docs.openwebui.com/tutorials/integrations/monitoring/helicone)
[Next Continue.dev](https://docs.openwebui.com/tutorials/integrations/dev-tools/continue-dev)
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