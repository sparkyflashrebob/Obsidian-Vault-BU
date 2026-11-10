---
tags:
  - notebooklm-import
notebook: "OpenWebUI"
category: "research"
---

Knowledge / Open WebUI
[Skip to main content](https://docs.openwebui.com/features/workspace/knowledge#__docusaurus_skipToContent_fallback)
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
\* [💬 Chat & Conversations](https://docs.openwebui.com/features/workspace/knowledge)
\* [🧠 Workspace](https://docs.openwebui.com/features/workspace/knowledge)
\* [Models](https://docs.openwebui.com/features/workspace/models)
\* [Prompts](https://docs.openwebui.com/features/workspace/prompts)
\* [Knowledge](https://docs.openwebui.com/features/workspace/knowledge)
\* [Skills](https://docs.openwebui.com/features/workspace/skills)
\* [📝 Notes](https://docs.openwebui.com/features/notes/)
\* [📢 Channels](https://docs.openwebui.com/features/channels/)
\* [💻 Open Terminal](https://docs.openwebui.com/features/open-terminal/)
\* [🔌 Plugins & Extensibility](https://docs.openwebui.com/features/extensibility/)
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
\* 🧠 Workspace
\* Knowledge
On this page

### 📚 Knowledge

**Give your AI access to your documents and let it find what matters.**
Knowledge is where you store the files and collections that your AI can search, read, and reason over. Upload PDFs, spreadsheets, code, or any text-based document. Build collections around projects, teams, or topics. When a model needs an answer, it pulls from your knowledge base instead of guessing.
Unlike [Notes](https://docs.openwebui.com/features/notes), which inject full content into every message, Knowledge uses retrieval (RAG) to find the relevant chunks on demand. This makes it the right choice for large document sets where injecting everything would exceed the context window.

#### Why Knowledge?

##### Your documents become searchable by AI

Upload a folder of contracts, technical specs, or research papers. The AI searches them by meaning, not just keywords, and cites where it found the answer.

##### Two retrieval modes for different needs

Choose **Focused Retrieval** (RAG) to let the AI search large collections efficiently, or **Full Context** to inject an entire document word-for-word when precision matters.

##### Autonomous exploration with native function calling

With [native function calling](https://docs.openwebui.com/features/extensibility/plugin/tools#tool-calling-modes-default-vs-native) enabled, models don't just search. They browse your knowledge bases, read files page by page, and synthesize across multiple documents without manual prompting.

##### Scoped access keeps things organized

Attach specific knowledge bases to a model so it only searches what's relevant. Or leave it unscoped and let the model discover everything the user has access to.

#### Key Features

|  |  |
| --- | --- |
| 📄 **9 vector databases** | ChromaDB, PGVector, Qdrant, Milvus, OpenSearch, Elasticsearch, and more |
| 🔍 **Hybrid search** | BM25 keyword search + vector search with cross-encoder reranking |
| 📑 **5 extraction engines** | Tika, Docling, Azure, Mistral OCR, custom loaders |
| 🤖 **Agentic retrieval** | Models browse, search, and read your documents autonomously |
| 📄 **Full context mode** | Inject entire documents with no chunking |
| 📦 **Export and API** | Back up knowledge bases as zip files, manage via REST API |

#### Retrieval Modes

When attaching files or knowledge bases to a model, click on the attached item to toggle between modes:

##### 🔍 Focused Retrieval (default)

Uses RAG to find and inject the most relevant chunks based on the user's query. When hybrid search is enabled ( ENABLE\_RAG\_HYBRID\_SEARCH ), retrieval combines BM25 keyword search with vector search, plus reranking for accuracy.
Best for large document sets where only specific sections are relevant.

##### 📄 Full Context

Injects the complete content of the file into every message. No chunking, no semantic search. Always injected regardless of native function calling settings, so the model doesn't need to call any tools to access it.
Best for short reference documents, style guides, or context that's always relevant.

#### Agentic Knowledge Tools

With [native function calling](https://docs.openwebui.com/features/extensibility/plugin/tools#tool-calling-modes-default-vs-native) enabled, models interact with your knowledge bases using built-in tools. Which tools appear depends on whether specific knowledge is attached to the model:

| Tool | Attached KB | No KB attached | Description |
| --- | --- | --- | --- |
| list\_knowledge | ✅ | ❌ | List all KBs, files, and notes attached to the model |
| list\_knowledge\_bases | ❌ | ✅ | Browse available knowledge bases with file counts |
| search\_knowledge\_bases | ❌ | ✅ | Find knowledge bases by name or description |
| query\_knowledge\_bases | ❌ | ✅ | Search KB names/descriptions by semantic similarity |
| search\_knowledge\_files | ✅ (scoped) | ✅ (all) | Search files by filename |
| query\_knowledge\_files | ✅ (scoped) | ✅ | Search file contents using the RAG pipeline |
| view\_file | ✅ | ❌ | Read file content with pagination (default 10K chars, cap 100K) |
| view\_knowledge\_file | ✅ | ✅ | Read file content from any accessible KB |
| view\_note | ✅ | ❌ | Read attached notes |

The key split: list\_knowledge and list\_knowledge\_bases are mutually exclusive. Attaching a KB scopes the model to only those documents. Leaving it unscoped lets the model discover everything the user has access to.
Autonomous exploration works best with frontier models that can intelligently chain search, browse, and synthesize. Smaller models may struggle with multi-step retrieval. Administrators can disable the **Knowledge Base** tool category per-model in **Workspace > Models > Edit > Builtin Tools** .
For the full list of built-in agentic tools, see the [Native/Agentic Mode Tools Guide](https://docs.openwebui.com/features/extensibility/plugin/tools#built-in-system-tools-nativeagentic-mode).
Knowledge is NOT auto-injected with native function calling
When native function calling is enabled, attached knowledge is **not automatically injected** . The model must call the knowledge tools to search and retrieve. If your model isn't using attached knowledge:
1. **Add system prompt instructions** telling the model to use list\_knowledge and query\_knowledge\_files .
1. **Disable native function calling** for that model to restore automatic RAG injection.
1. **Switch to Full Context mode** for the attachment to bypass RAG entirely.

#### Setting Up a Knowledge Base

```
1. Click  **Workspace**  in the sidebar, then select  **Knowledge** .
1. Click  **+ New Knowledge**  and give it a name and description.
1. Upload files or add existing documents.
1. Attach the knowledge base to a model in  **Workspace > Models > Edit** , or reference it in chat with # .
```

##### Exporting

Admins can export an entire knowledge base as a zip file via the item menu (three dots) > **Export** . Files are converted to .txt for universal compatibility. Regular users will not see the Export option.

##### API access

Knowledge bases can be managed programmatically:
\* POST /api/v1/files/ - Upload files
\* GET /api/v1/files/{id}/process/status - Check processing status
\* POST /api/v1/knowledge/{id}/file/add - Add files to a knowledge base
File processing happens asynchronously. You must poll the status endpoint until processing completes before adding files to a knowledge base, or you'll get an "empty content" error. See [API Endpoints](https://docs.openwebui.com/reference/api-endpoints#-retrieval-augmented-generation-rag) for workflow examples.

#### Use Cases

##### Project documentation

Upload your team's technical specs, architecture docs, and runbooks into a knowledge base. Attach it to a "Project Assistant" model. The AI answers questions grounded in your actual documentation instead of generic training data.

##### Legal and compliance review

Load contracts, policies, and regulatory documents. Ask the AI to find specific clauses, compare terms across agreements, or flag inconsistencies.

##### Research synthesis

Add dozens of papers to a knowledge base. The AI searches across all of them to answer questions, find supporting evidence, or identify contradictions between studies.

#### Limitations

##### Context window with Full Context mode

"Using Entire Document" injects the full text. A large document attached to a model with a small context window will crowd out conversation history.

##### Processing delay for API uploads

Files uploaded via API are processed asynchronously. Attempting to use a file before processing completes will fail silently or return empty results.

##### Native function calling changes behavior

Enabling native function calling changes how knowledge bases work. If your KB suddenly stops producing results, check whether function\_calling: native was set in global model defaults. See [Knowledge Base troubleshooting](https://docs.openwebui.com/troubleshooting/rag#13-knowledge-base-attached-to-model-not-working) for details.
[Edit this page](https://github.com/open-webui/docs/blob/main/docs/features/workspace/knowledge.md)
[Previous Prompts](https://docs.openwebui.com/features/workspace/prompts)
[Next Skills](https://docs.openwebui.com/features/workspace/skills)
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