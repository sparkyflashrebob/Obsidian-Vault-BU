# 📋 System Directives & Improvement Queue

> **Overview**: This queue aggregates spoken instructions, workflow directives, feature requests, and system improvement ideas captured from Andy's daily recordings (Linearity & Plaud).
> Items are automatically stacked here during daily transcription runs for review and implementation in Antigravity pair programming sessions.

---

## 📥 Pending Review & Implementation

- [ ] **[2026-10-10 05:17 AM - Linearity] Workflow improvement / instruction suggestion**:
  > *"I always I'll get some more hold on stay here for a second Thank you. How many do we eat one of these? Two. So they normally, these would be good till the middle or end of November. Okay, that's good. Alright, this is how..."*
  - **Status**: Pending Review

- [ ] **[2026-10-10 05:36 AM - Linearity] Workflow improvement / instruction suggestion**:
  > *"New England. Oh, it's not. It might be tougher than we think. They've been up and down. Drink me's only had a one good game. Oh, but they beat the Bills. the bill's are here yeah the bill's always I don't know every year they..."*
  - **Status**: Pending Review

- [ ] **[2026-10-10 05:23 AM - Plaud] Workflow improvement / instruction suggestion**:
  > *"those here That will fall off and it won't spill everywhere that does Do we have more? We don't have much more We didn't get any fruit at all Yeah you want to pick it? I'm getting a meatloaf So well you're the first person..."*
  - **Status**: Pending Review

- [ ] **[2026-10-10 05:38 AM - Plaud] Workflow improvement / instruction suggestion**:
  > *"Alright I gotta stack this in here a certain way. It is. Yeah I gotta put this in here so it doesn't slide around. He waited in the wrong bag. That's okay. It's gonna be heavy. A little bit of physicalness today. I'm glad we're..."*
  - **Status**: Pending Review


- [ ] **[2026-10-09 06:25 AM - Linearity] Workflow improvement / instruction suggestion**:
  > *"The flood watch is for 11 a.m. to one today. We didn't see anything when we were out there regarding the engine classification safeguards. Is it possible to tell when two or more people are talking before classifying it as a monologue, a chatbot conversation...."*
  - **Status**: Pending Review

- [ ] **[2026-10-09 06:31 AM - Plaud] Workflow improvement / instruction suggestion**:
  > *"with anti-gravity also and compare them to when chatbot things are happening I do a lot of speaking to the chatbots and sometimes I'm editing say blog posts of various documentation that has been written so I'm doing that kind of thing versus my initial..."*
  - **Status**: Pending Review


- [ ] **[2026-10-07 04:47 AM - Linearity] Audio storage / retention policy directive**:
  > *"I'm up just before 9 o'clock in the morning on 10-7 and starting the recordings right around 9 o'clock 901 902 interesting got a butt dial from Melissa Phillips who is Andrea's auntie and she accidentally called me again just a second ago when Han-Nep-Song..."*
  - **Status**: Pending Review


- [ ] **[2026-10-05 04:26 PM - Plaud] Workflow improvement / instruction suggestion**:
  > *"the maple one at first and then the maple one was seven bucks for two cubes and like a little expensive and then when I went searched on Gemini when I was in the store it it said that the Irish stuff was good so..."*
  - **Status**: Pending Review

- [ ] **[2026-10-05 02:43 PM - Plaud] Pipeline workflow / script modification**:
  > *"additional instructions and means and ways that we can improve. Maybe we could stack those commands up so that they could be reviewed once we do the the transcriptions."*
  - **Status**: Pending Review


- [ ] **[2026-10-04 06:26 PM - Plaud] Google Photos sync / deduplication directive**:
  > *"Okay but anyway it's great. No but it's great. So it's great that they give that to you you know and you have it. So but I have them sending all my photos to me back from when I first started using Google Photos. So..."*
  - **Status**: Pending Review

- [ ] **[2026-10-04 08:06 PM - Plaud] Google Photos sync / deduplication directive**:
  > *"It's new it's on the top. So what I did look at this one. So what I did was they have a thing they have a way you can get your photos you can get anything that you have sent to you and you can..."*
  - **Status**: Pending Review


- [ ] **[2026-10-04 11:27 AM - Linearity] Pipeline workflow / script modification**:
  > *"butter to the shopping list and also kava stress tea to the shopping list. Butter to the shopping list and add kava stress relief tea to the shopping list. I'm making a quick watch for the the starter the radar game. We had a couple..."*
  - **Status**: Pending Review

- [ ] **[2026-10-04 06:24 PM - Linearity] Google Photos sync / deduplication directive**:
  > *"By the way, I told you I was doing the thing with the photos today... one of the things I was doing with the Antigravity is so great. I was worried... Google Photos doesn't back up your photos to you. It's only in the cloud... So what I did was, they have a way where, I think it's called Takeout... what I'm going to have the Antigravity do is I've got albums already... I'm going to use those albums to automatically organize the photos, but it's going to compare photos I already have on my computer versus what Google photo has and not duplicate them..."*
  - **Status**: Pending Review

---

## ✅ Implemented & Resolved Directives

- [x] **[2026-10-04] Linear Audio Archival Rule**: Automatically convert Linear 48 kHz uncompressed WAV recordings older than 7 days into 128 kbps MP3 files in `G:\Linear Recordings\MP3 Archives\YYYY_MM_MonthName\` and remove raw WAV files. *(Implemented in `audio_archival_utility.py`)*
- [x] **[2026-10-04] Audio Retention Policy**: Do not delete Plaud or Wear audio files older than 1 month until the final day of each month (e.g. anything prior to `2026-08-31`). Reclaim `scratch_audio` cache space immediately. *(Implemented)*
- [x] **[2026-10-04] Sunday Sangha & Live NFL Schedule Reconciliation**: Correct Living Mindfully Sunday hybrid meeting schedule to 5:00 PM – 6:30 PM with Andrea attending, prioritize live Raiders games in afternoon logs, and attribute dharma parables directly to Andy's voice. *(Implemented in `generate_unified_daily_report.py`)*
