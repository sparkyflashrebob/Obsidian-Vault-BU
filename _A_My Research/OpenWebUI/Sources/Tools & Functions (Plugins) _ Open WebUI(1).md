---
tags:
  - notebooklm-import
notebook: "OpenWebUI"
category: "research"
---

Tools & Functions (Plugins) / Open WebUI
[Skip to main content](https://docs.openwebui.com/features/extensibility/plugin#__docusaurus_skipToContent_fallback)
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
\* [💬 Chat & Conversations](https://docs.openwebui.com/features/extensibility/plugin)
\* [🧠 Workspace](https://docs.openwebui.com/features/extensibility/plugin)
\* [📝 Notes](https://docs.openwebui.com/features/notes/)
\* [📢 Channels](https://docs.openwebui.com/features/channels/)
\* [💻 Open Terminal](https://docs.openwebui.com/features/open-terminal/)
\* [🔌 Plugins & Extensibility](https://docs.openwebui.com/features/extensibility/)
\* [Tools & Functions (Plugins)](https://docs.openwebui.com/features/extensibility/plugin/)
\* [Tools](https://docs.openwebui.com/features/extensibility/plugin/tools/)
\* [Functions](https://docs.openwebui.com/features/extensibility/plugin/functions/)
\* [Development](https://docs.openwebui.com/category/development)
\* [Migrating Tools & Functions: 0.4 to 0.5](https://docs.openwebui.com/features/extensibility/plugin/migration/)
\* [Model Context Protocol (MCP)](https://docs.openwebui.com/features/extensibility/mcp)
\* [Pipelines](https://docs.openwebui.com/features/extensibility/pipelines/)
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
\* Tools & Functions (Plugins)
On this page

### 🛠 Tools & Functions

⚠ Critical Security Warning
**Tools, Functions, Pipes, Filters, and Pipelines execute arbitrary Python code on your server.** This is by design—it's what makes them powerful. However, this also means:
1. **Only install from trusted sources.** Never import Tools or Functions from unknown or untrusted sources. Malicious code can compromise your entire system.
1. **Review code before importing.** Before installing any community Tool or Function, review its source code. If you don't understand what it does, don't install it.
1. **Protect your data directory.** The data directory (mounted at /app/backend/data in Docker) contains your database, configurations, and cached Tools/Functions. If an attacker gains write access to this directory, they can inject malicious code that will execute on your server.
1. **Restrict Workspace access.** Only trusted administrators should have permission to create, import, or modify Tools and Functions. Regular users should **not** have Workspace access unless explicitly required.
1. **Audit installed plugins regularly.** Periodically review the Tools and Functions installed in your instance via **Workspace → Tools** and **Admin Panel → Functions** .
**What could go wrong?** A malicious Tool or Function could exfiltrate data, install malware, mine cryptocurrency, pivot to other systems on your network, or corrupt your instance.

#### TL;DR

```
*   **Tools**  extend the abilities of LLMs, allowing them to collect real-world, real-time data like weather, stock prices, etc.
*   **Functions**  extend the capabilities of the Open WebUI itself, enabling you to add new AI model support (like Anthropic or Vertex AI) or improve usability (like creating custom buttons or filters).
*   **Pipelines**  are more for advanced users who want to transform Open WebUI features into API-compatible workflows—mainly for offloading heavy processing.
```

Getting started with Tools and Functions is easy because everything's already built into the core system! You just **click a button** and **import these features directly from the community** , so there's no coding or deep technical work required.

#### What are "Tools" and "Functions"?

Let's start by thinking of **Open WebUI** as a "base" software that can do many tasks related to using Large Language Models (LLMs). But sometimes, you need extra features or abilities that don't come *out of the box* —this is where **tools** and **functions** come into play.

##### Tools

**Tools** are an exciting feature because they allow LLMs to do more than just process text. They provide **external abilities** that LLMs wouldn't otherwise have on their own.

###### Example of a Tool:

Imagine you're chatting with an LLM and you want it to give you the latest weather update or stock prices in real time. Normally, the LLM can't do that because it's just working on pre-trained knowledge. This is where **tools** come in!
\* **Tools are like plugins** that the LLM can use to gather **real-world, real-time data** . So, with a "weather tool" enabled, the model can go out on the internet, gather live weather data, and display it in your conversation.
Tools are essentially **abilities** you're giving your AI to help it interact with the outside world. By adding these, the LLM can "grab" useful information or perform specialized tasks based on the context of the conversation.

###### Examples of Tools (extending LLM's abilities):

```
1.  **Real-time weather predictions**  🛰.
1.  **Stock price retrievers**  📈.
1.  **Flight tracking information**  ✈.
```

##### Functions

While **tools** are used by the AI during a conversation, **functions** help extend or customize the capabilities of Open WebUI itself. Imagine tools are like adding new ingredients to a dish, and functions are the process you use to control the kitchen! 🚪

###### Let's break that down:

```
*   **Functions**  give you the ability to tweak or add  **features**  inside  **Open WebUI**  itself.
*  You're not giving new abilities to the LLM, but instead, you're extending the  **interface, behavior, or logic**  of the platform itself!
```

For instance, maybe you want to:
1. Add a new AI model like **Anthropic** to the WebUI.
1. Create a custom button in your toolbar that performs a frequently used command.
1. Implement a better **filter** function that catches inappropriate or **spammy messages** from the incoming text.
Without functions, these would all be out of reach. But with this framework in Open WebUI, you can easily extend these features!

##### Where to Find and Manage Functions

Functions are not located in the same place as Tools.
\* **Tools** are about model access and live in your **Workspace tabs** (where you add models, prompts, and knowledge collections). They can be added by users if granted permissions.
\* **Functions** are about **platform customization** and are found in the **Admin Panel** . They are configured and managed only by admins who want to extend the platform interface or behavior for all users.

##### Summary of Differences:

```
*   **Tools**  are things that allow LLMs to  **do more things**  outside their default abilities (such as retrieving live info or performing custom tasks based on external data).
*   **Functions**  help the WebUI itself  **do more things** , like adding new AI models or creating smarter ways to filter data.
```

Both are designed to be **pluggable** , meaning you can easily import them into your system with just one click from the community! 🎉 You won't have to spend hours coding or tinkering with them.

#### What are Pipelines?

And then, we have **Pipelines** … Here's where things start to sound pretty technical—but don't despair.
**Pipelines** are part of an Open WebUI initiative focused on making every piece of the WebUI **inter-operable with OpenAI's API system** . Essentially, they extend what both **Tools** and **Functions** can already do, but now with even more flexibility. They allow you to turn features into OpenAI API-compatible formats. 🧠

##### But here's the thing…

You likely **won't need** pipelines unless you're dealing with super-advanced setups.
\* **Who are pipelines for?** Typically, **experts** or people running more complicated use cases.
\* **When do you need them?** If you're trying to offload processing from your primary Open WebUI instance to a different machine (so you don't overload your primary system).
In most cases, as a beginner or even an intermediate user, you won't have to worry about pipelines. Just focus on enjoying the benefits that **tools** and **functions** bring to your Open WebUI experience!

#### Want to Try? 🚀

Jump into Open WebUI, head over to the community section, and try importing a tool like **weather updates** or maybe adding a new feature to the toolbar with a function. Exploring these tools will show you how powerful and flexible Open WebUI can be!
🌟 There's always more to learn, so stay curious and keep experimenting!
[Edit this page](https://github.com/open-webui/docs/blob/main/docs/features/extensibility/plugin/index.mdx)
[Previous Extensibility](https://docs.openwebui.com/features/extensibility/)
[Next Tools](https://docs.openwebui.com/features/extensibility/plugin/tools/)
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