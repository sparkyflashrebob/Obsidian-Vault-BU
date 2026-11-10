---
tags:
  - notebooklm-import
notebook: "OpenWebUI"
category: "research"
---

Web Search / Open WebUI
[Skip to main content](https://docs.openwebui.com/troubleshooting/web-search#__docusaurus_skipToContent_fallback)
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
\* Web Search
On this page

### Web Search

Web Search in Open WebUI allows language models to access real-time information from the internet. When things don't work as expected, this guide will help you diagnose and fix common issues.

#### Common Web Search Issues

##### 1. Web Search Fails Behind HTTP Proxy

If you're running Open WebUI behind an HTTP proxy, you might notice that web search queries succeed (e.g., SearXNG returns results), but the subsequent content fetching fails with errors like:
\* [Errno -3] Temporary failure in name resolution
\* Connection timeout to host
\* The content provided is empty
This happens because the web content fetcher doesn't use your http\_proxy / https\_proxy environment variables by default.
✅ **Solution:**
1. Navigate to: **Admin Panel > Settings > Web Search**
1. Enable **Trust Proxy Environment**
1. Save changes
Alternatively, set the environment variable [WEB\_SEARCH\_TRUST\_ENV](https://docs.openwebui.com/reference/env-configuration#web_search_trust_env) :

```
WEB_SEARCH_TRUST_ENV=True
```

info
This is a **PersistentConfig** variable, meaning it can be set via environment variable on startup OR configured through the Admin Panel UI. Once set in the UI, the database value takes precedence over the environment variable.
This setting tells Open WebUI's web content loader to respect the proxy settings from your environment variables ( http\_proxy , https\_proxy ). Without this, even if your search engine works through the proxy, fetching content from the returned URLs will fail.

##### 2. 403 Forbidden Errors from SearXNG

If you're using SearXNG and seeing 403 Client Error: Forbidden in your logs, the JSON format is not enabled.
✅ **Solution:**
Edit your SearXNG settings.yml and add json to the formats list:

```
search:
  formats:
    - html
    - json
```

Restart SearXNG after making this change.

##### 3. Empty Content or Poor Results

If web search returns empty content or poor quality results, the issue is often related to context window size or content extraction.
✅ **Solutions:**
\* **Increase context length** : Web pages often contain 4,000-8,000+ tokens. If your model has a 2048-token limit, you're missing most of the content. Increase to 16384+ tokens in **Admin Panel > Models > Settings > Advanced Parameters** (anything below will be subpar for web content).
\* **Check result count** : Adjust WEB\_SEARCH\_RESULT\_COUNT to control how many results are fetched.
\* **Try different loaders** : Configure WEB\_LOADER\_ENGINE to use playwright for JavaScript-heavy sites or firecrawl / tavily for better extraction.
For more details on context window issues, see the [RAG Troubleshooting Guide](https://docs.openwebui.com/troubleshooting/rag).

##### 4. Connection Timeouts

If web searches are timing out:
✅ **Solutions:**
\* **Reduce concurrent requests** : Set WEB\_SEARCH\_CONCURRENT\_REQUESTS=1 for sequential execution (required for Brave free tier).
\* **Adjust loader concurrency** : Lower WEB\_LOADER\_CONCURRENT\_REQUESTS if fetching many pages simultaneously.
\* **Check network connectivity** : Ensure Open WebUI can reach both the search engine and the result URLs.

#### Environment Variables Reference

For a comprehensive list of all web search environment variables, see the [Environment Configuration documentation](https://docs.openwebui.com/reference/env-configuration#web-search).
Key variables:

| Variable | Description |
| --- | --- |
| WEB\_SEARCH\_TRUST\_ENV | Enable proxy support for content fetching |
| WEB\_SEARCH\_RESULT\_COUNT | Number of search results to fetch |
| WEB\_SEARCH\_CONCURRENT\_REQUESTS | Concurrent requests to search engine |
| WEB\_LOADER\_CONCURRENT\_REQUESTS | Concurrent page fetches |
| WEB\_LOADER\_ENGINE | Content extraction engine |

[Edit this page](https://github.com/open-webui/docs/blob/main/docs/troubleshooting/web-search.mdx)
[Previous SSO & OAuth](https://docs.openwebui.com/troubleshooting/sso)
[Next Scaling & HA](https://docs.openwebui.com/troubleshooting/multi-replica)
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