# Krisp & Bee Daily Notes Report Automation - Quote Extraction Rules Reference

## 📌 Executive Summary
This reference document defines the official **Quote Extraction Rules and Criteria** for automated synthesis of `Bee_Data` transcripts into Obsidian Daily Notes (`Bee Daily Note YYMMDD.md`).

Quote extraction operates from the analytical perspective of an **expert literary and data analyst**, filtering raw transcript dialogue to isolate original statements of spiritual wisdom or profound insight into society and human behavior.

---

## 🎯 Notable Quote Core Criteria

A transcript statement is eligible to be extracted as a **Notable Quote** ONLY if it meets the following primary requirements:

1. **Spiritual or Societal Insight**:
   - The statement must primarily be of a **spiritual nature** or offer a **key insight into society, culture, or human behavior**.
   - Routine technical tasks, software edits, or logistical remarks are strictly excluded.

2. **Full Sentence Requirement**:
   - The quote must be a **complete, grammatically whole sentence** (or multi-sentence thought). Fragmented phrases or incomplete clauses are strictly prohibited.

3. **Clear Pretext & Analytical Context**:
   - To ensure total clarity, every quote must be accompanied by **pretext explaining what was being discussed** so the reader immediately understands what the quote is pointing to.

---

## 🚫 Strict Exclusion Rules

Do **NOT** extract a quote if it matches any of the following:

* **Pop Culture & Media**: Lyrics from a song, dialogue from a movie/TV show, or background media playback.
* **External Material**: The speaker reading aloud from a book, article, or document.
* **Clichés & Idioms**: Common proverbs, overused buzzwords, or idioms lacking original insight.
* **Administrative Filler & App Edits**: Transactional talk, UI editing, slide directions, or equipment checks.
* **Out-of-Scope Speakers**: Quotes are strictly limited to original statements from **Andy**, **Andrea**, or direct human conversational partners.

---

## 🧼 Clean Verbatim & Formatting Standard

- **Clean Verbatim Scrubbing**: Automatically removes verbal filler words (`uh`, `um`, `like`, `you know`), stutters, and false starts without altering core meaning.
- **Structured 3-Part Output**:

```markdown
- **Quote**: "[Clean verbatim full-sentence text in quotation marks]"  
  **Speaker**: [Name of speaker: Andy, Andrea, or direct conversational partner]  
  **Context**: [Pretext explaining what was being discussed so the quote's subject is crystal clear.]
```

---
*Technical Reference Document maintained in `Flashrebob Obsidian\__Web Dev information`.*
