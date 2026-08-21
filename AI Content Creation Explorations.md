Gemini Storybook

Prompt

Create a storybook about how our perspective of the world changes and how we interact with the world we experience based on our relationship to things.  I  call this "The Story of Different Hats".  Include examples of waking up in the morning and our habitual mode of operation, driving in a car and commuting vs not having to be anywhere, being in a grocery line, interacting with our employer (boss) and coworkers, with your family, with people who you like and with those that you don't.  Note the default mode and also when you are engaging in a task where you forget your personal view and focus on others. It should incorporate aspects of mindfulness is all activities as a primary theme, not being perfect in that we have emotions, preferences, needs and desires, are conditioned beings, and have biases that have been developed (such as immediate gratification and dependency).  Elements of spiritual awakening, neuroscience, psychology.  Note where the neuroscience aspect of our predictive brain reacting prior to thinking.

----
Notebook LM to Gemini - Generic Prompt

As an expert in Information Architecture and AI Strategy, I will provide you with a high-performance "Bridging Prompt."

The goal of this prompt is to force Gemini to act as a connective layer between isolated notebooks, overcoming the "selective retrieval" limitation by requiring it to map the data from all sources before answering.

The "Connective Architecture" Prompt
This prompt uses a Structured Contextual Framework (Persona + Multi-Source Anchoring + Task + Format). Use this when you have attached two or more notebooks to your Gemini chat.

Copy and paste the following:

Persona: Act as a Senior Research Strategist and Information Architect.

Context: I have attached [Number, e.g., 2] NotebookLM notebooks: "[Notebook Name A]" which contains [Brief Topic, e.g., market research] and "[Notebook Name B]" which contains [Brief Topic, e.g., product specs].

The Retrieval Phase (Step 1): Before answering my main question, perform a "High-Level Index Scan." Identify the top 3 themes from Notebook A that intersect with the core objectives found in Notebook B. List these themes as a "Connection Map" first.

The Analysis Phase (Step 2): Based on the identified intersections, answer the following: [YOUR QUESTION HERE].

Constraints: > * Ground every claim in a specific source from the notebooks.

If the notebooks provide conflicting data on the same topic, highlight the discrepancy explicitly.

Use a "Synthesis" format: Provide the answer followed by a table of "Cross-Notebook Insights."

Why This Prompt Works
Forces Comprehensive Retrieval: By asking for a "Connection Map" in Step 1, you prevent Gemini from "lazily" pulling from just the first source it finds. It must scan both notebooks to find the overlap.

Conflict Detection: One of the biggest issues with multiple notebooks is contradictory information. This prompt builds in a "Red Team" instruction to alert you if your sources disagree.

Clickable Citations: Because you are using the NotebookLM integration in Gemini, the "Ground every claim" instruction will trigger the UI to show you exactly which source and note the information came from.

Pro-Tip: Use the "Master Summary" Hack
If your notebooks are very dense (e.g., hundreds of sources), Gemini’s retrieval may still miss subtle points.

Go into NotebookLM standalone first.

Select all notes and click "Create Table of Contents" or "Study Guide."

Back in Gemini, tell it: "Prioritize the 'Study Guide' and 'Table of Contents' notes in both notebooks to get the big picture before searching the raw sources."



---
