import pypdf

def populate_community_ed_pdf():
    input_pdf = "CS Course Outline 2024.pdf"
    output_pdf = "CS_Course_Outline_2024_Aspects_of_Mindfulness_READY_TO_SUBMIT.pdf"
    
    reader = pypdf.PdfReader(input_pdf)
    writer = pypdf.PdfWriter()
    writer.append(reader)
    
    # Enable multiline word-wrapping and set balanced fonts on fields where the original form had bugs
    for page in writer.pages:
        for annot in page.get("/Annots", []):
            obj = annot.get_object()
            t = str(obj.get("/T", ""))
            
            # Field 10 was created as single-line by mistake in the original template; enable multiline (flag 4096)
            if "10 DEGREESCREDENTIALS" in t:
                obj[pypdf.generic.NameObject("/Ff")] = pypdf.generic.NumberObject(4096)
                obj[pypdf.generic.NameObject("/DA")] = pypdf.generic.create_string_object("/Helv 8 Tf 0 g")
            
            # Field 12 (Requisites / Other)
            if "12 PREANDOR" in t:
                obj[pypdf.generic.NameObject("/Ff")] = pypdf.generic.NumberObject(4096)
                obj[pypdf.generic.NameObject("/DA")] = pypdf.generic.create_string_object("/Helv 9 Tf 0 g")
                
            # Normalize main narrative fields for consistent legible typography
            if t == "Course Description":
                obj[pypdf.generic.NameObject("/DA")] = pypdf.generic.create_string_object("/Helv 8.5 Tf 0 g")
            elif "13 STUDENT LEARNING" in t:
                obj[pypdf.generic.NameObject("/DA")] = pypdf.generic.create_string_object("/Helv 7.5 Tf 0 g")
            elif "14 CRITICAL THINKING" in t:
                obj[pypdf.generic.NameObject("/DA")] = pypdf.generic.create_string_object("/Helv 7.5 Tf 0 g")
            elif "15 METHODS" in t:
                obj[pypdf.generic.NameObject("/DA")] = pypdf.generic.create_string_object("/Helv 8 Tf 0 g")
            elif "16 EVALUATION" in t:
                obj[pypdf.generic.NameObject("/DA")] = pypdf.generic.create_string_object("/Helv 8 Tf 0 g")
            elif "17 SPECIAL ROOM" in t:
                obj[pypdf.generic.NameObject("/DA")] = pypdf.generic.create_string_object("/Helv 8 Tf 0 g")
            elif "18 LENGTH OF COURSE" in t:
                obj[pypdf.generic.NameObject("/DA")] = pypdf.generic.create_string_object("/Helv 8 Tf 0 g")
            elif "20 TEXTBOOKS" in t:
                obj[pypdf.generic.NameObject("/DA")] = pypdf.generic.create_string_object("/Helv 8.5 Tf 0 g")
            elif t in ["Week or Hour", "Text2"]:
                obj[pypdf.generic.NameObject("/DA")] = pypdf.generic.create_string_object("/Helv 8.5 Tf 0 g")

    page1_fields = {
        "1 COURSE TITLERow1": "Aspects of Mindfulness: Cultivating Presence, Focus, and Compassion",
        "3 INSTRUCTORS NAMERow1": "Andy",
        "7 STATERow1": "CA",
        "10 DEGREESCREDENTIALSOTHER RELATIVE QUALIFICATIONS PLEASE ATTACH A FULL RESUMERow1": (
            "Mindfulness Facilitator & Meditation Educator; Leader of Living Mindfully community groups; "
            "extensive background in attention regulation and contemplative inquiry. (See attached resume)."
        ),
        "11 MAXIMUM ENROLLMENTRow1": "20-25",
        "12 PREANDOR COREQUISITESRow1": "None (Open to all adult community members)",
        "Course Description": (
            "Designed for community members seeking greater mental clarity, emotional balance, and sustained focus, "
            "this 7-week course explores the foundations and lived practices of mindfulness. Students examine how digital "
            "distraction, attentional drift, and chronic stress patterns deplete vital energy and fracture concentration. "
            "Through guided experiential practices, cognitive neuroscience insights, and supportive group discussion, we "
            "cultivate the 'two wings of practice'—clear seeing and an open, caring heart. Participants learn practical "
            "techniques to anchor attention, recognize the body's natural stress reflexes without self-judgment, and "
            "distinguish raw sensory experiences from runaway mental narratives. Students gain accessible, lifelong tools "
            "for calm, single-tasking focus, and compassionate living."
        ),
        "13 STUDENT LEARNING OUTCOMES see back of form Upon completion of this course students will be able toRow1": (
            "1. Demonstrate Attentional Stability: Apply focused attention and sensory anchoring techniques to sustain focus, minimize cognitive drift, and practice single-tasking in daily activities.\n\n"
            "2. Distinguish Sensation from Story: Differentiate between raw sensory input (the First Arrow) and secondary mental narratives, worry, or self-judgment (the Second Arrow).\n\n"
            "3. Recognize Somatic Conditionality: Identify bodily tension (such as a tight or knotted stomach) as a conditioned biological survival response rather than a personal failure, using mindful pauses to restore physiological equilibrium.\n\n"
            "4. Apply Mindful Communication: Practice deep, compassionate listening and thoughtful speech to enhance connection, reduce conflict, and foster empathy in personal and professional relationships."
        ),
        "14 CRITICAL THINKING SKILLS see back of form During this course students will develop or use these critical thinking processes or activitiesRow1": (
            "1. Analyze Attention Dynamics: Analyze personal habits of digital distraction and multitasking, evaluating the mental cost of cognitive switching versus single-tasking focus.\n\n"
            "2. Differentiate Perception from Interpretation: Differentiate between neutral sensory data entering through the senses and subsequent catastrophic interpretations or narrative biases.\n\n"
            "3. Deconstruct Biological Stress Responses: Deconstruct automatic fight-or-flight reactions using principles of evolutionary biology, comparing wild animal threat recovery with human cognitive rumination.\n\n"
            "4. Formulate Grounded Action Plans: Formulate individualized mindfulness and compassion protocols to interrupt automatic reactivity and redirect mental energy into constructive, skillful living."
        ),
        "15 METHODS OF INSTRUCTION see back of formRow1": (
            "Interactive lecture, guided experiential mindfulness and attentional exercises, somatic awareness practices, "
            "facilitated group reflections, partner listening dyads, and weekly home observation experiments."
        ),
        "16 EVALUATION see back of formRow1": (
            "Weekly self-reflective practice logs, active engagement in group discussions and contemplative exercises, "
            "self-assessment of attentional habits, and completion of a personal mindfulness and focus action plan."
        ),
        "17 SPECIAL ROOM REQUIREMENTS ANDOR LOCATIONRow1": (
            "Quiet, comfortable classroom with movable chairs arranged in a circle or semi-circle; whiteboard; AV projector/screen for presentation slides. Kentfield Campus, Indian Valley Campus (Novato), or remote via Zoom."
        ),
        "18 LENGTH OF COURSERow1": (
            "7 weeks, meeting once weekly for 2 hours per session (14 total instructional hours). Standard COM Community Education quarter format (evenings or Saturday mornings preferred)."
        )
    }
    
    page2_outline_left = (
        "Week 1 (Hours 1-2)\n\n\n"
        "Week 2 (Hours 3-4)\n\n\n"
        "Week 3 (Hours 5-6)\n\n\n"
        "Week 4 (Hours 7-8)\n\n\n"
        "Week 5 (Hours 9-10)\n\n\n"
        "Week 6 (Hours 11-12)\n\n\n"
        "Week 7 (Hours 13-14)"
    )
    
    page2_outline_right = (
        "Foundations of Mindfulness & Attention: The Spotlight & The Floodlight\n"
        "• Demystifying mindfulness; sensory breath anchors; working with cognitive drift.\n\n"
        "Single-Tasking & Focus in the Digital Age: Working with Distraction\n"
        "• Cognitive switching costs; digital boundaries; mindful single-tasking laboratory.\n\n"
        "The Two Wings of Practice: Balancing Clear Seeing and an Open Heart\n"
        "• Clear Seeing (Head) and The Open Heart (Compassion/Warmth); avoiding self-criticism.\n\n"
        "Stress Physiology & Somatic Conditionality: Belly Tightness & Threat Response\n"
        "• Biological survival reflexes vs personal failure; animal vs human threat recovery.\n\n"
        "The Two Arrows: Discerning Primary Impact from Mental Fiction\n"
        "• Raw sensory data (First Arrow) vs runaway mental narrative & catastrophizing.\n\n"
        "Mindful Communication & Compassion: Deep Listening in Daily Life\n"
        "• Deep listening without defense; noticing somatic tension; empathy practice dyad.\n\n"
        "Rewiring the Stress Habit: A Sustainable Blueprint for Daily Living\n"
        "• Shifting chronic stress into calm vitality; micro-pauses; personal action plan."
    )
    
    page2_fields = {
        "Week or Hour": page2_outline_left,
        "Text2": page2_outline_right,
        "20 TEXTBOOKS AND REQUIRED MATERIALS see instructions AUTHOR TITLE PUBLISHER LOCATION NAME PUBLICATION DATE": (
            "All texts recommended, not required (per COM Community Education guidelines):\n"
            "1. Amishi P. Jha, Ph.D. - Peak Mind: Find Your Focus, Own Your Attention (HarperOne, 2021)\n"
            "2. Tara Brach, Ph.D. - Trusting the Gold: Uncovering Natural Goodness and Healing the Heart (Sounds True, 2021)\n"
            "3. Mark Williams & Danny Penman - Mindfulness: An Eight-Week Plan for Finding Peace (Hachette, 2021)"
        ),
        "EST COST PER STUDENT 1": "$0.00",
        "COMMENTS 1": "Digital handouts and syllabus provided via PDF",
        "EST COST PER STUDENT 2": "$0.00",
        "COMMENTS 2": "Standard classroom space provided by College of Marin",
        "EST COST PER STUDENT 3": "$0.00",
        "COMMENTS 3": "Students bring their own notebook and pen",
        "EST COST PER STUDENT 4": "$0.00",
        "COMMENTS 4": "Not applicable",
        "EST COST PER STUDENT 5": "$0.00",
        "COMMENTS 5": "Not applicable"
    }
    
    writer.update_page_form_field_values(writer.pages[0], page1_fields)
    writer.update_page_form_field_values(writer.pages[1], page2_fields)
    
    with open(output_pdf, "wb") as f_out:
        writer.write(f_out)
        
    print(f"Generated clean pre-filled PDF: {output_pdf}")

if __name__ == "__main__":
    populate_community_ed_pdf()
