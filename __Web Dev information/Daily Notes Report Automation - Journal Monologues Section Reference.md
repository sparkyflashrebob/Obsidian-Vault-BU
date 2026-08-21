# Krisp & Bee Daily Notes Report Automation - Journal Monologues Section Reference

## 📌 Executive Summary
This reference document defines the official classification rules for selecting and rendering **Andy's Personal Journal Entries** in Obsidian Daily Reports (`Bee Daily Note YYMMDD.md`).

Monologues are analyzed and categorized into three distinct communication types. Only genuine **Journal Entries** are included in Section 3.1.

---

## 🏷️ Monologue Classification Rules

### 1. 📖 Journal Entry (INCLUDE IN SECTION 3.1)
- **Definition**: Private reflection. The writer talks to themselves using 'I'. It focuses on inner thoughts, daily events, emotions, mindfulness, meditation, spirituality, human behavior, psychology, or comments on society.
- **Key Characteristics**: Has **no external audience**, **no commands**, and **no greetings**.
- **Scope**: Attends primarily to mindfulness, meditation, spiritual practice, human psychology, and societal reflections.

### 2. 🤖 One-Sided Chatbot Prompt (OMIT FROM SECTION 3.1)
- **Definition**: Task-oriented instruction asking an AI or software assistant for specific help, information, code, or generation.
- **Key Characteristics**: Contains commands or questions like *"explain"*, *"write"*, *"fix this code"*, *"summarize this"*, *"delete contacts"*, *"give me a logo"*.
- **Action**: Strictly **OMITTED** from Section 3.1.

### 3. 💬 One-Sided Message to a Person (OMIT FROM SECTION 3.1)
- **Definition**: Interpersonal communication addressing a specific individual or group using 'you'.
- **Key Characteristics**: Casual social elements like greetings (*"Hey"*, *"Hi"*), personal updates (*"Just wanted to let you know..."*), social questions (*"How have you been?"*), or plan coordination (*"Need 6 members for club..."*).
- **Action**: Strictly **OMITTED** from Section 3.1.

---

## 📋 Required Section Output Format

For every included **Journal Entry** in Section 3.1, the report outputs the classification header first, followed by a one-sentence rationale explaining the choice based on tone or format:

```markdown
### 3.1 Personal Monologues & Journal Entries

#### [Session Title] ([Timestamp])
**Journal Entry**  
*Reason: Private reflection focusing on inner awareness, personal psychology, and spiritual practice with no external audience or commands.*
> "Verbatim transcription of Andy's private reflective journal entry..."
```

---
*Technical Reference Document maintained in `Flashrebob Obsidian\__Web Dev information`.*
