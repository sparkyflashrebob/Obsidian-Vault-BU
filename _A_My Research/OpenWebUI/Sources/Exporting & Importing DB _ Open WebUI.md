---
tags:
  - notebooklm-import
notebook: "OpenWebUI"
category: "research"
---

Exporting & Importing DB / Open WebUI
[Skip to main content](https://docs.openwebui.com/tutorials/maintenance/database#__docusaurus_skipToContent_fallback)
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
\* [S3 Storage](https://docs.openwebui.com/tutorials/maintenance/s3-storage)
\* [Offline Mode](https://docs.openwebui.com/tutorials/maintenance/offline-mode)
\* [Exporting & Importing DB](https://docs.openwebui.com/tutorials/maintenance/database)
\* [Backups](https://docs.openwebui.com/tutorials/maintenance/backups)
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
\* [Maintenance](https://docs.openwebui.com/tutorials/maintenance/)
\* Exporting & Importing DB
On this page

### Exporting & Importing DB

warning
This tutorial is a community contribution and is not supported by the Open WebUI team. It serves only as a demonstration on how to customize Open WebUI for your specific use case. Want to contribute? Check out the contributing tutorial.
If you need to migrate your **Open WebUI** data (e.g., chat histories, configurations, etc.) from one server to another or back it up for later use, you can export and import the database. This guide assumes you're running Open WebUI using the internal SQLite database (not PostgreSQL).
Follow the steps below to export and import the webui.db file, which contains your database.

##### Exporting Database

To export the database from your current Open WebUI instance:
1. **Use docker cp to copy the database file** : The webui.db file is located in the container inside the directory /app/backend/data . Run the following command to copy it into your local machine:

```
docker cp open-webui:/app/backend/data/webui.db ./webui.db
```

```
1.  **Transfer the exported file to the new server** : You can use  **FileZilla**  or any other file transfer tool of your choice to move the webui.db file to the new server. info FileZilla is recommended for its ease of use when transferring files to the new server.
```

##### Importing Database

After moving the webui.db file to the new server, follow these steps:
1. **Install and Run Open WebUI on the New Server** : Set up and run Open WebUI using a Docker container. Follow the instructions provided in the [🚀 Getting Started](https://docs.openwebui.com/getting-started) to install and start the Open WebUI container. Once it's running, stop it before performing the import step.

```
docker stop open-webui
```

```
1.  **Use docker cp to copy the database file to the container** : Assuming the exported webui.db file is in your current working directory, copy it into the container:
```

```
docker cp ./webui.db open-webui:/app/backend/data/webui.db
```

```
1.  **Start the Open WebUI container** : Start the container again to use the imported database.
```

```
docker start open-webui
```

The new server should now be running Open WebUI with your imported database.

##### Notes

```
*  This export/import process  **only works if you're using the internal SQLite database ( webui.db )** .
*  If you're using an external PostgreSQL database, this method is not applicable because the database is managed outside the container. For PostgreSQL, you'd need to follow PostgreSQL-specific tools and procedures to back up and restore your database.
```

##### Why It's Important

This approach is particularly useful when:
\* Migrating your Open WebUI data to a new server or machine.
\* Creating backups of your data before an update or modification.
\* Testing Open WebUI on multiple servers with the same setup.

```
# Quick commands summary for export and import

# Export:
docker cp open-webui:/app/backend/data/webui.db ./webui.db

# Stop container on the new server:
docker stop open-webui

# Import:
docker cp ./webui.db open-webui:/app/backend/data/webui.db

# Start container:
docker start open-webui
```

With these steps, you can easily manage your Open WebUI migration or backup process. Keep in mind the database format you're using to ensure compatibility.

#### Related Guides

```
*  [SQLite Database Overview](https://docs.openwebui.com/reference/database-schema) - Detailed database schema and SQLCipher encryption setup
*  [Backups](https://docs.openwebui.com/tutorials/maintenance/backups) - Comprehensive backup strategies for your instance
```

[Edit this page](https://github.com/open-webui/docs/blob/main/docs/tutorials/maintenance/database.mdx)
[Previous Offline Mode](https://docs.openwebui.com/tutorials/maintenance/offline-mode)
[Next Backups](https://docs.openwebui.com/tutorials/maintenance/backups)
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