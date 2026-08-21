# Krisp and Bee Daily Notes Report Automation - Cultural Markers & Linguistic Extraction Reference

## 📌 Executive Summary
This document specifies the technical architecture, revised system prompts, strict negative filtering rules, few-shot examples, and extraction rules for capturing **Catchy & Recurring Phrases** and **Notable & Humorous Names/Nicknames** from raw Bee and Krisp conversation transcripts. This automation runs as part of the daily 6:15 AM `BeeKrispDailyReport` scheduled pipeline and appends cultural markers immediately following Section 5 (Quotes) in all Obsidian Daily Notes.

---

## 🎯 Role & Target Objective
You are a linguistic analyzer tasked with extracting cultural markers from the provided transcript. Your goal is to identify catchy, recurring phrases, internal jargon, and unusual, humorous, or unexpected names/nicknames.

---

## 🔍 Extraction Criteria
1. **Catchy/Common Phrases**: Look for high-frequency idioms, slang, conversational "inside jokes," or distinctive slogans repeated by speakers.
2. **Humorous/Unusual Names**: Identify proper nouns, phonetic misspellings from Whisper, creative handles, or eccentric nicknames that stand out as funny, rare, or uniquely contextualized.

---

## 🚫 Strict Negative Filtering Rules (DO NOT EXTRACT)
- **Voice Assistant Triggers**: Do NOT extract functional voice assistant triggers (e.g., `"Hey Google"`, `"Alexa"`, `"Siri"`, `"OK Google"`).
- **Mundane Household Requests**: Do NOT extract mundane, low-value household requests or generic questions (e.g., `"turn on the TV"`, `"what's for dinner"`, `"can you pass the salt"`, `"temperature report"`, `"76 in the kitchen"`).
- **Standard Filler Words**: Do NOT extract standard conversational filler words (e.g., `"uh-huh"`, `"you know"`, `"literally"`, `"like"`, `"i mean"`, `"sort of"`, `"kind of"`).
- **Generic System Names**: Do NOT extract uninteresting system names or generic app labels (e.g., `"Obsidian"`, `"Google"`, `"Krisp"`, `"Report"`, `"Summary"`, `"Daily Note"`, `"Bee Voice Engine"`, `"Spokane"`).

---

## 💡 Few-Shot Examples

### --- EXAMPLE 1: CORRECT EXTRACTIONS ---
**Transcript Input**:  
*"Yeah, so Bob 'The Garbage King' called. He kept saying 'it's a whole vibe' every five minutes. Then his Google Home went off because he said Hey Google, turn on the TV."*

**Expected Output**:
```markdown
### 💬 Catchy & Recurring Phrases
* **"It's a whole vibe"** — Repeated multiple times — *Context:* Used repeatedly by Bob as a catchphrase to describe mundane situations.

### 🎭 Notable & Humorous Names
* **Bob 'The Garbage King'** — *Context:* A humorous, eccentric nickname used by the speaker to reference a contact named Bob.
```
*(Reason for excluding "Hey Google, turn on the TV": This is a generic device automation command and carries no cultural or humorous value.)*

### --- EXAMPLE 2: FAMILY NICKNAMES ---
**Transcript Input**:  
*"Bunny Runner and I went for a walk around the neighborhood before dinner."*

**Expected Output**:
```markdown
### 🎭 Notable & Humorous Names
* **Bunny Runner** — *Context:* Affectionate nickname used for Andy's wife in conversation.
```
--- END OF EXAMPLES ---

---

## 📐 Required Output Format

The output must follow the **Quotes Section** (Section 5) in the exact Markdown structure below:

```markdown
### 💬 Catchy & Recurring Phrases
* **"[Exact Phrase]"** — [Frequency count or estimate] — *Context:* [1-sentence explanation of how/why it was used].

### 🎭 Notable & Humorous Names
* **[Name/Nickname]** — *Context:* [Briefly explain who or what this refers to in the conversation and why it stands out].
```

---

## 🛠️ Implementation Architecture

### 1. Extractor Function (`extract_cultural_markers`)
- Location: [`g:\Documents\_Antigravity Sandbox\Workflow Automations\krisp_bee_merger.py`](file:///g:/Documents/_Antigravity%20Sandbox/Workflow%20Automations/krisp_bee_merger.py)
- Implements `NEGATIVE_TRIGGER_PATTERNS` regex filter to block voice assistant triggers and generic fillers.
- Implements `EXCLUDED_GENERIC_NAMES` set to drop mundane app/system labels.
- Implements `SPECIFIC_NICKNAMES_MAP` dictionary for targeted nicknames (e.g. *Bunny Runner*, *Bob 'The Garbage King'*, *Jeffy*, *Ajahn Sumedho*, *Cori Bilyayev*, *Pugelist*, *Palm Skin*, *De Young*).

### 2. Master Template Integration
- Template Path: [`G:\Google Drive (260611)\Obsidian Master Vault\Flashrebob Obsidian\Templates\Krisp Daily  Notes Template.md`](file:///G:\Google Drive (260611)\Obsidian Master Vault\Flashrebob Obsidian\Templates\Krisp Daily  Notes Template.md)
- Injects `{{CATCHY_PHRASES}}` and `{{NOTABLE_NAMES}}` placeholders right after `### 5. Quotes`.

### 3. Execution Schedule
- Daily Scheduled Task: `BeeKrispDailyReport` (Runs daily at 6:15 AM).
- Vault Directory: `G:\Google Drive (260611)\Obsidian Master Vault\Flashrebob Obsidian\_A_My Journal and Notes\Bee - NLM Reports`
