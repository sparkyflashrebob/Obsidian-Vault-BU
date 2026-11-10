---
tags:
  - notebooklm-import
notebook: "M_Music Production 1"
category: "research"
---

Building Max for Live devices allows you to create custom instruments, audio effects, MIDI effects, and MIDI Tools to extend Ableton Live's functionality [1].

Here is a general workflow to start building your own Max devices:

**1. Load an Empty Device or Template**
To begin, drag an empty Max Instrument, Max Audio Effect, or Max MIDI Effect from Live's browser into your Set [2]. If you want to build a MIDI Tool specifically (like a note generator or transformation tool), you can use the Max MIDI Transformation or Generator templates found in the Clip View [3]. Alternatively, you can open an existing Max for Live device to modify and learn from it [3].

**2. Open the Max Editor (Patcher)**
In the title bar of the loaded Max device, click the **Edit** button [4]. This will launch the Max editor, commonly referred to as the "patcher," in a new separate window with the device ready for editing [4].

**3. Build Your Device**
Inside the patcher, you construct your device using various "objects." These objects send data to one another by connecting them together with virtual cables [2]. The specific objects and connections you use will determine exactly what your custom device does [4].

**4. Save Your Work**
Unlike Live's native devices, Max devices are saved as separate files rather than being contained inside the Live Set itself [4]. When you are finished editing, use the **Save** or **Save As** commands within the Max patcher's File menu [4]. It is highly recommended to save your Max devices and their associated presets into your User Library so that Live can easily keep track of any file dependencies [4, 5].

**How to Learn Max Programming:**
If you are new to programming in Max, there are several resources to help you learn the ropes:

* **Built-in Reference:** In any Max window, you can select "Reference" from the Help menu to access comprehensive documentation and tutorials provided by Cycling '74 (the co-developers of Max) [6].
* **Building Max Devices Pack:** You can download this specific Ableton Pack, which contains in-depth, hands-on lessons covering all the steps needed to build your own tools [7].

What kind of device are you looking to build first?