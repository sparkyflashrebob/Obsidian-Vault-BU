---
title: "Daily Notes Report Automation — System Prompt & Technical Reference"
date: "2026-08-19"
tags:
  - daily-notes-report
  - bee-nlm-report
  - krisp-daily-summary
  - plaud-daily-report
  - system-prompt
  - technical-reference
---

# Daily Notes Report Automation — System Prompt & Technical Reference

## 📌 Executive Purpose & Overview

The primary purpose of the **Daily Notes Report Automation** is to transform raw, fragmented ambient audio recordings captured across any of your devices (**Plaud NotePin**, **Bee Wearable**, **Krisp**, or future audio recorders) into a single, unified, searchable personal knowledge system within Obsidian.

Regardless of which physical device or combination of devices captures your day:
1. **Universal Audio Ingestion:** Ingests raw audio from Plaud, Bee, Krisp, or direct phone USB sync.
2. **Local PC Processing:** Uses direct `s16le 16kHz PCM` audio decoding and local `faster-whisper` AI models to generate word-for-word dialogue transcripts with 0 cloud subscription dependencies.
3. **Unified Daily Note Synthesis:** Distills waking hours into executive synopses, key thematic topics, personal reflections, and administrative task progress.
4. **Action Item Extraction:** Identifies explicit commitments and tasks, tagging them for `@AwnDee` and `@Andrea` in clean Markdown check-list format (`- [ ]`).
5. **Cross-Linking & Categorization:** Applies standardized YAML frontmatter tags for seamless querying across your Obsidian Master Vault (Dataview, Search, Graph view).

---

## 🤖 Universal LLM System Prompt

Below is the exact universal System Prompt used across your daily report generators ([`plaud_daily_report_generator.py`](file:///g:/Documents/_Antigravity%20Sandbox/Workflow%20Automations/plaud_daily_report_generator.py), [`bee_daily_report_generator.py`](file:///g:/Documents/_Antigravity%20Sandbox/Workflow%20Automations/bee_daily_report_generator.py), and [`krisp_daily_report_generator.py`](file:///g:/Documents/_Antigravity%20Sandbox/Workflow%20Automations/krisp_daily_report_generator.py)) to synthesize daily audio into Obsidian Daily Notes:

```markdown
You are an expert executive editor, personal archivist, and workflow strategist. Your job is to analyze raw transcript files from ambient voice recordings (Plaud, Bee, Krisp) and synthesize them into a structured, elegant Obsidian Daily Note Report.

### CORE INSTRUCTIONS & MANDATES:
1. **Preserve Spoken Dialogue Integrity:** Retain exact quotes, timestamps, and speaker identifications (AwnDee vs Andrea) without altering the true meaning.
2. **Synthesize Key Topics:** Group conversations logically by category (Technical Troubleshooting, Financials & Administration, Personal Health & Relationships, Current Events & Culture, Voice Profiling).
3. **Extract Actionable Tasks:** Locate every commitment made by AwnDee or Andrea and format them as `- [ ] Task Description - [Target Date]`.
4. **Apply Standardized Tags:** Include frontmatter tags for easy Obsidian Dataview indexing.

### OUTPUT SCHEMA & LAYOUT:
---
date: "YYYY-MM-DD"
tags:
  - plaud-daily-report
  - bee-nlm-report
  - krisp-daily-summary
  - 12-step-framework
  - ambient-sensors
  - household-logistics
---

# Daily Note [YYMMDD] — [Day of Week], [Month DD, YYYY]

## 📌 Executive Summary
A concise 2-3 sentence overview of the day's major themes, activities, and technical progress.

## 🗣️ Full Spoken Dialogue Highlights
Grouped dialogue blocks with timestamps `[HH:MM - HH:MM]` and speaker tags (**AwnDee** / **Andrea**).

## 🧠 System Audits & Personal Reflections
Detailed breakdowns of technical setups, philosophical reflections, health updates, and daily planning reviews.

## 📋 Action Items
**@AwnDee**
- [ ] [Task description] - [Target Date]

**@Andrea**
- [ ] [Task description] - [Target Date]
```

---

## ⚙️ Technical Architecture & Pipeline Data Flow

```mermaid
flowchart TD
    A["Audio Recorders (Plaud NotePin / Bee Device / Krisp)"] -->|Raw Audio (.opus / .wav)| B["Phone / PC Watch Folder"]
    B -->|USB Sync Watchdog| C["watchdog_phone_mp3_sync.py"]
    C -->|FFmpeg s16le 16kHz PCM| D["Local PC faster-whisper Model"]
    D -->|Word-for-Word Transcript| E["Plaud Conversations (.md)"]
    E -->|Master Prompt Generator| F["plaud_daily_report_generator.py"]
    F -->|Obsidian Daily Note| G["Obsidian Master Vault / Daily Note Reports"]
```

---

## 📁 Key Files & Directories Map

- **Obsidian Plaud Daily Note Reports:** [`G:\Google Drive (260611)\Obsidian Master Vault\Flashrebob Obsidian\_A_My Journal and Notes\Plaud Daily Note Reports\`](file:///G:/Google%20Drive%20%28260611%29/Obsidian%20Master%20Vault/Flashrebob%20Obsidian/_A_My%20Journal%20and%20Notes/Plaud%20Daily%20Note%20Reports/)
- **Obsidian Bee NLM Reports:** [`G:\Google Drive (260611)\Obsidian Master Vault\Flashrebob Obsidian\_A_My Journal and Notes\Bee - NLM Reports\`](file:///G:/Google%20Drive%20%28260611%29/Obsidian%20Master%20Vault/Flashrebob%20Obsidian/_A_My%20Journal%20and%20Notes/Bee%20-%20NLM%20Reports/)
- **Local Audio Transcripts:** [`G:\Google Drive (260611)\Plaud Conversations\`](file:///G:/Google%20Drive%20%28260611%29/Plaud%20Conversations/)
- **Audio Archive MP3s:** [`G:\Google Drive (260611)\Plaud Audio Archive\`](file:///G:/Google%20Drive%20%28260611%29/Plaud%20Audio%20Archive/)
- **Python Automation Generators:**
  - [`plaud_daily_report_generator.py`](file:///g:/Documents/_Antigravity%20Sandbox/Workflow%20Automations/plaud_daily_report_generator.py)
  - [`bee_daily_report_generator.py`](file:///g:/Documents/_Antigravity%20Sandbox/Workflow%20Automations/bee_daily_report_generator.py)
  - [`krisp_daily_report_generator.py`](file:///g:/Documents/_Antigravity%20Sandbox/Workflow%20Automations/krisp_daily_report_generator.py)
