---
tags:
  - notebooklm-import
notebook: "M_Music Production 1"
category: "research"
---

This manual provides a comprehensive guide to using **Ableton Push 2**, an instrument designed for song creation that offers hands-on control over melodies, harmonies, beats, samples, sounds, and song structure [1]. It allows for quick clip creation in Live's Session View from the hardware and serves as a powerful tool for real-time playing, step sequencing, and clip launching on stage [1].

### 1. Setup

Setting up your **Push 2 hardware** is largely automatic [2]. Once you connect the included power supply and the USB cable to your computer, Push 2 will be automatically detected by Live as long as Live is running [2]. There is no need to install drivers or manually configure Push 2 in Live's Settings [2].

From time to time, Ableton releases **firmware updates** for Push 2, which are included in Live updates [3]. If you are using Push 2 for the first time after installing a new version of Live, you might be prompted to update the firmware, and Push 2 will guide you through the process [3].

### 2. Browsing and Loading Sounds

You can **browse and load sounds directly from Push 2** without needing to use Live's browser [3]. This is done in **Push 2's Browse Mode** [3].

* **Entering Browse Mode**: Press the **Browse button** [3].
* **Display Layout**: The display is divided into columns. The leftmost column shows either the specific category of the device being browsed or the "Collections" label, which provides quick access to tagged browser items [3]. Columns to the right show subfolders or the contents of the current folder [3].
* **Navigation**: Scroll through presets and folders using the **eight encoders** above the display, or navigate one item at a time using the **arrow buttons** [3].
* **Loading**: After selecting a sound, choose a track type (MIDI, Audio, or Return) and optionally load a device to the new track at the same time [4].

### 3. Playing and Programming Beats

To create beats on Push 2, ensure **Note Mode** is enabled by pressing the **Note Mode Button** [5]. You can then load a Drum Rack preset from Live's library in Browse Mode [5].

* **Pad Grid Configurations**: When working with a MIDI track containing a Drum Rack, Push 2's 8x8 pad grid can be configured in three different ways, toggled by pressing the **Layout button** [5].
  + **Loop Selector**: Divides pads into three sections for simultaneous playing, step sequencing, and adjusting clip length [5]. Holding the Layout button provides momentary access, or you can lock it by holding Shift and pressing Layout [6, 7].
  + **16 Velocities Mode**: The bottom right 16 pads represent **16 different velocities** for the selected Drum Rack pad, allowing you to enter steps at specific velocities [6].
  + **64-Pad Mode**: Allows you to play drums across the entire 8x8 pad grid [8].
* **Navigation in Drum Racks**: Use Push 2's **touch strip** or **Octave Up and Octave Down buttons** to move up/down by 16 pads within Drum Racks [9]. Hold Shift while using these to move by single rows [9].
* **Loading Individual Drums**:
  + **Copying a Pad**: Hold the **Duplicate button** and press the pad you want to copy [10]. While still holding Duplicate, press the destination pad to paste it [10]. This replaces the destination pad's devices but not existing notes [10].
  + **Choke Group/Transpose**: When a single pad is selected, use the first encoder to adjust its **choke group assignment** or the second encoder to **transpose** the pad [10].
  + **Pad Colors**: Change a drum pad's color by holding Shift, tapping the pad, and then tapping one of the pads on the outer ring to choose a color [11]. These custom colors are saved with the Live Set but only appear on Push 2 [11].
* **Step Sequencing Beats**:
  + Tap a pad to select it and enable it for step sequencing [11].
  + The playing step is indicated by a **moving green pad**, which turns red when recording [12].
  + Tapping a step with a note deletes it [12]. Hold **Mute** while tapping to deactivate a step without deleting it [12].
  + Adjust **velocity and micro-timing** for individual notes [12].
* **Real-time Recording**:
  + Enable Live's built-in click track by pressing the **Metronome button** [13]. Adjust its volume by holding Shift and turning the Master volume encoder [13].
  + Press the **Record button** to begin recording [14]. Playing Drum Rack pads will be recorded [14]. Subsequent presses toggle between playback and overdub mode [14].
  + **New Button**: Pressing **New** stops playback of the current clip and prepares Live to record a new clip on the selected track [15]. By default, it duplicates playing clips to a new scene [15].
* **Fixed Length Recording**: Press the **Fixed Length button** to set the size of new clips to a predetermined length [15]. Hold it to set the length [16].
* **Repeat**: With the **Repeat button** enabled, hold down a pad to play or record continuous, rhythmically-even notes [17]. Varying finger pressure changes note volume [17]. The repeat rate is set with the Scene/Grid buttons [18].
* **Quantizing**: Pressing the **Quantize button** snaps notes to the grid in the selected clip [18].

