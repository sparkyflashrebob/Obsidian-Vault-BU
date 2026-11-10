---
tags:
  - notebooklm-import
notebook: "OpenWebUI"
category: "research"
---

Database Schema / Open WebUI
[Skip to main content](https://docs.openwebui.com/reference/database-schema#__docusaurus_skipToContent_fallback)
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
\* [Environment Variable Configuration](https://docs.openwebui.com/reference/env-configuration)
\* [HTTPS & Reverse Proxies](https://docs.openwebui.com/reference/https/)
\* [Monitoring](https://docs.openwebui.com/reference/monitoring/)
\* [Backend-Controlled API Flow](https://docs.openwebui.com/reference/api-flow)
\* [Database Schema](https://docs.openwebui.com/reference/database-schema)
\* [Network Diagrams](https://docs.openwebui.com/reference/network-diagrams)
\* [API Endpoints](https://docs.openwebui.com/reference/api-endpoints)
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
\* [📖 Reference](https://docs.openwebui.com/reference/)
\* Database Schema
On this page

### Database Schema

warning
This tutorial is a community contribution and is not supported by the Open WebUI team. It serves only as a demonstration on how to customize Open WebUI for your specific use case. Want to contribute? Check out the contributing tutorial.
[!WARNING] This documentation was created/updated based on version 0.8.6 and updated for recent migrations.

#### Open-WebUI Internal SQLite Database

For Open-WebUI, the SQLite database serves as the backbone for user management, chat history, file storage, and various other core functionalities. Understanding this structure is essential for anyone looking to contribute to or maintain the project effectively.

#### Internal SQLite Location

You can find the SQLite database at root -> data -> webui.db

```
📁 Root (/)
├── 📁 data
│   ├── 📁 cache
│   ├── 📁 uploads
│   ├── 📁 vector_db
│   └── 📄 webui.db
├── 📄 dev.sh
├── 📁 open_webui
├── 📄 requirements.txt
├── 📄 start.sh
└── 📄 start_windows.bat
```

#### Copy Database Locally

If you want to copy the Open-WebUI SQLite database running in the container to your local machine, you can use:

```
docker cp open-webui:/app/backend/data/webui.db ./webui.db
```

Alternatively, you can access the database within the container using:

```
docker exec -it open-webui /bin/sh
```

#### Table Overview

Here is a complete list of tables in Open-WebUI's SQLite database. The tables are listed alphabetically and numbered for convenience.

| **No.** | **Table Name** | **Description** |
| --- | --- | --- |
| 01 | access\_grant | Stores normalized access control grants for all resources |
| 02 | auth | Stores user authentication credentials and login information |
| 03 | channel | Manages chat channels and their configurations |
| 04 | channel\_file | Links files to channels and messages |
| 05 | channel\_member | Tracks user membership and permissions within channels |
| 06 | chat | Stores chat sessions and their metadata |
| 07 | chat\_file | Links files to chats and messages |
| 08 | chatidtag | Maps relationships between chats and their associated tags |
| 09 | config | Maintains system-wide configuration settings |
| 10 | document | Stores documents and their metadata for knowledge management |
| 11 | feedback | Captures user feedback and ratings |
| 12 | file | Manages uploaded files and their metadata |
| 13 | folder | Organizes files and content into hierarchical structures |
| 14 | function | Stores custom functions and their configurations |
| 15 | group | Manages user groups and their permissions |
| 16 | group\_member | Tracks user membership within groups |
| 17 | knowledge | Stores knowledge base entries and related information |
| 18 | knowledge\_file | Links files to knowledge bases |
| 19 | memory | Maintains chat history and context memory |
| 20 | message | Stores individual chat messages and their content |
| 21 | message\_reaction | Records user reactions (emojis/responses) to messages |
| 22 | migrate\_history | Tracks database schema version and migration records |
| 23 | model | Manages AI model configurations and settings |
| 24 | note | Stores user-created notes and annotations |
| 25 | oauth\_session | Manages active OAuth sessions for users |
| 26 | prompt | Stores templates and configurations for AI prompts |
| 27 | prompt\_history | Tracks version history and snapshots for prompts |
| 28 | skill | Stores reusable markdown instruction sets (Skills) |
| 29 | tag | Manages tags/labels for content categorization |
| 30 | tool | Stores configurations for system tools and integrations |
| 31 | user | Maintains user profiles and account information |

Note: there are two additional tables in Open-WebUI's SQLite database that are not related to Open-WebUI's core functionality, that have been excluded:
\* Alembic Version table
\* Migrate History table
Now that we have all the tables, let's understand the structure of each table.

#### Access Grant Table

| **Column Name** | **Data Type** | **Constraints** | **Description** |
| --- | --- | --- | --- |
| id | Integer | PRIMARY KEY, AUTOINCREMENT | Unique identifier |
| resource\_type | Text | NOT NULL | Type of resource (e.g., model , knowledge , tool ) |
| resource\_id | Text | NOT NULL | ID of the specific resource |
| principal\_type | Text | NOT NULL | Type of grantee: user or group |
| principal\_id | Text | NOT NULL | ID of the user or group (or \* for public) |
| permission | Text | NOT NULL | Permission level: read or write |
| created\_at | BigInteger | nullable | Grant creation timestamp |

Things to know about the access\_grant table:
\* Unique constraint on ( resource\_type , resource\_id , principal\_type , principal\_id , permission ) to prevent duplicate grants
\* Indexed on ( resource\_type , resource\_id ) and ( principal\_type , principal\_id ) for efficient lookups
\* Replaces the former access\_control JSON column that was previously embedded in each resource table
\* principal\_type of user with principal\_id of \* represents public (open) access
\* Supports both group-level and individual user-level access grants

#### Auth Table

| **Column Name** | **Data Type** | **Constraints** | **Description** |
| --- | --- | --- | --- |
| id | String | PRIMARY KEY | Unique identifier |
| email | String | - | User's email |
| password | Text | - | Hashed password |
| active | Boolean | - | Account status |

Things to know about the auth table:
\* Uses UUID for primary key
\* One-to-One relationship with users table (shared id)

#### Channel Table

| **Column Name** | **Data Type** | **Constraints** | **Description** |
| --- | --- | --- | --- |
| id | Text | PRIMARY KEY | Unique identifier (UUID) |
| user\_id | Text | - | Owner/creator of channel |
| type | Text | nullable | Channel type |
| name | Text | - | Channel name |
| description | Text | nullable | Channel description |
| data | JSON | nullable | Flexible data storage |
| meta | JSON | nullable | Channel metadata |

| created\_at | BigInteger | - | Creation timestamp (nanoseconds) | | updated\_at | BigInteger | - | Last update timestamp (nanoseconds) |
Things to know about the auth table:
\* Uses UUID for primary key
\* Case-insensitive channel names (stored lowercase)

#### Channel Member Table

| **Column Name** | **Data Type** | **Constraints** | **Description** |
| --- | --- | --- | --- |
| id | TEXT | NOT NULL | Unique identifier for the channel membership |
| channel\_id | TEXT | NOT NULL | Reference to the channel |
| user\_id | TEXT | NOT NULL | Reference to the user |
| created\_at | BIGINT | - | Timestamp when membership was created |

#### Channel File Table

| **Column Name** | **Data Type** | **Constraints** | **Description** |
| --- | --- | --- | --- |
| id | Text | PRIMARY KEY | Unique identifier (UUID) |
| user\_id | Text | NOT NULL | Owner of the relationship |
| channel\_id | Text | FOREIGN KEY(channel.id), NOT NULL | Reference to the channel |
| file\_id | Text | FOREIGN KEY(file.id), NOT NULL | Reference to the file |
| message\_id | Text | FOREIGN KEY(message.id), nullable | Reference to associated message |
| created\_at | BigInteger | NOT NULL | Creation timestamp |
| updated\_at | BigInteger | NOT NULL | Last update timestamp |

Things to know about the channel\_file table:
\* Unique constraint on ( channel\_id , file\_id ) to prevent duplicate entries
\* Foreign key relationships with CASCADE delete
\* Indexed on channel\_id , file\_id , and user\_id for performance

#### Chat Table

| **Column Name** | **Data Type** | **Constraints** | **Description** |
| --- | --- | --- | --- |
| id | String | PRIMARY KEY | Unique identifier (UUID) |
| user\_id | String | - | Owner of the chat |
| title | Text | - | Chat title |
| chat | JSON | - | Chat content and history |
| created\_at | BigInteger | - | Creation timestamp |
| updated\_at | BigInteger | - | Last update timestamp |
| share\_id | Text | UNIQUE, nullable | Sharing identifier |
| archived | Boolean | default=False | Archive status |
| pinned | Boolean | default=False, nullable | Pin status |
| meta | JSON | server\_default="" | Metadata including tags |
| folder\_id | Text | nullable | Parent folder ID |

#### Chat File Table

| **Column Name** | **Data Type** | **Constraints** | **Description** |
| --- | --- | --- | --- |
| id | Text | PRIMARY KEY | Unique identifier (UUID) |
| user\_id | Text | NOT NULL | User associated with the file |
| chat\_id | Text | FOREIGN KEY(chat.id), NOT NULL | Reference to the chat |
| file\_id | Text | FOREIGN KEY(file.id), NOT NULL | Reference to the file |
| message\_id | Text | nullable | Reference to associated message |
| created\_at | BigInteger | NOT NULL | Creation timestamp |
| updated\_at | BigInteger | NOT NULL | Last update timestamp |

Things to know about the chat\_file table:
\* Unique constraint on ( chat\_id , file\_id ) to prevent duplicate entries
\* Foreign key relationships with CASCADE delete
\* Indexed on chat\_id , file\_id , message\_id , and user\_id for performance
**Why this table was added:**
\* **Query Efficiency** : Before this, files were embedded in message objects. This table allows direct indexed lookups for finding all files in a chat without iterating through every message.
\* **Data Consistency** : Acts as a single source of truth for file associations. In multi-node deployments, all nodes query this table instead of relying on potentially inconsistent embedded data.
\* **Deduplication** : The database-level unique constraint prevents duplicate file associations, which is more reliable than application-level checks.

#### Chat ID Tag Table

| **Column Name** | **Data Type** | **Constraints** | **Description** |
| --- | --- | --- | --- |
| id | VARCHAR(255) | NOT NULL | Unique identifier |
| tag\_name | VARCHAR(255) | NOT NULL | Name of the tag |
| chat\_id | VARCHAR(255) | NOT NULL | Reference to chat |
| user\_id | VARCHAR(255) | NOT NULL | Reference to user |
| timestamp | INTEGER | NOT NULL | Creation timestamp |

#### Config

| **Column Name** | **Data Type** | **Constraints** | **Default** | **Description** |
| --- | --- | --- | --- | --- |
| id | INTEGER | NOT NULL | - | Primary key identifier |
| data | JSON | NOT NULL | - | Configuration data |
| version | INTEGER | NOT NULL | - | Config version number |
| created\_at | DATETIME | NOT NULL | CURRENT\_TIMESTAMP | Creation timestamp |
| updated\_at | DATETIME | - | CURRENT\_TIMESTAMP | Last update timestamp |

#### Feedback Table

| **Column Name** | **Data Type** | **Constraints** | **Description** |
| --- | --- | --- | --- |
| id | Text | PRIMARY KEY | Unique identifier (UUID) |
| user\_id | Text | - | User who provided feedback |
| version | BigInteger | default=0 | Feedback version number |
| type | Text | - | Type of feedback |
| data | JSON | nullable | Feedback data including ratings |
| meta | JSON | nullable | Metadata (arena, chat\_id, etc) |
| snapshot | JSON | nullable | Associated chat snapshot |
| created\_at | BigInteger | - | Creation timestamp |
| updated\_at | BigInteger | - | Last update timestamp |

#### File Table

| **Column Name** | **Data Type** | **Constraints** | **Description** |
| --- | --- | --- | --- |
| id | String | PRIMARY KEY | Unique identifier |
| user\_id | String | - | Owner of the file |
| hash | Text | nullable | File hash/checksum |
| filename | Text | - | Name of the file |
| path | Text | nullable | File system path |
| data | JSON | nullable | File-related data |
| meta | JSON | nullable | File metadata |

| created\_at | BigInteger | - | Creation timestamp | | updated\_at | BigInteger | - | Last update timestamp |
The meta field's expected structure:

```
{
    "name": string,          # Optional display name
    "content_type": string,  # MIME type
    "size": integer,         # File size in bytes
    # Additional metadata supported via ConfigDict(extra="allow")
}
```

#### Folder Table

| **Column Name** | **Data Type** | **Constraints** | **Description** |
| --- | --- | --- | --- |
| id | Text | PK (composite) | Unique identifier (UUID) |
| parent\_id | Text | nullable | Parent folder ID for hierarchy |
| user\_id | Text | PK (composite) | Owner of the folder |
| name | Text | - | Folder name |
| items | JSON | nullable | Folder contents |
| data | JSON | nullable | Additional folder data |
| meta | JSON | nullable | Folder metadata |
| is\_expanded | Boolean | default=False | UI expansion state |
| created\_at | BigInteger | - | Creation timestamp |
| updated\_at | BigInteger | - | Last update timestamp |

Things to know about the folder table:
\* Primary key is composite ( id , user\_id )
\* Folders can be nested ( parent\_id reference)
\* Root folders have null parent\_id
\* Folder names must be unique within the same parent

#### Function Table

| **Column Name** | **Data Type** | **Constraints** | **Description** |
| --- | --- | --- | --- |
| id | String | PRIMARY KEY | Unique identifier |
| user\_id | String | - | Owner of the function |
| name | Text | - | Function name |
| type | Text | - | Function type |
| content | Text | - | Function content/code |
| meta | JSON | - | Function metadata |
| valves | JSON | - | Function control settings |
| is\_active | Boolean | - | Function active status |
| is\_global | Boolean | - | Global availability flag |
| created\_at | BigInteger | - | Creation timestamp |
| updated\_at | BigInteger | - | Last update timestamp |

Things to know about the function table:
\* type can only be: ["filter", "action"]

#### Group Table

| **Column Name** | **Data Type** | **Constraints** | **Description** |
| --- | --- | --- | --- |
| id | Text | PRIMARY KEY, UNIQUE | Unique identifier (UUID) |
| user\_id | Text | - | Group owner/creator |
| name | Text | - | Group name |
| description | Text | - | Group description |
| data | JSON | nullable | Additional group data |
| meta | JSON | nullable | Group metadata |
| permissions | JSON | nullable | Permission configuration |
| created\_at | BigInteger | - | Creation timestamp |
| updated\_at | BigInteger | - | Last update timestamp |

Note: The user\_ids column has been migrated to the group\_member table.

#### Group Member Table

| **Column Name** | **Data Type** | **Constraints** | **Description** |
| --- | --- | --- | --- |
| id | Text | PRIMARY KEY, UNIQUE | Unique identifier (UUID) |
| group\_id | Text | FOREIGN KEY(group.id), NOT NULL | Reference to the group |
| user\_id | Text | FOREIGN KEY(user.id), NOT NULL | Reference to the user |
| created\_at | BigInteger | nullable | Creation timestamp |
| updated\_at | BigInteger | nullable | Last update timestamp |

Things to know about the group\_member table:
\* Unique constraint on ( group\_id , user\_id ) to prevent duplicate memberships
\* Foreign key relationships with CASCADE delete to group and user tables

#### Knowledge Table

| **Column Name** | **Data Type** | **Constraints** | **Description** |
| --- | --- | --- | --- |
| id | Text | PRIMARY KEY, UNIQUE | Unique identifier (UUID) |
| user\_id | Text | - | Knowledge base owner |
| name | Text | - | Knowledge base name |
| description | Text | - | Knowledge base description |
| data | JSON | nullable | Knowledge base content |
| meta | JSON | nullable | Additional metadata |

| created\_at | BigInteger | - | Creation timestamp | | updated\_at | BigInteger | - | Last update timestamp |

#### Knowledge File Table

| **Column Name** | **Data Type** | **Constraints** | **Description** |
| --- | --- | --- | --- |
| id | Text | PRIMARY KEY | Unique identifier (UUID) |
| user\_id | Text | NOT NULL | Owner of the relationship |
| knowledge\_id | Text | FOREIGN KEY(knowledge.id), NOT NULL | Reference to the knowledge base |
| file\_id | Text | FOREIGN KEY(file.id), NOT NULL | Reference to the file |
| created\_at | BigInteger | NOT NULL | Creation timestamp |
| updated\_at | BigInteger | NOT NULL | Last update timestamp |

Things to know about the knowledge\_file table:
\* Unique constraint on ( knowledge\_id , file\_id ) to prevent duplicate entries
\* Foreign key relationships with CASCADE delete
\* Indexed on knowledge\_id , file\_id , and user\_id for performance
Access control for resources (models, knowledge bases, tools, prompts, notes, files, channels) is managed through the access\_grant table rather than embedded JSON. Each grant entry specifies a resource, a principal (user or group), and a permission level (read or write). See the [Access Grant Table](https://docs.openwebui.com/reference/database-schema#access-grant-table) section above for details.

#### Memory Table

| **Column Name** | **Data Type** | **Constraints** | **Description** |
| --- | --- | --- | --- |
| id | String | PRIMARY KEY | Unique identifier (UUID) |
| user\_id | String | - | Memory owner |
| content | Text | - | Memory content |
| created\_at | BigInteger | - | Creation timestamp |
| updated\_at | BigInteger | - | Last update timestamp |

#### Message Table

| **Column Name** | **Data Type** | **Constraints** | **Description** |
| --- | --- | --- | --- |
| id | Text | PRIMARY KEY | Unique identifier (UUID) |
| user\_id | Text | - | Message author |
| channel\_id | Text | nullable | Associated channel |
| parent\_id | Text | nullable | Parent message for threads |
| content | Text | - | Message content |
| data | JSON | nullable | Additional message data |
| meta | JSON | nullable | Message metadata |
| created\_at | BigInteger | - | Creation timestamp (nanoseconds) |
| updated\_at | BigInteger | - | Last update timestamp (nanoseconds) |

#### Message Reaction Table

| **Column Name** | **Data Type** | **Constraints** | **Description** |
| --- | --- | --- | --- |
| id | Text | PRIMARY KEY | Unique identifier (UUID) |
| user\_id | Text | - | User who reacted |
| message\_id | Text | - | Associated message |
| name | Text | - | Reaction name/emoji |
| created\_at | BigInteger | - | Reaction timestamp |

#### Model Table

| **Column Name** | **Data Type** | **Constraints** | **Description** |
| --- | --- | --- | --- |
| id | Text | PRIMARY KEY | Model identifier |
| user\_id | Text | - | Model owner |
| base\_model\_id | Text | nullable | Parent model reference |
| name | Text | - | Display name |
| params | JSON | - | Model parameters |
| meta | JSON | - | Model metadata |

| is\_active | Boolean | default=True | Active status | | created\_at | BigInteger | - | Creation timestamp | | updated\_at | BigInteger | - | Last update timestamp |

#### Note Table

| **Column Name** | **Data Type** | **Constraints** | **Description** |
| --- | --- | --- | --- |
| id | Text | PRIMARY KEY | Unique identifier |
| user\_id | Text | nullable | Owner of the note |
| title | Text | nullable | Note title |
| data | JSON | nullable | Note content and data |
| meta | JSON | nullable | Note metadata |

| created\_at | BigInteger | nullable | Creation timestamp | | updated\_at | BigInteger | nullable | Last update timestamp |

#### OAuth Session Table

| **Column Name** | **Data Type** | **Constraints** | **Description** |
| --- | --- | --- | --- |
| id | Text | PRIMARY KEY | Unique session identifier |
| user\_id | Text | FOREIGN KEY(user.id) | Associated user |
| provider | Text | - | OAuth provider (e.g., 'google') |
| token | Text | - | OAuth session token |
| expires\_at | BigInteger | - | Token expiration timestamp |
| created\_at | BigInteger | - | Session creation timestamp |
| updated\_at | BigInteger | - | Session last update timestamp |

#### Prompt Table

| **Column Name** | **Data Type** | **Constraints** | **Description** |
| --- | --- | --- | --- |
| id | Text | PRIMARY KEY | Unique identifier (UUID) |
| command | String | UNIQUE, INDEX | Unique command identifier |
| user\_id | String | NOT NULL | Owner of the prompt |
| name | Text | NOT NULL | Display name of the prompt |
| content | Text | NOT NULL | Prompt content/template |
| data | JSON | nullable | Additional prompt data |
| meta | JSON | nullable | Prompt metadata |

| is\_active | Boolean | default=True | Active status | | version\_id | Text | nullable | Current version identifier | | tags | JSON | nullable | Associated tags | | created\_at | BigInteger | NOT NULL | Creation timestamp | | updated\_at | BigInteger | NOT NULL | Last update timestamp |

#### Prompt History Table

| **Column Name** | **Data Type** | **Constraints** | **Description** |
| --- | --- | --- | --- |
| id | Text | PRIMARY KEY | Unique identifier (UUID) |
| prompt\_id | Text | FOREIGN KEY(prompt.id), INDEX | Reference to the prompt |
| parent\_id | Text | nullable | Reference to the parent version |
| snapshot | JSON | NOT NULL | Snapshot of the prompt at version |
| user\_id | Text | NOT NULL | User who created the version |
| commit\_message | Text | nullable | Version commit message |
| created\_at | BigInteger | NOT NULL | Creation timestamp |

#### Skill Table

| **Column Name** | **Data Type** | **Constraints** | **Description** |
| --- | --- | --- | --- |
| id | Text | PRIMARY KEY | Unique identifier (UUID) |
| user\_id | Text | NOT NULL | Owner/creator of the skill |
| name | Text | NOT NULL | Display name of the skill |
| description | Text | nullable | Short description (used in manifest) |
| content | Text | NOT NULL | Full skill instructions (Markdown) |
| data | JSON | nullable | Additional skill data |
| meta | JSON | nullable | Skill metadata |
| is\_active | Boolean | default=True | Active status |
| created\_at | BigInteger | NOT NULL | Creation timestamp |
| updated\_at | BigInteger | NOT NULL | Last update timestamp |

Things to know about the skill table:
\* Uses UUID for primary key
\* Access control is managed through the access\_grant table (resource\_type skill )
\* description is injected into the system prompt as part of the manifest; content is loaded on-demand via the view\_skill builtin tool

#### Tag Table

| **Column Name** | **Data Type** | **Constraints** | **Description** |
| --- | --- | --- | --- |
| id | String | PK (composite) | Normalized tag identifier |
| name | String | - | Display name |
| user\_id | String | PK (composite) | Tag owner |
| meta | JSON | nullable | Tag metadata |

Things to know about the tag table:
\* Primary key is composite (id, user\_id)

#### Tool Table

| **Column Name** | **Data Type** | **Constraints** | **Description** |
| --- | --- | --- | --- |
| id | String | PRIMARY KEY | Unique identifier |
| user\_id | String | - | Tool owner |
| name | Text | - | Tool name |
| content | Text | - | Tool content/code |
| specs | JSON | - | Tool specifications |
| meta | JSON | - | Tool metadata |
| valves | JSON | - | Tool control settings |

| created\_at | BigInteger | - | Creation timestamp | | updated\_at | BigInteger | - | Last update timestamp |

#### User Table

| **Column Name** | **Data Type** | **Constraints** | **Description** |
| --- | --- | --- | --- |
| id | String | PRIMARY KEY | Unique identifier |
| username | String(50) | nullable | User's unique username |
| name | String | - | User's name |
| email | String | - | User's email |
| role | String | - | User's role |
| profile\_image\_url | Text | - | Profile image path |
| bio | Text | nullable | User's biography |
| gender | Text | nullable | User's gender |
| date\_of\_birth | Date | nullable | User's date of birth |
| last\_active\_at | BigInteger | - | Last activity timestamp |
| updated\_at | BigInteger | - | Last update timestamp |
| created\_at | BigInteger | - | Creation timestamp |
| api\_key | String | UNIQUE, nullable | API authentication key |
| settings | JSON | nullable | User preferences |
| info | JSON | nullable | Additional user info |
| oauth\_sub | Text | UNIQUE | OAuth subject identifier |
| scim | JSON | nullable | SCIM provisioning data |

Things to know about the user table:
\* Uses UUID for primary key
\* One-to-One relationship with auth table (shared id)
\* One-to-One relationship with oauth\_session table (via user\_id foreign key)
The scim field's expected structure:

```
{
    "": {
        "external_id": string,  # externalId from the identity provider
    },
    # Multiple providers can be stored simultaneously
    # Example:
    # "microsoft": { "external_id": "abc-123" },
    # "okta": { "external_id": "def-456" }
}
```

**Why this column was added:**
\* **SCIM account linking** : Stores per-provider externalId values from SCIM provisioning, enabling identity providers (like Azure AD, Okta) to match users by their external identifiers rather than relying solely on email.
\* **Multi-provider support** : The per-provider key structure allows a single user to be provisioned from multiple identity providers simultaneously, each storing their own externalId .
\* **OAuth fallback** : When looking up a user by externalId , the system falls back to matching against oauth\_sub if no scim entry is found, enabling seamless linking of SCIM-provisioned and OAuth-authenticated accounts.

#### Entity Relationship Diagram

To help visualize the relationship between the tables, refer to the below Entity Relationship Diagram (ERD) generated with Mermaid.
has
owns
owns
creates
owns
owns
provides
manages
manages
manages
owns
manages
creates
creates
has
creates
manages
manages
owns
has
has
tagged\_with
organized\_in
contains
replies
user
string
id
PK
string
username
string
name
string
email
string
role
text
profile\_image\_url
text
bio
text
gender
date
date\_of\_birth
bigint
last\_active\_at
string
api\_key
json
settings
json
info
text
oauth\_sub
json
scim
auth
string
id
PK
string
email
text
password
boolean
active
chat
string
id
PK
string
user\_id
FK
string
title
json
chat
text
share\_id
boolean
archived
boolean
pinned
json
meta
text
folder\_id
FK
channel
text
id
PK
text
user\_id
FK
text
name
text
description
json
data
json
meta
json
access\_control
message
text
id
PK
text
user\_id
FK
text
channel\_id
FK
text
parent\_id
FK
text
content
json
data
json
meta
folder
text
id
PK
composite
text
user\_id
PK
composite
text
parent\_id
FK
text
name
json
items
json
data
json
meta
boolean
is\_expanded
file
string
id
PK
string
user\_id
FK
text
hash
text
filename
text
path
json
data
json
meta
json
access\_control
feedback
text
id
PK
text
user\_id
FK
bigint
version
text
type
json
data
json
meta
json
snapshot
function
string
id
PK
string
user\_id
FK
text
name
text
content
json
meta
json
valves
boolean
is\_active
boolean
is\_global
group
text
id
PK
text
user\_id
FK
text
name
text
description
json
data
json
meta
json
permissions
json
user\_ids
knowledge
text
id
PK
text
user\_id
FK
text
name
text
description
json
data
json
meta
json
access\_control
memory
string
id
PK
string
user\_id
FK
text
content
model
text
id
PK
text
user\_id
FK
text
base\_model\_id
FK
text
name
json
params
json
meta
json
access\_control
boolean
is\_active
prompt
text
id
PK
string
command
string
user\_id
FK
text
name
text
content
json
data
json
meta
json
access\_control
boolean
is\_active
text
version\_id
json
tags
prompt\_history
text
id
PK
text
prompt\_id
FK
text
parent\_id
FK
json
snapshot
text
user\_id
FK
text
commit\_message
tag
string
id
PK
composite
string
user\_id
PK
composite
string
name
json
meta
skill
text
id
PK
text
user\_id
FK
text
name
text
description
text
content
json
data
json
meta
boolean
is\_active
tool
string
id
PK
string
user\_id
FK
text
name
text
content
json
specs
json
meta
json
valves
json
access\_control
note
text
id
PK
text
user\_id
FK
text
title
json
data
json
meta
json
access\_control
oauth\_session
text
id
PK
text
user\_id
FK
text
provider
text
token
bigint
expires\_at
message\_reaction
text
id
PK
text
user\_id
FK
text
message\_id
FK
text
name

#### Database Encryption with SQLCipher

For enhanced security, Open WebUI supports at-rest encryption for its primary SQLite database using SQLCipher. This is recommended for deployments handling sensitive data where using a larger database like PostgreSQL is not needed.

##### Prerequisites

SQLCipher encryption requires additional dependencies that are **not included by default** . Before using this feature, you must install:
\* The **SQLCipher system library** (e.g., libsqlcipher-dev on Debian/Ubuntu, sqlcipher on macOS via Homebrew)
\* The **sqlcipher3-wheels** Python package ( pip install sqlcipher3-wheels )
For Docker users, this means building a custom image with these dependencies included.

##### Configuration

To enable encryption, set the following environment variables:

```
# Required: Set the database type to use SQLCipher
DATABASE_TYPE=sqlite+sqlcipher

# Required: Set a secure password for database encryption
DATABASE_PASSWORD=your-secure-password
```

When these are set and a full DATABASE\_URL is **not** explicitly defined, Open WebUI will automatically create and use an encrypted database file at ./data/webui.db .

##### Important Notes

danger
\* The **DATABASE\_PASSWORD** environment variable is **required** when using sqlite+sqlcipher .
\* The **DATABASE\_TYPE** variable tells Open WebUI which connection logic to use. Setting it to sqlite+sqlcipher activates the encryption feature.
\* **Keep the password secure** , as it is needed to decrypt and access all application data.
\* **Losing the password means losing access to all data** in the encrypted database.
Migrating Existing Data to SQLCipher
**Open WebUI does not support automatic migration from an unencrypted SQLite database to an encrypted SQLCipher database.** If you enable SQLCipher on an existing installation, the application will fail to read your existing unencrypted data.
To use SQLCipher with existing data, you must either:
1. **Start fresh** - Enable SQLCipher on a new installation and have users export/re-import their chats manually
1. **Manual database migration** - Use external SQLite/SQLCipher tools to export data from the unencrypted database and import it into a new encrypted database (advanced users only)
1. **Use filesystem-level encryption** - Consider alternatives like LUKS (Linux) or BitLocker (Windows) for at-rest encryption without database-level changes
1. **Switch to PostgreSQL** - For multi-user deployments, PostgreSQL with TLS provides encryption in transit and can be combined with encrypted storage

##### Related Database Environment Variables

| Variable | Default | Description |
| --- | --- | --- |
| DATABASE\_TYPE | None | Set to sqlite+sqlcipher for encrypted SQLite |
| DATABASE\_PASSWORD | - | Encryption password (required for SQLCipher) |
| DATABASE\_ENABLE\_SQLITE\_WAL | False | Enable Write-Ahead Logging for better performance |
| DATABASE\_POOL\_SIZE | None | Database connection pool size |
| DATABASE\_POOL\_TIMEOUT | 30 | Pool connection timeout in seconds |
| DATABASE\_POOL\_RECYCLE | 3600 | Pool connection recycle time in seconds |

For more details, see the [Environment Variable Configuration](https://docs.openwebui.com/reference/env-configuration) documentation.
[Edit this page](https://github.com/open-webui/docs/blob/main/docs/reference/database-schema.md)
[Previous Backend-Controlled API Flow](https://docs.openwebui.com/reference/api-flow)
[Next Network Diagrams](https://docs.openwebui.com/reference/network-diagrams)
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