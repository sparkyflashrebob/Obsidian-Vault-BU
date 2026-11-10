---
tags:
  - notebooklm-import
notebook: "OpenWebUI"
category: "research"
---

Azure OpenAI with EntraID / Open WebUI
[Skip to main content](https://docs.openwebui.com/tutorials/integrations/llm-providers/azure-openai#__docusaurus_skipToContent_fallback)
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
\* [LLM Providers](https://docs.openwebui.com/tutorials/integrations/llm-providers/azure-openai)
\* [Azure OpenAI with EntraID](https://docs.openwebui.com/tutorials/integrations/llm-providers/azure-openai/)
\* [Azure CLI Authentication](https://docs.openwebui.com/tutorials/integrations/llm-providers/azure-openai/azure-cli-auth)
\* [Workload Identity Authentication](https://docs.openwebui.com/tutorials/integrations/llm-providers/azure-openai/workload-identity-auth)
\* [DeepSeek R1 Dynamic](https://docs.openwebui.com/tutorials/integrations/llm-providers/deepseekr1-dynamic)
\* [Intel GPU (IPEX-LLM)](https://docs.openwebui.com/tutorials/integrations/llm-providers/ipex_llm)
\* [Monitoring](https://docs.openwebui.com/tutorials/integrations/llm-providers/azure-openai)
\* [Dev Tools](https://docs.openwebui.com/tutorials/integrations/llm-providers/azure-openai)
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
\* LLM Providers
\* Azure OpenAI with EntraID
On this page

### Azure OpenAI with EntraID

warning
This tutorial is a community contribution and is not supported by the Open WebUI team. It serves only as a demonstration on how to customize Open WebUI for your specific use case. Want to contribute? Check out the contributing tutorial.
This sections contains guides on how to integrate Open WebUI with Azure OpenAI using secure, keyless authentication via Azure Entra ID (formerly Azure AD). Instead of managing static API keys, you can leverage Azure's identity and access management for enhanced security.
warning
OpenWebUI needs to be on version 0.6.30 or higher for this to work!

#### Overview

Open WebUI supports Azure OpenAI integration with **Entra ID authentication** , allowing you to authenticate without storing API keys. This provides several benefits:
\* **Enhanced Security** : No static API keys to manage or rotate
\* **Azure RBAC Integration** : Fine-grained access control using Azure role assignments
\* **Audit Trail** : All access is logged through Azure's audit system
\* **Automatic Token Management** : Azure handles token lifecycle automatically

#### Authentication Methods

Open WebUI supports all authentication methods supported by [DefaultAzureCredential](https://learn.microsoft.com/en-us/python/api/azure-identity/azure.identity.defaultazurecredential?view=azure-python) for Azure OpenAI.
warning
By default DefaultAzureCredential tries all Azure Credentials, both development and production types. This might not be desirable if you know what authentication type you want to use since:
\* DefaultAzureCredential is called on **every** request and tries most authentication types until it finds one that works
\* There is a performance overhead for some authentication types
\* If you don't have certain types of authentication configured but they are tried your logs might be polluted with erroneous errors.
To fix this, **if you're on version 0.6.31 or greater** you can set the environment variable AZURE\_TOKEN\_CREDENTIALS to one of these specific values:
\* EnvironmentCredential
\* WorkloadIdentityCredential
\* ManagedIdentityCredential
\* VisualStudioCodeCredential
\* AzureCliCredential
\* AzurePowershellCredential
\* AzureDeveloperCliCredential
\* InteractiveBrowserCredential
*This would result in it only ever choosing the selected credential type*
Or, if you prefer the automatic selection behaviour but wish to narrow it between development vs production options you can use:
\* prod for EnvironmentCredential , WorkloadIdentityCredential , and ManagedIdentityCredential .
\* dev for SharedTokenCacheCredential , AzureCliCredential , AzurePowershellCredential , and AzureDeveloperCliCredential .

##### Azure CLI Authentication

**Best for:** Local development
Azure CLI authentication uses your local Azure credentials to authenticate with Azure OpenAI. This is the simplest method for getting started and works well for development environments.
**Key Features:**
\* Simple setup with Azure CLI
\* Works on local machines and containers
\* Uses your personal Azure credentials
\* Requires Azure CLI to be installed
[→ Learn how to set up Azure CLI Authentication](https://docs.openwebui.com/tutorials/integrations/llm-providers/azure-openai/azure-cli-auth)

##### 2. Workload Identity Authentication

**Best for:** Azure Kubernetes Service (AKS) production deployments and multi-tenant environments
Workload Identity provides a managed identity solution for AKS clusters, allowing pods to authenticate to Azure services without storing any credentials in the cluster.
**Key Features:**
\* No credentials stored in cluster
\* Kubernetes-native authentication
\* Federated identity credentials
\* Production-ready security model
\* Infrastructure as Code via Terraform
[→ Learn how to set up Workload Identity Authentication](https://docs.openwebui.com/tutorials/integrations/llm-providers/azure-openai/workload-identity-auth)

#### Prerequisites

Regardless of which authentication method you choose, you'll need:
\* **Azure Subscription** : With access to Azure OpenAI resources
\* **Open WebUI** : Version 0.6.30 or later
\* **Azure RBAC Role** : Cognitive Services OpenAI User role assigned to your identity
\* **Azure OpenAI Resource** : A deployed Azure OpenAI instance

#### Quick Comparison

|  | Azure CLI Auth | Workload Identity |
| --- | --- | --- |
| **Environment** | Local development | Azure Kubernetes Service (AKS) |
| **Setup Complexity** | Simple | Moderate (requires Terraform or Azure experience) |
| **Security Model** | Azure CLI credentials | Workload identity |
| **Best For** | Development and testing | Production deployments |
| **Credential Storage** | Local .azure directory | None (federated tokens) |

#### Next Steps

Choose the authentication method that best fits your deployment environment:
\* **For local development or Docker deployments** : Start with [Azure CLI Authentication](https://docs.openwebui.com/tutorials/integrations/llm-providers/azure-openai/azure-cli-auth)
\* **For production AKS deployments** : Use [Workload Identity Authentication](https://docs.openwebui.com/tutorials/integrations/llm-providers/azure-openai/workload-identity-auth)
Both methods provide secure, keyless authentication to Azure OpenAI and can be configured through the Open WebUI admin interface once the infrastructure is set up.
[Edit this page](https://github.com/open-webui/docs/blob/main/docs/tutorials/integrations/llm-providers/azure-openai/index.mdx)
[Previous Integrations](https://docs.openwebui.com/tutorials/integrations/)
[Next Azure CLI Authentication](https://docs.openwebui.com/tutorials/integrations/llm-providers/azure-openai/azure-cli-auth)
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