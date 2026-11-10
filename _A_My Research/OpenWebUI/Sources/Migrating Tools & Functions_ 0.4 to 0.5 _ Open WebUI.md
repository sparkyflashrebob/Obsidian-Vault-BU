---
tags:
  - notebooklm-import
notebook: "OpenWebUI"
category: "research"
---

Migrating Tools & Functions: 0.4 to 0.5 / Open WebUI
[Skip to main content](https://docs.openwebui.com/features/extensibility/plugin/migration/#__docusaurus_skipToContent_fallback)
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
\* [💬 Chat & Conversations](https://docs.openwebui.com/features/extensibility/plugin/migration/)
\* [🧠 Workspace](https://docs.openwebui.com/features/extensibility/plugin/migration/)
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
\* [Tools & Functions (Plugins)](https://docs.openwebui.com/features/extensibility/plugin/)
\* Migrating Tools & Functions: 0.4 to 0.5
On this page

### 🚚 Migration Guide: Open WebUI 0.4 to 0.5

Welcome to the Open WebUI 0.5 migration guide! If you're working on existing projects or building new ones, this guide will walk you through the key changes from **version 0.4 to 0.5** and provide an easy-to-follow roadmap for upgrading your Functions. Let's make this transition as smooth as possible! 😊

#### 🧐 What Has Changed and Why?

With Open WebUI 0.5, we've overhauled the architecture to make the project **simpler, more unified, and scalable** . Here's the big picture:
\* **Old Architecture:** 🎯 Previously, Open WebUI was built on a **sub-app architecture** where each app (e.g., ollama , openai ) was a separate FastAPI application. This caused fragmentation and extra complexity when managing apps.
\* **New Architecture:** 🚀 With version 0.5, we have transitioned to a **single FastAPI app** with multiple **routers** . This means better organization, centralized flow, and reduced redundancy.

##### Key Changes:

Here's an overview of what changed:
1. **Apps have been moved to Routers.**
\* Previous: open\_webui.apps
\* Now: open\_webui.routers
1. **Main app structure simplified.**
\* The old open\_webui.apps.webui has been transformed into open\_webui.main , making it the central entry point for the project.
1. **Unified API Endpoint**
\* Open WebUI 0.5 introduces a **unified function** , chat\_completion , in open\_webui.main , replacing separate functions for models like ollama and openai . This offers a consistent and streamlined API experience. However, the **direct successor** of these individual functions is generate\_chat\_completion from open\_webui.utils.chat . If you prefer a lightweight POST request without handling additional parsing (e.g., files, tools, or misc), this utility function is likely what you want.

###### Example:

```
# Full API flow with parsing (new function):
from open_webui.main import chat_completion

# Lightweight, direct POST request (direct successor):
from open_webui.utils.chat import generate_chat_completion
```

Choose the approach that best fits your use case!
1. **Updated Function Signatures.**
\* Function signatures now adhere to a new format, requiring a request object.
\* The request object can be obtained using the **request** parameter in the function signature. Below is an example:

```
class Pipe:
    def __init__(self):
        pass

    async def pipe(
        self,
        body: dict,
        __user__: dict,
        __request__: Request, # New parameter
    ) -> str:
        # Write your function here
```

📌 **Why did we make these changes?**
\* To simplify the codebase, making it easier to extend and maintain.
\* To unify APIs for a more streamlined developer experience.
\* To enhance performance by consolidating redundant elements.

#### ✅ Step-by-Step Migration Guide

Follow this guide to smoothly update your project.

##### 🔄 1. Shifting from apps to routers

All apps have been renamed and relocated under open\_webui.routers . This affects imports in your codebase.
Quick changes for import paths:

| **Old Path** | **New Path** |
| --- | --- |
| open\_webui.apps.ollama | open\_webui.routers.ollama |
| open\_webui.apps.openai | open\_webui.routers.openai |
| open\_webui.apps.audio | open\_webui.routers.audio |
| open\_webui.apps.retrieval | open\_webui.routers.retrieval |
| open\_webui.apps.webui | open\_webui.main |

##### 📜 An Important Example

To clarify the special case of the main app ( webui ), here's a simple rule of thumb:
\* **Was in webui ?** It's now in the project's root or open\_webui.main .
\* For example:
\* **Before (0.4):**

```
from open_webui.apps.webui.models import SomeModel
```

```
*   **After (0.5):**
```

```
from open_webui.models import SomeModel
```

In general, **just replace open\_webui.apps with open\_webui.routers —except for webui , which is now open\_webui.main !**

##### 👩💻 2. Updating Import Statements

Let's look at what this update looks like in your code:

###### Before:

```
from open_webui.apps.ollama import main as ollama
from open_webui.apps.openai import main as openai
```

###### After:

```
# Separate router imports
from open_webui.routers.ollama import generate_chat_completion
from open_webui.routers.openai import generate_chat_completion

# Or use the unified endpoint
from open_webui.main import chat_completion
```

tip
Prioritize the unified endpoint ( chat\_completion ) for simplicity and future compatibility.

##### 📝 **Additional Note: Choosing Between main.chat\_completion and utils.chat.generate\_chat\_completion**

Depending on your use case, you can choose between:
1. **open\_webui.main.chat\_completion :**
\* Simulates making a POST request to /api/chat/completions .
\* Processes files, tools, and other miscellaneous tasks.
\* Best when you want the complete API flow handled automatically.
1. **open\_webui.utils.chat.generate\_chat\_completion :**
\* Directly makes a POST request without handling extra parsing or tasks.
\* This is the **direct successor** to the previous main.generate\_chat\_completions , ollama.generate\_chat\_completion and openai.generate\_chat\_completion functions in Open WebUI 0.4.
\* Best for simplified and more lightweight scenarios.

###### Example:

```
# Use this for the full API flow with parsing:
from open_webui.main import chat_completion

# Use this for a stripped-down, direct POST request:
from open_webui.utils.chat import generate_chat_completion
```

##### 📋 3. Adapting to Updated Function Signatures

We've updated the **function signatures** to better fit the new architecture. If you're looking for a direct replacement, start with the lightweight utility function generate\_chat\_completion from open\_webui.utils.chat . For the full API flow, use the new unified chat\_completion function in open\_webui.main .

###### Function Signature Changes:

| **Old** | **Direct Successor (New)** | **Unified Option (New)** |
| --- | --- | --- |
| openai.generate\_chat\_completion(form\_data: dict, user: UserModel) | generate\_chat\_completion(request: Request, form\_data: dict, user: UserModel) | chat\_completion(request: Request, form\_data: dict, user: UserModel) |

```
*   **Direct Successor ( generate_chat_completion )** : A lightweight, 1:1 replacement for previous ollama / openai methods.
*   **Unified Option ( chat_completion )** : Use this for the complete API flow, including file parsing and additional functionality.
```

###### Example:

If you're using chat\_completion , here's how your function should look now:

##### 🛠 How to Refactor Your Custom Function

Let's rewrite a sample function to match the new structure:

###### Before (0.4):

```
from pydantic import BaseModel
from open_webui.apps.ollama import generate_chat_completion

class User(BaseModel):
    id: str
    email: str
    name: str
    role: str

class Pipe:
    def __init__(self):
        pass

    async def pipe(self, body: dict, __user__: dict) -> str:
        # Calls OpenAI endpoint
        user = User(**__user__)
        body["model"] = "llama3.2:latest"
        return await ollama.generate_chat_completion(body, user)
```

###### After (0.5):

```
from pydantic import BaseModel
from fastapi import Request

from open_webui.utils.chat import generate_chat_completion

class User(BaseModel):
    id: str
    email: str
    name: str
    role: str

class Pipe:
    def __init__(self):
        pass

    async def pipe(
        self,
        body: dict,
        __user__: dict,
        __request__: Request,
    ) -> str:
        # Uses the unified endpoint with updated signature
        user = User(**__user__)
        body["model"] = "llama3.2:latest"
        return await generate_chat_completion(__request__, body, user)
```

##### Important Notes:

```
*  You must pass a Request object ( __request__ ) in the new function signature.
*  Other optional parameters (like __user__ and __event_emitter__ ) ensure flexibility for more complex use cases.
```

##### 🌟 4. Recap: Key Concepts in Simple Terms

Here's a quick cheat sheet to remember:
\* **Apps to Routers:** Update all imports from open\_webui.apps ➡ open\_webui.routers .
\* **Unified Endpoint:** Use open\_webui.main.chat\_completion for simplicity if both ollama and openai are involved.
\* **Adapt Function Signatures:** Ensure your functions pass the required request object.

#### 🎉 Hooray! You're Ready!

That's it! You've successfully migrated from **Open WebUI 0.4 to 0.5** . By refactoring your imports, using the unified endpoint, and updating function signatures, you'll be fully equipped to leverage the latest features and improvements in version 0.5.
💬 **Questions or Feedback?** If you run into any issues or have suggestions, feel free to open a [GitHub issue](https://github.com/open-webui/open-webui) or ask in the community forums!
Happy coding! ✨
[Edit this page](https://github.com/open-webui/docs/blob/main/docs/features/extensibility/plugin/migration/index.mdx)
[Previous Reserved Arguments](https://docs.openwebui.com/features/extensibility/plugin/development/reserved-args)
[Next Model Context Protocol (MCP)](https://docs.openwebui.com/features/extensibility/mcp)
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