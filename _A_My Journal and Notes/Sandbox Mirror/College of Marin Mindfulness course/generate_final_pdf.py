import fitz
import os
import shutil

def generate_proposal_pdf():
    input_pdf = "CS Course Outline 2024.pdf"
    output_pdf = "Living_Better_with_Mindfulness_Course_Proposal.pdf"
    
    doc = fitz.open(input_pdf)
    
    # ------------------ PAGE 1 ------------------
    page1 = doc[0]
    for w in page1.widgets():
        name = w.field_name
        if "1 COURSE TITLE" in name:
            w.field_flags |= fitz.PDF_TX_FIELD_IS_MULTILINE
            w.field_value = "Living Better with Mindfulness: Practical Tools for Calm, Focus, and Resilience"
            w.text_fontsize = 9.5
            w.update()
        elif "3 INSTRUCTORS NAME" in name:
            w.field_value = "Andy McGuire"
            w.text_fontsize = 10.0
            w.update()
        elif "4 PHONE NUMBER" in name:
            w.field_value = "(415)637-0348"
            w.text_fontsize = 10.0
            w.update()
        elif "5 ADDRESS" in name:
            w.field_value = "326 Larkspur Plaza Drive"
            w.text_fontsize = 10.0
            w.update()
        elif "6 CITY" in name:
            w.field_value = "Larkspur"
            w.text_fontsize = 10.0
            w.update()
        elif "7 STATE" in name:
            w.field_value = "CA"
            w.text_fontsize = 10.0
            w.update()
        elif "8 ZIP CODE" in name:
            w.field_value = "94939"
            w.text_fontsize = 10.0
            w.update()
        elif "9 EMAIL" in name:
            w.field_value = "sparkyflashrebob@gmail.com"
            w.text_fontsize = 9.2
            w.update()
        elif "10 DEGREES" in name:
            w.field_flags |= fitz.PDF_TX_FIELD_IS_MULTILINE
            w.field_value = (
                "MMTCP Certified Mindfulness Meditation Facilitator (2023) & Mindfulness Educator since 2009; "
                "Meditation Teacher at Bayside Marin & Azure Acres; Leader, Living Mindfully. (See attached resume)."
            )
            w.text_fontsize = 7.2
            w.update()
        elif "11 MAXIMUM" in name:
            w.field_value = "20-25"
            w.text_fontsize = 10.0
            w.update()
        elif "12 PREANDOR" in name:
            w.field_flags |= fitz.PDF_TX_FIELD_IS_MULTILINE
            w.field_value = "None (Open to all adult community members)"
            w.text_fontsize = 9.0
            w.update()
        elif name == "Course Description":
            w.field_flags |= fitz.PDF_TX_FIELD_IS_MULTILINE
            w.field_value = (
                "Designed for anyone seeking greater calm, mental clarity, and focus in a hectic world, "
                "this welcoming 7-week course offers practical, science-backed tools for daily life. Students explore how digital "
                "distraction, racing thoughts, and chronic stress deplete vital energy and fracture concentration. "
                "Through guided experiential practices, supportive group discussions, and simple daily micro-exercises, we "
                "learn to anchor scattered attention, soothe bodily tension without self-judgment, and "
                "distinguish everyday reality from runaway mental worry. Whether navigating workplace pressures, difficult interactions, "
                "or simply seeking greater presence, you will gain accessible, lifelong tools for living with greater ease, clarity, and heart."
            )
            w.text_fontsize = 8.5
            w.update()
        elif "13 STUDENT" in name:
            w.field_flags |= fitz.PDF_TX_FIELD_IS_MULTILINE
            w.field_value = (
                "1. Demonstrate Attentional Stability: Apply focused attention and sensory anchoring techniques to sustain focus, minimize cognitive drift, and practice single-tasking in daily activities.\n\n"
                "2. Distinguish Sensation from Story: Differentiate between raw sensory input (the First Arrow) and secondary mental narratives, worry, or self-judgment (the Second Arrow).\n\n"
                "3. Recognize Somatic Conditionality: Identify bodily tension (such as a tight or knotted stomach) as a conditioned biological survival response rather than a personal failure, using mindful pauses to restore physiological equilibrium.\n\n"
                "4. Apply Mindful Communication: Practice deep, compassionate listening and thoughtful speech to enhance connection, reduce conflict, and foster empathy in personal and professional relationships."
            )
            w.text_fontsize = 7.5
            w.update()
        elif "14 CRITICAL" in name:
            w.field_flags |= fitz.PDF_TX_FIELD_IS_MULTILINE
            w.field_value = (
                "1. Analyze Attention Dynamics: Analyze personal habits of digital distraction and multitasking, evaluating the mental cost of cognitive switching versus single-tasking focus.\n\n"
                "2. Differentiate Perception from Interpretation: Differentiate between neutral sensory data entering through the senses and subsequent catastrophic interpretations or narrative biases.\n\n"
                "3. Deconstruct Biological Stress Responses: Deconstruct automatic fight-or-flight reactions using principles of evolutionary biology, comparing wild animal threat recovery with human cognitive rumination.\n\n"
                "4. Formulate Grounded Action Plans: Formulate individualized mindfulness and compassion protocols to interrupt automatic reactivity and redirect mental energy into constructive, skillful living."
            )
            w.text_fontsize = 7.5
            w.update()
        elif "15 METHODS" in name:
            w.field_flags |= fitz.PDF_TX_FIELD_IS_MULTILINE
            w.field_value = (
                "Interactive lecture, guided experiential mindfulness and attentional exercises, somatic awareness practices, "
                "facilitated group reflections, partner listening dyads, and weekly home observation experiments."
            )
            w.text_fontsize = 8.0
            w.update()
        elif "16 EVALUATION" in name:
            w.field_flags |= fitz.PDF_TX_FIELD_IS_MULTILINE
            w.field_value = (
                "Weekly self-reflective practice logs, active engagement in group discussions and contemplative exercises, "
                "self-assessment of attentional habits, and completion of a personal mindfulness and focus action plan."
            )
            w.text_fontsize = 8.0
            w.update()
        elif "17 SPECIAL" in name:
            w.field_flags |= fitz.PDF_TX_FIELD_IS_MULTILINE
            w.field_value = (
                "Quiet, comfortable classroom with movable chairs arranged in the standard manner; whiteboard; "
                "AV projector/screen/or large display for presentation slides. Kentfield Campus."
            )
            w.text_fontsize = 8.2
            w.update()
        elif "18 LENGTH" in name:
            w.field_flags |= fitz.PDF_TX_FIELD_IS_MULTILINE
            w.field_value = (
                "7 weeks, meeting once weekly for 2 hours per session (14 total instructional hours). "
                "Standard COM Community Education quarter format."
            )
            w.text_fontsize = 8.5
            w.update()

    # ------------------ PAGE 2 ------------------
    page2 = doc[1]
    page2_outline_left = (
        "Week 1 (Hours 1-2)\n\n\n\n"
        "Week 2 (Hours 3-4)\n\n\n"
        "Week 3 (Hours 5-6)\n\n\n"
        "Week 4 (Hours 7-8)\n\n\n"
        "Week 5 (Hours 9-10)\n\n\n"
        "Week 6 (Hours 11-12)\n\n\n"
        "Week 7 (Hours 13-14)"
    )

    page2_outline_right = (
        "Foundations of Mindfulness: The Spotlight, Floodlight & Benefits\n"
        "- Real-world benefits & the 'mental gym'; Demystifying mindfulness; sensory anchors; working with cognitive drift; 60-sec reset.\n\n"
        "Single-Tasking & Focus in the Digital Age: Working with Distraction\n"
        "- Cognitive switching costs; digital boundaries; mindful single-tasking laboratory.\n\n"
        "The Two Wings of Practice: Balancing Clear Seeing and an Open Heart\n"
        "- Clear Seeing (Head) and The Open Heart (Compassion/Warmth); avoiding self-criticism.\n\n"
        "Stress Physiology & Somatic Conditionality: Belly Tightness & Threat Response\n"
        "- Biological survival reflexes vs personal failure; animal vs human threat recovery.\n\n"
        "The Two Arrows: Discerning Primary Impact from Mental Fiction\n"
        "- Raw sensory data (First Arrow) vs runaway mental narrative & catastrophizing.\n\n"
        "Mindful Communication & Compassion: Deep Listening in Daily Life\n"
        "- Deep listening without defense; noticing somatic tension; empathy practice dyad.\n\n"
        "Rewiring the Stress Habit: A Sustainable Blueprint for Daily Living\n"
        "- Shifting chronic stress into calm vitality; micro-pauses; personal action plan."
    )

    textbooks = (
        "All texts recommended, not required (per COM Community Education guidelines):\n"
        "1. Amishi P. Jha, Ph.D. - Peak Mind: Find Your Focus, Own Your Attention (HarperOne, 2021)\n"
        "2. Tara Brach, Ph.D. - Trusting the Gold: Uncovering Natural Goodness and Healing the Heart (Sounds True, 2021)\n"
        "3. Mark Williams & Danny Penman - Mindfulness: An Eight-Week Plan for Finding Peace (Hachette, 2021)"
    )

    for w in page2.widgets():
        name = w.field_name
        if name == "Week or Hour":
            w.field_value = page2_outline_left
            w.text_fontsize = 8.5
            w.update()
        elif name == "Text2":
            w.field_flags |= fitz.PDF_TX_FIELD_IS_MULTILINE
            w.field_value = page2_outline_right
            w.text_fontsize = 8.5
            w.update()
        elif "20 TEXTBOOKS" in name:
            w.field_flags |= fitz.PDF_TX_FIELD_IS_MULTILINE
            w.field_value = textbooks
            w.text_fontsize = 8.5
            w.update()
        elif "EST COST" in name:
            w.field_value = "$0.00"
            w.text_fontsize = 8.5
            w.update()
        elif "COMMENTS 1" in name:
            w.field_value = "Digital handouts and syllabus provided via PDF"
            w.text_fontsize = 8.5
            w.update()
        elif "COMMENTS 2" in name:
            w.field_value = "Standard classroom space provided by College of Marin"
            w.text_fontsize = 8.5
            w.update()
        elif "COMMENTS 3" in name:
            w.field_value = "Students bring their own notebook and pen"
            w.text_fontsize = 8.5
            w.update()
        elif "COMMENTS 4" in name or "COMMENTS 5" in name:
            w.field_value = "Not applicable"
            w.text_fontsize = 8.5
            w.update()

    doc.save(output_pdf)
    print(f"Generated fully wrapped proposal PDF: {output_pdf}")
    
    # Copy to submittal directories
    workspace_submittal = os.path.join("COM Submittal", output_pdf)
    desktop_submittal = os.path.join(r"C:\Users\SparkyDesktop\Desktop\COM Submittal", output_pdf)
    
    shutil.copyfile(output_pdf, workspace_submittal)
    try:
        shutil.copyfile(output_pdf, desktop_submittal)
        print(f"Copied to Desktop: {desktop_submittal}")
    except PermissionError:
        print("Desktop file was locked; retry after closing viewer if open.")

if __name__ == "__main__":
    generate_proposal_pdf()
