# ✉️ Gmail Mail Merge with Google Contacts Labels

A complete, production-ready Google Apps Script solution to merge your **Google Contacts labels (groups)** into a **Gmail draft email template** using **First Name**, **Last Name**, **Full Name**, and **Email**.

---

## 🌟 Features

- **Direct Google Contacts Integration**: Select any label/group from your Google Contacts ([contacts.google.com](https://contacts.google.com/)).
- **Gmail Draft Templates**: Use standard Gmail drafts as templates. HTML formatting, font styles, links, and email attachments attached to the draft are preserved.
- **Supported Placeholders**:
    - `{{First Name}}` (or `{{first name}}`)
    - `{{Last Name}}` (or `{{last name}}`)
    - `{{Full Name}}` (or `{{full name}}`)
    - `{{Email}}` (or `{{email}}`)
- **Dry-Run Preview Mode**: Safely test your template and review parsed names/subjects without sending any real emails.
- **Daily Quota Monitor**: Checks your Gmail daily sending limits automatically.
- **Interactive UI**: Comes with a modern sidebar panel for easy point-and-click operation inside Google Sheets or Google Apps Script.

---

## 🚀 Quick Setup Guide

### Step 1: Organize Google Contacts

1. Go to [contacts.google.com](https://contacts.google.com/).
2. Create or select a **Label** (e.g., `VIP Clients`, `Event Attendees`, `Family`).
3. Add the contacts you want to message to that label. Ensure each contact has a **First Name**, **Last Name**, and **Email Address**.

---

### Step 2: Create Your Gmail Draft Template

1. Go to [gmail.com](https://gmail.com/) and click **Compose** to start a new draft.
2. Enter your email **Subject** with placeholders if desired:
    - _Example:_ `Special update for {{First Name}}!`
3. Type your email **Body** using placeholders:
    - _Example:_
        
        text
        
        Hi {{First Name}},
        
        We're reaching out to follow up on your recent request.
        
        Best regards,
        
        Your Team
        
4. **Do NOT click Send!** Just close the compose window so it remains saved in your Gmail **Drafts**.

---

### Step 3: Install the Apps Script

You can install this script into **Google Sheets** (recommended for easy menu access) or directly at [script.google.com](https://script.google.com/).

#### Option A: In Google Sheets (Recommended)

1. Open a new Google Sheet at [sheets.new](https://sheets.new/).
2. Click **Extensions** > **Apps Script** in the top menu bar.
3. In the script editor:
    - Paste the contents of `Code.gs` into `Code.gs`.
    - Click the **+** icon next to Files, select **HTML**, name it `Sidebar`, and paste the contents of `Sidebar.html`.
4. Click **Save** (💾 icon).
5. Reload your Google Sheet. You will now see a new menu item called **`✉️ Mail Merge`**!

#### Option B: Standalone at script.google.com

1. Go to [script.google.com](https://script.google.com/) and click **New project**.
2. Paste `Code.gs` into `Code.gs`.
3. Add an HTML file named `Sidebar` and paste `Sidebar.html`.
4. Save the project.

---

## 🛠️ How to Run Mail Merge

1. Click **`✉️ Mail Merge`** > **`Launch Mail Merge Panel`** in Google Sheets (or run `showSidebar` / `quickDryRun` from Apps Script).
2. Select your **Google Contacts Label** from the dropdown.
3. Select your **Gmail Draft Template** from the dropdown.
4. Click **🔍 Dry Run** to preview merged subjects and recipient names without sending emails.
5. Once you confirm everything looks correct, click **🚀 Send Mail Merge** to send out the emails!

---

## 🛡️ Safety & Rate Limits

- Gmail free accounts have a standard sending limit of **100 recipients/day**, while Google Workspace accounts have up to **1,500/day**.
- The script includes automatic pause delays (`Utilities.sleep`) between sends to comply with Google email rate limits.

---

## 📁 File Structure

- `Code.gs`: Core Apps Script logic, Google Contacts parsing, placeholder replacer engine, and Gmail sending loop.
- `Sidebar.html`: Interactive HTML control panel.
- `appsscript.json`: Apps Script manifest declaration.