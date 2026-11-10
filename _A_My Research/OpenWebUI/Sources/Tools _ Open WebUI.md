---
tags:
  - notebooklm-import
notebook: "OpenWebUI"
category: "research"
---

Tools / Open WebUI
[Skip to main content](https://docs.openwebui.com/features/extensibility/plugin/tools/#__docusaurus_skipToContent_fallback)
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
\* [💬 Chat & Conversations](https://docs.openwebui.com/features/extensibility/plugin/tools/)
\* [🧠 Workspace](https://docs.openwebui.com/features/extensibility/plugin/tools/)
\* [📝 Notes](https://docs.openwebui.com/features/notes/)
\* [📢 Channels](https://docs.openwebui.com/features/channels/)
\* [💻 Open Terminal](https://docs.openwebui.com/features/open-terminal/)
\* [🔌 Plugins & Extensibility](https://docs.openwebui.com/features/extensibility/)
\* [Tools & Functions (Plugins)](https://docs.openwebui.com/features/extensibility/plugin/)
\* [Tools](https://docs.openwebui.com/features/extensibility/plugin/tools/)
\* [Development](https://docs.openwebui.com/features/extensibility/plugin/tools/development)
\* [OpenAPI Tool Servers](https://docs.openwebui.com/features/extensibility/plugin/tools/openapi-servers/)
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
\* Tools
On this page

### What are Tools?

⚠ Critical Security Warning
**Workspace Tools and Functions execute arbitrary Python code on your server.** Only install from trusted sources, review code before importing, and restrict Workspace access to trusted administrators only. Granting a user the ability to create or import Tools is equivalent to giving them shell access to the server. For full details, see the [Plugin Security Warning](https://docs.openwebui.com/features/extensibility/plugin/).
⚙ Tools are the various ways you can extend an LLM's capabilities beyond simple text generation. When enabled, they allow your chatbot to do amazing things — like search the web, scrape data, generate images, talk back using AI voices, and more.
Because there are several ways to integrate "Tools" in Open WebUI, it's important to understand which type you are using.

#### Tooling Taxonomy: Which "Tool" are you using?

🧩 Users often encounter the term "Tools" in different contexts. Here is how to distinguish them:

| Type | Location in UI | Best For... | Source |
| --- | --- | --- | --- |
| **Native Features** | Admin/Settings | Core platform functionality | Built-in to Open WebUI |
| **Workspace Tools** | Workspace > Tools | User-created or community Python scripts | [Community Library](https://openwebui.com/search) |
| **Native MCP (HTTP)** | Settings > Connections | Standard MCP servers reachable via HTTP/SSE | External MCP Servers |
| **MCP via Proxy (MCPO)** | Settings > Connections | Local stdio-based MCP servers (e.g., Claude Desktop tools) | [MCPO Adapter](https://github.com/open-webui/mcpo) |
| **OpenAPI Servers** | Settings > Connections | Standard REST/OpenAPI web services | External Web APIs |
| **Open Terminal** | Settings > Integrations | Full shell access in an isolated Docker container (always-on) | [Open Terminal](https://github.com/open-webui/open-terminal) |

##### 1. Native Features (Built-in)

These are deeply integrated into Open WebUI and generally don't require external scripts.
\* **Web Search** : Integrated via engines like SearXNG, Google, or Tavily.
\* **URL Fetching** : Extract text content directly from websites using # or native tools.
\* **Image Generation** : Integrated with DALL-E, ComfyUI, or Automatic1111.
\* **Memory** : The ability for models to remember facts about you across chats.
\* **RAG (Knowledge)** : The ability to query uploaded documents ( # ).
In [Native Mode](https://docs.openwebui.com/features/extensibility/plugin/tools/#built-in-system-tools-nativeagentic-mode), these features are exposed as **Tools** that the model can call independently.

##### 2. Workspace Tools (Custom Plugins)

These are **Python scripts** that run directly within the Open WebUI environment.
\* **Capability** : Can do anything Python can do (web scraping, complex math, API calls).
\* **Access** : Managed via the Workspace menu.
\* **Safety** : Always review code before importing, as these run on your server.
\* **⚠ Security Warning** : Normal or untrusted users should **not** be given permission to access the Workspace Tools section. This access allows a user to upload and execute arbitrary Python code on your server, which could lead to a full system compromise.

##### 3. MCP (Model Context Protocol)

🔌 MCP is an open standard that allows LLMs to interact with external data and tools.
\* **Native HTTP MCP** : Open WebUI can connect directly to any MCP server that exposes an HTTP/SSE endpoint.
\* **MCPO (Proxy)** : Most community MCP servers use stdio (local command line). To use these in Open WebUI, you use the [MCPO Proxy](https://docs.openwebui.com/features/extensibility/plugin/tools/openapi-servers/mcp) to bridge the connection.

##### 4. OpenAPI / Function Calling Servers

Generic web servers that provide an OpenAPI ( .json or .yaml ) specification. Open WebUI can ingest these specs and treat every endpoint as a tool.

#### How to Install & Manage Workspace Tools

📦 Workspace Tools are the most common way to extend your instance with community features.
1. Go to [Community Tool Library](https://openwebui.com/search)
1. Choose a Tool, then click the **Get** button.
1. Enter your Open WebUI instance's URL (e.g. http://localhost:3000 ).
1. Click **Import to WebUI** .
Safety Tip
Never import a Tool you don't recognize or trust. These are Python scripts and might run unsafe code on your host system. **Crucially, ensure you only grant "Tool" permissions to trusted users** , as the ability to create or import tools is equivalent to the ability to run arbitrary code on the server.

#### How to Use Tools in Chat

🔧 Once installed or connected, here's how to enable them for your conversations:

##### Option 1: Enable on-the-fly (Specific Chat)

While chatting, click the **➕ (plus)** icon in the input area. You'll see a list of available Tools — you can enable them specifically for that session.

##### Option 2: Enable by Default (Global/Model Level)

```
1. Go to  **Workspace ➡ Models** .
1. Choose the model you're using and click the ✏ edit icon.
1. Scroll to the  **Tools**  section.
1. ✅ Check the Tools you want this model to always have access to by default.
1. Click  **Save** .
```

You can also let your LLM auto-select the right Tools using the [AutoTool Filter](https://openwebui.com/f/hub/autotool_filter/).
Attached Tools Still Require User Access
Attaching a workspace tool to a model does **not** bypass access control. When a user chats with the model, Open WebUI checks whether **that specific user** has read access to each attached tool. Tools the user cannot access are silently skipped — the model won't be able to call them.
**Example scenario** : An admin creates a private tool and attaches it to a model shared with all users. Regular users chatting with this model will **not** have the tool available because they don't have read access to the tool itself.
**Solution** : Make sure users who need the model's tools also have read access to each tool (via access grants, group permissions, or by making the tool public). The "Workspace → Tools" permission controls whether users can *create and manage* tools — it does **not** affect whether model-attached tools work for them.

#### Tool Calling Modes: Default vs. Native

Open WebUI offers two distinct ways for models to interact with tools: a standard **Default Mode** and a high-performance **Native Mode (Agentic Mode)** . Choosing the right mode depends on your model's capabilities and your performance requirements.

##### 🟡 Default Mode (Prompt-based) — Legacy

Legacy Mode
Default Mode is maintained purely for **backwards compatibility** with older or smaller models that lack native function-calling support. It is considered **legacy** and should not be used when your model supports native tool calling. New deployments should use **Native Mode** exclusively.
In Default Mode, Open WebUI manages tool selection by injecting a specific prompt template that guides the model to output a tool request.
\* **Compatibility** : Works with **practically any model** , including older or smaller local models that lack native function-calling support.
\* **Flexibility** : Highly customizable via prompt templates.
\* **Caveats** :
\* Can be slower (requires extra tokens) and less reliable for complex, multi-step tool chaining.
\* **Breaks KV cache** : The injected prompt changes every turn, preventing LLM engines from reusing cached key-value pairs. This increases latency and cost for every message in the conversation.
\* Does not support built-in system tools (memory, notes, channels, etc.).

##### 🟢 Native Mode (Agentic Mode / System Function Calling) — Recommended

Native Mode (also called **Agentic Mode** ) leverages the model's built-in capability to handle tool definitions and return structured tool calls (JSON). This is the **recommended mode** for all models that support it — which includes the vast majority of modern models (2024+).
Model Quality Matters
**Agentic tool calling requires high-quality models to work reliably.** While small local models may technically support function calling, they often struggle with the complex reasoning required for multi-step tool usage. For best results, use frontier models like **GPT-5** , **Claude 4.5 Sonnet** , **Gemini 3 Flash** , or **MiniMax M2.5** . Small local models may produce malformed JSON or fail to follow the strict state management required for agentic behavior.

###### Why use Native Mode (Agentic Mode)?

```
*   **Speed & Efficiency** : Lower latency as it avoids bulky prompt-based tool selection.
*   **KV Cache Friendly** : Tool definitions are sent as structured parameters (not injected into the prompt), so they don't invalidate the KV cache between turns. This can significantly reduce latency and token costs.
*   **Reliability** : Higher accuracy in following tool schemas (with quality models).
*   **Multi-step Chaining** : Essential for  **Agentic Research**  and  **Interleaved Thinking**  where a model needs to call multiple tools in succession.
*   **Autonomous Decision-Making** : Models can decide when to search, which tools to use, and how to combine results.
*   **System Tools** : Only Native Mode unlocks the [built-in system tools](https://docs.openwebui.com/features/extensibility/plugin/tools/#built-in-system-tools-nativeagentic-mode) (memory, notes, knowledge, channels, etc.).
```

###### How to Enable Native Mode (Agentic Mode)

Native Mode can be enabled at two levels:
1. **Global/Administrator Level (Recommended)** :
\* Navigate to **Admin Panel > Settings > Models** .
\* Scroll to **Model Specific Settings** for your target model.
\* Under **Advanced Parameters** , find the **Function Calling** dropdown and select Native .
1. **Per-Chat Basis** :
\* Inside a chat, click the ⚙ **Chat Controls** icon.
\* Go to **Advanced Params** and set **Function Calling** to Native .

###### Model Requirements & Caveats

Recommended Models for Agentic Mode
For reliable agentic tool calling, use high-tier frontier models:
\* **GPT-5** (OpenAI)
\* **Claude 4.5 Sonnet** (Anthropic)
\* **Gemini 3 Flash** (Google)
\* **MiniMax M2.5**
These models excel at multi-step reasoning, proper JSON formatting, and autonomous tool selection.
\* **Large Local Models** : Some large local models (e.g., Qwen 3 32B, Llama 3.3 70B) can work with Native Mode, but results vary significantly by model quality.
\* **Small Local Models Warning** : **Small local models** (under 30B parameters) often struggle with Native Mode. They may produce malformed JSON, fail to follow strict state management, or make poor tool selection decisions. For these models, **Default Mode** is usually more reliable.

###### Known Model-Specific Issues

DeepSeek V3.2 Function Calling Issues
**DeepSeek V3.2** has known issues with native function calling that cause **reproducible failures** . Despite being a 600B+ parameter model, it often outputs malformed tool calls.
**The Problem** : DeepSeek V3.2 was trained using a proprietary format called **DSML (DeepSeek Markup Language)** for tool calls. When using native function calling, the model sometimes outputs raw DSML/XML-like syntax instead of proper JSON:
\*

| Feature | Default Mode (Legacy) | Native Mode (Recommended) |
| --- | --- | --- |
| **Status** | Legacy / backwards compat | ✅ Recommended |
| **Latency** | Medium/High | Low |
| **KV Cache** | ❌ Can break cache | ✅ Cache-friendly |
| **Model Compatibility** | Universal | Requires Tool-Calling Support |
| **Logic** | Prompt-based (Open WebUI) | Model-native (API/Ollama) |
| **System Tools** | ❌ Not available | ✅ Full access |
| **Complex Chaining** | ⚠ Limited | ✅ Excellent |

##### Built-in System Tools (Native/Agentic Mode)

🛠 When **Native Mode (Agentic Mode)** is enabled, Open WebUI automatically injects powerful system tools. This unlocks truly agentic behaviors where capable models (like GPT-5, Claude 4.5 Sonnet, Gemini 3 Flash, or MiniMax M2.5) can perform multi-step research, explore knowledge bases, or manage user memory autonomously.
Tool
Purpose
**Search & Web**
*Requires ENABLE\_WEB\_SEARCH enabled AND per-chat "Web Search" toggle enabled.* search\_web
Search the public web for information. Best for current events, external references, or topics not covered in internal documents. fetch\_url
Visits a URL and extracts text content via the Web Loader.
**Knowledge Base**
*Requires per-model "Knowledge Base" category enabled (default: on). Which tools are injected depends on whether the model has attached knowledge — see note below.* list\_knowledge
List attached knowledge (KBs, files, notes). Start here when attachments exist. list\_knowledge\_bases
List accessible knowledge bases with file counts. query\_knowledge\_bases
Semantic search over KB names/descriptions to find the right KB. search\_knowledge\_bases
Text search over KB names/descriptions. query\_knowledge\_files
Search file contents via the RAG retrieval pipeline (hybrid + rerank when enabled). Main tool for finding answers in docs. search\_knowledge\_files
Search files by filename. view\_file
Read a user-accessible file by ID with pagination ( offset , max\_chars ). view\_knowledge\_file
Read a knowledge-base file by ID with pagination ( offset , max\_chars ).
**Image Gen**
*Requires image generation enabled (per-tool) AND per-chat "Image Generation" toggle enabled.* generate\_image
Generates a new image based on a prompt. Requires ENABLE\_IMAGE\_GENERATION . edit\_image
Edits existing images based on a prompt and image URLs. Requires ENABLE\_IMAGE\_EDIT .
**Code Interpreter**
*Requires ENABLE\_CODE\_INTERPRETER enabled (default: on) AND per-chat "Code Interpreter" toggle enabled.* execute\_code
Executes code in a sandboxed environment and returns the output.
**Memory**
*Requires Memory feature enabled AND per-model "Memory" category enabled (default: on).* search\_memories
Searches the user's personal memory/personalization bank. add\_memory
Stores a new fact in the user's personalization memory. replace\_memory\_content
Updates an existing memory record by its unique ID. delete\_memory
Deletes a memory by its ID. list\_memories
Lists all stored memories for the user with content and dates.
**Notes**
*Requires ENABLE\_NOTES AND per-model "Notes" category enabled (default: on).* search\_notes
Search the user's notes by title and content. view\_note
Get the full markdown content of a specific note. write\_note
Create a new private note for the user. replace\_note\_content
Update an existing note's content or title.
**Chat History**
*Requires per-model "Chat History" category enabled (default: on).* search\_chats
Simple text search across chat titles and message content. Returns matching chat IDs and snippets. view\_chat
Reads and returns the full message history of a specific chat by ID.
**Channels**
*Requires ENABLE\_CHANNELS AND per-model "Channels" category enabled (default: on).* search\_channels
Find public or accessible channels by name/description. search\_channel\_messages
Search for specific messages inside accessible channels. view\_channel\_message
View a specific message or its details in a channel. view\_channel\_thread
View a full message thread/replies in a channel.
**Skills**
*Requires at least one skill to be attached to the model via Workspace/Admin Panel → Models → Edit → Skills. The model receives a summary of attached skills in its system prompt and can call view\_skill to load full instructions on demand. No separate builtin tools category checkbox is needed — attaching a skill is the only requirement.* view\_skill
Load the full instructions of a skill by name. The tool is injected when skills are attached; resolving a skill still follows normal ownership/access-grant checks.
**Time Tools**
*Requires per-model "Time & Calculation" category enabled (default: on).* get\_current\_timestamp
Get the current UTC Unix timestamp and ISO date. calculate\_timestamp
Calculate relative timestamps (e.g., "3 days ago").

###### Knowledge Tool Availability (At a Glance)

Use this quick matrix instead of memorizing per-row caveats.

| Tool | Model has attached knowledge | Model has no attached knowledge |
| --- | --- | --- |
| list\_knowledge | ✅ | ❌ |
| list\_knowledge\_bases | ❌ | ✅ |
| search\_knowledge\_bases | ❌ | ✅ |
| query\_knowledge\_bases | ❌ | ✅ |
| search\_knowledge\_files | ✅ (auto-scoped) | ✅ (all accessible KBs) |
| query\_knowledge\_files | ✅ (auto-scoped) | ✅ |
| view\_file | ✅ (when attached items include files/collections) | ❌ |
| view\_knowledge\_file | ✅ (when attached items include files/collections) | ✅ |
| view\_note | ✅ (when attached items include notes) | ❌ |

Quick rule: list\_knowledge and list\_knowledge\_bases are mutually exclusive.

###### Tool Reference

| Tool | Parameters | Output |
| --- | --- | --- |
| **Search & Web** |  |  |
| search\_web | query (required), count (default: 5) | Array of {title, link, snippet} |
| fetch\_url | url (required) | Plain text content (max 50,000 chars) |
| **Knowledge Base** |  |  |
| list\_knowledge | None | {knowledge\_bases: [{id, name, description, file\_count, files: [{id, filename}]}], files: [{id, filename}], notes: [{id, title}]} |
| list\_knowledge\_bases | count (default: 10), skip (default: 0) | Array of {id, name, description, file\_count} |
| query\_knowledge\_bases | query (required), count (default: 5) | Array of {id, name, description} by similarity |
| search\_knowledge\_bases | query (required), count (default: 5), skip (default: 0) | Array of {id, name, description, file\_count} |
| query\_knowledge\_files | query (required), knowledge\_ids (optional), count (default: 5) | Array of chunks like {content, source, file\_id, distance?} ; note hits include {note\_id, type: "note"} |
| search\_knowledge\_files | query (required), knowledge\_id (optional), count (default: 5), skip (default: 0) | Array of {id, filename, knowledge\_id, knowledge\_name} |
| view\_file | file\_id (required), offset (default: 0), max\_chars (default: 10000, cap: 100000) | {id, filename, content, updated\_at, created\_at} — includes truncated , total\_chars , next\_offset when paginated |
| view\_knowledge\_file | file\_id (required), offset (default: 0), max\_chars (default: 10000, cap: 100000) | {id, filename, content, knowledge\_id, knowledge\_name} — includes pagination metadata when truncated |
| **Image Gen** |  |  |
| generate\_image | prompt (required) | {status, message, images} — auto-displayed |
| edit\_image | prompt (required), image\_urls (required) | {status, message, images} — auto-displayed |
| **Code Interpreter** |  |  |
| execute\_code | code (required) | {status, stdout, stderr, result} |
| **Memory** |  |  |
| search\_memories | query (required), count (default: 5) | Array of {id, date, content} |
| add\_memory | content (required) | {status: "success", id} |
| replace\_memory\_content | memory\_id (required), content (required) | {status: "success", id, content} |
| delete\_memory | memory\_id (required) | {status: "success", message} |
| list\_memories | None | Array of {id, content, created\_at, updated\_at} |
| **Notes** |  |  |
| search\_notes | query (required), count (default: 5), start\_timestamp , end\_timestamp | Array of {id, title, snippet, updated\_at} |
| view\_note | note\_id (required) | {id, title, content, updated\_at, created\_at} |
| write\_note | title (required), content (required) | {status: "success", id} |
| replace\_note\_content | note\_id (required), content (required), title (optional) | {status: "success", id, title} |
| **Chat History** |  |  |
| search\_chats | query (required), count (default: 5), start\_timestamp , end\_timestamp | Array of {id, title, snippet, updated\_at} |
| view\_chat | chat\_id (required) | {id, title, messages: [{role, content}]} |
| **Channels** |  |  |
| search\_channels | query (required), count (default: 5) | Array of {id, name, description, type} |
| search\_channel\_messages | query (required), count (default: 10), start\_timestamp , end\_timestamp | Array of {channel\_id, channel\_name, message\_id, content\_snippet, is\_thread\_reply, parent\_id, created\_at} |
| view\_channel\_message | message\_id (required) | {id, content, user\_name, created\_at, reply\_count} |
| view\_channel\_thread | parent\_message\_id (required) | {channel\_id, channel\_name, thread\_id, message\_count, messages: [...]} |
| **Skills** |  |  |
| view\_skill | name (required) | {name, content} |
| **Time Tools** |  |  |
| get\_current\_timestamp | None | {current\_timestamp, current\_iso} |
| calculate\_timestamp | days\_ago , weeks\_ago , months\_ago , years\_ago (all default: 0) | {current\_timestamp, current\_iso, calculated\_timestamp, calculated\_iso} |

Automatic Timezone Detection
Open WebUI automatically detects and stores your timezone when you log in. This allows time-related tools and features to provide accurate local times without any manual configuration. Your timezone is determined from your browser settings.
Knowledge Tool Injection Depends on Attachments
Knowledge tool availability changes based on whether the model has attached knowledge. Use the **Knowledge Tool Availability** matrix above as the source of truth.
\* With attachments: the model gets scoped knowledge tools.
\* Without attachments: the model gets KB discovery tools.
\* list\_knowledge and list\_knowledge\_bases are mutually exclusive.
Attached Knowledge Still Requires User Access
Attaching a knowledge base to a custom model does **not** bypass access control. When a user chats with the model, query\_knowledge\_files checks whether **that specific user** has permission to access each attached knowledge item. Items the user cannot access are silently excluded from search results.
**Access requirements by knowledge type:**

| Attached Type | User Needs |
| --- | --- |
| **Knowledge Base** (collection) | Owner, admin, or explicit read access grant |
| **Individual File** | Owner or admin only (no access grants) |
| **Note** | Owner, admin, or explicit read access grant |

**Example scenario** : An admin creates a private knowledge base and attaches it to a custom model shared with all users. Regular users chatting with this model will get **empty results** from query\_knowledge\_files because they don't have read access to the KB itself — even though they can use the model.
**Solution** : Make sure users who need access to the model's knowledge also have read access to the underlying knowledge base (via access grants or group permissions in the Knowledge settings).
Recommended KB Tool Workflow
**With attached knowledge:**
1. First call list\_knowledge to discover attached KBs, files, and notes
1. Use query\_knowledge\_files to search file contents (auto-scoped to attachments)
1. Use view\_file or view\_knowledge\_file to read specific files — use offset and max\_chars for large files
**Without attached knowledge:**
1. First call list\_knowledge\_bases to discover what knowledge is available
1. Then use query\_knowledge\_files to search file contents within relevant KBs
1. If still empty, the files may not be embedded yet, or you may have **Full Context mode enabled** which bypasses the vector store
**Do NOT use Full Context mode with knowledge tools** — Full Context injects file content directly and doesn't store embeddings, so query\_knowledge\_files will return empty. Use Focused Retrieval (default) for tool-based access.
Knowledge Base Tools and Hybrid Search
The native query\_knowledge\_files tool uses **hybrid search + reranking** when ENABLE\_RAG\_HYBRID\_SEARCH is enabled in admin settings, giving you the same search quality as the standard RAG pipeline. When hybrid search is disabled, it falls back to simple vector search.
Knowledge is NOT Auto-Injected in Native Mode
**Important:** When using Native Function Calling, attached knowledge is **not automatically injected** into the conversation. The model must actively call knowledge tools to search and retrieve information.
**If your model isn't using attached knowledge:**
1. **Add instructions to your system prompt** telling the model to discover and query knowledge bases. Example: *"When users ask questions, first use list\_knowledge to see what knowledge is available, then use query\_knowledge\_files to search the relevant knowledge base before answering. If no knowledge is attached to this model, use list\_knowledge\_bases first to discover available KBs."*
1. **Or disable Native Function Calling** for that model to restore automatic RAG injection.
1. **Or use "Full Context" mode** for attached knowledge (click on the attachment and select "Use Entire Document") which always injects the full content.
See [Knowledge Scoping with Native Function Calling](https://docs.openwebui.com/features/workspace/knowledge#scoped-access-keeps-things-organized) for more details.
**Why use these?** It allows for **Deep Research** (searching the web multiple times, or querying knowledge bases), **Contextual Awareness** (looking up previous chats or notes), **Dynamic Personalization** (saving facts), and **Precise Automation** (generating content based on existing notes or documents).

###### Disabling Builtin Tools (Per-Model)

The **Builtin Tools** capability can be toggled on or off for each model in the **Workspace > Models** editor under **Capabilities** . When enabled (the default), all the system tools listed above are automatically injected when using Native Mode.
**When to disable Builtin Tools:**

| Scenario | Reason to Disable |
| --- | --- |
| **Model doesn't support function calling** | Smaller or older models may not handle the tools parameter correctly |
| **Simpler/predictable behavior needed** | You want the model to work only with pre-injected context, no autonomous tool calls |
| **Security/control concerns** | Prevents the model from actively querying knowledge bases, searching chats, accessing memories, etc. |
| **Token efficiency** | Tool specifications consume tokens; disabling saves context window space |

**What happens when Builtin Tools is disabled:**
1. **No tool injection** : The model won't receive any of the built-in system tools, even in Native Mode.
1. **RAG still works** (if File Context is enabled): Attached files are still processed via RAG and injected as context.
1. **No autonomous retrieval** : The model cannot decide to search knowledge bases or fetch additional information—it works only with what's provided upfront.

###### Granular Builtin Tool Categories (Per-Model)

When the **Builtin Tools** capability is enabled, you can further control which **categories** of builtin tools are available to the model. This appears in the Model Editor as a set of checkboxes under **Builtin Tools** .

| Category | Tools Included | Description |
| --- | --- | --- |
| **Time & Calculation** | get\_current\_timestamp , calculate\_timestamp | Get current time and perform date/time calculations |
| **Memory** | search\_memories , add\_memory , replace\_memory\_content , delete\_memory , list\_memories | Search and manage user memories |
| **Chat History** | search\_chats , view\_chat | Search and view user chat history |
| **Notes** | search\_notes , view\_note , write\_note , replace\_note\_content | Search, view, and manage user notes |
| **Knowledge Base** | list\_knowledge , list\_knowledge\_bases , search\_knowledge\_bases , query\_knowledge\_bases , search\_knowledge\_files , query\_knowledge\_files , view\_file , view\_knowledge\_file | Browse and query knowledge bases |
| **Web Search** | search\_web , fetch\_url | Search the web and fetch URL content |
| **Image Generation** | generate\_image , edit\_image | Generate and edit images |
| **Code Interpreter** | execute\_code | Execute code in a sandboxed environment |
| **Channels** | search\_channels , search\_channel\_messages , view\_channel\_message , view\_channel\_thread | Search channels and channel messages |

All categories are **enabled by default** . Disabling a category prevents those specific tools from being injected, while keeping other categories active.
Skills / view\_skill — Not a Category Toggle
The view\_skill tool does **not** appear in the Builtin Tools category checkboxes. It is injected when at least one skill is **attached to the model** via **Workspace → Models → Edit → Skills** . When skills are attached:
1. The model receives a summary of each attached skill (name + description) in its system prompt via  tags
1. The view\_skill tool is injected so the model can load full instructions on demand
1. If no skills are attached, view\_skill is not available
Users can also select skills per-chat (via the chat input bar), which injects the skill's full content directly into the system prompt instead of requiring a view\_skill call.
**Use cases for granular control:**

| Scenario | Recommended Configuration |
| --- | --- |
| **Privacy-focused model** | Disable Memory and Chat History to prevent access to personal data |
| **Read-only assistant** | Disable Notes (prevents creating/modifying notes) but keep Knowledge Base enabled |
| **Minimal token usage** | Enable only the categories the model actually needs |
| **Knowledge-centric bot** | Disable everything except Knowledge Base and Time |

note
These per-category toggles only appear when the main **Builtin Tools** capability is enabled. If you disable Builtin Tools entirely, no tools are injected regardless of category settings.
Global Features Take Precedence
Enabling a per-model category toggle does **not** override global feature flags. For example, if ENABLE\_NOTES is disabled globally (Admin Panel), Notes tools will not be available even if the "Notes" category is enabled for the model. The per-model toggles only allow you to *further restrict* what's already available—they cannot enable features that are disabled at the global level.
Per-Chat Feature Toggles (Web Search, Image Generation, Code Interpreter)
**Web Search** , **Image Generation** , and **Code Interpreter** built-in tools have an additional layer of control: the **per-chat feature toggle** in the chat input bar. For these tools to be injected in Native Mode, **all three conditions** must be met:
1. **Global config enabled** — the feature is turned on in Admin Panel (e.g., ENABLE\_WEB\_SEARCH )
1. **Model capability enabled** — the model has the capability checked in Workspace > Models (e.g., "Web Search")
1. **Per-chat toggle enabled** — the user has activated the feature for this specific chat via the chat input bar toggles
This means users can disable web search (or image generation, or code interpreter) on a per-conversation basis, even if it's enabled globally and on the model. This is useful for chats where information must stay offline or where you want to prevent unintended tool usage.
Full Agentic Experience
For the best out-of-the-box agentic experience, administrators can enable **Web Search** , **Image Generation** , and **Code Interpreter** as default features for a model. In the **Admin Panel > Settings > Models** , find the **Model Specific Settings** for your target model and toggle these three on under **Default Features** . This ensures they are active in every new chat by default, so users get the full tool-calling experience without manually enabling each toggle. Users can still turn them off per-chat if needed.
Builtin Tools vs File Context
**Builtin Tools** controls whether the model gets *tools* for autonomous retrieval. It does **not** control whether file content is injected via RAG—that's controlled by the separate **File Context** capability.
\* **File Context** = Whether Open WebUI extracts and injects file content (RAG processing)
\* **Builtin Tools** = Whether the model gets tools to autonomously search/retrieve additional content
See [File Context vs Builtin Tools](https://docs.openwebui.com/features/chat-conversations/rag#file-context-vs-builtin-tools) for a detailed comparison.

##### Interleaved Thinking

🧠 When using **Native Mode (Agentic Mode)** , high-tier models can engage in **Interleaved Thinking** . This is a powerful "Thought → Action → Thought → Action → Thought → ..." loop where the model can reason about a task, execute one or more tools, evaluate the results, and then decide on its next move.
Quality Models Required
Interleaved thinking requires models with strong reasoning capabilities. This feature works best with frontier models (GPT-5, Claude 4.5+, Gemini 3+) that can maintain context across multiple tool calls and make intelligent decisions about which tools to use when.
This is fundamentally different from a single-shot tool call. In an interleaved workflow, the model follows a cycle:
1. **Reason** : Analyze the user's intent and identify information gaps.
1. **Act** : Call a tool (e.g., query\_knowledge\_files for internal docs or search\_web and fetch\_url for web research).
1. **Think** : Read the tool's output and update its internal understanding.
1. **Iterate** : If the answer isn't clear, call another tool (e.g., view\_knowledge\_file to read a specific document or fetch\_url to read a specific page) or refine the search.
1. **Finalize** : Only after completing this "Deep Research" cycle does the model provide a final, grounded answer.
This behavior is what transforms a standard chatbot into an **Agentic AI** capable of solving complex, multi-step problems autonomously.

#### 🚀 Summary & Next Steps

Tools bring your AI to life by giving it hands to interact with the world.
\* **Browse Tools** : [openwebui.com/search](https://openwebui.com/search)
\* **Advanced Setup** : Learn more about [MCP Support](https://docs.openwebui.com/features/extensibility/plugin/tools/openapi-servers/mcp)
\* **Development** : [Writing your own Custom Toolkits](https://docs.openwebui.com/features/extensibility/plugin/tools/development)
[Edit this page](https://github.com/open-webui/docs/blob/main/docs/features/extensibility/plugin/tools/index.mdx)
[Previous Tools & Functions (Plugins)](https://docs.openwebui.com/features/extensibility/plugin/)
[Next Development](https://docs.openwebui.com/features/extensibility/plugin/tools/development)
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