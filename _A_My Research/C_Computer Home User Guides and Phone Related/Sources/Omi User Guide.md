---
tags:
  - notebooklm-import
notebook: "C_Computer Home User Guides and Phone Related"
category: "research"
---

Regarding OMI and Zom integration Since you are on a PC (Windows), using Omi for Zoom calls is slightly different than on Mac, as Omi currently prioritizes its Mac Desktop App and Web App for direct computer capture.
As an AV Project Engineer, you'll know that Windows handles audio routing differently (and often more strictly) than macOS. Here is how to achieve the best results with Omi on your PC:

1. The Web App Method (Best for PC) Since there is currently no dedicated Omi Windows desktop ".exe" for system audio capture, the Omi Web App is your primary tool.
   How to do it: Open the Omi Web App in Chrome or Edge before your call.
   The Technical Challenge: Windows does not naturally allow a browser tab to "hear" what is happening in another app (Zoom) without permission.
   The Fix: When you start recording in the Omi Web App, your browser will pop up a "Share your screen" window. You must select the "Entire Screen" tab and check the box that says "Also share system audio." This allows Omi to "hear" the other participants on the Zoom call.
2. The "Air-Gap" Method (Hardware) If you have the Omi wearable device (pendant), you can record the call ambiently.
   Setup: Set your Zoom output to your PC Speakers (not your headset).
   Execution: The Omi device will pick up your voice and the voices coming out of the speakers.
   Pro Tip: As an audio expert, you know this can result in lower fidelity or room echo. For the best AI transcription, keep the Omi device within 2–3 feet of your speakers and keep the volume at a moderate level to avoid clipping.
3. The Professional Route: Virtual Audio Cable If you want "clean" digital audio without using speakers, you can use a Virtual Audio Cable (VAC) or VB-Audio Cable (standard tools in the AV world).
   Routing: Set Zoom’s speaker output to "CABLE Input."
   Capture: Set the Omi Web App’s microphone input to "CABLE Output."
   Monitoring: Use Windows "Listen to this device" settings so you can still hear the meeting in your own headphones while it routes to Omi.
   Expert Recommendations for Your Workflow Transcription Quality: Because you deal with technical AV terms (like "DSP," "Dante," or "latency"), Omi's default model might occasionally trip. You can go into the Omi settings and add Custom Vocabulary to ensure these terms are transcribed correctly.
   Privacy: Unlike "bot" recorders (like Otter), Omi is invisible. Since you're on a PC using the screen-share/audio-share method, Zoom will not automatically notify others that you are recording. From a professional ethics standpoint, it's always best to give a quick "heads up" to the group.
   Monitoring: Use Windows "Listen to this device" settings so you can still hear the meeting in your own headphones while it routes to Omi.