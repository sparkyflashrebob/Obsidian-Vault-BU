Daily Project Log: December 1, 2025

This document provides a chronological log of key conversations, technical decisions, and actionable outcomes for the project on December 1, 2025.


--------------------------------------------------------------------------------


1. Morning Technical Review (07:31)

The day began with a technical alignment session to synchronize on project documentation and prepare for upcoming milestones. This initial conversation was critical for establishing a common understanding of the current drawing set, the client's detailed specifications, and the equipment lists that will guide both installation and programming efforts.

Project Drawings and Pull List Synchronization

The primary focus was on ensuring all team members are working from the most current documentation. A new, updated cable pull list spreadsheet was identified, which needs to replace a preliminary version previously shared. The discussion highlighted the importance of rigorous document management, including proper file naming and storage in designated project folders (Ignite, Engineering) to avoid confusion as the project progresses. Using Bluebeam for tracking late-stage changes was also reinforced as a key project process.

Action Items:

* Replace the outdated cable pull list link with the link to the new, current spreadsheet.
* Archive the old pull list file in the engineering folder to maintain a historical record while removing it from active use.
* Standardize the practice of placing key engineering documents in both the main Ignite folder and the specific Engineering subfolder for better organization.

Review of Room Types and Client Specifications

A review of the project scope confirmed there are seven distinct room types. Three of these are unique, single-room designs, while the remaining types are deployed across multiple spaces (e.g., ten medium rooms, several huddle rooms). The client has provided highly specific instructions that must be followed, including detailed color-coding for HDMI cables and fabrication requirements for umbilicals between racks and lecterns. The team was directed to the consultant's "roughin" drawings and other specification documents within the Bluebeam session as the primary source for this information.

Action Items:

* Review client specification documents to fully understand the requirements for cable color-coding, lectern fabrication, and other detailed instructions.
* Utilize the consultant's drawing set for information regarding projector locations and initial infrastructure layout.

Equipment List Discrepancies and Programming Plan

An analysis of the equipment list revealed a discrepancy: RackLink units were noted on the client's provided list but were missing from the project's Bill of Materials (BOM). This will require a formal Request for Information (RFI) to clarify responsibility. The conversation also touched on the programming timeline, with an initial target of December 18th for the programmer to deliver a preliminary code template based on the client's existing system.

Action Items:

* Initiate an RFI to address the missing RackLink units and confirm whether they should be added to the project BOM.
* Follow up with the project manager to confirm the programming schedule and ensure the programmer is on track for a pre-Christmas code delivery.
* Discuss the feasibility of a pre-commissioning lab setup (mock lectern and display) to test the code before deploying to the field.

This morning review successfully aligned the engineering team on critical documentation and identified key tasks required to ensure the pull lists, drawings, and equipment orders are accurate.

1. Mid-Morning Coordination (09:31)

This session served as a direct follow-up to the morning's technical review. The focus shifted to executing the tasks identified earlier, including updating the cable pull list with newly discovered details, clarifying drawing ambiguities, and formalizing the project timeline through development and commissioning.

Document Management and Stakeholder Updates

Progress was confirmed on document cleanup. Obsolete preparatory drawings have been archived to the engineering folder, and the link in the project's Slack channel has been updated to point directly to the current cable pull list. This ensures that all stakeholders, including field teams, are accessing the correct and most recent version.

Action Items:

* Continue to archive outdated or superseded documents to maintain a clean and unambiguous working project folder.

Cable Pull List Audit and Revision

A detailed review of the drawings against the newly adopted pull list revealed that several spare network cables specified in the drawings were missing from the spreadsheet. These spares were identified in two rooms (System Type 2, specifically room A241) and must be added to ensure the installation matches the engineered design.

Action Items:

* Edit the master cable pull list spreadsheet to add the spare cables as indicated on the functional drawings for the System Type 2 rooms.

Drawing Clarifications and USB Extender De-scoping

A potential issue was identified on the drawings for one room type, which showed a USB extender connecting equipment. It was determined that since all source equipment is located in a credenza directly below the display, there is no extended distance to justify the use of an extender. This component is therefore unnecessary. The drawing will be marked up to reflect this de-scoping.

Action Items:

