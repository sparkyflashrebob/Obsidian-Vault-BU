### Technical Implementation Plan: Standardizing Enterprise Agentic Workflows with Antigravity CLI
#### 1. Strategic Alignment and Objectives
In the current high-velocity engineering landscape, the transition from fragmented "vibe-coding" to disciplined, enterprise-grade AI orchestration is no longer optional. As Lead DevOps Architect, the objective of this implementation plan is to move beyond individual-centric AI usage toward a standardized, team-wide agentic workflow powered by the Antigravity CLI. This Go-based engine acts as a unified terminal interface that coordinates reasoning, multi-file editing, and tool execution, replacing the sunsetting Gemini CLI with a snappier, lower-memory footprint environment.
The "So What?" factor of this standardization lies in the shift from human trust to programmatic enforcement. By utilizing AGENTS.md and automated Lifecycle Hooks, we establish a  **Policy-as-Code**  model for AI agents. This ensures that every interaction—regardless of the developer's experience level—adheres to strict architectural parity, maintains high code quality via mandatory testing triggers, and follows safety compliance protocols that block unauthorized modifications to sensitive directories.
This plan rests on three primary pillars:
*   **Environmental Consistency:**  Establishing a unified binary deployment and SSH-aware authentication flow across all local and remote surfaces.
*   **Reusable Skillsets:**  Codifying team-level knowledge into version-controlled "Agent Skills" to eliminate prompt engineering overhead.
*   **Automated Lifecycle Governance:**  Implementing event-driven interceptors for idempotent code formatting and safety-gate enforcement.
Standardizing this foundational environment is the prerequisite for scaling autonomous agents into the broader CI/CD and production lifecycle.
#### 2. Baseline Environment Configuration and Deployment
A predictable agentic environment requires a unified binary installation and a robust authentication flow. As an Architect, I prescribe a standardized installation protocol to ensure the agy binary remains globally accessible and functional across heterogeneous operating systems and remote headless environments.
##### Cross-Platform Installation and Path Verification
The installation must be executed via the official Antigravity distribution scripts.
*   **macOS and Linux:**
*  The binary resides in ~/.local/bin/.
*   **Windows (Native PowerShell):**
*  The binary resides in %LOCALAPPDATA%\Antigravity\.
**Post-Install Protocol:**  The installer is designed to print the specific shell profile line required if the directory is not detected on the PATH. All engineers must verify the binary is globally reachable by running agy --version.
##### Legacy Migration Path
For teams transitioning from the legacy Gemini CLI, an idempotent migration command is provided to pull extensions, preferences, and auth states into the new runtime:
```bash
agy plugin import gemini

```
##### SSH-Aware Authentication
To solve friction points in remote development, the CLI utilizes  **SSH-aware logic** . When agy detects a remote session, it bypasses local browser triggers and instead provides a unique authorization URL and a one-time code. The developer completes the OAuth handshake on their local machine, and the CLI caches the credentials in the system keyring (Keychain, Credential Manager, or libsecret). For CI/CD pipelines, the ANTIGRAVITY_API_KEY environment variable must be utilized for headless authentication.
##### Verification and State Inspection
Verification of the orchestration layer is performed via:
*  agy inspect: The definitive tool for verifying active hooks, skills, and project configurations.
*  /usage: Used within the TUI to monitor rate-limit status across model families.
#### 3. Workspace Governance via AGENTS.md
The AGENTS.md file acts as the "instructional anchor" for all agentic interactions within a repository. Strategically, this file eliminates manual prompt repetition by prepending repository-level constraints to every agent interaction. This ensures that the agent's "brain" is always synchronized with the team's architectural standards before a single line of code is written.
##### Implementation Standard
All repositories must include an AGENTS.md at the project root. This file should codify language preferences, pattern constraints, and operational triggers. A critical standard for our team is the mandatory testing trigger:  **"Run**  **pnpm test**  **after every change that touches**  **src/**  **."**  This specific instruction minimizes CI/CD overhead by ensuring agents verify their work locally before a commit is ever pushed.
##### Markdown Specification Example
```markdown
# Repository Governance & Standards

## Architectural Constraints
- Primary Language: TypeScript.
- Pattern Preference: Functional programming (avoid class-based implementations).
- Typing: Strict mode enabled. Never use the `any` type; define explicit interfaces.

## Operational Triggers
- Testing: Run `pnpm test` after every change that touches `src/`.
- Documentation: All exported functions must include JSDoc headers.

## Safety Guardrails
- Protected Directories: Never modify files in `vendor/` or `dist/`.
- Permission: Alert user before any tool call that deletes more than 5 files.

```
By prepending these rules, we move from "asking" the AI for compliance to "defining" the environment's operational bounds.
#### 4. Engineering Reusable Team Operations with Agent Skills
"Agent Skills" are reusable, Markdown-defined slash commands that package complex instructions into one-word interactions. They are essential for reducing prompt engineering variance across a distributed team.
##### Distribution and Governance Model
To ensure version-controlled parity, all team-level skills must be committed to the repository.
*   **Workspace-Specific Skills:**  Reside in .agents/skills/. These are the standard for project-specific operations.
*   **Global Skills:**  Reside in ~/.gemini/antigravity-cli/skills/. Reserved for universal developer utilities.
##### Skill Definition Protocol
A Skill file must define the prompt, allowed tools, and any nested subagents. For instance, a /lint or /refactor skill can be implemented by creating a refactor.md file in the workspace skills directory. Once saved, the command becomes immediately available as a slash command within the Terminal User Interface (TUI). This structure allows us to turn high-frequency engineering tasks into predictable, repeatable sub-routines.
#### 5. Implementing Automated Lifecycle Hooks and Safety Interceptors
Lifecycle Hooks transform the Antigravity agent into an active, compliant worker by enabling  **Idempotent Hook Execution** . These JSON-defined interceptors allow us to programmatically enforce standards at three critical triggers:  **before a tool call** ,  **after a file edit** , and at  **session start** .
##### Policy Enforcement Case Study: Post-Edit Hooks
The high-value use case for Hooks is the implementation of automated "Safety Interceptors." For example, a Post-Edit Hook can be configured to automatically run gofmt after every file write, ensuring the agent's output is always compliant with the language's style guide.
More importantly, Hooks provide a technical safeguard against "hallucinated" edits. A hook can be programmed to block any attempt to modify the vendor/ directory, regardless of the prompt. This "trust-but-verify" technical architecture ensures that the agent operates within a strictly governed sandbox, providing an essential layer of protection for enterprise codebases.
#### 6. Orchestrating Parallelism with Async Subagents
For large-scale technical migrations, such as converting callback handlers to context.Context, we utilize  **Async Subagent Mode** . This allows the primary agent to dispatch long-running tasks to specialized workers while the developer maintains an active foreground conversation.
##### Dispatch and Command Shortcuts
Subagents are dispatched via the /agent command. For quick, one-shot completions or terminal-specific help, developers should utilize  **Command Mode**  via the following keyboard shortcuts:
*   **Cmd + I**  (macOS)
*   **Ctrl + I**  (Windows/Linux)
##### Parallelism vs. Quota Trade-off
While subagents provide massive velocity gains, they consume API quota in parallel. Architects must enforce a directive where developers check /usage before dispatching massive /agent tasks to prevent workflow lockouts.
##### Operating Mode Comparison Matrix
| Operating Mode | Primary Interface | Ideal Use Case | Shortcut |
| ------ | ------ | ------ | ------ |
| **Interactive TUI** | Scrollable Pane | Exploratory coding & reasoning | agy |
| **Command Mode** | One-shot / Inline | Quick terminal help / CI jobs | Cmd/Ctrl + I |
| **Async Subagent** | Background Tasking | Parallel refactors & migrations | /agent |
| **SDK / API Mode** | Programmatic | Custom agent harnesses / Bots | N/A |

