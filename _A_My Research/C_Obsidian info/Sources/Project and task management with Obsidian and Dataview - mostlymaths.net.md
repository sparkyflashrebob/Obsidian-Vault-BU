---
tags:
  - notebooklm-import
notebook: "C_Obsidian info"
category: "research"
---

mostlymaths.net | Project and task management with Obsidian and Dataview
[mostlymaths.net](https://mostlymaths.net/)
\* [about](https://mostlymaths.net/pages/about/)

### Project and task management with Obsidian and Dataview

It actually works very well August 22, 2022 11 minutes read | 2303 words by [Ruben Berenguel](https://mostlymaths.net/) Some links are affiliate links
This post is about how I manage my tasks and projects using Obsidian with the [Dataview](https://blacksmithgu.github.io/obsidian-dataview/) plugin.
This is going to sound like *a lot* . A complex setup that seems overkill. It's not *completely* the case. It has evolved naturally from what my setup used to be with [Things](https://culturedcode.com/things/), and by adding features I wanted Things to have. At the end I will explain how it all evolved to show the historical perspective.
Overall, it is roughly based on a very loose interpretation of GTD (Getting Things Done). If you don't know what GTD is, [here's a quick reference](https://hamberg.no/gtd). Otherwise, [get the book](https://www.amazon.com/-/es/David-Allen/dp/0349408947?_encoding=UTF8&qid=1661192626&sr=8-1&linkCode=ll1&tag=rbersblog-20&linkId=ab0f422d0fce8e5c2db86834b5dcc5da&language=es_US&ref_=as_li_ss_tl). It's a bit outdated but still worth reading.

##### Projects

Shortcuts to simplify project processing
\* alt+t : enter template by name
\* project template shown below
\* reviewed template expands to reviewed: YYYYMMDD for “now”. It has a shortcut as alt+.
\* cmd+d : insert current date and time as [[YYYYMMDD]]@HH:mm
\* cmd+[ : go to previous page
\* cmd+] : go to next page
Projects are the main container for tasks. Except for periodical tasks (like, watering plants or recharging headphones) all my tasks are part of *exactly* one project. For periodical tasks, I use logic in templates crafted for each day of the week, as detailed in [this post](https://mostlymaths.net/2022/02/random-quote-and-templates.html/).
Creating projects is very cheap on my setup: create a new note and insert the “project” template, which looks like this:

```
---
status:
type: project
prio:
org:
reviewed:
---

---

- [ ]

---

- !
```

Here's an annotated version for clarity:

```
---
status: should be open or closed
type: project
prio: an integer
org: anything (pybcn, work, empty)
reviewed: a date in my preferred format, YYYYMMDD
---

Space for support material. Usually I make this a list
of links to Notion pages, URLs, other notes.

---

- [ ] This would be a task. More later

---

- !
- [[20220814]]@18:48 Space to enter a log of events related to the project
```

I keep the format fast and loose, except for the task section which I keep always as in here. Sometimes reference material is part of the log, and sometimes the support material is so long it spins out a separate page.

###### Project review

One of the fundamental practices of GTD is regularly reviewing your projects. [OmniFocus](https://www.omnigroup.com/omnifocus/) has facilities for reviewing projects on schedules, but Things had nothing: either I reviewed everything or nothing. I created [some crazy automation](https://mostlymaths.net/2018/12/things3-weekly-review-mode-shortcuts.html/) to get something close to reviews.
But, using Dataview I can build my own review schedule. I have several project views, main ones being *Personal* (anything except work) and *Work* (only work, duh). The Dataview query for reviewing projects in *Personal* looks like this:

|  | TABLE |
| --- | --- |
|  | status, |
|  | length(filter( file. tasks, (t) => ! t. completed)) AS 🔳, |
|  | "" AS 🎫, |
|  | prio AS 🏷, |
|  | org, |
|  | " " as 📅 |
|  | FROM "/" |
|  | WHERE type = " project" |
|  | AND file. folder != " templates" |
|  | AND status != " closed" |
|  | AND org != " work" |
|  | SORT |
|  | (string(reviewed)> string(dateformat( date(today) - dur(default(period, " 7d")), " yyyyMMdd"))) ASC, |
|  | (default(prio, 1) \* length(filter( file. tasks, (t) => ! t. completed))) DESC |

[view raw](https://gist.github.com/rberenguel/b128fc0621e41ee58f4a704b747cd19d/raw/792311aae7454fbe0ff0325c0a4a0710ef54bdb8/dataview_review_projects.sql) [dataview\_review\_projects.sql](https://gist.github.com/rberenguel/b128fc0621e41ee58f4a704b747cd19d#file-dataview_review_projects-sql) hosted with ❤ by [GitHub](https://github.com/)
I know, WTF? But this is how it looks for 2 projects. These two are reviewed.
Clicking on the file name takes me there. I can then go back to the review list with the go-back command, cmd+[ .
The header of the project view needs some explaining:
\* File : quite obvious. This is the same as the project name.
\* status : This is the view for open, only. I have a separate view for closed, and one for *fuck, why did I put something else there?*
\* ◼: How many incomplete tasks there are in this file.
\* 🎫: If there are tasks with due or start dates in the file (that's the t.annotated lambda in the query). More on this in the Tasks section.
\* 🏷: Shorthand for priority to save on column width.
\* org : Most of my personal ones have this empty, but PyBCN would be here too.
\* 📅: If this project has been reviewed or is due for review. More details below. This is used in sorting: false will be first.
To show these green check/red cross (for 📅 and 🎫) in that HTML block in the query, I have a custom CSS snippet:

```
.true {
  width: 24px;
  height: 20px;
  font-size: 15px;
  text-align: center;
  padding: 0px 0px 21px 0px;
}
.true:before {
  content: "✅";
}
.false {
  width: 24px;
  height: 20px;
  font-size: 15px;
  text-align: center;
  padding: 0px 0px 21px 0px;
}
.false:before {
  content: "❌";
}
```

The most important part of this query in a way is the *reviewed* block. How does it work?
\* Projects have a reviewed field with a date in the header;
\* Optionally, they have a period field with a duration (default is otherwise 7d );
\* The query checks whether reviewed > today - period .
By customising period in each project file header, I can have projects I only review once every 2 weeks, or once every month. In general, projects I am actively working on I want the default, but some things I want to just be reminded every 2 or 4 weeks. Visiting each unreviewed project, I have mapped alt+. to expand to the template reviewed mentioned in the beginning, so review has a very low overhead aside from having to check each project needing review. Which should be few!
What is done during a project review?
This is what I do:
\* Think if I still want to do the project, overall.
\* Has anything changed about this project in the past period? If so, log it/document it in the project note.
\* Are there any tasks to do that are missing? Add them. Anything done and not tracked? Add it.
\* Mark as reviewed with date today.

###### New/modified note review

I hijack the reviewed field to use it to review any notes I have created recently. This would include projects, of course. The Dataview query is the following:

```
TABLE
FROM "/"
  WHERE file.mtime > (date(now) - dur(14 days))
  AND !regexmatch("\d+", file.name)
  AND file.name != this.file.name
  AND file.folder != "templates"
  AND file.name != "Inbox"
  AND file.name != "Pending reading"
  AND file.name != "Pending watching"
  AND !reviewed
SORT file.ctime asc
```

It excludes certain files that I don't want to see appearing here or don't need the header. I have recently switched from file.ctime (creation time) to file.mtime (modified time), to include notes I have touched, not only notes I have created recently. I'm not sure what I prefer yet. If I keep mtime I may need to add more exclusion rules.

##### Tasks

Shortcuts to simplify task processing
\* alt+t : enter template by name
\* start : expands to [▶:: ], ;
\* due : expands to [⏏:: ], ;
\* prio : expands to [🏷:: ], ;
\* checked : expands to [🧷::YYYY-MM-DD], with alt+/ as a shortcut.
\* cmd+d : insert current date and time as [[YYYYMMDD]]@HH:mm
\* @today : The [Natural Language Dates](https://github.com/argenos/nldates-obsidian) plugin lets me type *at sign next Tuesday* to get the format I need for the due and start dates.
Tasks are where the rubber meets the road, the shit hits the fan, etc. Tasks that I plan to do are tagged (and untagged and tagged tasks appear in the project review query shown before), and a fully tagged task would look like this:

```
- [ ] Conquer the world [⏏️:: YYYY-MM-DD], [▶️:: YYYY-MM-DD], [🏷:: 42],  [🧷::YYYY-MM-DD],
```

Each of these tags means:
\* ⏏: due date. I want this task done on this day.
\* ▶: start date. I plan on starting this task on this day. I don't use this tag much, and may remove it. It is still on all my queries though. One of due or start is needed for a task to show on a specific day.
\* 🏷: priority for the task, an integer.
\* 🧷: reviewed. It means I'm still happy with this task as being due on this date, or having this priority. More on this below.
In general, I only fill due date when I create a task, if I know I'll be doing it on that day or around that week. Otherwise, I'll choose the date when I review the project the task is in.

###### Task review

Reviewing tasks is more akin to *reviewing the week ahead* . This is something I do on Sundays, as part of my Sunday recurring template, sometimes on Monday morning. For one, I want to know what random crap out of my projects I have coming up, but I also want to be sure I've had a look and I don't have 25 things to do on Monday and 3 the rest of the week. For that, I have a special note called Upcoming 7 days . It has two queries:
\* One for tasks that are due in the next 7 days and where the reviewed date is in the past, or tasks that are overdue and were reviewed in the past. This lets me be sure I'm *still* convinced I want to do this and lets me adjust dates accordingly.
\* One for tasks that have been reviewed, are due in the next 7 days, grouped by day and project. This gives me an overview of the 7 days ahead.
The first query, wrapped in an [Admonition](https://github.com/valentine195/obsidian-admonition) block to make it look better:

```
```ad-warning
title: To review
```dataview
TASK
FROM "/"
  WHERE (
    (▶️ < (date(today) + dur(7 days)) AND ▶️)
    OR
    (⏏️ < (date(today) + dur(7 days)) AND date(⏏️))
    AND !completed
    AND (🧷 <= (date(today) - dur(7 days)) OR !🧷)
  )
GROUP BY "" + default(▶️, "") + dateformat(default(⏏️, date("2001-01-01")), "dd LLL ccc")+ " " + "" + file.name + ""
```

Admonition and embedded Dataview blocks
3or some reason Admonition blocks with embedded Dataview blocks need to be closed only *once* . If you try to copy paste on your Obsidian, play with the closing triple-tick until it looks correct. It can be made to work.
This is how this block looks:
Clicking on the task takes me to the file with the task, so I can mark it as reviewed, for example. Then I can go back with cmd+[
The second block, is defined by

```
```ad-info
title: upcoming
```dataview
TASK
FROM "/"
  WHERE 🧷 AND (🧷 >= (date(today) - dur(7 days))) AND
  (
    ((▶️ < (date(today) + dur(7 days)) AND ▶️)
	OR
	(⏏️ < (date(today) + dur(7 days)) AND date(⏏️)))
    AND !completed
  )
GROUP BY "" + default(▶️, "") + dateformat(default(⏏️, ""), "dd LLL ccc")+ " " + "" + file.name + ""
```

And it looks like this:

##### The daily view

This is the main driver of my work and process. I have a *very* complex daily template that fills up certain things, including a Dataview query of tasks due today (where today depends on the filename, to play well with the Journal and Calendar plugins). I have 4 Dataview blocks:
\* urgent : priority at least 42;
\* top 3 : except for 42s, top 3 ordered by priority;
\* all due : all tasks with priority less than 42;
\* done today : tasks marked as done today.
You can find more details about the templating method and plugins I use in this post: [Templates for quotes and recurrent tasks in Obsidian](https://mostlymaths.net/2022/02/random-quote-and-templates.html/). For more information, [here's a gist with these blocks before automated interpolation](https://gist.github.com/rberenguel/a831d83074cd7aa1ae82defe6feb072d). This needs the Templater plugin with Javascript (auto)expansion enabled.
The (interpolated for exactly today Sunday, so has all projects except work ) Dataview blocks, wrapped in Admonitions, look as follows:

```
```ad-danger
title: urgent
icon: fire
```dataview
TASK from "/" WHERE
    type = "project" AND
    ((▶️ < date(2022-08-14)
AND ▶️ AND !completed)
    OR (▶️ = date(2022-08-14) AND ▶️ AND !completed)
    OR (⏏️ = date(2022-08-14) AND ⏏️ AND !completed)
    OR (⏏️ < date(2022-08-14) AND ⏏️ AND !completed))
    AND 🏷 >= 42
	SORT completed asc, 🏷 DESC
	GROUP by file.name
```ad-warning
title: top 3
icon: arrow-up
```dataview
TASK from "/" WHERE
    🏷 < 42 AND
    type = "project" AND org != "work" AND
    ((▶️ < date(2022-08-14)
AND ▶️ AND !completed)
    OR (▶️ = date(2022-08-14) AND ▶️ AND !completed)
    OR (⏏️ = date(2022-08-14) AND ⏏️ AND !completed)
    OR (⏏️ < date(2022-08-14) AND ⏏️ AND !completed))
	SORT completed asc, 🏷 DESC LIMIT 3
```ad-info
title: tasks
icon: list
```dataview
TASK from "/" WHERE
    type = "project"
    AND (org != "work") AND
    🏷 < 42 AND
    ((▶️ < date(2022-08-14)
AND ▶️ AND !completed)
    OR (▶️ = date(2022-08-14) AND ▶️ AND !completed)
    OR (⏏️ = date(2022-08-14) AND ⏏️ AND !completed)
    OR (⏏️ < date(2022-08-14) AND ⏏️ AND !completed))
    SORT completed asc, 🏷 DESC, prio desc, org desc
    GROUP by file.name
```ad-success
title: done
icon: checkmark
```dataview
TASK from "/" WHERE
    type = "project" AND
    ✔️ = date(2022-08-14)
```

They would look like this, when empty of tasks (with tasks, they'd look similar to those above):
The queries are crazy, I know. They involved a lot of trial and error to play well with Dataview, and in my template are mixed with Javascript to interpolate the current date, too. Also, having start and due f-ks up a lot the queries, when I remove start I can simplify them a great deal.
Default checks
I have setup Dataview to add a check ✔ when I complete a task from a Dataview query. This is what gets parsed for the *done* query block.
Off-hours
I'm exploring having “off hours” where after certain time I only see non-work tasks. The Dataview condition to add looks like this: ((dateformat(date(now), "HH") < "17" AND org = "work") OR (org != "work"))

##### How this process has evolved

I started by just having tasks on days.
First, recurrent tasks that I had to do repeatedly (see [this post](https://mostlymaths.net/2022/02/random-quote-and-templates.html/)), then, project tasks that I would manually copy from one day to the next.
Eventually, I realised I needed projects… And started copying tasks from projects to the day I wanted to do them.
Then, using Dataviews for tasks from projects. I kept adding to the query to make it better, until I had the 4 blocks above.
I stumbled upon somebody checking recently created files, and I wanted that too.
From there, I realised I could review projects more effectively by listing projects that needed review instead of checking each project, which was slow and very repetitive.
The most recent addition is removing work-related tasks after work hours.
Some ideas I'm exploring, are to automated “holiday checks” so my templates don't expand for *work* on days I'm not working because I'm off.
\* [Productivity](https://mostlymaths.net/tags/productivity)
\* [GTD](https://mostlymaths.net/tags/gtd)
\* [Obsidian](https://mostlymaths.net/tags/obsidian)
Related
\* [Templates for quotes and recurrent tasks in Obsidian](https://mostlymaths.net/2022/02/random-quote-and-templates.html/)
\* [Things3 Weekly Review mode shortcut(s)](https://mostlymaths.net/2018/12/things3-weekly-review-mode-shortcuts.html/)
\* [2022#26 Readings 🇺🇦🌻](https://mostlymaths.net/2022/12/202226-readings.html/)
\* [2022#21 Readings 🇺🇦🌻](https://mostlymaths.net/2022/09/202221-readings.html/)
\* [2022#19 Readings 🇺🇦🌻](https://mostlymaths.net/2022/08/202219-readings.html/)
[© 2026 mostlymaths.net](https://mostlymaths.net/)