---
tags:
  - notebooklm-import
notebook: "OpenWebUI"
category: "research"
---

Contributing to Docs / Open WebUI
[Skip to main content](https://docs.openwebui.com/tutorials/contributing-tutorial#__docusaurus_skipToContent_fallback)
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
\* Contributing to Docs
On this page

### Contributing to Documentation

warning
This tutorial is a community contribution and is not supported by the Open WebUI team. It serves only as a demonstration on how to customize Open WebUI for your specific use case. Want to contribute? Check out the contributing tutorial.
We appreciate your interest in contributing tutorials to the Open WebUI documentation. Follow the steps below to set up your environment and submit your tutorial.

#### Contributing Steps

```
1.  **Fork the open-webui/docs GitHub Repository**
*  Navigate to the [Open WebUI Docs Repository](https://github.com/open-webui/docs) on GitHub.
    *  Click the  **Fork**  button at the top-right corner to create a copy under your GitHub account.
1.  **Enable GitHub Actions**
*  In your forked repository, navigate to the  **Actions**  tab.
    *  If prompted, enable GitHub Actions by following the on-screen instructions.
1.  **Enable GitHub Pages**
*  Go to  **Settings**  >  **Pages**  in your forked repository.
    *  Under  **Source** , select the branch you want to deploy (e.g., main ) and the folder (e.g., /docs ).
    *  Click  **Save**  to enable GitHub Pages.
1.  **Configure GitHub Environment Variables**
*  In your forked repository, go to  **Settings**  >  **Secrets and variables**  >  **Actions**  >  **Variables** .
    *  Add the following environment variables:
        *  BASE_URL set to /docs (or your chosen base URL for the fork).
        *  SITE_URL set to https://.github.io/ .
```

##### 📝 Updating the GitHub Pages Workflow and Config File

If you need to adjust deployment settings to fit your custom setup, here's what to do:
a. **Update .github/workflows/gh-pages.yml**
\* Add environment variables for BASE\_URL and SITE\_URL to the build step if necessary:

```
  - name: Build
    env:
      BASE_URL: ${{ vars.BASE_URL }}
      SITE_URL: ${{ vars.SITE_URL }}
    run: npm run build
```

b. **Modify docusaurus.config.ts to Use Environment Variables**
\* Update docusaurus.config.ts to use these environment variables, with default values for local or direct deployment:

```
const config: Config = {
  title: "Open WebUI",
  tagline: "ChatGPT-Style WebUI for LLMs (Formerly Ollama WebUI)",
  favicon: "images/favicon.png",
  url: process.env.SITE_URL || "https://openwebui.com",
  baseUrl: process.env.BASE_URL || "/",
  ...
};
```

```
*  This setup ensures consistent deployment behavior for forks and custom setups.
1.  **Run the gh-pages GitHub Workflow**
*  In the  **Actions**  tab, locate the gh-pages workflow.
    *  Trigger the workflow manually if necessary, or it may run automatically based on your setup.
1.  **Browse to Your Forked Copy**
*  Visit https://.github.io/ to view your forked documentation.
1.  **Draft Your Changes**
*  In your forked repository, navigate to the appropriate directory (e.g., docs/tutorial/ ).
    *  Create a new markdown file for your tutorial or edit existing ones.
    *  Ensure that your tutorial includes the unsupported warning banner.
1.  **Submit a Pull Request**
*  Once your tutorial is ready, commit your changes to your forked repository.
    *  Navigate to the original open-webui/docs repository.
    *  Click  **New Pull Request**  and select your fork and branch as the source.
    *  Provide a descriptive title and description for your PR.
    *  Submit the pull request for review.
```

#### Important

Community-contributed tutorials must include the the following:

```
:::warning

This tutorial is a community contribution and is not supported by the Open WebUI team. It serves only as a demonstration on how to customize Open WebUI for your specific use case. Want to contribute? Check out the contributing tutorial.

:::
```

tip
How to Test Docusaurus Locally You can test your Docusaurus site locally with the following commands:

```
npm install   # Install dependencies
npm run build # Build the site for production
```

This will help you catch any issues before deploying
[Edit this page](https://github.com/open-webui/docs/blob/main/docs/tutorials/contributing-tutorial.md)
[Previous Backups](https://docs.openwebui.com/tutorials/maintenance/backups)
[Next ❓ FAQ](https://docs.openwebui.com/faq)
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