#### 7. Verification, Monitoring, and Enterprise Maintenance
In an agentic ecosystem, observability is the final frontier. Maintaining technical excellence requires active  **State Inspection**  and resource governance.
##### MCP and State Inspection
The agy inspect command is the definitive tool for troubleshooting. It provides a real-time summary of:
*   **mcp_config.json:**  Discovered MCP servers, ensuring remote servers include the mandatory serverUrl field.
*   **Active Hooks:**  Verification that safety interceptors are correctly loaded.
*   **Project Context:**  Discovered AGENTS.md and Skills.
##### Quota Governance and Advanced Review
Developers must monitor the /usage command to track rate limits across  **Gemini 3.6 Flash** ,  **Gemini 3.1 Pro** ,  **Claude Sonnet 4.6** ,  **Claude Opus 4.6** , and  **GPT-OSS 120B** .
For tasks involving complex architectural changes, we utilize the /export command to sync sessions to the  **Antigravity 2.0**  desktop application. This transition is strategic: the GUI provides  **Visual Diff Reviews**  and  **Graph Views**  that are essential for verifying the integrity of large-scale refactors that exceed the visualization capabilities of a standard terminal.
By adhering to this implementation plan, the organization ensures a scalable, high-performance development lifecycle where AI agents are integrated, governed, and optimized for long-term technical excellence.
