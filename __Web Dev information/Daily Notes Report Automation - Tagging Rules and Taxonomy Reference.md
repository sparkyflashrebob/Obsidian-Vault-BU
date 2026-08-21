# Krisp & Bee Daily Notes Report Automation - Tagging Rules and Taxonomy Reference

## 📌 Executive Summary
This reference document defines the official **Tagging Rules and Taxonomy Architecture** for automated synthesis of `Bee_Data` transcripts into Obsidian Daily Notes (`Bee Daily Note YYMMDD.md`).

To maintain a high-fidelity, searchable knowledge architecture, tags are dynamically extracted per date from explicit content and structured into **four distinct metadata categories**.

---

## 🏷️ The 4 Metadata Tag Categories

Every daily report dynamically extracts and categorizes metadata tags into the following four groups:

### 1. 📌 Core Topics
- **Definition**: The primary subject matter, high-level themes, or overarching domains discussed during the day's recording sessions.
- **Rules**: 1–3 words maximum. No vague filler words. Reflects explicit date content.
- **Examples**: `#docker-setup`, `#fixed-income-strategy`, `#team-leadership`, `#meditation-group`, `#quantum-physics`, `#electronic-music`.

### 2. 🛠️ Entities
- **Definition**: Specific software products, hardware tools, named frameworks, organizations, places, or titled media mentioned in the transcripts.
- **Rules**: 1–3 words maximum. Exact named references.
- **Examples**: `#docker-desktop`, `#fidelity-investments`, `#college-of-marin`, `#palm-skin-productions`, `#canopy-library-service`, `#crispr-ng-script`, `#what-the-bleep-film`.

### 3. ⚡ Action Categories
- **Definition**: The operational, intellectual, or practical modes of activity engaged in during the date.
- **Rules**: 1–3 words maximum. Functional category terms ending in `-ing` or `-strategy` where appropriate.
- **Examples**: `#troubleshooting`, `#financial-inquiry`, `#software-automation`, `#media-curation`, `#community-building`, `#environmental-monitoring`, `#quality-auditing`.

### 4. 🔍 Keywords
- **Definition**: 5 to 10 highly specific, searchable index terms extracted for instant vault querying and cross-note linking.
- **Rules**: 1–2 words maximum per keyword. Strictly 5–10 terms total per report.
- **Examples**: `#docker`, `#bonds`, `#meditation`, `#leadership`, `#crispr`, `#dubstep`, `#canopy`, `#wildfires`, `#tai-chi`, `#quantum`.

---

## ⚙️ Extraction & Formatting Rules

1. **Short Length Constraint**: Every individual tag must strictly be **1 to 3 words maximum** (slugified with hyphens, e.g. `team-leadership`).
2. **No Filler Words**: Generic or ambiguous terms (e.g. `stuff`, `things`, `discussion`, `daily-chat`, `general`) are strictly prohibited.
3. **Explicit Content Only**: Tags must be derived from explicit words, titles, tools, or subjects recorded in the `Bee_Data` summaries and transcripts. Never infer unstated assumptions.
4. **Frontmatter vs. Logistics Display**:
   - **YAML Frontmatter**: All tags from all 4 categories are aggregated cleanly as standard YAML list items (`tags: - docker-setup ...`).
   - **Logistics Header (Section 1)**: Displayed under four dedicated icon rows:
     - 📌 **Core Topics**: `#docker-setup, #quantum-physics`
     - 🛠️ **Entities**: `#docker-desktop, #what-the-bleep-film`
     - ⚡ **Action Categories**: `#troubleshooting, #media-curation`
     - 🔍 **Keywords**: `#docker, #quantum, #recovery`

---
*Technical Reference Document maintained in `Flashrebob Obsidian\__Web Dev information`.*
