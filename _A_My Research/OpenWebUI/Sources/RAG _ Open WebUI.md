---
tags:
  - notebooklm-import
notebook: "OpenWebUI"
category: "research"
---

RAG / Open WebUI
[Skip to main content](https://docs.openwebui.com/troubleshooting/rag#__docusaurus_skipToContent_fallback)
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
\* [Connection Errors](https://docs.openwebui.com/troubleshooting/connection-error)
\* [Reset Admin Password](https://docs.openwebui.com/troubleshooting/password-reset)
\* [Audio](https://docs.openwebui.com/troubleshooting/audio)
\* [RAG](https://docs.openwebui.com/troubleshooting/rag)
\* [SSO & OAuth](https://docs.openwebui.com/troubleshooting/sso)
\* [Web Search](https://docs.openwebui.com/troubleshooting/web-search)
\* [Scaling & HA](https://docs.openwebui.com/troubleshooting/multi-replica)
\* [Performance & RAM](https://docs.openwebui.com/troubleshooting/performance)
\* [Custom CA Store](https://docs.openwebui.com/troubleshooting/custom-ca)
\* [Image Generation](https://docs.openwebui.com/troubleshooting/image-generation)
\* [Manual Migration](https://docs.openwebui.com/troubleshooting/manual-database-migration)
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
\* [🛠 Troubleshooting](https://docs.openwebui.com/troubleshooting/)
\* RAG
On this page

### RAG

Retrieval-Augmented Generation (RAG) enables language models to reason over external content—documents, knowledge bases, and more—by retrieving relevant info and feeding it into the model. When things don't work as expected (e.g., the model "hallucinates" or misses relevant info), it's often not the model's fault—it's a context issue.
This page covers the most common RAG problems and their solutions.

#### Common RAG Issues and How to Fix Them

##### 1. The Model "Can't See" Your Content

This is the most common problem—and it's typically caused by issues during content ingestion. The model doesn't hallucinate because it's wrong; it hallucinates because it was never given the right content in the first place.
**Solution:** Check your content extraction settings.
\* Navigate to: **Admin Settings > Documents** .
\* Make sure you're using a robust content extraction engine such as:
\* Apache Tika
\* Docling
\* Custom extractors (depending on your document types)
tip
Try uploading a document and preview the extracted content. If it's blank or missing key sections, you need to adjust your extractor settings or use a different engine.

##### 2. Only a Small Part of the Document is Being Used

Open WebUI is designed to work with models that have limited context windows by default. For instance, many local models (e.g., Ollama's default models) are limited to 2048 tokens. Because of this, Open WebUI aggressively trims down the retrieved content to fit within the assumed available space.
**Solutions:**
\* Go to **Admin Settings > Documents**
\* Either:
\* **Enable "Bypass Embedding and Retrieval"** — sends full content directly without applying retrieval filters.
\* **Toggle on "Full Context Mode"** — injects more comprehensive content into the model prompt.
warning
Be mindful of context limits—if your model can't handle more tokens, content will still be truncated.

##### 3. Token Limit is Too Short

Even if retrieval works, your model might still not process all the content it receives—because it simply can't.
By default, many models (especially Ollama-hosted LLMs) are limited to a 2048-token context window. That means only a fraction of your retrieved data will actually be used.
**Why Web Search Especially Needs Larger Context Windows:** Web pages are particularly challenging for small context windows because they contain far more content than typical documents. A single web page often includes:
\* Main content (the actual information you want)
\* Navigation menus, headers, and footers
\* Sidebar content and advertisements
\* Comments sections and related links
\* Metadata and embedded scripts
Even after content extraction and cleaning, web pages easily consume 4,000-8,000+ tokens of context. With a 2048-token limit, you're getting less than half the content, often missing the most relevant information that appears later in the page. Even 4096 tokens is frequently insufficient for comprehensive web content analysis.
**Solutions:**
\* **For Ollama Models** : Extend the model's context length:
\* Navigate to: **Admin Panel > Models > Settings** (of the model you want to edit)
\* Go to **Advanced Parameters**
\* Modify the context length (e.g., increase to 8192+ or ideally beyond 16000 tokens if supported by your model)
\* **For OpenAI and Other Integrated Models** : These models typically have their own context limits that cannot be modified through Open WebUI settings. Ensure you're using a model with sufficient context length.
The 2048-token default is a significant limiter for web search. For better RAG results with web content, use at least 8192 tokens, with 16384+ being ideal for complex web pages.
**Alternative:** Use an external LLM with larger context capacity (e.g., GPT-4o, Claude, Gemini with 8k+ context). Comparing results with a large-context model is a good way to isolate whether token limits are the bottleneck.
tip
For web search and complex document analysis, stick with models that support 8192+ token contexts in production use cases.

##### 4. Embedding Model is Low-Quality or Mismatched

Bad embeddings = bad retrieval. If the vector representation of your content is poor, the retriever won't pull the right content—no matter how powerful your LLM is.
**Solution:**
\* Change to a high-quality embedding model (e.g., all-MiniLM-L6-v2, Instructor X, or OpenAI embeddings)
\* Go to: **Admin Settings > Documents**
\* After changing the model, be sure to: After changing the model, **reindex all existing documents** so the new embeddings take effect. Embedding quality directly affects what content is retrieved.

##### 5. 400: 'NoneType' object has no attribute 'encode'

This error indicates a misconfigured or missing embedding model. When Open WebUI tries to create embeddings but doesn't have a valid model loaded, it can't process the text—and the result is this cryptic error.
**Cause:**
\* Your embedding model isn't set up properly.
\* It might not have downloaded completely.
\* Or if you're using an external embedding model, it may not be accessible.
**Solution:**
\* Go to: **Admin Settings > Documents > Embedding Model**
\* Save the embedding model again—even if it's already selected. This forces a recheck/download.
\* If you're using a remote/external embedding tool, make sure it's running and accessible to Open WebUI.
tip
After fixing the configuration, try re-embedding a document and verify no error is shown in the logs.

##### 6. Upload Limits and Restrictions

Open WebUI implements various limits to ensure system stability and prevent abuse. It is important to understand how these limits apply to different upload methods:
\* **Chat Uploads:** Subject to global file size and count limits.
\* **Max File Size:** Controlled by RAG\_FILE\_MAX\_SIZE (default: Unlimited). Configurable in **Admin Panel > Settings > Documents > General > Max Upload Size** .
\* **Max File Count:** Controlled by RAG\_FILE\_MAX\_COUNT (default: Unlimited). Configurable in **Admin Panel > Settings > Documents > General > Max Upload Count** .
\* **Allowed File Extensions:** Controlled by RAG\_ALLOWED\_FILE\_EXTENSIONS (default: All). Configurable in **Admin Panel > Settings > Documents > General > Allowed File Extensions** .
\* **Folder Uploads:** Subject to the FOLDER\_MAX\_FILE\_COUNT [environment variable](https://docs.openwebui.com/reference/env-configuration/#folder_max_file_count) (defaults to 100). This limit applies to the number of files directly associated with a folder.
\* **Knowledge Base Uploads:**
\* **File Limit:** Subject to the same RAG\_FILE\_MAX\_SIZE limit as chats, but **not** subject to the RAG\_FILE\_MAX\_COUNT limit, allowing for unlimited file uploads.
\* **RAG Enforcement:** All files uploaded to a Knowledge Base are automatically indexed. However, similar to chat uploads, Knowledge Bases can also be used in **Full Context Mode** (accessible in chat settings), which feeds the full document content to the model instead of using vector search retrieval.
info
By separating these limits, administrators can better manage resource usage across different features. For example, you might want to allow larger uploads in a curated Knowledge Base while restricting the number of files in ad-hoc Folder uploads.

##### 7. Fragmented or Tiny Chunks

When using the **Markdown Header Splitter** , documents can sometimes be split into very small fragments (e.g., just a table of contents entry or a short sub-header). These tiny chunks often lack enough semantic context for the embedding model to represent them accurately, leading to poor RAG results and unnecessary overhead.
**Solution:**
\* Go to **Admin Settings > Documents** .
\* Increase the **Chunk Min Size Target** .
\* Setting this to a value like 1000 (or ~50-60% of your CHUNK\_SIZE ) merges small fragments with neighboring chunks, resulting in better semantic coherence and fewer total chunks.

##### 8. Slow Follow-up Responses (KV Cache Invalidation)

If your initial response is fast but follow-up questions become increasingly slow, you are likely experiencing **KV Cache invalidation** .
**The Problem** : By default, Open WebUI injects RAG context into the **user message** . As the chat progresses, new messages shift the position of this context, forcing models (like Ollama, llama.cpp, or vLLM) and cloud providers (like OpenAI or Vertex AI) to re-process the entire context for every turn.
**Solution:**
\* Set the environment variable RAG\_SYSTEM\_CONTEXT=True .
\* This injects the RAG context into the **system message** , which stays at a fixed position at the start of the conversation.
\* This allows providers to effectively use **KV prefix caching** or **Prompt Caching** , resulting in nearly instant follow-up responses even with large documents.

| Problem | Fix |
| --- | --- |
| 🤔 Model can't "see" content | Check document extractor settings |
| 🧹 Only part of content used | Enable Full Context Mode or Bypass Embedding |
| ⏱ Limited by 2048 token cap | Increase model context length or use large-context LLM |
| 📉 Inaccurate retrieval | Switch to a better embedding model, then reindex |
| ❌ Upload limits bypass | Use Folder uploads (with FOLDER\_MAX\_FILE\_COUNT ); Knowledge Base limits are separate |
| 🧩 Fragmented/Tiny Chunks | Increase **Chunk Min Size Target** to merge small sections |
| 🐌 Slow follow-up responses | Enable RAG\_SYSTEM\_CONTEXT=True to fix KV cache invalidation |
| 📄 API returns "empty content" | Wait for file processing to complete before adding to knowledge base |
| 💥 CUDA OOM during embedding | Reduce batch size, isolate GPU, or restart container |
| 📷 PDF images not extracted | Use Tika/Docling, enable OCR, or update pypdf |
| 💀 Worker dies during upload (instant) | Switch away from default ChromaDB (SQLite) in multi-worker setups |
| 💀 Worker dies during upload (timeout) | Update Open WebUI, or increase --timeout-worker-healthcheck |
| 🧠 Model ignores attached KB | Enable Builtin Tools, add system prompt hints, or disable native function calling |

##### 9. API File Upload: "The content provided is empty" Error

When uploading files via the API and immediately adding them to a knowledge base, you may encounter:

```
400: The content provided is empty. Please ensure that there is text or data present before proceeding.
```

**The Problem** : This is a **race condition** , not an actual empty file. By default, file uploads are processed asynchronously—the upload endpoint returns immediately with a file ID while content extraction and embedding computation happen in the background. If you try to add the file to a knowledge base before processing completes, the system sees empty content.
✅ **Solution: Wait for Processing to Complete**
Before adding a file to a knowledge base, poll the status endpoint until processing is done:

```
import requests
import time

def wait_for_processing(token, file_id, timeout=300):
    url = f'http://localhost:3000/api/v1/files/{file_id}/process/status'
    headers = {'Authorization': f'Bearer {token}'}
    
    start_time = time.time()
    while time.time() - start_time < timeout:
        response = requests.get(url, headers=headers)
        status = response.json().get('status')
        
        if status == 'completed':
            return True
        elif status == 'failed':
            raise Exception(f"Processing failed: {response.json().get('error')}")
        
        time.sleep(2)  # Poll every 2 seconds
    
    raise TimeoutError("File processing timed out")
```

**Status Values:**

| Status | Meaning |
| --- | --- |
| pending | Still processing |
| completed | Ready to add to knowledge base |
| failed | Processing failed (check error field) |

tip
For complete API workflow examples including proper status checking, see the [API Endpoints documentation](https://docs.openwebui.com/reference/api-endpoints#checking-file-processing-status).

##### 10. CUDA Out of Memory During Embedding

When processing large files or many files in sequence, you may encounter CUDA OOM errors like:

```
CUDA out of memory. Tried to allocate X MiB. GPU has a total capacity of Y GiB of which Z MiB is free.
```

**Common Causes:**
\* Embedding model competing with chat model for GPU memory
\* PyTorch memory fragmentation from repeated small allocations
\* Large documents creating memory spikes during embedding
✅ **Solutions:**
1. **Isolate Embedding to a Different GPU** (if available): Set CUDA\_VISIBLE\_DEVICES to pin embedding to a specific GPU separate from your chat model.
1. **Reduce Embedding Batch Size** : Lower RAG\_EMBEDDING\_BATCH\_SIZE (e.g., from 32 to 8 or 4) to reduce peak memory usage.
1. **Enable Expandable Segments** : Set the environment variable to reduce fragmentation:

```
PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
```

```
1.  **Restart Between Large Ingestion Jobs** : If memory fragmentation builds up, restart the Open WebUI container to clear CUDA contexts.
1.  **Use Smaller Embedding Models** : Consider using lighter embedding models for bulk ingestion, then switch to higher-quality models for production queries.
1.  **Separate Ingestion from Chat** : Don't run the chat model during large ingestion jobs. Load the chat model after embeddings finish.
```

##### 10b. 429 Rate Limit Errors During Embedding

When using a **remote/external embedding provider** (OpenAI, Azure OpenAI, etc.) with [ENABLE\_ASYNC\_EMBEDDING](https://docs.openwebui.com/reference/env-configuration#enable_async_embedding) enabled, you may see HTTP 429 "Too Many Requests" errors in the logs during bulk document ingestion:

```
Error generating embeddings: 429 Rate limit reached
```

**The Problem** : With async embedding enabled, Open WebUI sends embedding requests concurrently. If you're ingesting many documents or large documents at once, this can easily exceed your provider's API rate limits — especially on free-tier or lower-tier plans.
✅ **Solutions:**
1. **Limit Concurrent Embedding Requests** : Set [RAG\_EMBEDDING\_CONCURRENT\_REQUESTS](https://docs.openwebui.com/reference/env-configuration#rag_embedding_concurrent_requests) to cap the number of simultaneous embedding API calls. For example, set it to 5 or 10 depending on your provider's rate limits:

```
# docker-compose.yaml
environment:
  RAG_EMBEDDING_CONCURRENT_REQUESTS: 5
```

Or configure it in the **Admin Panel > Settings > Documents > Concurrent Requests** field. The default of 0 means unlimited concurrency. 2. **Reduce Batch Size** : Lower [RAG\_EMBEDDING\_BATCH\_SIZE](https://docs.openwebui.com/reference/env-configuration#rag_embedding_batch_size) to send fewer texts per API call. 3. **Disable Async Embedding** : If rate limits remain an issue, set ENABLE\_ASYNC\_EMBEDDING to False to process embeddings sequentially (slower but avoids rate limit pressure).

##### 11. PDF OCR Not Extracting Text from Images

If PDFs containing images with text are returning empty content:
**The Problem** : The default "pypdf" content extractor may struggle with certain PDF formats, especially those containing primarily image-based content.
✅ **Solutions:**
1. **Use a Different Content Extraction Engine** :
\* Navigate to **Admin Settings > Documents**
\* Try **Apache Tika** or **Docling** for better OCR support
1. **Enable PDF Image Extraction** :
\* In **Admin Settings > Documents** , ensure **PDF Extract Images (OCR)** is enabled
1. **Update pypdf** (if using the default engine): Recent pypdf releases (6.0.0+) have improved handling of various PDF formats
1. **Check for Corrupted PDFs** : Verify the PDF opens correctly in a standard PDF viewer before uploading

##### 12. Worker Dies During Document Upload

When uploading documents in a **multi-worker** deployment, you may see:

```
INFO:     Waiting for child process [12]
INFO:     Child process [12] died
```

There are **two distinct causes** for this in multi-worker setups:

###### Cause A: ChromaDB SQLite + Fork (Instant Crash)

If you are using the **default ChromaDB** vector database (which uses a local SQLite-backed PersistentClient ) with UVICORN\_WORKERS > 1 , the crash is caused by SQLite being **not fork-safe** . When uvicorn forks multiple workers, each process inherits the same SQLite database connection. Concurrent writes to the vector database from multiple workers cause an immediate crash — not a timeout, but an instant fatal error.
You will typically see this pattern all within the same second:

```
save_docs_to_vector_db:1619 - adding to collection file-id
INFO:     Waiting for child process [pid]
INFO:     Child process [pid] died
```

**Solution:** You **must** switch away from the default local ChromaDB when using multiple workers:
\* Set [VECTOR\_DB](https://docs.openwebui.com/reference/env-configuration#vector_db) to pgvector , mariadb-vector , milvus , or qdrant
\* Or run ChromaDB as a separate HTTP server and set [CHROMA\_HTTP\_HOST](https://docs.openwebui.com/reference/env-configuration#chroma_http_host) / [CHROMA\_HTTP\_PORT](https://docs.openwebui.com/reference/env-configuration#chroma_http_port)
See the [Scaling & HA guide](https://docs.openwebui.com/troubleshooting/multi-replica#6-worker-crashes-during-document-upload-chromadb--multi-worker) for full details.

###### Cause B: SentenceTransformers Health Check Timeout (Older Versions)

When using the **default SentenceTransformers** embedding engine (local embeddings) with multiple workers, uvicorn monitors worker health via periodic pings. The default health check timeout is just **5 seconds** . In older versions of Open WebUI, the embedding call blocked the event loop entirely — preventing the worker from responding to health checks. Uvicorn then killed the worker as unresponsive.
note
This issue was **fixed** in Open WebUI. The embedding system now uses run\_coroutine\_threadsafe to keep the main event loop responsive during embedding operations, so workers will no longer be killed during uploads regardless of how long embeddings take.
If you are running a version with this fix and still experiencing worker death, check **Cause A** above (ChromaDB SQLite) first, then ensure your Open WebUI is up to date.
**Who is affected:**
\* Only deployments using the **default SentenceTransformers** embedding engine (local embeddings).
\* Only when running **multiple uvicorn workers** . Single-worker deployments don't have health check timeouts.
\* External embedding engines (Ollama, OpenAI, Azure OpenAI) are **not affected** since their API calls don't block the event loop.
✅ **Solutions (for older versions without the fix):**
1. **Update Open WebUI** to a version that includes the run\_coroutine\_threadsafe fix.
1. **Increase the health check timeout** as a workaround:

```
# docker-compose.yaml
command: ["bash", "start.sh", "--workers", "2", "--timeout-worker-healthcheck", "120"]
```

```
1.  **Switch to an external embedding engine**  to avoid local blocking entirely:
```

```
RAG_EMBEDDING_ENGINE=ollama
RAG_EMBEDDING_MODEL=nomic-embed-text
```

```
1.  **Optionally set a safety timeout**  via [RAG_EMBEDDING_TIMEOUT](https://docs.openwebui.com/reference/env-configuration#rag_embedding_timeout) to abort abnormally long embedding operations (does not affect health checks).
```

##### 13. Knowledge Base Attached to Model Not Working

You attached a knowledge base to a model in **Workspace > Models > Edit** , but when you chat with the model it doesn't seem to know about the knowledge base content at all.
**The Problem** : Open WebUI has two distinct RAG modes, and they handle model-attached knowledge bases very differently:

| Mode | How Knowledge Works |
| --- | --- |
| **Default (non-native)** | Open WebUI automatically performs RAG — it queries the attached knowledge base, retrieves relevant chunks, and injects them into the conversation context. This happens behind the scenes without the model doing anything. |
| **Native Function Calling** | Knowledge is **not auto-injected** . Instead, the model receives tools (like query\_knowledge\_bases ) and must actively decide to call them. This is **agentic RAG** — the model autonomously searches when it determines it needs information. |

If you have **Native Function Calling enabled** , the model needs both the **ability** and the **instruction** to use the knowledge tools.

###### Knowledge Retrieval Behavior Matrix

|  | **KB Attached to Model** | **No KB Attached** |
| --- | --- | --- |
| **Default Mode** | Open WebUI auto-injects RAG results from the **attached KB(s) only** | No automatic RAG — user must manually add a knowledge base to the chat via # |
| **Native Function Calling** | Model receives tools scoped to **attached KB(s) only** — must actively call them | Model receives tools with access to **all accessible KBs** (if Builtin Tools enabled) — must actively call them |

Key takeaway: in default mode, attaching a KB enables automatic RAG scoped to those KBs. In native mode, the model must use its tools regardless — attaching a KB only restricts *which* KBs are searchable.
Preventing Knowledge Base Access in Native Mode
If you want to prevent a model from accessing **any** knowledge base in native mode, you don't need to disable Builtin Tools entirely. Instead, disable only the **Knowledge Base** category in **Workspace > Models > Edit > Builtin Tools** . This removes all knowledge-related tools while keeping other builtin tools (web search, memory, notes, etc.) active. See [Granular Builtin Tool Categories](https://docs.openwebui.com/features/extensibility/plugin/tools#granular-builtin-tool-categories-per-model) for the full list of categories.
✅ **Solutions (check in order):**
1. **Check Global Model Settings first** :
\* Go to **Admin Panel > Settings > Models > ⚙ (gear icon)**
\* Expand **Model Parameters** and check if **Function Calling** is set to native
\* If it is, this **overrides all models** that don't explicitly set their own function\_calling parameter — even if you never intended for a specific model to use native mode
\* Either change the global setting to default , or explicitly set function\_calling in the per-model **Advanced Params** to override the global value
\* Also check the **Model Capabilities** section — if **File Context** is disabled globally, RAG won't process files for any model that doesn't explicitly enable it
Global Settings Override
The most common cause of this issue is a global Function Calling: native setting in **Admin Panel > Settings > Models > ⚙ > Model Parameters** . This silently applies to **every model** that doesn't explicitly set its own function\_calling parameter. Per-model settings in **Workspace > Models > Edit > Advanced Params** will override the global default, but only if explicitly set — a model that simply doesn't have function\_calling configured will inherit the global value.
1. **Ensure Built-in Tools are enabled for the model** (if using native mode):
\* Go to **Workspace > Models > Edit** for your model
\* Under **Builtin Tools** , make sure the **Knowledge Base** category is enabled (it is by default)
\* If this is disabled, the model has no way to query attached knowledge bases
1. **Add a system prompt hint** (if using native mode):
\* Some models need explicit guidance to use their tools. Add something like: "When users ask questions, first use list\_knowledge\_bases to see what knowledge is available, then use query\_knowledge\_bases to search for relevant information before answering."
1. **Or disable Native Function Calling** for that model:
\* In the model settings, disable Native Function Calling to restore the classic auto-injection RAG behavior from earlier versions
1. **Or use Full Context mode** :
\* Click on the attached knowledge base and select **"Use Entire Document"**
\* This bypasses RAG entirely and always injects the full content, regardless of native function calling settings
Why the Change?
Open WebUI is moving toward **agentic RAG** , where the model autonomously decides when and how to search knowledge bases. This is more powerful than classic RAG because the model can retry searches with different queries if the first attempt didn't yield good results. However, it does require models that are capable of using tools effectively. For smaller or older models that struggle with tool calling, disabling Native Function Calling is the recommended approach.
For the full explanation of how knowledge scoping and retrieval modes work, see the [Knowledge documentation](https://docs.openwebui.com/features/workspace/knowledge#agentic-knowledge-tools) and [File Context vs Builtin Tools](https://docs.openwebui.com/features/chat-conversations/rag#file-context-vs-builtin-tools).
By optimizing these areas—extraction, embedding, retrieval, and model context—you can dramatically improve how accurately your LLM works with your documents.
[Edit this page](https://github.com/open-webui/docs/blob/main/docs/troubleshooting/rag.mdx)
[Previous Audio](https://docs.openwebui.com/troubleshooting/audio)
[Next SSO & OAuth](https://docs.openwebui.com/troubleshooting/sso)
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