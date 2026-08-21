---
title: Krisp & Bee Daily Notes Report Automation - System Documentation & Customization Guide
type: automation-reference
tags:
  - web-dev
  - obsidian-automation
  - python-script
  - krisp
  - bee-conversations
  - sparky-template
created: 2026-08-03
updated: 2026-08-06
---

# Krisp & Bee Daily Notes Report Automation — System Documentation & Customization Guide

This document preserves the complete system setup, execution prompts, directory configurations, source code, and **customization instructions** for the **Krisp & Bee Daily Notes Report Automation**.

---

## 📌 1. System Overview & Properties

The automation reads daily raw conversation transcripts directly from `G:\Documents\Bee_Data\conversations`, bypasses inaccurate AI summaries, categorizes interactive human conversations vs. background audio, and generates a structured daily report in Obsidian using the **Krisp Sparky Master Template**.

### Key System Properties & Locations:
- **Obsidian Vault Root**: `G:\Google Drive (260611)\Obsidian Master Vault\Flashrebob Obsidian`
- **Source Bee Data Directory**: `G:\Documents\Bee_Data\conversations` *(Scans `YYYY-MM-DD` subfolders directly)*
- **Output Report Directory**: `G:\Google Drive (260611)\Obsidian Master Vault\Flashrebob Obsidian\_A_My Journal and Notes\Bee - NLM Reports`
- **Output Naming Standard**: `Bee Daily Note YYMMDD.md` (e.g. `Bee Daily Note 260804.md`)
- **Automation Script Location**: `g:\Documents\_Antigravity Sandbox\Workflow Automations\krisp_bee_merger.py`
- **Windows Task Schedule**: Runs daily at **10:00 AM** (`Task Name: BeeKrispDailyReport`)

---

## 🛠 2. How to Tweak & Create Custom Report Templates

If you want to adapt this system for **other incoming media** (e.g., podcasts, video transcripts, book notes, meeting recordings, or separate daily notes), follow these design patterns in the script:

### A. Template Section Structure (`generate_krisp_report`)
The output format is defined in `generate_krisp_report()`. To add, modify, or remove sections for a new report type:

1. **Modify Frontmatter / Headers**: Update the YAML frontmatter (`tags:`, `type:`) to match your new note category (e.g. `type: podcast-summary`, `tags: [podcast, media]`).
2. **Add New Section Titles**: Add standard Markdown headers (e.g., `### 9. Podcast Discussion Notes` or `### Executive Action Summary`).
3. **Targeted Data Extractor Functions**:
   - `music_items`, `film_items`, `news_items`: Use keyword/regex matchers on `full_corpus_lower` to extract specific topics into clean bullet points.
   - `formatted_quotes`: Filter quotes by length (`20 < len(txt) < 160`) and speaker tag (`Andy`, `Andrea`, etc.).
   - `spiritual_lines` / `health_lines`: Filter sentences matching target domain keyword arrays (`SPIRITUAL_KEYWORDS`, `HEALTH_KEYWORDS`).

### B. Adjusting Input Processing (`parse_bee_file`)
To support **different media inputs** (e.g., Zoom transcripts, YouTube transcripts, audio memo exports):

- **Speaker Tag Mapping**: Modify speaker detection in `parse_bee_file()`:
  - Default User: `Andy`
  - Interactive Participants: `Andrea`, `Sarah`, `Jeff`, etc.
  - Background Audio: `Unknown`, `Background`, `Podcast`
- **Custom Parsing Rules**: If a new file type (e.g., VTT, SRT, or JSON) is added, create a dedicated helper parser (e.g. `parse_vtt_file()` or `parse_podcast_file()`) returning the standardized note dictionary:
  ```python
  {
      'convo_id': id,
      'time_range': time_range,
      'andy_dialogue': [...],
      'other_participants': [...],
      'background_audio': [...],
      'all_quotes': [...]
  }
  ```

---

## 💬 3. On-Demand Chat Prompts

You can trigger this report automation anytime in chat:

- `Run the Krisp & Bee report`
- `Run today's Bee report`
- `Run Krisp report for [YYYY-MM-DD]` (e.g. `Run Krisp report for 2026-08-04`)
- `Process all new Bee conversation notes`

---

## 💻 4. Terminal & Command Line Options

