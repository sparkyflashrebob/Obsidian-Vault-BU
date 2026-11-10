---
tags:
  - notebooklm-import
notebook: "OpenWebUI"
category: "research"
---

🤝 Contributing / Open WebUI
[Skip to main content](https://docs.openwebui.com/contributing#__docusaurus_skipToContent_fallback)
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
\* [❓ FAQ](https://docs.openwebui.com/faq)
\* [🛣 Roadmap](https://docs.openwebui.com/roadmap)
\* [🛡 Security Policy](https://docs.openwebui.com/security)
\* [🤝 Contributing](https://docs.openwebui.com/contributing)
\* [💖 Sponsorships](https://docs.openwebui.com/sponsorships)
\* [🎨 Brand Guidelines](https://docs.openwebui.com/brand)
\* [⚖ Open WebUI License](https://docs.openwebui.com/license)
\* [🎯 Our Mission](https://docs.openwebui.com/mission)
\* [👥 Our Team](https://docs.openwebui.com/team)
\* 🤝 Contributing
On this page

### 🤝 Contributing

**Help build the AI interface everyone deserves.**
Open WebUI is an independent project built and maintained by a small, dedicated core team. Whether you test dev builds, fix bugs, improve docs, or translate the UI, every contribution makes the project better for thousands of users. This page explains how to get involved and what to expect.

#### Code of Conduct

All contributors and community participants must follow the **Code of Conduct** . We operate under a **zero-tolerance policy** : disrespectful, demanding, or hostile behavior results in immediate action without prior warning.
This project is built by volunteers in their free time. Treat every interaction with professionalism and respect.

#### Ways to Contribute

##### Test the development branch

One of the most valuable contributions requires no code at all. Run the dev branch, use it daily, and report what breaks.

```
docker run -d -p 3000:8080 -v open-webui:/app/backend/data --name open-webui ghcr.io/open-webui/open-webui:dev
```

The dev branch moves fast, so **pull updates regularly** . If Docker is not your preference, follow the [Developing Open WebUI](https://docs.openwebui.com/getting-started/advanced-topics/development) instead.
Report issues on [GitHub](https://github.com/open-webui/open-webui/issues) with clear reproduction steps. We cannot deliver high-quality releases without community testing.

##### Submit code

We welcome pull requests. Before submitting one:
1. **Open a discussion first.** Propose your idea [here](https://github.com/open-webui/open-webui/discussions/new/choose) so the team can align on approach before you write code.
1. **Follow existing conventions.** Match the project's coding standards, naming patterns, and architecture.
1. **Keep PRs atomic.** Each pull request should address a single objective. If scope grows, split it into smaller, logically independent PRs.
1. **Avoid new external dependencies.** Do not add libraries or frameworks without prior discussion. We aim to stay framework-agnostic and implement functionality ourselves when practical.
1. **Include tests.** Cover new features with tests and update documentation as needed.
1. **Write clear commit messages.** Descriptive messages make review and history tracking easier.

##### Improve documentation

Help make Open WebUI more accessible by improving docs, writing tutorials, or creating setup guides. Documentation lives in the [docs repository](https://github.com/open-webui/docs).

##### Translate the UI

Open WebUI uses JSON translation files in src/lib/i18n/locales . Each subdirectory is named with an [ISO 639 language code](http://www.lingoes.net/en/translator/langcode.htm) (e.g., en-US , fr-FR ).
To add a new language:
1. Create a new directory under src/lib/i18n/locales named with the appropriate language code
1. Copy the en-US translation files into the new directory
1. Translate the string values in each JSON file while preserving the object structure
1. Register the language in src/lib/i18n/locales/languages.json

##### Improve accessibility

Accessibility is a core part of good design. When contributing UI changes:

| Principle | What to do |
| --- | --- |
| **Semantic HTML** | Use  ,  ,  , and other semantic elements instead of generic wrappers |
| **Keyboard navigation** | Ensure all interactive elements work without a mouse |
| **ARIA labels** | Add [ARIA](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA) roles and labels where semantic HTML alone is insufficient |
| **Color contrast** | Verify contrast ratios with [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/) |
| **Alt text** | Provide descriptive alt for meaningful images; use alt="" for decorative ones |

Test your changes with Lighthouse or your browser's accessibility tools.

#### Reporting Issues

Check the [Issues tab](https://github.com/open-webui/open-webui/issues) before opening a new one. When filing:
\* **Use the issue template.** Issues that do not follow the template or lack requested information will be closed.
\* **Include reproduction steps.** Describe what you did, what you expected, and what actually happened.
\* **Be specific.** Vague reports ("it doesn't work") cannot be investigated effectively.
Scope of support
Open WebUI supports Docker deployment, but we assume familiarity with Docker fundamentals. Issues related to reverse proxy configuration, container networking, or host OS setup are outside the project's support scope. Refer to the [official Docker documentation](https://docs.docker.com/get-started/overview/) for those topics.

#### Get in Touch

| Channel | Link |
| --- | --- |
| **Discord** | [discord.gg/5rJgQTnV4s](https://discord.gg/5rJgQTnV4s) |
| **Reddit** | [r/OpenWebUI](https://www.reddit.com/r/OpenWebUI/) |
| **GitHub Issues** | [open-webui/open-webui/issues](https://github.com/open-webui/open-webui/issues) |
| **GitHub Discussions** | [open-webui/open-webui/discussions](https://github.com/open-webui/open-webui/discussions) |

[Edit this page](https://github.com/open-webui/docs/blob/main/docs/contributing.mdx)
[Previous 🛡 Security Policy](https://docs.openwebui.com/security)
[Next 💖 Sponsorships](https://docs.openwebui.com/sponsorships)
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