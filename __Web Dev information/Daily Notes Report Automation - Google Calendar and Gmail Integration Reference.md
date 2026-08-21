# Krisp & Bee Daily Notes Report Automation - Google Calendar and Gmail Integration Reference

## 📌 Executive Summary
This reference document defines the official rules for integrating **Google Calendar Busy Events** and **Gmail Outgoing Sent Emails** into Obsidian Daily Reports (`Bee Daily Note YYMMDD.md`).

Daily reports across the entire vault (**May 29, 2026 to present**) automatically fetch scheduled calendar events and outgoing email correspondence to provide a complete picture of daily operations.

---

## 📅 Google Calendar Filtering Rules

Calendar items are included in **Section 1.1 Scheduled Calendar Events (Busy Only)** if they satisfy all of the following rules:

1. **Busy Status Only**:
   - Event transparency must show as **Busy** (`transparency != 'transparent'`). Free/transparent blockouts (e.g. ambient alerts, tide notifications) are excluded.
2. **Exclude Tasks**:
   - Only actual calendar events are included; standalone tasks, working locations, and focus time blocks are excluded.
3. **Single Scheduled Occurrences Only**:
   - Recurring events (`recurringEventId` present) are excluded unless they represent an explicitly scheduled single occurrence.
4. **Vault-Wide Historical Scope**:
   - Applied across **all daily notes from May 29, 2026 to present**.

---

## ✉️ Gmail Sent Items Filtering Rules

Outgoing emails are included in **Section 1.1 Outgoing Sent Emails** if they satisfy all of the following rules:

1. **Sent Folder Messages**:
   - Outgoing messages sent FROM Andy (`sparkyflashrebob@gmail.com`).
2. **Direct Communications & Replies**:
   - Specifically captures direct replies, personal correspondence, or outreach to individuals.
3. **Exclude Self-Sent Follow-Up Notes**:
   - Emails sent from Andy to himself (`To: sparkyflashrebob@gmail.com`) are excluded.
4. **Exclude AI-Generated Daily Briefs & Unsubscribes**:
   - Excludes automated emails (e.g. *"Your Day Ahead"*), mailing list confirmations, system alerts, and "unsubscribe" / "opt-out" transactions.
5. **Vault-Wide Historical Scope**:
   - Applied across **all daily notes from May 29, 2026 to present**.

---

## 📋 Template Section Layout (Section 1.1)

```markdown
### 1.1 Scheduled Calendar Events & Outgoing Email Correspondence

#### 📅 Scheduled Calendar Events (Busy Only)
- **Event Summary** (10:15 AM)

#### ✉️ Outgoing Sent Emails
- **To**: `user@example.com` | **Subject**: Email Subject (2:30 PM)
  *Summary*: Brief snippet of outgoing reply...
```

---
*Technical Reference Document maintained in `Flashrebob Obsidian\__Web Dev information`.*