### 4. Playing Melodies and Harmonies

After creating a beat, you can add new tracks for basslines, harmonies, etc. [19].

* **Adding Tracks**:
  + Switch between existing tracks using the **lower display buttons** or **left/right arrow keys** [19].
  + Press the **Add Track button** to add a new MIDI, Audio, or Return track [4, 19]. If adding to a Group Track, new tracks are inserted within it [4].
  + Change track color by holding Shift, pressing the track's lower display button, and tapping a pad on the outer ring [4].
* **Pad Grid for Instruments**: Push 2's 8x8 pad grid automatically configures to play notes [4].
  + By default, every note is in the key of C major [4]. The bottom left pad plays C1 [4]. Moving up, each pad is a fourth higher; moving right, each pad is the next note in the C major scale [4].
* **Playing in Other Keys**: Press Push 2's **Scale button** to change the selected key and/or scale [7].
  + Use the **upper and lower display buttons** to change the key [7].
  + Change to other scale types using **encoders 2 through 7** [20].
  + **Layout (Encoder 1)** and **Direction (Encoder 8)** controls determine pad grid orientation (e.g., 4ths, 3rds, Sequent) [20].
  + **In Key/Chromatic**: The lower left display button toggles between "In Key" (only notes within the key are available) and "Chromatic" (all notes available, in-key notes lit) [21].
  + Scale options are saved with the Set and can be set in your Default Set [21].
* **Step Sequencing Melodies and Harmonies**:
  + The **loop length controls** set the clip's loop length and determine the visible/editable part in sequencers [22]. Each loop length pad corresponds to a page of steps [22].
  + **Page Left/Right buttons** navigate between pages of steps [23].
  + **Duplicating Pages**: Hold Duplicate, press the loop length pad to copy, then press the destination pad [24].
  + **Melodic Sequencer + 32 Notes Layout**: Combines step sequencing and real-time playing, ideal for chords, harmonies, and longer phrases [22, 25]. Tap a step to add selected notes; holding a step shows its notes [26].

### 5. Working with Samples

Push 2 allows you to play samples from the pads with detailed control over sample parameters using encoders and the display [27]. **Simpler** is the instrument that powers Push 2's sample playback [27].

* **Loading a Sample**: Add a new MIDI track or enter Browse Mode on an existing MIDI track [28]. Push 2 will prompt you to browse for a sample if Simpler is empty [28].
* **Sample Waveform Display**: After loading a sample, its waveform appears in Push 2's display with playback parameters [28].
* **Edit Mode**: Press Simpler's **upper display button** to enter **Edit Mode**, where lower display buttons select additional parameter pages, and upper display buttons toggle settings [29]. Pressing it again exits Edit Mode [29].
* **Key Parameters**:
  + **Zoom encoder**: Zooms into a portion of the waveform [29].
  + **Gate**: When enabled, the sample fades out upon pad release; **Fade Out time** determines fade length [30].
  + **Transpose encoder**: Transposes the sample up or down by up to 48 semitones (four octaves) [30].
  + **Gain encoder**: Sets the overall volume of the Simpler instrument [30].
  + **Legato Playback**: Classic and One-Shot Modes allow re-pitching a sample without changing its playback position, acting as a playable version of Legato Mode in clips [30].
  + **Nudge**: Adjusts the position of each slice marker for fine-tuning, especially in Manual mode [31].
  + **Split Slice**: Creates a new slice in the middle of the currently selected slice, useful with Nudge for fine-tuning [31].

### 6. Playing and Recording Audio

* **Arming Tracks**: Selecting a MIDI track on Push 2 automatically arms it for immediate playback [32]. Manually arm any track by holding its lower display button or holding the Record button and pressing the track's lower display button [32].
* **Navigation with Up/Down Arrows**: The behavior of the Up/Down Arrows depends on the **Workflow mode** in Push 2's Setup menu [33]. In both "Scene Workflow" and "Clip Workflow," they move up or down by a single scene [33]. Playback begins immediately, and a triggered clip takes over the play position (similar to Live's Legato Mode) [33].

### 7. Working With Instruments and Effects

**Device Mode** allows you to use the encoders to control parameters in Live's devices and third-party plug-ins [34].