* Delete the unnecessary USB extender and its associated cabling from the design for the affected rooms.
* Cloud the relevant drawing section with a note indicating that all infrastructure is located behind the display, making the extender obsolete.

Programmer Coordination and Project Milestone Confirmation

The project timeline was discussed and confirmed. A key technical meeting with the programmer is scheduled for the following day (December 2nd). The critical path milestones were reaffirmed:

* Rack Build: Scheduled for the third week of December (15th-19th).
* Preliminary Code Delivery: Expected from the programmer by December 18th.
* Commissioning: Set to begin at the end of January.

Action Items:

* Ensure senior engineering staff are included in the meeting invitation with the programmer.
* Propose a one-to-two-day lab development session in early January to test the programming on a mock system (one rack, one lectern setup) to de-risk the field commissioning phase.

Bill of Materials (BOM) and Owner-Furnished Equipment (OFE) Integration

A significant task is to integrate a large list of Owner-Furnished Equipment (OFE) into the project's master BOM. An Internal Change Order (ICO) has been prepared with over 600 line items, initially based on the client's equipment list. This ICO needs to be audited for accurate counts and variations across room types before being imported.

Action Items:

* Audit the prepared ICO, verifying equipment quantities for all room type variations (e.g., adding projectors for larger rooms).
* Organize the ICO by location (e.g., Rack, Lectern, Display) to facilitate rack fabrication, field installation planning, and asset tracking.
* Import the audited and organized ICO into the project to create a comprehensive master equipment list.

Projection Screen Schedule Verification

A review of the consultant's projection schedule indicated two screen sizes are specified: 92-inch and 116-inch widths. However, a cross-check with a different document suggested a 133-inch screen for the large rooms. This discrepancy requires verification.

Action Items:

* Conduct a full audit of all project documents to confirm the correct projection screen sizes for each room type.
* Request an updated and definitive projection screen schedule from the client to resolve any discrepancies.
* Mark up the drawings with the confirmed screen sizes once verified.

This coordination session resulted in tangible progress on document accuracy and a clear, confirmed schedule for the critical rack build and programming phases.

1. Field Coordination Call (11:31)

This call was a direct touchpoint with the field team, represented by Tim, to translate engineering decisions into clear, actionable guidance for the on-site installation crew.

Drawing Markups and Equipment Clarification

Instructions were provided to Tim on how to locate the specific drawing markups in Bluebeam, which now clearly identify the relevant room locations. A previous concern about mismatched part numbers for a receiver (2304) was clarified; it was confirmed that the equipment on site is acceptable, and the issue was simply a documentation clarification rather than an equipment problem.

Action Items:

* Field team to reference the clouded markups in the Bluebeam session to identify the correct device locations for installation.

LED Wall Installation Guidance

A critical warning was issued regarding the installation of the flat-panel LED walls. Due to the minimal space behind these displays, care must be taken to ensure that data cables are not pinched or damaged when the wall is mounted. To aid in future commissioning and service, a directive was given to pull one extra data cable to each side of the wall. This will allow technicians to easily connect a laptop to the control switch during configuration.

Action Items:

* During LED wall installation, ensure a clear and safe cable path to prevent pinching of data lines.
* Pull one additional data cable to each side of the LED wall infrastructure to serve as a commissioning/service port.

This call ensured that the on-site team has the precise information needed to proceed with installation, mitigating potential issues with equipment and infrastructure.

1. Afternoon Check-in (13:31)

This brief conversation was a final check-in to confirm the division of labor for a specific installation task with team member Russ.

Ceiling Speaker Installation Confirmation

The discussion confirmed that Russ's team will take responsibility for installing the ceiling speakers located in the break room and reception area. It was noted that care should be taken to ensure the speakers are mounted securely to avoid any sagging in the ceiling tiles.

Action Items:

* Russ's team is confirmed to handle the installation of ceiling speakers in the break room and reception areas.

This final check-in concluded the day's coordination, ensuring all outstanding installation tasks were clearly assigned.


--------------------------------------------------------------------------------


1. Personal and Non-Business Log

* (07:31) Exchanged Thanksgiving pleasantries at the beginning of the morning call.
* (09:31) Joked about audio issues at the start of the call, pretending a team member couldn't hear the conversation.
* (13:31) Brief personal small talk about surviving the day and getting back into the work groove after the holiday.
