---
tags:
  - notebooklm-import
notebook: "OpenWebUI"
category: "research"
---

Authentication & Access / Open WebUI
[Skip to main content](https://docs.openwebui.com/features/authentication-access#__docusaurus_skipToContent_fallback)
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
\* [Federated Authentication](https://docs.openwebui.com/category/federated-authentication)
\* [Role-Based Access Control (RBAC)](https://docs.openwebui.com/features/authentication-access/rbac/)
\* [API Keys](https://docs.openwebui.com/features/authentication-access/api-keys)
\* [🔧 Administration](https://docs.openwebui.com/features/administration/)
\* [💬 Chat & Conversations](https://docs.openwebui.com/features/authentication-access)
\* [🧠 Workspace](https://docs.openwebui.com/features/authentication-access)
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
\* 🔐 Authentication & Access
On this page

### 🔐 Authentication & Access

**Control who gets in, what they can do, and how your instance integrates with your identity stack.**
Open WebUI is multi-user from day one. Whether you're running a personal instance or managing thousands of seats across an organization, you have full control over authentication, authorization, and programmatic access. Connect your identity provider, define granular permissions, and automate user lifecycle management, all without touching a line of code.

#### What's In This Section

|  |  |
| --- | --- |
| 👥 **RBAC** | Roles, groups, and per-resource permissions. Define who can access what |
| 🔑 **SSO / OIDC** | Federated authentication with Google, Microsoft, Okta, Keycloak, or any OIDC provider |
| 📂 **LDAP** | Authenticate against your existing directory service |
| 📋 **SCIM 2.0** | Automated user and group provisioning and deprovisioning from your IdP |
| 🔐 **API Keys** | Programmatic access for scripts, bots, pipelines, and integrations |

#### How It Fits Together

SSO / OIDC / LDAP
SCIM 2.0
Roles + Groups
Bearer Token
Identity Provider
(Google, Okta, LDAP...)
Authentication
User & Group
Provisioning
RBAC Engine
Per-User
Permissions
Models · Knowledge
Tools · Channels
API Keys
1. **Users authenticate** via SSO, OIDC, LDAP, or local credentials.
1. **SCIM provisions** users and groups automatically from your identity provider.
1. **RBAC determines access** based on roles (Admin, User) and group memberships.
1. **Permissions are additive** : each group membership adds capabilities, never removes them.
1. **API keys** inherit the creating user's full permissions for programmatic access.

#### Quick Start

##### Solo or small team? Start simple

Open WebUI works out of the box with local email/password authentication. No external identity provider required. Create accounts, assign admin or user roles, and you're done.

##### Organization? Layer in SSO and SCIM

```
1.  **Set up SSO** : Configure your identity provider for single sign-on
1.  **Configure RBAC** : Create groups, assign permissions, and set up access control lists
1.  **Enable SCIM**   *(optional)* : Automate user lifecycle from your IdP
1.  **Generate API keys**   *(optional)* : Enable programmatic access for automation
```

#### Key Concepts

##### Additive permissions

Open WebUI's security model is **additive** . Users start with their role's default permissions, and group memberships only ever *add* capabilities. A user's effective permissions are the union of everything granted by their role and all their groups.

##### Per-resource access control

Models, Knowledge bases, Tools, and Skills all support fine-grained access control. Resources are **private by default** . The creator controls who can see and use them via user grants, group grants, or public visibility.

##### Admin vs. User

There are two primary roles. **Admins** have full system access. **Users** have capabilities defined by default permissions plus group memberships. A third role, **Pending** , holds new sign-ups in a queue for admin approval.
[Roles →](https://docs.openwebui.com/features/authentication-access/rbac/roles)
· [Permissions →](https://docs.openwebui.com/features/authentication-access/rbac/permissions)
· [Groups →](https://docs.openwebui.com/features/authentication-access/rbac/groups)
[Edit this page](https://github.com/open-webui/docs/blob/main/docs/features/authentication-access/index.mdx)
[Previous ⭐ Features](https://docs.openwebui.com/features/)
[Next Federated Authentication](https://docs.openwebui.com/category/federated-authentication)
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