* **Entering Device Mode**: Press the **Device button** [34].
* **Device Selection**: In Device Mode, the **upper display buttons** select devices in the current track, highlighting the selected device [34].
* **Edit Mode**: Once a device is selected, pressing its upper display button again enters **Edit Mode**, where **lower display buttons** select additional pages of parameters [34]. The leftmost upper display button exits Edit Mode [35].
* **Navigation in Edit Mode**: For devices with more than eight parameter pages, the rightmost lower display button shows an arrow to scroll to additional pages [35].
* **Deleting/Disabling Devices**:
  + **Delete**: Hold the **Delete button** and press the upper display button for the device [36].
  + **Disable**: Hold the **Mute button** and press the upper display button for the device [36]. Disabled devices appear gray [36]. Hold Mute again to re-enable [36].
* **Moving Effects**: Press and hold the upper display button for an effect, then use any of the **eight encoders** to scroll the device to a new position [37].
* **Working with Racks**: Instrument, Drum, and Effect Racks allow multiple chains of devices within a single device [37].
  + **Opening a Rack**: Select it with the corresponding upper display button, then press that button again [38]. The Rack unfolds, revealing devices in the selected chain [38]. Pressing the button again toggles it open/closed [38].

### 8. Mixing with Push 2

Push 2 provides control over volumes, pans, and sends for tracks [39].

* **Mix Modes**: Pressing the **Mix button** toggles between **Track Mix Mode** and **Global Mix Mode** [40].
  + **Track Mix Mode**: Encoders adjust volume, pan, and send levels for the **currently selected track** [39]. Lower display buttons select the track [39].
  + **Global Mix Mode**: Encoders adjust volumes, pans, or send levels for the **eight visible tracks** [39]. Upper display buttons select the parameter to be controlled [39].
* **Fine-Tune Control**: Hold Shift while adjusting encoders for fine-tune control [39].
* **Rack and Group Track Mixing**: Expand Group Tracks and tracks containing Racks on Push 2's display to mix their contents [41]. Use left/right arrows to access additional chains/tracks [41].

### 9. Recording Automation

Changes made to device and mixer parameters can be recorded to clips as automation [41].

* **Recording**: Press the **Automation button** so it turns red to toggle Live's Session Automation Arm [41, 42]. This allows recording changes made to Push 2's encoders into the clip [42]. Press Automation again to stop recording [42].
* **Deleting Automation**: Hold the **Delete button** and touch the corresponding encoder to delete recorded changes for that parameter [42]. If no automation is recorded, this resets the parameter to its default value [42].
* **Step Sequencing Automation**: In both drum and melodic step sequencers, you can automate parameters for selected steps [43].
  + **Note-Specific Parameters**: Press and hold a step to access its note settings (Nudge, Length, Velocity) via encoders [43, 44]. You can adjust multiple steps simultaneously [44].
  + **Per-Step Automation**: In Device Mode or Volume Mode, hold one or more steps to create/edit device or mixer automation specifically for that time [43].

### 10. Clip Mode

**Clip Mode** allows you to view and refine played or sequenced MIDI [45].

* **Entering Clip Mode**: Press the **Clip button** [40].
* **Display in MIDI Tracks**: The display changes based on the selected pad layout [45].
* **Controls**: Includes Zoom, Start, End, Loop controls, and a Crop control to delete material outside the loop [45].
* **Real-Time Playing Layouts**: Shows incoming MIDI notes, and the view adjusts to fit all existing notes [45].
* **Sequencing Layouts (Loop Selector, 16 Velocities)**: Shows only the selected pad [46]. The sequenceable area can be moved horizontally via loop length pads or Page Left/Right buttons, or vertically by selecting a different pad [46].

### 11. Controlling Live’s Session View

**Session Mode** allows you to launch clips and scenes [47].

* **Entering Session Mode**: Press Push 2's **Session button** [47]. Hold it to temporarily toggle Session Mode [47].
* **Launching Clips/Scenes**: Pressing a pad triggers the clip in that location in Live's Session View [47]. If the track is selected, pressing the button records a new clip [47]. The Scene/Grid Buttons launch scenes [47].
* **Navigation**:
  + **Arrows and Shift**: Increase the scope of the 8x8 grid [48]. Up/Down moves one scene; Shift+Up/Down moves eight scenes [48]. Left/Right moves one track; Shift+Left/Right moves eight tracks [48].
* **Session Overview**: Hold the **Layout button** to access Session Overview, where each pad represents an 8-scene-by-8-track block of clips [49]. Hit a pad to focus on that section [49].
  + **Color Coding in Session Overview**: Amber (selected block), Green (clips playing in block), Red (no clips playing), No color (no tracks/scenes) [49].
* **Stop All Clips**: Press and hold Shift, then press Stop Clip [48].
* **Copy Clip**: Hold Duplicate and press a clip to copy; continue holding Duplicate and tap another slot to paste [48].

