---
tags:
  - notebooklm-import
notebook: "OpenWebUI"
category: "research"
---

Performance & RAM / Open WebUI
[Skip to main content](https://docs.openwebui.com/troubleshooting/performance#__docusaurus_skipToContent_fallback)
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
\* Performance & RAM
On this page

### Optimization, Performance & RAM Usage

This guide provides a comprehensive overview of strategies to optimize Open WebUI. Your ideal configuration depends heavily on your specific deployment goals. Consider which of these scenarios describes you best:
1. **Maximum Privacy on Weak Hardware (e.g., Raspberry Pi)** :
\* *Goal* : keep everything local; minimize resource usage.
\* *Trade-off* : You must use lightweight local models (SentenceTransformers) and disable heavy features to prevent crashes.
1. **Maximum Quality for Single User (e.g., Desktop)** :
\* *Goal* : Best possible experience with high speed and quality.
\* *Strategy* : Leverage external APIs (OpenAI/Anthropic) for embeddings and task models to offload compute from your local machine.
1. **High Scale for Many Users (e.g., Enterprise/Production)** :
\* *Goal* : Stability and concurrency.
\* *Strategy* : Requires dedicated Vector DBs (Milvus/Qdrant), increased thread pools, caching to handle load, and **PostgreSQL** instead of SQLite.

#### ⚡ Performance Tuning (Speed & Responsiveness)

If Open WebUI feels slow or unresponsive, especially during chat generation or high concurrency, specialized optimizations can significantly improve the user experience.

##### 1. Dedicated Task Models

By default, Open WebUI automates background tasks like title generation, tagging, and autocomplete. These run in the background and can slow down your main chat model if they share the same resources.
**Recommendation** : Use a **very fast, small, and cheap NON-REASONING model** for these tasks. Avoid using large reasoning models (like o1, r1, or Claude) as they are too slow and expensive for simple background tasks.
**Configuration:** There are two separate settings in **Admin Panel > Settings > Interface** . The system intelligently selects which one to use based on the model you are currently chatting with:
\* **Task Model (External)** : Used when you are chatting with an external model (e.g., OpenAI).
\* **Task Model (Local)** : Used when you are chatting with a locally hosted model (e.g., Ollama).
**Best Options (2025):**
\* **External/Cloud** : gpt-5-nano , gemini-2.5-flash-lite , llama-3.1-8b-instant (OpenAI/Google/Groq/OpenRouter).
\* **Local** : qwen3:1b , gemma3:1b , llama3.2:3b .

##### 2. Caching & Latency Optimization

Configure these settings to reduce latency and external API usage.

###### Model Caching

Drastically reduces startup time and API calls to external providers.
Important for OpenRouter and Multi-Model Providers
If you are using **OpenRouter** or any provider with hundreds/thousands of models, enabling model caching is **highly recommended** . Without caching, initial page loads can take **10-15+ seconds** as the application queries all available models. Enabling the cache reduces this to near-instant.
\* **Admin Panel** : Settings > Connections > Cache Base Model List
\* **Env Var** : ENABLE\_BASE\_MODELS\_CACHE=True
\* *Note* : Caches the list of models in memory. Only refreshes on App Restart or when clicking **Save** in Connections settings.
\* **Env Var** : MODELS\_CACHE\_TTL=300
\* *Note* : Sets a 5-minute cache for external API responses.

###### Search Query Caching

Reuses the LLM-generated Web-Search search queries for RAG search within the same chat turn. This prevents redundant LLM calls when multiple retrieval features act on the same user prompt.
\* **Env Var** : ENABLE\_QUERIES\_CACHE=True
\* *Note* : If enabled, the same search query will be reused for RAG instead of generating new queries for RAG, saving on inference cost and API calls, thus improving performance.

###### KV Cache Optimization (RAG Performance)

Drastically improves the speed of follow-up questions when chatting with large documents or knowledge bases.
\* **Env Var** : RAG\_SYSTEM\_CONTEXT=True
\* **Effect** : Injects RAG context into the **system message** instead of the user message.
\* **Why** : Many LLM engines (like Ollama, llama.cpp, vLLM) and cloud providers (OpenAI, Vertex AI) support **KV prefix caching** or **Prompt Caching** . System messages stay at the start of the conversation, while user messages shift position each turn. Moving RAG context to the system message ensures the cache remains valid, leading to **near-instant follow-up responses** instead of re-processing large contexts every turn.

#### 📦 Database Optimization

For high-scale deployments, your database configuration is the single most critical factor for stability.

##### PostgreSQL (Mandatory for Scale)

For any multi-user or high-concurrency setup, **PostgreSQL is mandatory** . SQLite (the default) is not designed for high concurrency and will become a bottleneck (database locking errors).
\* **Variable** : DATABASE\_URL
\* **Example** : postgres://user:password@localhost:5432/webui

##### Chat Saving Strategy

By default, Open WebUI saves chats **after generation is complete** . While saving in real-time (token by token) is possible, it creates massive database write pressure and is **strongly discouraged** .
\* **Env Var** : ENABLE\_REALTIME\_CHAT\_SAVE=False (Default)
\* **Effect** : Chats are saved only when the generation is complete (or periodically).
\* **Recommendation** : **DO NOT ENABLE ENABLE\_REALTIME\_CHAT\_SAVE in production.** It is highly recommended to keep this False to prevent database connection exhaustion and severe performance degradation under concurrent load. See the [Environment Variable Configuration](https://docs.openwebui.com/reference/env-configuration#enable_realtime_chat_save) for details.

##### Database Session Sharing

Starting with v0.7.1, Open WebUI includes a database session sharing feature that can improve performance under high concurrency by reusing database sessions instead of creating new ones for each request.
\* **Env Var** : DATABASE\_ENABLE\_SESSION\_SHARING
\* **Default** : False
Recommendations by Database Type
\* **SQLite:** Keep this setting **disabled** (default). Enabling session sharing on SQLite with limited hardware resources may cause severe performance degradation or timeouts.
\* **PostgreSQL with adequate resources:** Consider **enabling** this setting for improved performance, especially in multi-user or high-concurrency deployments.
Low-Spec Hardware
If you upgraded to v0.7.0 and experienced slow admin page loads, API timeouts, or unresponsive UI, this was likely caused by database session sharing being enabled. Ensure DATABASE\_ENABLE\_SESSION\_SHARING=False on low-spec hardware (Raspberry Pi, containers with limited CPU allocation like 250m or less).

##### Connection Pool Sizing

For high-concurrency PostgreSQL deployments, the default connection pool settings may be insufficient. If you experience QueuePool limit reached errors or connection timeouts, increase the pool size:
\* **Env Var** : DATABASE\_POOL\_SIZE=15 (default: uses SQLAlchemy defaults)
\* **Env Var** : DATABASE\_POOL\_MAX\_OVERFLOW=20 (default: 0)
**Important:** The combined total ( DATABASE\_POOL\_SIZE + DATABASE\_POOL\_MAX\_OVERFLOW ) should remain well below your database's max\_connections limit. PostgreSQL defaults to 100 max connections, so keep the combined total under 50-80 per Open WebUI instance to leave room for other clients and maintenance operations.

##### Vector Database (RAG)

For multi-user setups, the choice of Vector DB matters.
\* **ChromaDB (Default)** : **NOT SAFE** for multi-worker ( UVICORN\_WORKERS > 1 ) or multi-replica deployments. The default ChromaDB configuration uses a local PersistentClient backed by **SQLite** . SQLite connections are not fork-safe — when uvicorn forks multiple workers, each process inherits the same database connection, and concurrent writes cause instant worker crashes ( Child process died ) or database corruption. This is a fundamental SQLite limitation, not a bug. See the [Scaling & HA troubleshooting guide](https://docs.openwebui.com/troubleshooting/multi-replica#6-worker-crashes-during-document-upload-chromadb--multi-worker) for the full crash sequence and solutions.
\* **Recommendations** :
\* **Milvus** or **Qdrant** : Best for improved scale and performance. These are client-server databases, inherently safe for multi-process access.
\* **PGVector** : Excellent choice if you are already using PostgreSQL. Also fully multi-process safe.
\* **ChromaDB HTTP mode** : If you want to keep using ChromaDB, run it as a [separate server](https://docs.openwebui.com/reference/env-configuration#chroma_http_host) so Open WebUI connects via HTTP instead of local SQLite.
\* **Multitenancy** : If using Milvus or Qdrant, enabling multitenancy offers better resource sharing.
\* ENABLE\_MILVUS\_MULTITENANCY\_MODE=True
\* ENABLE\_QDRANT\_MULTITENANCY\_MODE=True

##### Content Extraction Engine

Default Content Extractor Causes Memory Leaks
The **default content extraction engine** uses Python libraries including **pypdf** , which are known to have **persistent memory leaks** during document ingestion. In production deployments with regular document uploads, this will cause Open WebUI's memory usage to grow continuously until the process is killed or the container is restarted.
This is the **#1 cause of unexplained memory growth** in production deployments.
**Recommendation** : Switch to an external content extraction engine for any deployment that processes documents regularly:

| Engine | Best For | Configuration |
| --- | --- | --- |
| **Apache Tika** | General-purpose, widely used, handles most document types | CONTENT\_EXTRACTION\_ENGINE=tika + TIKA\_SERVER\_URL=http://tika:9998 |
| **Docling** | High-quality extraction with layout-aware parsing | CONTENT\_EXTRACTION\_ENGINE=docling |
| **External Loader** | Recommended for production and custom extraction pipelines | CONTENT\_EXTRACTION\_ENGINE=external + EXTERNAL\_DOCUMENT\_LOADER\_URL=... |

Using an external extractor moves the memory-intensive parsing out of the Open WebUI process entirely, eliminating this class of memory leaks.

##### Embedding Engine

SentenceTransformers at Scale
The **default SentenceTransformers** embedding engine (all-MiniLM-L6-v2) loads a machine learning model into the Open WebUI process memory. While lightweight enough for personal use, at scale this model:
\* **Consumes significant RAM** (~500MB+ per worker process)
\* **Blocks the event loop** during embedding operations on older versions
\* **Multiplies with workers** — each Uvicorn worker loads its own copy of the model
For multi-user or production deployments, **offload embeddings to an external service** .
\* **Recommended** : Use RAG\_EMBEDDING\_ENGINE=openai (for cloud embeddings via OpenAI, Azure, or compatible APIs) or RAG\_EMBEDDING\_ENGINE=ollama (for self-hosted embedding via Ollama with models like nomic-embed-text ).
\* **Env Var** : RAG\_EMBEDDING\_ENGINE=openai
\* **Effect** : The embedding model is no longer loaded into the Open WebUI process, freeing hundreds of MB of RAM per worker.

##### Optimizing Document Chunking

The way your documents are chunked directly impacts both storage efficiency and retrieval quality.
\* **Use Markdown Header Splitting** : This preserves the semantic structure of your documents.
\* **Set a Chunk Min Size Target** : When using the markdown header splitter, tiny chunks (e.g., just a single sub-header) can be created. These are inefficient to store and poor for retrieval.
\* **Env Var** : CHUNK\_MIN\_SIZE\_TARGET=1000 (Example value)
\* **Benefit** : Intelligently merges small chunks with neighbors, significantly reducing the total vector count and improving RAG performance.

#### 📈 Scaling Infrastructure (Multi-Tenancy & Kubernetes)

If you are deploying for **enterprise scale** (hundreds of users), simple Docker Compose setups may not suffice. You will need to move to a clustered environment.
For a step-by-step walkthrough of the entire scaling journey (PostgreSQL, Redis, vector DB, storage, observability), see the **Scaling Open WebUI** guide.
\* **Kubernetes / Helm** : For deploying on K8s with multiple replicas, see the **Multi-Replica & High Availability Guide** .
\* **Redis (Mandatory)** : When running multiple workers ( UVICORN\_WORKERS > 1 ) or multiple replicas, **Redis is required** to handle WebSocket connections and session syncing. See **Redis Integration** .
\* **Load Balancing** : Ensure your Ingress controller supports **Session Affinity** (Sticky Sessions) for best performance.
\* **Reverse Proxy Caching** : Configure your reverse proxy (e.g., Nginx, Caddy, Cloudflare) to **cache static assets** (JS, CSS, Images). This significantly reduces load on the application server. See **Nginx Config** or **Caddy Config** .
\* **Disable Proxy Buffering (Critical for Streaming)** : If using Nginx, you **must** disable proxy\_buffering for Open WebUI. Proxy buffering re-chunks SSE streams, causing garbled markdown and slow streaming. Add proxy\_buffering off; and proxy\_cache off; to your location block. See **Streaming Troubleshooting** .

#### ⚡ High-Concurrency & Network Optimization

For setups with many simultaneous users, these settings are crucial to prevent bottlenecks.

###### Batch Streaming Tokens

By default, Open WebUI streams *every single token* arriving from the LLM. High-frequency streaming increases network IO and CPU usage on the server. If real-time saving is enabled (which is strongly discouraged), it also destroys database performance.
Increasing the chunk size buffers these updates, sending them to the client in larger groups. The only downside is a slightly choppier UI experience when streaming the response, but it can make a big difference in performance.
\* **Env Var** : CHAT\_RESPONSE\_STREAM\_DELTA\_CHUNK\_SIZE=7
\* *Recommendation* : Set to **5-10** for high-concurrency instances.

###### Thread Pool Size

Defines the number of worker threads available for handling requests.
\* **Default** : 40
\* **High-Traffic Recommendation** : **2000+**
\* **Warning** : **NEVER decrease this value.** Even on low-spec hardware, an idle thread pool does not consume significant resources. Setting this too low (e.g., 10) **WILL cause application freezes** and request timeouts.
\* **Env Var** : THREAD\_POOL\_SIZE=2000

###### AIOHTTP Client Timeouts

Long LLM completions can exceed default HTTP client timeouts. Configure these to prevent requests being cut off mid-response:
\* **Env Var** : AIOHTTP\_CLIENT\_TIMEOUT=1800 (30 minutes for completions)
\* **Env Var** : AIOHTTP\_CLIENT\_TIMEOUT\_MODEL\_LIST=15 (shorter for model listing)
\* **Env Var** : AIOHTTP\_CLIENT\_TIMEOUT\_OPENAI\_MODEL\_LIST=15

###### Container Resource Limits

For Docker deployments, ensure adequate resource allocation:

```
deploy:
  resources:
    limits:
      memory: 8G      # Adjust based on usage
      cpus: '4.0'
    reservations:
      memory: 4G
      cpus: '2.0'

# Increase file descriptor limits
ulimits:
  nofile:
    soft: 65536
    hard: 65536
```

**Diagnosis commands:**

```
# Check container resource usage
docker stats openwebui --no-stream

# Check connection states
docker exec openwebui netstat -an | grep -E "ESTABLISHED|TIME_WAIT|CLOSE_WAIT" | sort | uniq -c

# Check open file descriptors
docker exec openwebui ls -la /proc/1/fd | wc -l
```

#### ☁ Cloud Infrastructure Latency

When deploying Open WebUI in cloud Kubernetes environments (AKS, EKS, GKE), you may notice significant performance degradation compared to local Kubernetes (Rancher Desktop, kind, Minikube) or bare-metal deployments—even with identical resource allocations. This is almost always caused by **latency** in the underlying infrastructure.

##### Network Latency (Database & Services)

The most common cause of cloud performance issues is **network latency between Open WebUI and its database** .
Many cloud deployments place the database on a separate node, availability zone, or even a managed database service. While this is architecturally sound, it introduces latency to *every single database query* . Open WebUI makes multiple database calls per request, so even 10-20ms of network latency per query can compound into multi-second response times under concurrent load.
**Symptoms:**
\* Health check endpoints show high response times instead of being near-instant.
\* Simple API calls or normal chat completions become sluggish under concurrent load, even when CPU and Memory usage appear low.
\* Significant performance gap between local development/testing and cloud production environments.
**Diagnosis:**
\* Check network latency between your Open WebUI pod and your database. From within the pod:

```
# For PostgreSQL
psql -h  -U  -c "SELECT 1" -d 

# Or use ping/nc to check raw latency
nc -zv  5432
```

```
*   **Ideal Latency Target:**  You should aim for  **1-2ms or lower**  for database queries. If network latency to your database exceeds  **5ms** , it is highly not recommended for production deployments and will likely be your primary performance bottleneck.
```

**Solutions:**
1. **Co-locate services:** Deploy Open WebUI and PostgreSQL in the same availability zone, or even on the same node pool if possible, to minimize network hops.
1. **Managed DB Consideration:** Note that "one-click" managed database solutions in the cloud, while scalable, often introduce significant network latency compared to a self-hosted DB on the same node. This tradeoff must be carefully considered.
1. **Enable caching:** Use ENABLE\_BASE\_MODELS\_CACHE=True and other caching options to reduce the frequency of database queries.
1. **Reduce database writes:** Set ENABLE\_REALTIME\_CHAT\_SAVE=False to batch database updates and reduce IOPS pressure.

##### Disk I/O Latency (SQLite & Storage)

If you're using **SQLite** (the default) in a cloud environment, you may be trading network latency for **disk latency** .
Cloud storage (Azure Disks, AWS EBS, GCP Persistent Disks) often has significantly higher latency and lower IOPS than local NVMe/SSD storage—especially on lower-tier storage classes.
Warning: Performance Risk with Network File Systems
Using Network-attached File Systems like **NFS, SMB, or Azure Files** for your database storage (especially for SQLite) **may** introduce severe latency into the file locking and synchronous write operations that SQLite relies on.
SQLite is particularly sensitive to disk performance because it performs synchronous writes. Moving from local SSDs to a network share can increase latency by 10x or more per operation.
**Symptoms:**
\* Performance is acceptable with a single user but degrades rapidly as concurrency increases.
\* High "I/O Wait" on the server despite low CPU usage.
**Solutions:**
1. **Use high-performance Block Storage:**
\* Ensure you are using SSD-backed **Block Storage** classes (e.g., Premium\_LRS on Azure Disks, gp3 on AWS EBS, pd-ssd on GCP). Avoid "File" based storage classes (like azurefile-csi ) for database workloads.
1. **Use PostgreSQL instead:** For any medium to large production deployment, **Postgres is mandatory** . SQLite is generally not recommended at scale in cloud environments due to the inherent latency of network-attached storage and the compounding effect of file locking over the network.

##### Other Cloud-Specific Considerations

| Factor | Impact | Mitigation |
| --- | --- | --- |
| **Burstable VMs** (e.g., Azure B-series, AWS T-series) | CPU throttling under sustained load, even at low reported usage | Use standard/compute-optimized node pools |
| **DNS Resolution** | CoreDNS overhead on every external request | Ensure CoreDNS is properly scaled; consider node-local DNS cache |
| **Service Mesh Sidecars** | Istio/Linkerd proxies add latency to every request | Check for unexpected sidecar containers in your pods |
| **Network Policies** | CNI processing overhead | Audit and simplify network policies if possible |
| **Cross-Zone Traffic** | Latency + egress costs when services span zones | Pin services to the same availability zone |

#### 📉 Resource Efficiency (Reducing RAM)

If deploying on memory-constrained devices (Raspberry Pi, small VPS), use these strategies to prevent the application from crashing due to OOM (Out of Memory) errors.

##### 1. Offload Auxiliary Models (Local Deployments Only)

Open WebUI loads local ML models for features like RAG and STT. **This section is only relevant if you are running models LOCALLY.**

###### RAG Embeddings

```
*   **Low-Spec Recommendation** :
    *   **Option A (Easiest)** : Keep the default  **SentenceTransformers**  (all-MiniLM-L6-v2). It is lightweight, runs on CPU, and is significantly more efficient than running a full Ollama instance on the same Raspberry Pi.
    *   **Option B (Best Performance)** : Use an  **External API**  (OpenAI/Cloud).
*   **Configuration** :
    *   **Admin Panel** : Settings > Documents > Embedding Model Engine
    *   **Env Var** : RAG_EMBEDDING_ENGINE=openai (to offload completely)
```

###### Speech-to-Text (STT)

Local Whisper models are heavy (~500MB+ RAM).
\* **Recommendation** : Use **WebAPI** (Browser-based). It uses the user's device capabilities, costing 0 server RAM.
\* **Configuration** :
\* **Admin Panel** : Settings > Audio > STT Engine
\* **Env Var** : AUDIO\_STT\_ENGINE=webapi

##### 2. Disable Unused Features

Prevent the application from loading **local** models you don't use.
\* **Image Generation** : ENABLE\_IMAGE\_GENERATION=False (Admin: Settings > Images )
\* **Code Interpreter** : ENABLE\_CODE\_INTERPRETER=False (Admin: Settings > Tools )

##### 3. Disable Background Tasks

If resource usage is critical, disable automated features that constantly trigger model inference.
**Recommendation order (Highest Impact first):**
1. **Autocomplete** : ENABLE\_AUTOCOMPLETE\_GENERATION=False ( **High Impact** : Triggers on every keystroke!)
\* Admin: Settings > Interface > Autocomplete
1. **Follow-up Questions** : ENABLE\_FOLLOW\_UP\_GENERATION=False
\* Admin: Settings > Interface > Follow-up
1. **Title Generation** : ENABLE\_TITLE\_GENERATION=False
\* Admin: Settings > Interface > Chat Title
1. **Tag Generation** : ENABLE\_TAGS\_GENERATION=False

#### 🚀 Recommended Configuration Profiles

##### Profile 1: Maximum Privacy (Weak Hardware/RPi)

*Target: 100% Local, Raspberry Pi / <4GB RAM.*
1. **Embeddings** : Default (SentenceTransformers) - *Runs on CPU, lightweight.*
1. **Audio** : AUDIO\_STT\_ENGINE=webapi - *Zero server load.*
1. **Task Model** : Disable or use tiny model ( llama3.2:1b ).
1. **Scaling** : Keep default THREAD\_POOL\_SIZE (40).
1. **Disable** : Image Gen, Code Interpreter, Autocomplete, Follow-ups.
1. **Database** : SQLite is fine.

##### Profile 2: Single User Enthusiast

*Target: Max Quality & Speed, Local + External APIs.*
1. **Embeddings** : RAG\_EMBEDDING\_ENGINE=openai (or ollama with nomic-embed-text on a fast server).
1. **Task Model** : gpt-5-nano or llama-3.1-8b-instant .
1. **Caching** : MODELS\_CACHE\_TTL=300 .
1. **Database** : ENABLE\_REALTIME\_CHAT\_SAVE=False (Keeping this disabled is recommended even for single users to ensure maximum stability).
1. **Vector DB** : PGVector (recommended) or ChromaDB (either is fine unless dealing with massive data).

##### Profile 3: High Scale / Enterprise

*Target: Many concurrent users, Stability > Persistence.*
1. **Database** : **PostgreSQL** (Mandatory).
1. **Content Extraction** : **Tika** or **Docling** (Mandatory — default pypdf leaks memory). See [Content Extraction Engine](https://docs.openwebui.com/troubleshooting/performance#content-extraction-engine).
1. **Embeddings** : **External** — RAG\_EMBEDDING\_ENGINE=openai or ollama (Mandatory — default SentenceTransformers consumes too much RAM at scale). See [Embedding Engine](https://docs.openwebui.com/troubleshooting/performance#embedding-engine).
1. **Tool Calling** : **Native Mode** (strongly recommended — Default Mode is legacy and breaks KV cache). See [Tool Calling Modes](https://docs.openwebui.com/features/extensibility/plugin/tools#tool-calling-modes-default-vs-native).
1. **Workers** : THREAD\_POOL\_SIZE=2000 (Prevent timeouts).
1. **Streaming** : CHAT\_RESPONSE\_STREAM\_DELTA\_CHUNK\_SIZE=7 (Reduce CPU/Net/DB writes).
1. **Chat Saving** : ENABLE\_REALTIME\_CHAT\_SAVE=False .
1. **Vector DB** : **Milvus** , **Qdrant** , or **PGVector** . **Do not use ChromaDB's default local mode** — its SQLite backend will crash under multi-worker/multi-replica access.
1. **Task Model** : External/Hosted (Offload compute).
1. **Caching** : ENABLE\_BASE\_MODELS\_CACHE=True , MODELS\_CACHE\_TTL=300 , ENABLE\_QUERIES\_CACHE=True .
1. **Redis** : Single instance with timeout 1800 and high maxclients (10000+). See [Redis Tuning](https://docs.openwebui.com/troubleshooting/performance#redis-tuning) below.

###### Redis Tuning

A single Redis instance is sufficient for the vast majority of deployments, including those with thousands of users. **You almost certainly do not need Redis Cluster or Redis Sentinel** unless you have specific HA requirements.
Common Redis configuration issues that cause unnecessary scaling:

| Issue | Symptom | Fix |
| --- | --- | --- |
| **Stale connections** | Redis runs out of connections or memory grows indefinitely | Set timeout 1800 in redis.conf (kills idle connections after 30 minutes) |
| **Low maxclients** | max number of clients reached errors | Set maxclients 10000 or higher |
| **No connection limits** | Open WebUI pods may accumulate connections that never close | Combine timeout with connection pool limits in your Redis client config |

#### ⚠ Common Anti-Patterns

These are real-world mistakes that cause organizations to massively over-provision infrastructure:
Anti-Pattern
What Happens
Fix
**Using default content extractor in production**
pypdf leaks memory → containers restart constantly → you add more replicas to compensate
Switch to Tika or Docling ( CONTENT\_EXTRACTION\_ENGINE=tika )
**Running SentenceTransformers at scale**
Each worker loads ~500MB embedding model → RAM usage explodes → you add more machines
Use external embeddings ( RAG\_EMBEDDING\_ENGINE=openai or ollama )
**Redis Cluster when single Redis suffices**
Too many replicas → too many connections → Redis can't handle them → you deploy Redis Cluster to compensate
Fix the root cause (fewer replicas, timeout 1800 , maxclients 10000 )
**Scaling replicas to mask memory leaks**
Leaky processes → OOM kills → auto-scaler adds more pods → more Redis connections → Redis overwhelmed
Fix the leaks first (content extraction, embedding engine), then right-size
**Using Default (prompt-based) tool calling**
Injected prompts may break KV cache → higher latency → more resources needed per request
Switch to Native Mode for all capable models
**Not configuring Redis stale connection timeout**
Connections accumulate forever → Redis OOM → you deploy Redis Cluster
Add timeout 1800 to redis.conf
**Using base64-encoded icons in Actions/Filters**
Icon data is embedded in /api/models responses sent to the frontend on every page load for every model. A 500 KB base64 icon on 3 actions across 20 models = **30 MB of payload bloat** per request → slow frontend loads, high bandwidth usage, unnecessary backend memory pressure
Host icons as static files and reference them by URL in icon\_url / self.icon . See [Action Function icon\_url warning](https://docs.openwebui.com/features/extensibility/plugin/functions/action#example---specifying-action-frontmatter)

#### 🔗 Environment Variable References

For detailed information on all available variables, see the [Environment Configuration](https://docs.openwebui.com/reference/env-configuration) guide.

| Variable | Description & Link |
| --- | --- |
| TASK\_MODEL | [Task Model (Local)](https://docs.openwebui.com/reference/env-configuration#task_model) |
| TASK\_MODEL\_EXTERNAL | [Task Model (External)](https://docs.openwebui.com/reference/env-configuration#task_model_external) |
| ENABLE\_BASE\_MODELS\_CACHE | [Cache Model List](https://docs.openwebui.com/reference/env-configuration#enable_base_models_cache) |
| MODELS\_CACHE\_TTL | [Model Cache TTL](https://docs.openwebui.com/reference/env-configuration#models_cache_ttl) |
| ENABLE\_QUERIES\_CACHE | [Queries Cache](https://docs.openwebui.com/reference/env-configuration#enable_queries_cache) |
| DATABASE\_URL | [Database URL](https://docs.openwebui.com/reference/env-configuration#database_url) |
| ENABLE\_REALTIME\_CHAT\_SAVE | [Realtime Chat Save](https://docs.openwebui.com/reference/env-configuration#enable_realtime_chat_save) |
| CHAT\_RESPONSE\_STREAM\_DELTA\_CHUNK\_SIZE | [Streaming Chunk Size](https://docs.openwebui.com/reference/env-configuration#chat_response_stream_delta_chunk_size) |
| THREAD\_POOL\_SIZE | [Thread Pool Size](https://docs.openwebui.com/reference/env-configuration#thread_pool_size) |
| RAG\_EMBEDDING\_ENGINE | [Embedding Engine](https://docs.openwebui.com/reference/env-configuration#rag_embedding_engine) |
| CONTENT\_EXTRACTION\_ENGINE | [Content Extraction Engine](https://docs.openwebui.com/reference/env-configuration#content_extraction_engine) |
| AUDIO\_STT\_ENGINE | [STT Engine](https://docs.openwebui.com/reference/env-configuration#audio_stt_engine) |
| ENABLE\_IMAGE\_GENERATION | [Image Generation](https://docs.openwebui.com/reference/env-configuration#enable_image_generation) |
| ENABLE\_AUTOCOMPLETE\_GENERATION | [Autocomplete](https://docs.openwebui.com/reference/env-configuration#enable_autocomplete_generation) |
| RAG\_SYSTEM\_CONTEXT | [RAG System Context](https://docs.openwebui.com/reference/env-configuration#rag_system_context) |
| DATABASE\_ENABLE\_SESSION\_SHARING | [Database Session Sharing](https://docs.openwebui.com/reference/env-configuration#database_enable_session_sharing) |

[Edit this page](https://github.com/open-webui/docs/blob/main/docs/troubleshooting/performance.md)
[Previous Scaling & HA](https://docs.openwebui.com/troubleshooting/multi-replica)
[Next Custom CA Store](https://docs.openwebui.com/troubleshooting/custom-ca)
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