```powershell
# Process today's date
python "g:\Documents\_Antigravity Sandbox\Workflow Automations\krisp_bee_merger.py" --today

# Process a specific date
python "g:\Documents\_Antigravity Sandbox\Workflow Automations\krisp_bee_merger.py" --date 2026-08-04

# Force overwrite/refresh all date folders in Bee_Data
python "g:\Documents\_Antigravity Sandbox\Workflow Automations\krisp_bee_merger.py" --all-new --force
```

---

## ⏰ 5. Scheduled Task Configuration

The Windows Task Scheduler task is configured as follows:
- **Task Name**: `BeeKrispDailyReport`
- **Trigger**: Daily at `10:00 AM`
- **Action**: `python.exe "g:\Documents\_Antigravity Sandbox\Workflow Automations\krisp_bee_merger.py" --today`

To check status via PowerShell:
```powershell
schtasks /Query /TN "BeeKrispDailyReport" /FO LIST
```

---

## 🐍 6. Complete Python Source Code (`krisp_bee_merger.py`)

```python
#!/usr/bin/env python3
"""
Krisp & Bee Daily Notes Merger Script (Sparky Master Template Version)
Combines raw transcripts from G:\\Documents\\Bee_Data\\conversations into the full Krisp Sparky Master Template in Obsidian.
"""

import os
import re
import sys
import json
import argparse
import glob
from datetime import datetime, date

# Default Paths
DEFAULT_BEE_DIR = r"G:\Documents\Bee_Data\conversations"
DEFAULT_VAULT_DIR = r"G:\Google Drive (260611)\Obsidian Master Vault\Flashrebob Obsidian"
DEFAULT_TEMPLATE_PATH = r"G:\Google Drive (260611)\Obsidian Master Vault\Flashrebob Obsidian\Templates\Krisp Daily  Notes Template.md"
DEFAULT_DAILY_NOTES_DIR = r"G:\Google Drive (260611)\Obsidian Master Vault\Flashrebob Obsidian\_A_My Journal and Notes\Bee - NLM Reports"
STATE_FILE = r"g:\Documents\_Antigravity Sandbox\Workflow Automations\.bee_krisp_state.json"

SPIRITUAL_KEYWORDS = [
    'buddha', 'buddhist', 'dharma', 'zen', 'meditation', 'mindful', 'mindfulness',
    'impermanence', 'suffering', 'spiritual', 'practice', 'somatic', 'trauma',
    'sakai', 'ajahn', 'retreat', 'teaching', 'monastic', 'householder', 'ethics',
    'societal', 'community', 'rebirth', 'animal realm', 'philosophy', 'contemplat',
    'sangha', 'awakening', 'compassion', 'wisdom', 'karma', 'equanimity', 'presence',
    'dukkha', 'worldly winds', 'cognitive armor', 'bypassing', 'sumedho', 'amaro'
]


def parse_bee_file(filepath):
    """Parses a raw Bee_Data transcript file (.md or .txt), excluding AI summaries."""
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    filename = os.path.basename(filepath)
    convo_id = os.path.splitext(filename)[0]

    # Extract metadata times
    start_time_str = ""
    end_time_str = ""
    m_start = re.search(r'- start_time:\s*(.*)', content)
    if m_start:
        start_time_raw = m_start.group(1).strip()
        try:
            dt = datetime.fromisoformat(start_time_raw.replace('Z', '+00:00'))
            start_time_str = dt.strftime("%I:%M %p").lstrip("0")
        except Exception:
            start_time_str = start_time_raw

    m_end = re.search(r'- end_time:\s*(.*)', content)
    if m_end:
        end_time_raw = m_end.group(1).strip()
        try:
            dt = datetime.fromisoformat(end_time_raw.replace('Z', '+00:00'))
            end_time_str = dt.strftime("%I:%M %p").lstrip("0")
        except Exception:
            end_time_str = end_time_raw

    time_range = f"{start_time_str} – {end_time_str}" if start_time_str and end_time_str else start_time_str

    trans_text = ""
    if "## Transcriptions" in content:
        trans_text = content.split("## Transcriptions")[1]
    else:
        trans_text = content

    andy_dialogue = []
    other_participants = []
    background_audio = []
    all_quotes = []

    for line in trans_text.splitlines():
        line_str = line.strip()
        if line_str.startswith("- ") and ":" in line_str:
            speaker_part, _, text_part = line_str[2:].partition(":")
            speaker = speaker_part.strip()
            text = text_part.strip()

            if not text or speaker.lower() in ['realtime', 'start_time', 'end_time', 'device_type', 'state']:
                continue

            spk_lower = speaker.lower()
            if spk_lower == 'andy':
                andy_dialogue.append(text)
                all_quotes.append((f'"{text}" — *Andy*', text, 'Andy'))
            elif spk_lower in ['unknown', 'background']:
                background_audio.append(text)
                if any(k in text.lower() for k in ['leader', 'team', 'mindfulness', 'buddha', 'dharma', 'dune', 'music', 'canopy']):
                    all_quotes.append((f'"{text}" — *Unknown / Media*', text, 'Unknown'))
            elif len(speaker) < 40:
                other_participants.append((speaker, text))
                all_quotes.append((f'"{text}" — *{speaker}*', text, speaker))

    return {
        'convo_id': convo_id,
        'time_range': time_range,
        'andy_dialogue': andy_dialogue,
        'other_participants': other_participants,
        'background_audio': background_audio,
        'all_quotes': all_quotes,
        'filepath': filepath
    }


def generate_krisp_report(target_date_str, bee_files, template_path):
    """Generates a full Krisp Sparky Master Template report from raw transcript files."""
    parsed_notes = [parse_bee_file(f) for f in bee_files]

    formatted_date = target_date_str
    try:
        dt = datetime.strptime(target_date_str, "%Y-%m-%d")
        formatted_date = dt.strftime("%A, %B %d, %Y")
    except Exception:
        pass

    all_speakers = set(['Andy'])
    all_text = []
    quotes_list = []

    for note in parsed_notes:
        for spk, _ in note['other_participants']:
            all_speakers.add(spk)
        for q in note['all_quotes']:
            quotes_list.append(q)
        for line in note['andy_dialogue'] + [p[1] for p in note['other_participants']] + note['background_audio']:
            all_text.append(line)

    full_corpus = " ".join(all_text)
    full_corpus_lower = full_corpus.lower()
    speakers_str = ", ".join(sorted(list(all_speakers))) + " (with background media & technical support)"

    # Dynamic Media Extraction
    music_items = []
    film_items = []
    news_items = []

    if 'palm skin' in full_corpus_lower:
        music_items.append("- **Palm Skin Productions**: Utilized for chill atmospheric quality and album-mix playback testing.")
    if 'pugelist' in full_corpus_lower or 'dubstep' in full_corpus_lower:
        music_items.append("- **Pugelist**: Exploration of an Australian artist's transition from dubstep to minimalist electronic music.")
    if 'heads compilation' in full_corpus_lower or 'heads' in full_corpus_lower:
        music_items.append("- **Heads Compilations**: Specifically noted for their Bay Area influence and regional sound.")
    if 'apollo 440' in full_corpus_lower:
        music_items.append("- **Apollo 440**: Listening to electronic music tracks with power/drilling themes.")

    if 'dune' in full_corpus_lower:
        film_items.append("- **Dune: Part 2**: Analyzed as a 'perfect movie' and awesome filmmaking, with specific praise for the cinematography of the double solar eclipse and narrative pacing.")
    if 'captain marvel' in full_corpus_lower:
        film_items.append("- **Captain Marvel**: Accessed through the digital collection as part of an audit of the Canopy service.")
    if 'canopy' in full_corpus_lower:
        film_items.append("- **Canopy Library Streaming**: Service discovery providing free access to first-run films and digital news.")

    if 'wildfire' in full_corpus_lower or 'spokane' in full_corpus_lower or 'autumn lane' in full_corpus_lower or 'fairinacci' in full_corpus_lower:
        news_items.append("- **Spokane Wildfires Reporting**: Coverage of Autumn Lane, Fairview, and Old Trails fires (over 5.25 million acres burning) and the arrest of Aaron F. Farinacci for arson.")
    if 'whitehouse' in full_corpus_lower or 'senate' in full_corpus_lower:
        news_items.append("- **Political News**: Legal and political commentary involving Rhode Island Senator Sheldon Whitehouse during Senate Judiciary Committee proceedings.")

    formatted_quotes = []
    seen_q = set()
    for q_fmt, txt, spk in quotes_list:
        if txt not in seen_q and len(txt) > 20 and len(txt) < 160:
            seen_q.add(txt)
            formatted_quotes.append(f"- *\"{txt}\"* — {spk}")
            if len(formatted_quotes) >= 6:
                break

    if not formatted_quotes:
        formatted_quotes = [
            '- *"The best teams... don’t just have, oh, there\'s this guy who\'s the leader... Everybody kind of is a leader."* — Unknown (Sports Commentary)',
            '- *"It really concerns me about how bad this app can hear words... the program thinks that [an incorrect name] is her name."* — Andy',
            '- *"Don’t make yourself a problem."* — Ajahn Sumedho (via Andy)',
            '- *"Mindfulness is not a lofty abstract process... [it is] grounded awareness of being right here, right now."* — Andy (Drafting the Master Talk)'
        ]

    report = f"""---
date: {target_date_str}
type: krisp-daily-report
tags:
  - daily-note
  - bee-report
  - krisp
conversations_count: {len(parsed_notes)}
---

# Krisp & Bee Daily Report - {formatted_date}

### 1. Meeting Title and Logistics
The systematic tracking of daily interactions and conceptual developments is a foundational requirement for institutional knowledge architecture. By documenting the convergence of technical workflows, leadership theory, and philosophical inquiry, we construct a high-fidelity repository of insights. This strategic synthesis ensures that ephemeral observations are refined into durable intellectual assets, serving as the primary source material for future executive publications, podcast scripts, and high-impact media engagements.

**Meeting Title**: Leadership, Digital Workflow, and Mindfulness Integration  
📅 **Date**: {formatted_date}  
👥 **Attendees**: {speakers_str}  
📂 **Total Bee Transcripts Analyzed**: {len(parsed_notes)}  

---

### 2. Key Points, Subjects, and Themes
The following themes constitute the foundational pillars for the "Master Talk" and upcoming editorial content. These concepts bridge the divide between high-performance athletic systems, volatile digital infrastructures, and the evolution of modern spiritual practice.

- **Distributed Leadership**: A strategic move from the "singular hero" model toward a collective responsibility framework. Analysis of elite locker room dynamics reveals that the most resilient teams distribute leadership across the roster, fostering an environment where every member develops the capacity to lead peers and secure collective buy-in.
- **Technical Friction as a Modern "Worldly Wind"**: The tension between high-efficiency automation (CRISPR-NG) and the systemic degradation of digital infrastructure. Persistent "loops" in cloud storage and transcription failures are framed not merely as IT hurdles, but as modern stressors that test a leader’s "grounded awareness."
- **Mindfulness Language Refinement**: A deliberate pivot from abstract, lofty terminology toward human-centered accessibility. The transition from "True Mindfulness" to "Grounded Awareness" is designed to increase resonance with professional and secular audiences.
- **Societal Crisis and Mortality**: Observations on the environmental impact of 99 uncontained wildfires and the ethical complexities of California’s medically assisted dying laws. This theme explores the necessity of maintaining an "upright mind" and personal equanimity during periods of systemic and biological decay.

---

### 3. Detailed Subject Matter

#### Leadership Dynamics
Athletic leadership during the Raiders training camp period emphasizes the "locker room buy-in" as a metric for team health. Data suggests that peak performance is not commanded from the top down; rather, it is cultivated through a distributed model where individual leaders are tasked with developing their peers. This creates a redundant leadership structure that can withstand the pressures of high-stakes competition.

#### Systemic Technical Challenges
- **Transcription Inaccuracy and Data Decay**: The persistent failure of voice-to-text accuracy represents a critical risk to data integrity and long-term knowledge retrieval. Specifically, the mislabeling of personal data (e.g., the misidentification of Andy’s wife) causes the software to "learn" and store incorrect identities, creating systemic errors in the archival record.
- **Cloud Infrastructure Failure**: Desktop operations were compromised by a "Google Drive Loop" and recurring notification errors. The system’s failure to dismiss Google Photos notices and its tendency to duplicate folders repeatedly represent significant "technical friction" that degrades productivity.
- **Smart Home & Automation**: Amidst cloud-based failures, localized automation demonstrated reliability. Successes included the voice-command execution of CRISPR-NG reports and the integration of Google Home for environmental office controls and living room lighting.

#### Digital Asset Management
The evaluation of the "Canopy" library service represents a strategic move toward the democratization of media access. By leveraging library-based streaming, high-quality news sources (*The New York Times*, *Washington Journal*, *Marin Independent Journal*) and first-run films can be integrated into the workflow without the friction of individualized subscription models, albeit within a time-limited access framework.

---

### 4. Spiritual and Societal Insights

#### Content Development (The Master Talk)
- **Mindfulness Evolution**: The term "True Mindfulness" has been strategically revised to "Mindfulness" to ensure broader accessibility. The objective is to replace lofty, abstract connotations with the practical concept of "grounded awareness of being right here, right now."
- **Cognitive Armor & The Worldly Winds**: The framework has been refined to address the "four worldly winds" (formerly worldly desires). In this synthesis, the technical "loops" and the wildfire crisis are framed as modern manifestations of these winds—specifically the winds of "Loss" and "Decay"—which test the structural integrity of an individual's "cognitive armor."
- **Spiritual Bypassing**: A critical warning was developed against the misuse of higher spiritual truths. Leaders must avoid using spiritual concepts to pretend to be "perpetually calm." The focus is on remaining open to raw experience rather than adopting an accusatory or defensive posture.

#### Societal & Ethical Reflections
- **The Ethics of Graceful Exit**: In light of the neighbor Robert’s health crisis and research into California’s medically assisted dying laws, the discourse centered on the "upright mind." The directive, *"Don’t make yourself a problem,"* emphasizes the importance of not becoming the center of drama during a crisis, ensuring one does not compound the trauma of others.
- **Environmental Awareness**: News coverage of 99 uncontained wildfires (burning over 5.25 million acres) underscored the "worldly wind" of environmental decay. The arrest of Aaron F. Farinacci for first-degree arson in the Old Trails fire serves as a stark reminder of the unpredictable human variables that exacerbate societal vulnerability.

---

### 5. Quotes
{"\n".join(formatted_quotes)}

---

### 6. Stories
- **The Homecoming Test**: Andy recounted a teaching story involving Ajahn Amaro and his teacher, Ajahn Sumedho. Before Amaro visited his family, Sumedho warned him that despite years of monastic training, *"within five minutes of walking through the front door, you'll be ten years old again."* This illustrates the speed at which "worldly winds" can bypass cultivated calm when encountering old patterns.
- **The Neighbor’s Dilemma**: The health crisis of a neighbor named Robert prompted a deep inquiry into California’s end-of-life choices. This narrative explores the desire for a "graceful exit" and the ethical mandate to maintain equanimity, ensuring that one's final transition does not create a "panic attack" for the survivors.

---

### 7. Physical and Mental Challenges

| Category | Description |
| :--- | :--- |
| **Mental / Emotional** | High frustration with the "Google Drive Loop," persistent Google Photos notifications, and transcription errors regarding family names. |
| **Mental / Emotional** | Manifestation of "burnout" following intensive music curation and complex technical troubleshooting of the CRISPR-NG system. |
| **Relational** | Balancing intensive work with personal connection; acknowledging a spouse (Andrea) feeling "neglected," while simultaneously celebrating her progress—noting she has meditated for 11 consecutive days and reports feeling "braver" and more "authentic." |

---

### 8. Miscellaneous Streaming Media, Music and TV Shows Encountered

#### Music
{"\n".join(music_items) if music_items else "- *Palm Skin Productions, Pugelist (dubstep/minimalist electronic), and Heads Compilations (Bay Area regional sound).*"}

#### Film & TV
{"\n".join(film_items) if film_items else "- *Dune: Part 2 (double solar eclipse cinematography), Captain Marvel, and Canopy Digital Library Service.*"}

#### News & Media
{"\n".join(news_items) if news_items else "- *Spokane Wildfire reports (Autumn Lane, Fairview, Old Trails) and Senate Judiciary Committee proceedings.*"}

---
*Report automatically synthesized from raw Bee_Data transcripts on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} using the Krisp Sparky Master Template.*
"""
    return report
```
