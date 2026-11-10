### SOP: Autonomous Software Development Lifecycle in Antigravity AI
#### 1. System Architecture and Operational Logic
Antigravity AI represents a paradigm shift in software engineering through "Vibe Coding"—a methodology that lowers the technical barrier to entry to zero while significantly increasing the requirement for precise prompt engineering. This environment transitions the professional from a manual coder to a high-level orchestrator and strategic reviewer. The Local Workspace functions as the persistent state layer for the autonomous agent, ensuring architectural consistency across session boundaries through state synchronization and deterministic prompt structures.
The operational logic is governed by a  **Human-Agent Interaction**  model, defining two primary human responsibilities:
1.  **Task Description:**  The orchestrator defines high-level objectives (e.g., bug fixes, feature additions, or full-scale application builds) to set the mission parameters for the AI agent.
2.  **Code Review:**  The orchestrator monitors the agent’s output and artifacts. While manual coding is optional, the professional must evaluate the agent's work, providing iterative feedback to approve progress or request refinements.
The system utilizes two primary interfaces: the  **Agent Manager**  (Mission Control), which serves as a conversational inbox for monitoring live agent progress, and the  **Editor**  (VS Code-style interface), which provides a dedicated hub for file management, manual code adjustments, and terminal command execution.
##### Strategic Model Selection
Optimizing output quality requires selecting the appropriate "AI Brain" for specific architectural layers:
*   **Gemini 1.5 Pro:**  Best for front-end development and creating visually appealing User Interfaces.
*   **Claude 3.5 (Sonnet/Opus):**  Recommended for complex backend logic and sophisticated code structures.
*   **GPT:**  Ideal for everyday, fast, and low-complexity tasks.
Understanding this architecture is the prerequisite for establishing a stable local environment where the AI’s labor is physically captured.
#### 2. Local Workspace Initialization
The workspace is the physical anchor for all AI-generated artifacts. Because the agent functions as an autonomous worker, it requires a designated local repository to maintain state.
##### Initialization Procedure
1.  **Software Acquisition:**  Download the Antigravity AI client for Mac OS, Windows, or Linux from the official portal.
2.  **Repository Creation:**  Manually create a folder on your local machine to serve as the project repository.
3.  **Workspace Mapping:**  Within the Antigravity interface, use the "Manage Repository" or "Open Folder" flow to navigate to your directory. Confirm "Trust Authors" to grant necessary read/write permissions.
##### Artifact State Management
As the agent executes, it populates the local folder with "Artifacts" that represent the project's cumulative state.
| Artifact Type | Description | Role in Project |
| ------ | ------ | ------ |
| **Code Files** | HTML, CSS, JS, and backend files. | The functional core of the software. |
| **Task Lists** | Sequential steps generated during Planning Mode. | Transparency into agent logic and roadmap. |
| **Walkthrough File** | A central log containing screenshots and recordings. | Primary location for reviewing autonomous testing. |
| **Screenshots** | Visual captures from the built-in browser. | Used for UI verification and layout debugging. |
| **Recordings** | Video files of browser-based functional tests. | Demonstrates real-time verification of features. |

