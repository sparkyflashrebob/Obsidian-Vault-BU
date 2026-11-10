---
tags:
  - notebooklm-import
notebook: "C_AI_AI Prompting - Agents - Computer - Tips"
category: "research"
---

It's clear why you're noticing a big difference between the two infographics!

The core reason why the NotebookLM infographic looks better isn't actually about a specific magic word you used or a small prompt change you could make. It comes down to a fundamental difference in **how the underlying AI technologies are designed to function.**

Here’s a breakdown of why they look so different and why you can’t get the NotebookLM level of design with the simple prompting approach you were using.

### 1. The Fundamental Difference: Task-Specific AI vs. General-Purpose AI

This is the single most important factor. The two tools are built for completely different purposes:

* **NotebookLM (Task-Specific AI):** Think of this as a highly-skilled specialist. It's not a general-purpose image generator. **NotebookLM is an application built by Google engineers specifically to understand, process, and present your source materials.**
* It has a dedicated "Infographic" function. When you click that button, you aren't just sending a text prompt to a general image AI. You are triggering a sophisticated pipeline.
* First, its language model (LLM) **deeply analyzes your sources** to extract key concepts, relationships, and hierarchies.
* Then, it takes that structured information and uses **pre-programmed design templates and rules** that Google's UI/UX designers have created. These templates dictate the overall layout (e.g., this "spoke-and-hub" style), color palette selection, font choices, icon placement, and balance of text and visuals.
* The final output is **highly structured, coherent, and design-led** because design principles were "baked-in" to the process from the start.
* **Your Image (General-Purpose AI):** Your image was likely created using a general-purpose, text-to-image generator like DALL-E 3, Midjourney, or Stable Diffusion. These are incredibly powerful generalists—like a brilliant artist who can paint anything you describe. But that means their primary skill is **interpreting your description, not understanding a complex database.**
* When you provide text for a complex concept like a mind map, the AI doesn't "know" the deeper meaning or hierarchical structure of that text. It sees it as a sequence of words to label parts of a picture.
* It has to invent a design from scratch based *only* on the text you provided. It isn't pulling from a curated set of infographic templates designed by experts.
* The result is often visually coherent as an image but **lacks the structured, precise, and design-forward layout** of a purpose-built tool like NotebookLM. The design choices (layout, spacing, icon quality) are generated on the fly, not guided by expert design rules.

**Analogy:**

**General AI:** You ask a very talented illustrator to paint a picture of "a map of my mind about aggregates." They will paint a creative and visually interesting interpretation.

**NotebookLM:** You give a set of detailed lecture notes to a professional infographic designer. They will create a clean, organized, and structurally precise diagram using charts and icons, based on their expertise in data visualization.

### Why Your Specific Prompt Changes Didn't Work

* **Changing "mind map" to "image":** This is a red herring. It didn't make the generation "better" or more "design-forward." It just made it less specific, allowing the AI to invent *any* kind of image. For a complex concept, this often results in something more chaotic or artistic and *less* structured. It doesn't trigger a secret "infographic" mode.
* **Complex, long prompt with all the data:** You tried to "feed" the AI all the data for all the branches within a single prompt. This is incredibly difficult for general image models to manage. The prompt becomes extremely dense and hard to "unravel." The AI might get some of the hierarchy right but will often struggle to create a clean layout, consistent icon quality, or balance all the textual elements. It becomes "word soup" trying to fit into a visual structure it's inventing on the fly.

### How to Get Your General AI Image to Look More Like NotebookLM's

You can't perfectly replicate the process, but you can dramatically improve your results by changing **your prompting strategy**. Instead of just giving it all the data, you need to "become the designer" and tell the AI **how to structure and visually present that data.**

**Here is the type of prompt you need to write:**

A professional, modern **spoke-and-hub infographic** on a clean, light off-white background. The central hub is a large, glowing blue-white circle labeled **"AGGREGATES: THE SUM OF THE PARTS"** with a subtitle "A single whole formed by many individual components across various disciplines."

Four distinct main "spokes" or branches radiate outward. Each branch is a different color and contains a distinct hub with a key concept, leading to smaller, detailed nodes.

**Branch 1 (Top Left, Teal Blue):** A hub labeled **"PHILOSOPHY & PSYCHOLOGY"** with a detailed human brain icon. Nodes connect to it with minimalist icons and text for **FORM**, **SENSATION**, **PERCEPTION**, **MENTAL FORMATIONS**, and **CONSCIOUSNESS**.

**Branch 2 (Top Right, Emerald Green):** A hub labeled **"DATA SCIENCE & STATISTICS"** with a chart and magnifying glass icon. Nodes connect with icons and text for **SUM**, **AVERAGE**, **COUNT**, and **MIN/MAX**.

**Branch 3 (Bottom Left, Burnt Orange):** A hub labeled **"CONSTRUCTION & GEOLOGY"** with a construction crane and hard hat icon. Nodes connect with icons for **SKELETAL FOUNDATION**, **SAND & GRAVEL**, **CRUSHED STONE**, and **RECYCLED CONCRETE**.

**Branch 4 (Bottom Right, Rich Purple):** A hub labeled **"ECONOMICS"** with a globe and rising arrow icon. Nodes connect with icons for **AGGREGATE DEMAND**, **AGGREGATE SUPPLY**, and **GLOBAL MARKET**.

The overall style should be minimal, clean, with bold, high-contrast text and sharp, flat or semi-flat graphic icons. All text should be clear and legible. Use connecting lines that are clean and flow well. Include a tiny "NotebookLM" watermark in the very bottom right.

### Summary of Prompting Changes

1. **Focus on Design & Layout First:** Define the core structure (**spoke-and-hub**, concentric circles, tree diagram, etc.).
2. **Be Your Own Art Director:** Specify colors (**teal**, **emerald**, **orange**, **purple**), background (**clean off-white**), and text style (**clear**, **legible**, **bold**).
3. **Detail Each Section Individually:** Instead of one massive data dump, explicitly describe the contents of each "spoke," naming the icon and the text for every node.
4. **Demand Clarity and Hierarchy:** Tell the AI that text should be clear and that there is a hierarchy of information.

By taking this descriptive, design-focused approach, you are effectively giving the general-purpose AI the **instructions and constraints** that are "baked-in" to a purpose-built tool like NotebookLM.