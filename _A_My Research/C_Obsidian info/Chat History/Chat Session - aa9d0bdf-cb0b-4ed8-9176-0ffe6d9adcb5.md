---
tags:
  - notebooklm-import
notebook: "C_Obsidian info"
category: "research"
---

MODEL:

Adding inline metadata to your loose notes is a fantastic way to organize them without needing to set up formal YAML frontmatter blocks at the top of every page [1, 2]. Inline fields can be quickly typed anywhere within the body of your note, making them perfect for quick captures [2].

Here is how you can implement them:

**1. Standard Inline Fields**
You can create an inline field using a simple `key:: value` syntax with double colons [2, 3]. For example, if you are jotting down a quick note, you could type:
`Category:: Concept`
`Topic:: Dataview`
Because Dataview "sanitizes" these keys, you don't need to worry about exact formatting. It will automatically remove bolding, connect words with dashes, and ignore capitalization [4]. This means a field written as `**Category**::` or `CATEGORY::` will simply be queried as `category` [4, 5].

**2. Bracketed Inline Fields**
If you want to embed metadata naturally into a sentence without disrupting the flow of your writing, you can wrap the key and value in square brackets using the syntax `[key:: value]` [2, 5].
For instance, you might write:

* "I just had an interesting thought about machine learning `[topic:: Machine Learning]`."
* "This is a fantastic article `[rating:: 9]`!" [5].

These bracketed fields are visible in your editing view, but Dataview reads the metadata quietly in the background [6].

**3. Filtering into your Knowledge Base**
Once you add these quick inline fields to your loose notes, Dataview will index them [2]. You can then easily filter them into your Knowledge Base table using the `WHERE` command [7].

For example, your central dashboard query could look like this:

```
TABLE topic
FROM ""
WHERE category = "Concept"
```

Even if a note is buried in a random folder without any tags, this query will scan your entire vault, find the note with your inline `Category:: Concept` field, and neatly display it in your Knowledge Base [7-9].

Would you like to learn how to use built-in "implicit" metadata—like a note's creation date or folder path—to automatically organize notes that don't have any custom metadata at all?

USER:

yes

MODEL:

Building a Knowledge Base using your existing folder structure and loose notes is one of Dataview's most powerful applications. By querying specific paths and utilizing implicit data, you can turn a scattered vault into an organized, dynamic library.

Here is how you can use Dataview to aggregate your folder structures and wrangle your loose notes into a cohesive Knowledge Base:

**1. Querying by Folder Structure**
Dataview allows you to target specific directories in your vault using the `FROM` command [1, 2]. This means you don't necessarily need to tag every single note if they are already organized into folders.

* **Targeting specific folders:** If you keep your notes in a specific folder path, such as a "cards" or "concepts" folder, you can generate a table of everything inside it by using `FROM "cards/concepts"` [3, 4].
* **Excluding folders:** You can refine your Knowledge Base by excluding folders that might clutter your results (like templates or daily logs) by using an exclamation point, such as `FROM !"Templates"` [5].
* **Combining folders:** You can combine multiple folders into a single Knowledge Base view using the `OR` operator, such as `FROM "Literature" OR "Concepts"` [6].

**2. Managing "Loose" Notes**
Loose notes—those that aren't categorized, tagged, or linked—can easily get lost in a large vault. Dataview provides several ways to track them down so you can integrate them into your Knowledge Base:

* **Finding Untagged Notes:** You can build a list of all notes floating around without tags using the query `LIST WHERE length(file.tags) = 0` [7]. This uses the built-in `file.tags` property, which automatically arrays all tags in a note [1, 8].
* **Finding Empty Notes:** You can write a query designed to "flush out any empty notes" in your vault [9]. This is helpful for finding pages you created a link for but never actually wrote content for.
* **Finding Broken Links:** You can also design queries to find and display "broken or non-existent internal links" to ensure your Knowledge Base remains properly interconnected [10].

**3. Structuring a Knowledge Base Table**
Once you have your folders targeted, you can create a centralized dashboard note that acts as the front page of your Knowledge Base. By combining Dataview's `TABLE` format with metadata, you can view your notes with additional context [11, 12].

For example, if you have a folder of notes and you want to see them organized by category and topic, you could write a query like this:

```
TABLE category, topics
FROM "KnowledgeBaseFolder"
SORT file.mtime DESC
```

This query will display all notes from the "KnowledgeBaseFolder", output their `category` and `topics` fields as columns, and sort them so the most recently modified notes (`file.mtime`) appear at the top [1, 11].

If your loose notes cover multiple subjects, you could also use the `GROUP BY` command to cluster them together by category (e.g., `GROUP BY category`) [13], or group them by their tags [14, 15].

Would you like to see how to add simple inline metadata to your loose notes so they can be easily filtered into these Knowledge Base tables?

USER:

I would like to focus on a Knowledge Base for based on my Obsidian folder structure and loose notes.

MODEL:

**Project dashboards** in Obsidian can be set up in just a few minutes by using the Dataview plugin to aggregate specific notes and metadata into a centralized visual hub [1, 2]. By adding frontmatter properties like `status`, `priority`, and `due` to individual project notes, users can generate dynamic **project status tracking tables** that automatically update as their notes change [3, 4].

Within project dashboards, users leverage Dataview for various tracking features:

* **Visual task monitoring:** Dashboards can feature calendar views of upcoming project deadlines [5, 6] or custom progress bars built with DataviewJS that calculate the percentage of completed tasks within a project [5].
* **Advanced GTD workflows:** Users can emulate "Getting Things Done" methodologies by building custom project review schedules. These dashboards can filter for open projects, count incomplete tasks, and use custom logic to flag when a project is due for its regular review [7-10].
* **Daily and weekly views:** A daily dashboard can be divided into specific query blocks such as "urgent," "top 3," "all due," and "done today" tasks [11, 12]. Users can also create an "Upcoming 7 days" view to review impending tasks grouped by day and project [13, 14].
* **Interactive interfaces:** Using integrations with other plugins, Dataview can generate dashboards—like a "cycles and reviews dashboard" or a "system engineer wiki dashboard"—that display clickable navigation buttons organized into neat columns [15, 16].

**The Larger Context of Use Cases**
In the broader scope, Dataview turns an Obsidian vault into a live database, making data aggregation highly customizable for almost any interest [17]. Project management is just one facet of how the plugin is used. Other prominent use cases include:

* **Vault Maintenance:** Users frequently build queries to keep their vaults clean, such as finding empty notes [16], tracking down missing or broken internal links [15], or listing all pages that have no tags for follow-up [17, 18].
* **Personal Tracking & Events:** Dataview can be used to track daily habits, such as recording sleep data in daily notes to generate weekly sleep schedules [17]. It is also widely used to calculate and list upcoming birthdays or events, displaying the person's age and days until their next birthday [17, 19].
* **Media and Knowledge Bases:** Users construct dynamic libraries, such as compiling book notes into tables sorted by author and rating [17, 20], building complex recipe databases [21], or tracking the total word count of specific tagged pages [22].
* **Geolocational Tools:** Advanced users utilize DataviewJS to calculate straight-line or driving distances between geographic coordinates, creating a "nearby" list that automatically links friends, family members, or places of interest based on your current location [23, 24].

Are you interested in seeing the specific code required to build any of these dashboard components, such as the task progress bar or the upcoming birthdays table?

USER:

Discuss what these sources say about Project Dashboards, in the larger context of Use Cases.