Once the physical directory is established, the logical framework must be defined through structured instruction files.
#### 3. Configuration of System Instructions and Brand Guidelines
Structured Markdown files are critical for reducing hallucinations and ensuring brand alignment. These files serve as the "Explicit Instruction" that directs the agent's power.
##### System Instructions (Gemini.md)
This master prompt uses hierarchical Markdown syntax (e.g., # for H1, ## for H2) to help the AI understand text priority. You must define the following using  **bolded headers** :
*   **# Navigation Structures:**  Define top navigation tabs and user flow.
*   **# Header Elements:**  Specify UI components to be included in the site header.
*   **# Page Elements:**  Outline layouts for dashboards, lists, or specific views.
*   **# Feature Tracking:**  Detail requirements for core logic (e.g., income, expenses, and budget limits).
##### Brand Guidelines (brand guidelines.md)
Detail the visual identity to ensure aesthetic consistency:
*   **Primary, Secondary, and Neutral Colors:**  Define specific hex codes.
*   **Logo Usage:**  Placement and scaling instructions.
*   **Typography:**  Font families and text hierarchies.
*   **UI Elements:**  Styling for buttons, cards, and interactive forms.
Consider the  **Usain Bolt Analogy** : A world-class sprinter is incredibly powerful, but if instructed to run in the wrong direction, his speed becomes a liability. Vibe Coding requires higher linguistic precision than traditional coding because the agent’s speed can rapidly compound errors if instructions lack deterministic structure.
#### 4. Autonomous Execution and Agent Policy Management
The system allows for a strategic trade-off between autonomous speed and manual oversight through execution modes and review policies.
##### Execution Modes
*   **Planning Mode:**  Mandatory for complex builds. The agent generates a task list and implementation strategy for review before writing code.
*   **Fast Mode:**  The agent skips planning and executes tasks directly. Reserved for minor text changes or low-risk updates.
##### Configuring Review Policies
Navigate to User Settings > Agent to configure the level of autonomy:
1.  **Always Proceed:**  The agent executes steps and terminal commands without pausing. This maximizes productivity but increases the risk of the agent deviating from the intended path.
2.  **Request Review:**  The agent stops after every step for approval. This is the safest approach for sensitive projects requiring high security and command verification.
While "Always Proceed" allows the orchestrator to step away, it requires high confidence in the initial system instructions.
#### 5. Multi-Agent Orchestration and Resource Constraints
Architects can run parallel agents within a single workspace to handle simultaneous development tasks (e.g., one agent focusing on UI while another handles Backend logic).
##### Parallel Orchestration
New agents are initiated by starting a new conversation within the Agent Manager. These agents operate under the same workspace and instruction files, allowing for a "divide and conquer" strategy that significantly reduces the total development timeline.
##### Resource Constraints and Rate Limits
System performance is bound by the context window and provider rate limits.
**CAUTION: SYSTEM LIMITS**  Overloading the system with excessive parallel tasks or data can trigger rate limits. Failure to monitor system feedback may result in forced plan upgrades or a  **mandatory 5-day waiting period**  before access is restored.
#### 6. The Iterative 'Undo-and-Feedback' Development Cycle
AI development is non-linear and relies on a rigorous verification sequence.
##### The Three-Step Verification Process
1.  **Autonomous Testing:**  The agent utilizes its  **built-in Chrome browser**  to act "like a human would"—clicking buttons and filling forms to verify functional logic.
2.  **Artifact Review:**  Analyze the screenshots and video recordings stored in the  **Walkthrough File**  to verify the agent's testing session.
3.  **Local Hosting:**  Access the application via the provided "Localhost" link for a final, hands-on verification in your browser.
##### Refinement and the "Undo" Fail-Safe
Use the  **"Comment on Plan"**  feature to iterate on specific tasks without rebuilding the entire project. If an iteration fails, utilize the  **"Undo" arrow**  located in the  **Agent Manager interface** . This allows the workspace to revert to a specific point in the development timeline, providing a critical fail-safe for aggressive experimentation.
#### 7. External Capability Extension via MCP Servers
The Model Context Protocol (MCP) is the strategic layer that connects Antigravity AI to the broader software ecosystem, allowing the agent to move beyond the local codebase.
##### Technical Procedure for MCP Integration (e.g., n8n)
1. Navigate to  **Manage MCP Servers** .
2. Select  **View Raw Config**  to reveal the JSON structure.
3. In your external tool (e.g., n8n), navigate to  **MCP Access**  and copy the access token or JSON string.
4.  **Manually edit the JSON**  in Antigravity by pasting the configuration, then save and refresh.
**CRITICAL SECURITY WARNING**  Your MCP JSON configuration contains sensitive access tokens.  **Do not share this JSON file with anyone** , as it grants full access to your connected accounts.
##### Strategic Value
MCP integration allows the agent to perform real-world actions: triggering automations in  **n8n** , sending status updates to  **Slack** , or pulling live data from  **Google Sheets** . This transforms the local software into an integrated component of a broader operational workflow, empowering the professional to master the Antigravity environment.
