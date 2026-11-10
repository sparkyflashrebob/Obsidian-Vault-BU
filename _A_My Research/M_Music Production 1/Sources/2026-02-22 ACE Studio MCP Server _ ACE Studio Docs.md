---
tags:
  - notebooklm-import
notebook: "M_Music Production 1"
category: "research"
---

# WebSync metadata

* title: ACE Studio MCP Server | ACE Studio Docs
* url: https://docs.acestudio.ai/ai-tools/ace-studio-mcp-server
* date: 2026-02-22T21:57:02.609Z

circle-exclamation Experimental Status

The ACE Studio MCP Server is currently in *experimental phase*.

*Please note:*

Some features and settings may not be fully implemented yet

Features and functionality may change

You may encounter bugs or performance issues during use

Usage guidelines and rate limits will be published when the stable version is released

We are actively improving this feature. If you have any feedback or encounter issues, please contact us at *[email protected]* envelope .

The ACE Studio MCP server offers a rich toolkit enabling AI agents to autonomously navigate and execute creative edits. By giving AI agents comprehensive insight into every detail of your project, it empowers them to assist you in creating and editing songs with greater speed and creative freedom.

The Model Context Protocol arrow-up-right <https://modelcontextprotocol.io/docs/getting-started/intro> (MCP) is an open standard that enables AI assistants to seamlessly connect with external applications and data sources. The ACE Studio MCP server implements this protocol to give AI agents direct access to your creative workspace.

Quick Start hashtag

1.

Open the *ACE Studio 2.0*

2.

From the preferences, check the *General → MCP Server*

\*Server Address:\*http://localhost:21572/mcp

*Technical Note*: The ACE Studio MCP Server uses the *Streamable HTTP transport protocol*. Keep this address for the next configuration step.

hashtag

Choose the appropriate configuration method based on your AI client:

Claude Desktop

⚠Setting up the ACE Studio MCP Server in Claude Desktop requires editing a JSON configuration file. If you're not comfortable with technical configuration, we recommend trying more user-friendly clients.

*Configuration Steps:*

1.

Install Node.js (if not already installed)

Visit nodejs.org arrow-up-right <https://nodejs.org> and download the LTS version

2.

Locate the Claude Desktop configuration file

*macOS*: ~/Library/Application Support/Claude/claude\_desktop\_config.json

*Windows*: %APPDATA%\Claude\claude\_desktop\_config.json

3.

Edit the configuration file and add the following:

1.

Save the file and restart Claude Desktop

\*Verify Connection:\*Type in Claude:

If Claude returns project details, the connection is successful!

---

Cursor

You can directly add MCP server to Cursor by clicking here arrow-up-right <https://cursor.com/en-US/install-mcp?name=ACE-Studio&config=eyJ1cmwiOiJodHRwOi8vbG9jYWxob3N0OjIxNTcyL21jcCJ9>.

Or manually setup:

1.

Open Cursor settings

2.

Find the "Tools & MCP" section

3.

Click "New MCP Server"

4.

Fill in the following JSON:

5.

Click "Save"

6.

Restart Cursor

\*Verify Connection:\*Type in Cursor Chat:

---

hashtag

You can directly add MCP server to VS Code by clicking here arrow-up-right <https://insiders.vscode.dev/redirect?url=vscode%3Amcp%2Finstall%3F%7B%22name%22%3A%22acestudio%22%2C%22type%22%3A%22http%22%2C%22url%22%3A%22http%3A%2F%2Flocalhost%3A21572%2Fmcp%22%7D>.

Or manually setup:

1.

Install the Cline or Roo Cline extension

2.

Open extension settings

3.

Find the MCP Servers configuration section

4.

Add a new server:

---

hashtag

1.

Install the Cline or Roo Code extension

2.

Open extension settings

3.

Find the MCP Servers configuration section

4.

Add a new server:

---

hashtag

For most clients\*,\* use these configuration settings:

*Transport type:* Streamable HTTP (some clients may call this "Remote")

\*Server URL:\*http://localhost:21572/mcp

Or import MCP server by the following JSON:

Usage Examples

Once connected, you can try the following prompts to collaborate with your AI assistant:

hashtag hashtag Edit MIDI

Previous Doubles  Next Cloning A Voice for Vocal Synth

Last updated