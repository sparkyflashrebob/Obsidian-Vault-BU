# 🎙️ Plaud NotePin Automated Voice Archiving & Daily Report System
## System Architecture & Technical Reference Manual

---

## 📌 Overview
The Plaud NotePin Voice Archiving System provides automated 16-hour daily voice recording (7:00 AM – 11:00 PM), local export via Tasker + AutoInput, Wi-Fi auto-sync via DriveSync Pro, silence trimming via Pydub, speaker diarization, MP3 audio reduction, and daily report generation ready by 7:00 AM.

---

## 📁 System Directory Map

| Resource | Path | Description |
| :--- | :--- | :--- |
| **Phone Local Export** | `/storage/emulated/0/Tasker/Plaud Recordings/` | Local export location on Samsung S24 |
| **PC Watchfolder** | `G:\Google Drive (260611)\Plaud Watch folder` | Wi-Fi sync landing folder from DriveSync |
| **Voice Directory** | `G:\Google Drive (260611)\Plaud Voice Directory` | Reference voice samples (`.wav`) & embeddings |
| **Audio Archive** | `G:\Google Drive (260611)\Plaud Audio Archive` | Reduced MP3 archive of processed audio |
| **Daily Reports** | `G:\Google Drive (260611)\Obsidian Master Vault\Flashrebob Obsidian\_A_My Journal and Notes\Plaud Daily Note Reports` | Final Obsidian Daily Note Reports (`.md`) |
| **Documentation** | `G:\Google Drive (260611)\Obsidian Master Vault\Flashrebob Obsidian\__Web Dev information\` | System & implementation reference docs |

---

## 🟢🔴 Mobile Tasker & Phone Controls

- **Armed Schedule**: 7:00 AM – 11:00 PM (bound to `%RecordingAllowed == 1`).
- **Green Button (`Activate_Voice_Archiving`)**: Sets `%RecordingAllowed = 1`, arms daily recording.
- **Red Button (`Pause_Voice_Archiving`)**: Sets `%RecordingAllowed = 0`, pauses recording & releases mic.
- **Manual Hardware Override**: Pressing the physical button on the Plaud NotePin outside 7 AM – 11 PM initiates a manual recording session, which is preserved and processed.

---

## 📲 Phone Export Automation (11:00 PM)

1. At **11:00 PM**, Tasker launches the Plaud App on your Samsung S24.
2. AutoInput executes the UI export sequence:
   - Selects today's recordings.
   - Taps **Export Audio**.
   - Saves files to `/storage/emulated/0/Tasker/Plaud Recordings/`.
3. **DriveSync Pro** automatically syncs files from `/Tasker/Plaud Recordings/` to `G:\Google Drive (260611)\Plaud Watch folder` on your PC.

---

## ⚙️ Audio Processing & Speaker Diarization

1. **Silence Elimination (Pydub)**: Trims non-speech/silent segments while preserving exact `HH:MM:SS` timestamp markers.
2. **Audio Reduction**: Converts raw audio to optimized 64kbps/128kbps MP3 for archive in `Plaud Audio Archive`.
3. **Speaker Diarization & Voice Directory**: Matches speaker audio features against labeled reference samples (`Andy.wav`, `Mom.wav`, `Gordon.wav`) in `Plaud Voice Directory`.
4. **Speaker Labeling Tool (`plaud_voice_labeler.py`)**: Run this CLI script to inspect and label new/unknown voices into your directory.

---

## 📄 Obsidian Daily Note Report Structure

Reports follow the updated Bee/Plaud specification saved in:
`G:\Google Drive (260611)\Obsidian Master Vault\Flashrebob Obsidian\_A_My Journal and Notes\Plaud Daily Note Reports\Plaud Daily Note YYMMDD.md`

### Key Sections:
1. **Frontmatter Tags**
2. **Header Metadata** (`Date`, `Attendees`, `Total Conversations Processed`)
3. **📌 Executive & Core Topics Overview (Keywords/Tags)**
4. **📅 Google Calendar Events Today**
5. **📧 Gmail Activity Log**
6. **💡 Key Points, Subjects and Themes**
7. **📖 Detailed Subject Matter** (Strictly chronological with bulleted conversation topics)
8. **🗣️ Personal Monologues & Direct Thoughts**
9. **🧘 Spiritual and Societal Insights**
10. **💬 Quoted Expressions & Catchy Phrases**
11. **📚 Stories & Case Examples Shared**
12. **🧠 Physical & Mental Challenges Table**
13. **📻 Miscellaneous Media & References Encountered**

---

## 🧹 Cleansing & Maintenance Schedules

- **12:00 AM (Midnight) Tasker Purge**: Tasker purges processed local files from phone storage and Plaud App cache.
- **12:00 PM (Noon) Watchfolder Purge**: Python cleans up `G:\Google Drive (260611)\Plaud Watch folder` daily at Noon.
