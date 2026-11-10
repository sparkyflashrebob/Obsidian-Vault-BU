---
tags:
  - notebooklm-import
notebook: "OpenWebUI"
category: "research"
---

Entra ID Group Name Sync / Open WebUI
[Skip to main content](https://docs.openwebui.com/tutorials/auth-sso/entra-group-name-sync#__docusaurus_skipToContent_fallback)
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
\* [Okta SSO (OIDC)](https://docs.openwebui.com/tutorials/auth-sso/okta-oidc-sso)
\* [Dual OAuth Configuration](https://docs.openwebui.com/tutorials/auth-sso/dual-oauth-configuration)
\* [Entra ID Group Name Sync](https://docs.openwebui.com/tutorials/auth-sso/entra-group-name-sync)
\* [Tailscale](https://docs.openwebui.com/tutorials/auth-sso/tailscale)
\* [Azure AD LDAP](https://docs.openwebui.com/tutorials/auth-sso/azure-ad-ds-ldap)
\* [Integrations](https://docs.openwebui.com/tutorials/integrations/)
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
\* [Authentication & SSO](https://docs.openwebui.com/tutorials/auth-sso/)
\* Entra ID Group Name Sync
On this page

### Microsoft Entra ID Group Name Sync

warning
This tutorial is a community contribution and is not supported by the Open WebUI team. It serves only as a demonstration on how to customize Open WebUI for your specific use case. Want to contribute? Check out the contributing tutorial.
By default, when you configure Microsoft Entra ID OAuth and automatic group creation with Open WebUI, security groups are synced using their **Group IDs (GUIDs)** rather than human-readable group names. This is a Microsoft limitation where the ID token doesn't include group display names by default.
This tutorial explains how to configure Microsoft Entra ID to return group **names** instead of IDs, enabling a much better user experience when working with groups in Open WebUI.

#### Prerequisites

```
*  An Open WebUI instance configured with [Microsoft OAuth](https://docs.openwebui.com/features/authentication-access/auth/sso#microsoft)
*  An Azure account with permissions to modify App Registrations
*  Access to the Microsoft Entra admin center
*  Basic understanding of Microsoft Entra ID application configuration
```

#### Overview

To get human-readable group names in Open WebUI, you need to:
1. Configure your App Registration to include groups in the token
1. Modify the application manifest to use cloud\_displayname
1. Set groupMembershipClaims to ApplicationGroup only
1. Assign security groups to the Enterprise Application
1. Configure Open WebUI environment variables for [OAuth Group Management](https://docs.openwebui.com/features/authentication-access/auth/sso#oauth-group-management)
Key Requirement
The cloud\_displayname property in the manifest **only works** when groupMembershipClaims is set to ApplicationGroup . If you include other options (like SecurityGroup or All ), the token will revert to using Group IDs instead of names.

#### Step 1: Configure Token Claims in App Registration

```
1. Navigate to the  **Microsoft Entra admin center**  >  **App registrations**
1. Select your Open WebUI application
1. Go to  **Token configuration**  in the left menu
1. Click  **Add groups claim**
1. Select  **Security groups**  (or the appropriate group type for your needs)
1. Under  **Customize token properties by type** , ensure groups are added for:
*  ID token
    *  Access token
1. Click  **Add**
```

#### Step 2: Modify the Application Manifest

This is the critical step that enables group names instead of IDs.
1. In your App Registration, go to **Manifest** in the left menu
1. Locate the optionalClaims section
1. Add cloud\_displayname to the additionalProperties array for each token type
Your manifest should look like this:

```
"optionalClaims": {
    "idToken": [
        {
            "name": "groups",
            "source": null,
            "essential": false,
            "additionalProperties": [
                "cloud_displayname"
            ]
        }
    ],
    "accessToken": [
        {
            "name": "groups",
            "source": null,
            "essential": false,
            "additionalProperties": [
                "cloud_displayname"
            ]
        }
    ],
    "saml2Token": [
        {
            "name": "groups",
            "source": null,
            "essential": false,
            "additionalProperties": [
                "cloud_displayname"
            ]
        }
    ]
}
```

```
1.  **Critical** : Set groupMembershipClaims to ApplicationGroup only:
```

```
"groupMembershipClaims": "ApplicationGroup"
```

warning
If groupMembershipClaims includes other values like SecurityGroup or All , the cloud\_displayname property will be ignored and the token will contain Group IDs instead of names. See [Microsoft's optional claims documentation](https://learn.microsoft.com/en-us/entra/identity-platform/optional-claims) for more details.
1. Click **Save**

#### Step 3: Assign Groups to the Enterprise Application

When using ApplicationGroup , only groups explicitly assigned to the Enterprise Application will be included in the token.
1. Navigate to **Microsoft Entra admin center** > **Enterprise applications**
1. Find and select your Open WebUI application
1. Go to **Users and groups** in the left menu
1. Click **Add user/group**
1. Select the security groups you want to sync with Open WebUI
1. Click **Assign**
Multiple Group Assignment
When a user belongs to multiple groups, ensure all relevant groups are assigned to the Enterprise Application. Note that only groups explicitly assigned here will appear in the user's token and subsequently sync to Open WebUI.

#### Step 4: Configure API Permissions

Ensure your App Registration has the required Microsoft Graph permissions:
1. In your App Registration, go to **API permissions**
1. Click **Add a permission** > **Microsoft Graph** > **Delegated permissions**
1. Add the following permissions from the OpenID section if not already present:
\* openid
\* email
\* profile
1. Click **Grant admin consent for [your organization]**

#### Step 5: Configure Open WebUI Environment Variables

Configure the following environment variables for your Open WebUI deployment. For more details on each variable, see the [environment variable documentation](https://docs.openwebui.com/reference/env-configuration).

```
# Required: Your public WebUI address
WEBUI_URL=https://your-open-webui-domain

# Microsoft OAuth Configuration (required)
MICROSOFT_CLIENT_ID=your_client_id
MICROSOFT_CLIENT_SECRET=your_client_secret
MICROSOFT_CLIENT_TENANT_ID=your_tenant_id
MICROSOFT_REDIRECT_URI=https://your-open-webui-domain/oauth/microsoft/callback

# Required for logout to work properly
OPENID_PROVIDER_URL=https://login.microsoftonline.com/your_tenant_id/v2.0/.well-known/openid-configuration

# Enable OAuth signup
ENABLE_OAUTH_SIGNUP=true

# OAuth Group Management
OAUTH_GROUP_CLAIM=groups
ENABLE_OAUTH_GROUP_MANAGEMENT=true
ENABLE_OAUTH_GROUP_CREATION=true

# Recommended: Set a consistent secret key
WEBUI_SECRET_KEY=your_secure_secret_key
```

##### Environment Variable Reference

| Variable | Default | Description |
| --- | --- | --- |
| OAUTH\_GROUP\_CLAIM | groups | The claim in the ID/access token containing the user's group memberships. |
| ENABLE\_OAUTH\_GROUP\_MANAGEMENT | false | When true , user group memberships are synchronized with OAuth claims upon each login. |
| ENABLE\_OAUTH\_GROUP\_CREATION | false | When true , enables **Just-in-Time (JIT) group creation** - groups present in OAuth claims but not in Open WebUI will be created automatically. |

Strict Group Synchronization
When ENABLE\_OAUTH\_GROUP\_MANAGEMENT is set to true , a user's group memberships in Open WebUI are **strictly synchronized** with the groups received in their OAuth claims upon each login.
\* Users will be **added** to Open WebUI groups that match their OAuth claims.
\* Users will be **removed** from any Open WebUI groups (including those manually assigned within Open WebUI) if those groups are **not** present in their OAuth claims for that login session.

#### Verification

After completing the configuration:
1. **Test the token** : Use [https://jwt.ms](https://jwt.ms/) to decode your ID token and verify that the groups claim contains display names instead of GUIDs.
1. **Log in as a non-admin user** : Admin users' group memberships are not automatically updated via OAuth group management. Use a standard user account for testing.
1. **Check Open WebUI** : Navigate to the Admin Panel and verify that groups appear with readable names.
Admin Users
Admin users' group memberships are **not** automatically updated via OAuth group management. If you need to test the configuration, use a non-admin user account.

#### Additional Resources

```
*  [SSO (OAuth, OIDC, Trusted Header)](https://docs.openwebui.com/features/authentication-access/auth/sso) - OAuth configuration overview
*  [OAuth Group Management](https://docs.openwebui.com/features/authentication-access/auth/sso#oauth-group-management) - Group synchronization details
*  [Groups](https://docs.openwebui.com/features/authentication-access/rbac/groups) - Group management in Open WebUI
*  [SSO Troubleshooting Guide](https://docs.openwebui.com/troubleshooting/sso) - Common OAuth issues and solutions
*  [Environment Configuration](https://docs.openwebui.com/reference/env-configuration) - All environment variables
*  [Microsoft Optional Claims Documentation](https://learn.microsoft.com/en-us/entra/identity-platform/optional-claims) - Microsoft's official documentation
```

[Edit this page](https://github.com/open-webui/docs/blob/main/docs/tutorials/auth-sso/entra-group-name-sync.md)
[Previous Dual OAuth Configuration](https://docs.openwebui.com/tutorials/auth-sso/dual-oauth-configuration)
[Next Tailscale](https://docs.openwebui.com/tutorials/auth-sso/tailscale)
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