### 12. Setup Menu / User Preferences

Press the **Setup button** to adjust settings [50].

* **Pad Sensitivity**: Adjusts force needed for higher velocity [50].
* **Pad Gain**: Boosts or cuts the overall velocity curve [50].
* **Display Light**: Adjusts display brightness [51].
* **LED Brightness**: Adjusts brightness of pads and buttons [51].
* **Workflow**: Determines how Push 2 behaves with Duplicate, New, or Up/Down arrow buttons [51].
  + **Scene Workflow (default)**: Musical ideas are organized and navigated in scenes [51]. Duplicate creates a new scene with playing clips; New prepares an empty clip slot [52]. Up/Down Arrows move up/down by a single scene [52].
  + **Clip Workflow**: Focuses on the currently selected clip [51].

### 13. Push 2 Control Reference

* **Tap Tempo**: Press once per beat to set Live's tempo [52]. Encoder adjusts tempo in 1 BPM increments; Shift+encoder for 0.1 BPM increments [52].
* **Undo**: Undoes the last action [53]. Shift+Undo for Redo [53].
* **Mute**: Mutes the selected track, pad, or deactivates a step/device [53]. Hold Mute to lock the function [53].
* **Add Device**: Opens Browse Mode to add a new device to the track [54].
* **Add Track**: Puts Push 2 into Browse Mode to select track type and load a device [55].
* **Master**: Selects the Main track [55].
* **Scene/Grid buttons**: Launch Session View scenes in Session Mode; determine rhythmic resolution in Note Mode [55].
* **User**: Disables Push 2's built-in functionality, allowing it to be reprogrammed [56].
* **Shift**: Press and hold to access additional functionality or finer resolution for encoders [57].
* **Select**: In Session Mode, selects a clip without launching [57]. In Note Mode, selects a Drum Rack pad without triggering [57].
* **Page Left/Right**: Navigates step sequencer pages or shifts Session View control by eight tracks [57].
* **Footswitches**: Two ports on the back [58]. Footswitch 1 acts as a **sustain pedal** [58]. Footswitch 2 controls **recording functionality**: single tap toggles Record, double-tap is like pressing New [58].

### 14. General Operations (Knobs, Sliders, Interface)

* **Knobs and Sliders**: Adjust by clicking and dragging up/down or left/right [59]. Hold **Shift** for fine-tuning [59]. Double-click to display a text box for precise value entry [59]. Right-click to open a context menu with settings and modulation options [60].
* **MIDI Learn**: Right-click a knob/slider and select MIDI Learn to assign a MIDI CC [61]. This assignment is saved with the preset [62].
* **Reset Control**: Cmd-clicking (macOS) or Ctrl-clicking (Windows) resets a control to its default value [61].
* **Lock Parameter**: Locks a control's setting, preventing value changes when loading presets (though it can still be manually adjusted) [61].
* **Output Volume**: Controlled by the **MAIN knob** (top right) [63].
* **Modulation**: When a modulation source (like an LFO) is connected to a destination, a blue halo appears around the knob, indicating the modulator's depth [64]. This depth can be adjusted via the mod source tab or the Modulation Matrix [65].
* **Bypassing Modulation**: Each row in the Modulation Matrix has a bypass button [66].
* **MPE (MIDI Polyphonic Expression)**: Allows attaching parameter control to individual notes [67]. Push 2 responds to Pressure, Slide, and NotePB (per-note pitch bend) [68]. These can be transformed via curves and smoothed for consistent rise/fall times [69]. MPE data can be echoed by the Note Echo effect [70].
* **Pencil Tool**: In the Wave Editor, allows drawing straight lines between Slice markers to adjust parameters like volume for each slice [71].
* **Undo/Redo**: Click the curved arrow button to undo, and the right-facing arrow button to redo [63]. This helps compare changes side-by-side [63].
* **Presets**: You can save user presets and recall them [72, 73]. Serum automatically saves the file path of imported audio/wavetables but doesn't embed the audio itself unless specified [74].
* **Performance View**: Any panel of an Instrument Script can be turned into a Performance View by adding `make_perfview` to the script [75].
* **Folders**: In Serum, you can navigate folders, search presets, and manage tags [76, 77].
* **Control Data Processes**: Changes to synthesizer/sampler parameters (knobs, dials, sliders) over time are called control data processes [78]. These changes can be recorded onto controller lanes, which can then become an integral feature of the composition [79]. You can also automate these changes using a pencil tool [79].
* **Hardware Sequencing**: Many dance musicians use hardware step sequencers and only employ a DAW at the end for mixing and mastering [80].