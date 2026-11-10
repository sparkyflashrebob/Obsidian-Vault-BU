---
tags:
  - notebooklm-import
notebook: "OpenWebUI"
category: "research"
---

Pipelines / Open WebUI
[Skip to main content](https://docs.openwebui.com/features/extensibility/pipelines/#__docusaurus_skipToContent_fallback)
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
\* [💬 Chat & Conversations](https://docs.openwebui.com/features/extensibility/pipelines/)
\* [🧠 Workspace](https://docs.openwebui.com/features/extensibility/pipelines/)
\* [📝 Notes](https://docs.openwebui.com/features/notes/)
\* [📢 Channels](https://docs.openwebui.com/features/channels/)
\* [💻 Open Terminal](https://docs.openwebui.com/features/open-terminal/)
\* [🔌 Plugins & Extensibility](https://docs.openwebui.com/features/extensibility/)
\* [Tools & Functions (Plugins)](https://docs.openwebui.com/features/extensibility/plugin/)
\* [Model Context Protocol (MCP)](https://docs.openwebui.com/features/extensibility/mcp)
\* [Pipelines](https://docs.openwebui.com/features/extensibility/pipelines/)
\* [Filters](https://docs.openwebui.com/features/extensibility/pipelines/filters)
\* [Pipes](https://docs.openwebui.com/features/extensibility/pipelines/pipes)
\* [Valves](https://docs.openwebui.com/features/extensibility/pipelines/valves)
\* [Tutorials](https://docs.openwebui.com/features/extensibility/pipelines/tutorials)
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
\* [🔌 Plugins & Extensibility](https://docs.openwebui.com/features/extensibility/)
\* Pipelines
On this page

### Pipelines: UI-Agnostic OpenAI API Plugin Framework

warning
**DO NOT USE PIPELINES IF!**
If your goal is simply to add support for additional providers like Anthropic or basic filters, you likely don't need Pipelines . For those cases, Open WebUI Functions are a better fit—it's built-in, much more convenient, and easier to configure. Pipelines, however, comes into play when you're dealing with computationally heavy tasks (e.g., running large models or complex logic) that you want to offload from your main Open WebUI instance for better performance and scalability.
Welcome to **Pipelines** , an [Open WebUI](https://github.com/open-webui) initiative. Pipelines bring modular, customizable workflows to any UI client supporting OpenAI API specs – and much more! Easily extend functionalities, integrate unique logic, and create dynamic workflows with just a few lines of code.

#### 🚀 Why Choose Pipelines?

```
*   **Limitless Possibilities:**  Easily add custom logic and integrate Python libraries, from AI agents to home automation APIs.
*   **Seamless Integration:**  Compatible with any UI/client supporting OpenAI API specs. (Only pipe-type pipelines are supported; filter types require clients with Pipelines support.)
*   **Custom Hooks:**  Build and integrate custom pipelines.
```

##### Examples of What You Can Achieve:

```
*  [Function Calling Pipeline](https://github.com/open-webui/pipelines/blob/main/examples/filters/function_calling_filter_pipeline.py): Easily handle function calls and enhance your applications with custom logic.
*  [Custom RAG Pipeline](https://github.com/open-webui/pipelines/blob/main/examples/pipelines/rag/llamaindex_pipeline.py): Implement sophisticated Retrieval-Augmented Generation pipelines tailored to your needs.
*  [Message Monitoring Using Langfuse](https://github.com/open-webui/pipelines/blob/main/examples/filters/langfuse_filter_pipeline.py): Monitor and analyze message interactions in real-time using Langfuse.
*  [Rate Limit Filter](https://github.com/open-webui/pipelines/blob/main/examples/filters/rate_limit_filter_pipeline.py): Control the flow of requests to prevent exceeding rate limits.
*  [Real-Time Translation Filter with LibreTranslate](https://github.com/open-webui/pipelines/blob/main/examples/filters/libretranslate_filter_pipeline.py): Seamlessly integrate real-time translations into your LLM interactions.
*  [Toxic Message Filter](https://github.com/open-webui/pipelines/blob/main/examples/filters/detoxify_filter_pipeline.py): Implement filters to detect and handle toxic messages effectively.
*   **And Much More!** : The sky is the limit for what you can accomplish with Pipelines and Python. [Check out our scaffolds](https://github.com/open-webui/pipelines/blob/main/examples/scaffolds) to get a head start on your projects and see how you can streamline your development process!
```

#### 🔧 How It Works

Integrating Pipelines with any OpenAI API-compatible UI client is simple. Launch your Pipelines instance and set the OpenAI URL on your client to the Pipelines URL. That's it! You're ready to leverage any Python library for your needs.

#### ⚡ Quick Start with Docker

⚠ Security Warning
Pipelines are a plugin system with arbitrary code execution — **don't fetch random pipelines from sources you don't trust** . A malicious Pipeline could access your file system, exfiltrate data, mine cryptocurrency, or compromise your system. Always review Pipeline source code before installing. See the [Security Policy](https://docs.openwebui.com/security) for more details.
For a streamlined setup using Docker:
1. **Run the Pipelines container:**

```
docker run -d -p 9099:9099 --add-host=host.docker.internal:host-gateway -v pipelines:/app/pipelines --name pipelines --restart always ghcr.io/open-webui/pipelines:main
```

```
1.  **Connect to Open WebUI:**
*  Navigate to the  **Admin Panel > Settings > Connections**  section in Open WebUI.
    *  When you're on this page, you can press the + button to add another connection.
    *  Set the API URL to http://localhost:9099 and the API key to 0p3n-w3bu! .
    *  Once you've added your pipelines connection and verified it, you will see an icon appear within the API Base URL field for the added connection. When hovered over, the icon itself will be labeled Pipelines . Your pipelines should now be active.
```

info
If your Open WebUI is running in a Docker container, replace localhost with host.docker.internal in the API URL.
1. **Manage Configurations:**
\* In the admin panel, go to **Admin Panel > Settings > Pipelines** tab.
\* Select your desired pipeline and modify the valve values directly from the WebUI.
tip
If you are unable to connect, it is most likely a Docker networking issue. We encourage you to troubleshoot on your own and share your methods and solutions in the discussions forum.
If you need to install a custom pipeline with additional dependencies:
\* **Run the following command:**

```
docker run -d -p 9099:9099 --add-host=host.docker.internal:host-gateway -e PIPELINES_URLS="https://github.com/open-webui/pipelines/blob/main/examples/filters/detoxify_filter_pipeline.py" -v pipelines:/app/pipelines --name pipelines --restart always ghcr.io/open-webui/pipelines:main
```

Alternatively, you can directly install pipelines from the admin settings by copying and pasting the pipeline URL, provided it doesn't have additional dependencies.
That's it! You're now ready to build customizable AI integrations effortlessly with Pipelines. Enjoy!

#### 📦 Installation and Setup

Get started with Pipelines in a few easy steps:
1. **Ensure Python 3.11 is installed.** It is the only officially supported Python version.
1. **Clone the Pipelines repository:**

```
git clone https://github.com/open-webui/pipelines.git
cd pipelines
```

```
1.  **Install the required dependencies:**
```

```
pip install -r requirements.txt
```

```
1.  **Start the Pipelines server:**
```

```
sh ./start.sh
```

Once the server is running, set the OpenAI URL on your client to the Pipelines URL. This unlocks the full capabilities of Pipelines, integrating any Python library and creating custom workflows tailored to your needs.

#### 📂 Directory Structure and Examples

The /pipelines directory is the core of your setup. Add new modules, customize existing ones, and manage your workflows here. All the pipelines in the /pipelines directory will be **automatically loaded** when the server launches.
You can change this directory from /pipelines to another location using the PIPELINES\_DIR env variable.

##### Integration Examples

Find various integration examples in the https://github.com/open-webui/pipelines/blob/main/examples directory. These examples show how to integrate different functionalities, providing a foundation for building your own custom pipelines.

#### 🎉 Work in Progress

We're continuously evolving! We'd love to hear your feedback and understand which hooks and features would best suit your use case. Feel free to reach out and become a part of our Open WebUI community!
Our vision is to push **Pipelines** to become the ultimate plugin framework for our AI interface, **Open WebUI** . Imagine **Open WebUI** as the WordPress of AI interfaces, with **Pipelines** being its diverse range of plugins. Join us on this exciting journey! 🌍
[Edit this page](https://github.com/open-webui/docs/blob/main/docs/features/extensibility/pipelines/index.mdx)
[Previous Model Context Protocol (MCP)](https://docs.openwebui.com/features/extensibility/mcp)
[Next Filters](https://docs.openwebui.com/features/extensibility/pipelines/filters)
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