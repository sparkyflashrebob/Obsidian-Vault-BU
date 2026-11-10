---
tags:
  - notebooklm-import
notebook: "OpenWebUI"
category: "research"
---

Scaling & HA / Open WebUI
[Skip to main content](https://docs.openwebui.com/troubleshooting/multi-replica#__docusaurus_skipToContent_fallback)
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
\* Scaling & HA
On this page

### Multi-Replica, High Availability & Concurrency Troubleshooting

This guide addresses common issues encountered when deploying Open WebUI in **multi-replica** environments (e.g., Kubernetes, Docker Swarm) or when using **multiple workers** ( UVICORN\_WORKERS > 1 ) for increased concurrency.
If you are setting up a scaled deployment for the first time, start with the [Scaling Open WebUI](https://docs.openwebui.com/getting-started/advanced-topics/scaling) guide for a step-by-step walkthrough.

#### Core Requirements Checklist

Before troubleshooting specific errors, ensure your deployment meets these **absolute requirements** for a multi-replica setup. Missing any of these will cause instability, login loops, or data loss.
1. **Shared Secret Key:** [WEBUI\_SECRET\_KEY](https://docs.openwebui.com/reference/env-configuration#webui_secret_key) **MUST** be identical on all replicas.
1. **External Database:** You **MUST** use an external PostgreSQL database (see [DATABASE\_URL](https://docs.openwebui.com/reference/env-configuration#database_url) ). SQLite is **NOT** supported for multiple instances.
1. **Redis for WebSockets:** [ENABLE\_WEBSOCKET\_SUPPORT=True](https://docs.openwebui.com/reference/env-configuration#enable_websocket_support) and [WEBSOCKET\_MANAGER=redis](https://docs.openwebui.com/reference/env-configuration#websocket_manager) with a valid [WEBSOCKET\_REDIS\_URL](https://docs.openwebui.com/reference/env-configuration#websocket_redis_url) are required.
1. **Shared Storage:** A persistent volume (RWX / ReadWriteMany if possible, or ensuring all replicas map to the same underlying storage for data/ ) is critical for RAG (uploads/vectors) and generated images.
1. **External Vector Database (Required):** The default ChromaDB uses a local SQLite-backed PersistentClient that is **not safe for multi-worker or multi-replica deployments** . SQLite connections are not fork-safe, and concurrent writes from multiple processes will crash workers instantly. You **must** use a dedicated external Vector DB (e.g., [PGVector](https://docs.openwebui.com/reference/env-configuration#pgvector_db_url), [MariaDB Vector](https://docs.openwebui.com/reference/env-configuration#mariadb_vector_db_url), Milvus, Qdrant) via [VECTOR\_DB](https://docs.openwebui.com/reference/env-configuration#vector_db) , or run ChromaDB as a [separate HTTP server](https://docs.openwebui.com/reference/env-configuration#chroma_http_host).
1. **Database Session Sharing (Optional):** For PostgreSQL deployments with adequate resources, consider enabling [DATABASE\_ENABLE\_SESSION\_SHARING=True](https://docs.openwebui.com/reference/env-configuration#database_enable_session_sharing) to improve performance under high concurrency.

#### Common Issues

##### 1. Login Loops / 401 Unauthorized Errors

**Symptoms:**
\* You log in successfully, but the next click logs you out.
\* You see "Unauthorized" or "401" errors in the browser console immediately after login.
\* "Error decrypting tokens" appears in logs.
**Cause:** Each replica is using a different WEBUI\_SECRET\_KEY . When Replica A issues a session token (JWT), Replica B rejects it because it cannot verify the signature with its own different key.
**Solution:** Set the WEBUI\_SECRET\_KEY environment variable to the **same** strong, random string on all backend replicas.

```
# Example in Kubernetes/Compose
env:
  - name: WEBUI_SECRET_KEY
    value: "your-super-secure-static-key-here"
```

##### 2. WebSocket 403 Errors / Connection Failures

**Symptoms:**
\* Chat stops responding or hangs.
\* Browser console shows WebSocket connection failed: 403 Forbidden or Connection closed .
\* Logs show engineio.server: https://your-domain.com is not an accepted origin .
**Cause:**
\* **CORS:** The load balancer or ingress origin does not match the allowed origins.
\* **Missing Redis:** WebSockets are defaulting to in-memory, so events on Replica A (e.g., LLM generation finish) are not broadcast to the user connected to Replica B.
**Solution:**
1. **Configure CORS:** Ensure [CORS\_ALLOW\_ORIGIN](https://docs.openwebui.com/reference/env-configuration#cors_allow_origin) includes your public domain *and* http/https variations. If you see logs like engineio.base\_server:\_log\_error\_once:354 - https://yourdomain.com is not an accepted origin , you must update this variable. It accepts a **semicolon-separated list** of allowed origins. **Example:**

```
CORS_ALLOW_ORIGIN="https://chat.yourdomain.com;http://chat.yourdomain.com;https://yourhostname;http://localhost:3000"
```

*Add all valid IPs, Domains, and Hostnames that users might use to access your Open WebUI.* 2. **Enable Redis for WebSockets:** Ensure these variables are set on **all** replicas:

```
ENABLE_WEBSOCKET_SUPPORT=True
WEBSOCKET_MANAGER=redis
WEBSOCKET_REDIS_URL=redis://your-redis-host:6379/0
```

##### 3. "Model Not Found" or Configuration Mismatch

**Symptoms:**
\* You enable a model or change a setting in the Admin UI, but other users (or you, after a refresh) don't see the change.
\* Chats fail with "Model not found" intermittently.
**Cause:**
\* **Configuration Sync:** Replicas are not synced. Open WebUI uses Redis Pub/Sub to broadcast configuration changes (like toggling a model) to all other instances.
\* **Missing Redis:** If REDIS\_URL is not set, configuration changes stay local to the instance where the change was made.
**Solution:** Set REDIS\_URL to point to your shared Redis instance. This enables the Pub/Sub mechanism for real-time config syncing.

```
REDIS_URL=redis://your-redis-host:6379/0
```

##### 4. Database Corruption / "Locked" Errors

**Symptoms:**
\* Logs show database is locked or severe SQL errors.
\* Data saved on one instance disappears on another.
**Cause:** Using **SQLite** with multiple replicas. SQLite is a file-based database and does not support concurrent network writes from multiple containers.
**Solution:** Migrate to **PostgreSQL** . Update your connection string:

```
DATABASE_URL=postgresql://user:password@postgres-host:5432/openwebui
```

##### 5. Uploaded Files or RAG Knowledge Inaccessible

**Symptoms:**
\* You upload a file (for RAG) on one instance, but the model cannot find it later.
\* Generated images appear as broken links.
**Cause:** The /app/backend/data directory is not shared or is not consistent across replicas. If User A uploads a file to Replica 1, and the next request hits Replica 2, Replica 2 won't have the file physically on disk.
**Solution:**
\* **Kubernetes:** Use a PersistentVolumeClaim with ReadWriteMany (RWX) access mode if your storage provider supports it (e.g., NFS, CephFS, AWS EFS).
\* **Docker Swarm/Compose:** Mount a shared volume (e.g., NFS mount) to /app/backend/data on all containers.

##### 6. Worker Crashes During Document Upload (ChromaDB + Multi-Worker)

**Symptoms:**
\* Logs show the following sequence, all within the same second:

```
save_docs_to_vector_db:1619 - adding to collection file-id
INFO:     Waiting for child process [pid]
INFO:     Child process [pid] died
```

```
*  Workers die immediately during RAG document ingestion.
*  The crash is instant (not a timeout).
```

**Cause:** The default ChromaDB configuration uses a local PersistentClient backed by **SQLite** . When uvicorn forks multiple workers ( UVICORN\_WORKERS > 1 ), each worker process inherits a copy of the same SQLite database connection — all pointing at the same file on disk ( data/vector\_db/ ).
When two workers attempt to write to the collection simultaneously (e.g., during document upload), SQLite's file-level locking fails across forked processes. The result is either a database lock error or a segfault from corrupted internal state inherited across the fork() call, which kills the worker process instantly.
This is a [well-known SQLite limitation](https://www.sqlite.org/howtocorrupt.html#_carrying_an_open_database_connection_across_a_fork_): open database connections must not be carried across a fork() .
**Solution:** You **must** stop using the default local ChromaDB with multiple workers. Pick one of these options:

| Option | Change | Tradeoff |
| --- | --- | --- |
| **Keep 1 worker** | Set UVICORN\_WORKERS=1 (the default) | Simplest, but limits concurrency |
| **Use ChromaDB HTTP mode** | Set [CHROMA\_HTTP\_HOST](https://docs.openwebui.com/reference/env-configuration#chroma_http_host) / [CHROMA\_HTTP\_PORT](https://docs.openwebui.com/reference/env-configuration#chroma_http_port) to point to a separate Chroma server | Each worker connects via HTTP instead of SQLite — fully fork-safe |
| **Switch vector DB** | Set [VECTOR\_DB](https://docs.openwebui.com/reference/env-configuration#vector_db) to pgvector , mariadb-vector , milvus , qdrant , etc. | These are client-server databases, inherently multi-process safe |

**Recommended fix** — run ChromaDB as a separate server:

```
# Run chroma server separately
chroma run --host 0.0.0.0 --port 8000 --path /data/vector_db

# Then set these env vars for Open WebUI
CHROMA_HTTP_HOST=localhost
CHROMA_HTTP_PORT=8000
UVICORN_WORKERS=4
```

##### 7. Slow Performance in Cloud vs. Local Kubernetes

**Symptoms:**
\* Open WebUI performs well locally but experiences significant degradation or timeouts when deployed to cloud providers (AKS, EKS, GKE).
\* Performance drops sharply under concurrent load despite adequate resource allocation.
**Cause:** This is typically caused by infrastructure latency (Network Latency to the database or Disk I/O latency for SQLite) that is inherently higher in cloud environments compared to local NVMe/SSD storage and local networks.
**Solution:** Refer to the **Cloud Infrastructure Latency** section in the Performance Guide for a detailed breakdown of diagnosis and mitigation strategies.
If you need more tips for performance improvements, check out the full [Optimization & Performance Guide](https://docs.openwebui.com/troubleshooting/performance).

##### 8. Optimizing Database Performance

For PostgreSQL deployments with adequate resources, consider these optimizations:

###### Database Session Sharing

Enabling session sharing can improve performance under high concurrency:

```
DATABASE_ENABLE_SESSION_SHARING=true
```

See [DATABASE\_ENABLE\_SESSION\_SHARING](https://docs.openwebui.com/reference/env-configuration#database_enable_session_sharing) for details.

###### Connection Pool Sizing

If you experience QueuePool limit reached errors or connection timeouts under high concurrency, increase the pool size:

```
DATABASE_POOL_SIZE=15 (or higher)
DATABASE_POOL_MAX_OVERFLOW=20 (or higher)
```

**Important:** The combined total ( DATABASE\_POOL\_SIZE + DATABASE\_POOL\_MAX\_OVERFLOW ) should remain well below your database's max\_connections limit. PostgreSQL defaults to 100 max connections, so keep the combined total under 50-80 per Open WebUI instance to leave room for other clients and maintenance operations.
Pool Size Multiplies with Concurrency
**Each Open WebUI process maintains its own independent connection pool.** This applies to multiple replicas (Kubernetes pods, Docker Swarm replicas) *and* multiple Uvicorn workers within each replica.
The actual maximum number of database connections is:

```
Total connections = (DATABASE_POOL_SIZE + DATABASE_POOL_MAX_OVERFLOW) × Total processes
```

Where Total processes = Number of replicas × UVICORN\_WORKERS per replica .
For example, with DATABASE\_POOL\_SIZE=15 , DATABASE\_POOL\_MAX\_OVERFLOW=20 , 3 replicas, and 2 workers each, you could open up to **210 connections** (35 × 6 processes).
See [DATABASE\_POOL\_SIZE](https://docs.openwebui.com/reference/env-configuration#database_pool_size) for details. For comprehensive database optimization including caching, session sharing, and content extraction tuning, see the [Performance & RAM](https://docs.openwebui.com/troubleshooting/performance) guide.

##### 9. Function/Tool Dependency Installation Crashes

**Symptoms:**
\* Workers crash with AssertionError on startup or when a function/tool is first loaded.
\* Logs show pip locking errors or multiple pip processes competing.
**Cause:** When a function or tool specifies requirements in its frontmatter, Open WebUI runs pip install at runtime. With multiple workers or replicas, each process attempts the installation independently, causing pip's internal lock to detect the conflict and crash.
**Solution:** **Set ENABLE\_PIP\_INSTALL\_FRONTMATTER\_REQUIREMENTS=False** to disable runtime pip installs entirely. Then pre-install all required packages at image build time:

```
FROM ghcr.io/open-webui/open-webui:main

RUN pip install --no-cache-dir python-docx requests beautifulsoup4
```

Runtime requirements installation is only appropriate for single-worker development or homelab environments.
For more details, see the [External Packages](https://docs.openwebui.com/features/extensibility/plugin/tools/development#external-packages) section of the Tools documentation.

#### Deployment Best Practices

##### Updates and Migrations

Critical: Avoid Concurrent Migrations
**Always ensure only one process is running database migrations when upgrading Open WebUI versions.**
Database migrations run automatically on startup. If multiple replicas (or multiple workers within a single container) start simultaneously with a new version, they may try to run migrations concurrently, potentially leading to race conditions or database schema corruption.
**Safe Update Procedure:**
There are two ways to safely handle migrations in a multi-replica environment:

###### Option 1: Designate a Master Migration Pod (Recommended)

```
1. Identify one pod/replica as the "master" for migrations.
1. Set ENABLE_DB_MIGRATIONS=True (default) on the master pod.
1. Set ENABLE_DB_MIGRATIONS=False on all other pods.
1. When updating, the master pod will handle the database schema update while other pods skip the migration step.
```

###### Option 2: Scale Down During Update

```
1.  **Scale Down:**  Set replicas to 1 (and ensure UVICORN_WORKERS=1 ).
1.  **Update Image:**  Update the image or version.
1.  **Wait for Health Check:**  Wait for the single instance to start fully and complete migrations.
1.  **Scale Up:**  Increase replicas back to your desired count.
```

##### Session Affinity (Sticky Sessions)

While Open WebUI is designed to be stateless with proper Redis configuration, enabling **Session Affinity** (Sticky Sessions) at your Load Balancer / Ingress level can improve performance and reduce occasional jitter in WebSocket connections.
\* **Nginx Ingress:** nginx.ingress.kubernetes.io/affinity: "cookie"
\* **AWS ALB:** Enable Target Group Stickiness.

#### Related Documentation

```
*  [Scaling Open WebUI](https://docs.openwebui.com/getting-started/advanced-topics/scaling) — Step-by-step guide to scaling from single instance to production
*  [Environment Variable Configuration](https://docs.openwebui.com/reference/env-configuration)
*  [Optimization, Performance & RAM Usage](https://docs.openwebui.com/troubleshooting/performance)
*  [Redis WebSocket Support](https://docs.openwebui.com/tutorials/integrations/redis) — Detailed Redis setup tutorial
*  [Troubleshooting Connection Errors](https://docs.openwebui.com/troubleshooting/connection-error)
*  [RAG Troubleshooting](https://docs.openwebui.com/troubleshooting/rag) — Document upload and embedding issues
*  [Logging Open WebUI](https://docs.openwebui.com/getting-started/advanced-topics/logging)
```

[Edit this page](https://github.com/open-webui/docs/blob/main/docs/troubleshooting/multi-replica.mdx)
[Previous Web Search](https://docs.openwebui.com/troubleshooting/web-search)
[Next Performance & RAM](https://docs.openwebui.com/troubleshooting/performance)
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