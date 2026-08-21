# Krisp & Bee Daily Notes Report Automation - Attendee Extraction and Definition Rules Reference

## 📌 Executive Summary
This reference document defines the official **Attendee Extraction and Definition Rules** for automated synthesis of `Bee_Data` transcripts into Obsidian Daily Notes (`Bee Daily Note YYMMDD.md`).

To maintain a high-fidelity knowledge architecture, **Attendees** must strictly reflect real, identified human participants who actively engage in intentional, two-way conversations on that date. Non-person takeaway headers, retail clerk encounters, passive background listeners, and transcript mislabelings are strictly excluded.

---

## 👥 Attendee Extraction and Definition Rules

### 1. Core Definition
An **Attendee** is defined as a known, identified individual who actively participates in a structured, purposeful, two-way conversation with the primary speaker (Andy).

---

### 2. Inclusion Criteria (Must meet ALL)
- **Identified**: The person's identity is known (by name, title, or specific relationship).
- **Engaged**: The person actively speaks, responds, or collaborates in the dialogue (minimum 2 dialogue turns in a multi-turn session).
- **Intentional**: The meeting has a clear context or purpose (e.g., scheduled sync, interview, or focused discussion, or confirmed via Google Calendar event).

---

### 3. Exclusion Criteria (Do NOT extract as attendees)
- **Non-Person Summary Headers**: Section titles or takeaway bullet headers from raw Bee markdown files (e.g., *Accessibility*, *Awareness*, *Appreciation*, *Automation Gap*, *Weather observation*).
- **Casual Strangers / Retail Workers**: Brief, unstructured encounters on the street, with cashier/clerk workers during errands, or pharmacy counter transactions.
- **Passive Listeners**: People who are present in the room or background but do not speak or contribute to the dialogue.
- **Self-Talk & Monologues**: Dictated thoughts, journal monologues, personal voice assistant commands, or observations about the environment.
- **Unidentified Voices & Audio Engine Mislabelings**: Unknown background voices, podcast/news media content, or single-turn mislabelings captured by the transcript engine.

---

### 4. Extraction & Formatting Rules

#### Standard Format
For each valid conversation, extract and format attendees using this exact structure:
`- [Name / Title] ([Relationship/Organization if known])`

#### Relationship & Title Mapping
Known contacts are automatically enriched with their relationship or organization context:

| Speaker Name | Formatted Attendee Display | Context / Relationship |
| :--- | :--- | :--- |
| **Andy** | `Andy` | Host / Primary Speaker |
| **Andrea** | `Andrea (Wife)` | Wife / Household Partner |
| **Audel** | `Audel (SDRT Collaborator)` | Co-Participant in SDRT Meetings |
| **Will** | `Will (Collaborator)` | Technical / Project Collaborator |
| **Bruce** | `Bruce (Friend / Brother)` | Close Personal Friend |
| **Cori Bilyayev** | `Cori Bilyayev (Pariyatti Instructor)` | Pariyatti Course Instructor |
| **Ed Brown** | `Ed Brown (Zen Teacher)` | Zen Teacher / Practice Facilitator |
| **Ajahn Sumedho** | `Ajahn Sumedho (Theravada Monastic Teacher)` | Theravada Buddhist Teacher |
| **Ajahn Amaro** | `Ajahn Amaro (Abhayagiri Monastery Abbot)` | Abhayagiri Monastery Abbot |
| **Ajahn Nyaniko** | `Ajahn Nyaniko (Abhayagiri Monk)` | Abhayagiri Resident Monk |

---

## ⚙️ Technical Resolution & Calendar Cross-Referencing

1. **Dialogue Section Scoping**: Ingestion only parses dialogue lines from the `## Transcriptions` section of raw Bee files, ignoring summary/takeaway bullet headers.
2. **Engagement Threshold**: Speakers extracted from audio transcripts must have $\ge 2$ active dialogue turns in a multi-turn conversation to rule out single-fragment mislabelings or retail clerk interactions.
3. **Google Calendar Sync Resolution**: When a scheduled meeting takes place (e.g., `Audel & Andy SDRT`), the pipeline cross-references confirmed calendar events for `target_date_str` to resolve identified participants even if raw transcript engines labeled their speech as `Unknown`.

---
*Technical Reference Document maintained in `Flashrebob Obsidian\__Web Dev information`.*
