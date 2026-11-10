---
tags:
  - notebooklm-import
notebook: "C_Obsidian info"
category: "research"
---

An Introduction to Dataview - Obsidian Hub - Obsidian Publish
[Obsidian Hub](https://publish.obsidian.md/hub/00+-+Start+here)
[Obsidian Hub](https://publish.obsidian.md/hub/00+-+Start+here)

### An Introduction to Dataview

```
author: SkepticMystic
aliases: 
- 
tags:
- seedling
publish: true
```

### An Introduction to [Dataview](https://publish.obsidian.md/hub/02+-+Community+Expansions/02.05+All+Community+Expansions/Plugins/dataview)

This is a reformatted, web-compatible version of the very first [Obsidian Community Talk](https://publish.obsidian.md/hub/01+-+Community/Events/Obsidian+Community+Talks), an overview of the [Dataview](https://publish.obsidian.md/hub/02+-+Community+Expansions/02.05+All+Community+Expansions/Plugins/dataview) plugin, held by [SkepticMystic](https://publish.obsidian.md/hub/01+-+Community/People/SkepticMystic).
The original slides can be found [here](https://publish.obsidian.md/hub/04+-+Guides%2C+Workflows%2C+%26+Courses/Guides/An+Introduction+to+Dataview+Slides) and are best viewed with Obsidian and the [Advanced Slides](https://publish.obsidian.md/hub/02+-+Community+Expansions/02.05+All+Community+Expansions/Plugins/obsidian-advanced-slides) plugin or converted to [revealjs](https://publish.obsidian.md/hub/02+-+Community+Expansions/02.05+All+Community+Expansions/Auxiliary+Tools/revealjs) with [Pandoc](https://publish.obsidian.md/hub/04+-+Guides%2C+Workflows%2C+%26+Courses/Community+Talks/YT+-+Pandoc+and+Obsidian+-+Create+slideshows%2C+PDFs+and+Word+documents). Make sure to also take a look at the [YouTube video](https://publish.obsidian.md/hub/04+-+Guides%2C+Workflows%2C+%26+Courses/Community+Talks/YT+-+An+Introduction+to+Dataview) for in-depth explanations.
By [SkepticMystic](https://publish.obsidian.md/hub/01+-+Community/People/SkepticMystic)

#### Overview

```
1. [Broad Intro to Dataview](https://publish.obsidian.md/hub/04+-+Guides%2C+Workflows%2C+%26+Courses/Guides/An+Introduction+to+Dataview#Introduction)
1. [Metadata](https://publish.obsidian.md/hub/04+-+Guides%2C+Workflows%2C+%26+Courses/Guides/An+Introduction+to+Dataview#Metadata)
1. [Dataview Queries](https://publish.obsidian.md/hub/04+-+Guides%2C+Workflows%2C+%26+Courses/Guides/An+Introduction+to+Dataview#Dataview Queries)
*  [List](https://publish.obsidian.md/hub/04+-+Guides%2C+Workflows%2C+%26+Courses/Guides/An+Introduction+to+Dataview#List)
    *  [From](https://publish.obsidian.md/hub/04+-+Guides%2C+Workflows%2C+%26+Courses/Guides/An+Introduction+to+Dataview#From)
    *  [Where](https://publish.obsidian.md/hub/04+-+Guides%2C+Workflows%2C+%26+Courses/Guides/An+Introduction+to+Dataview#Where)
    *  [Task](https://publish.obsidian.md/hub/04+-+Guides%2C+Workflows%2C+%26+Courses/Guides/An+Introduction+to+Dataview#Task)
    *  [Table](https://publish.obsidian.md/hub/04+-+Guides%2C+Workflows%2C+%26+Courses/Guides/An+Introduction+to+Dataview#Table)
    *  [Sort](https://publish.obsidian.md/hub/04+-+Guides%2C+Workflows%2C+%26+Courses/Guides/An+Introduction+to+Dataview#Sort)
    *  [Flatten](https://publish.obsidian.md/hub/04+-+Guides%2C+Workflows%2C+%26+Courses/Guides/An+Introduction+to+Dataview#Flatten)
    *  [Group by](https://publish.obsidian.md/hub/04+-+Guides%2C+Workflows%2C+%26+Courses/Guides/An+Introduction+to+Dataview#Group by)
```

#### Introduction

[Dataview](https://publish.obsidian.md/hub/02+-+Community+Expansions/02.05+All+Community+Expansions/Plugins/dataview) is a plugin which lets you query data from your vault. The *official documentation* which you can use for reference is available here:
<https://blacksmithgu.github.io/obsidian-dataview>

#### Metadata

##### What is it?

Metadata provides information *about* your data.
It is *extra* info that is either already *inherent* in your data, or info that you **manually add** .

##### Examples of Metadata 💡

###### Photographs

```
*  Date & time ⏰
*  Location 🌍
*  People 🧑🤝🧑
```

My display picture has the following *inherent* metadata:
But it could also be given other properties:

###### Markdown Notes

We can also add metadata to **Markdown notes** using a language called *YAML* .
\* YAML is a **structured** way of adding *arbitrary* metadata to a file.

##### Adding YAML Metadata

```
1. At the  **top**  of your note, add 3 dashes ---
1. Underneath that, you can start adding key-value pairs in the form key: value
1. To finish the metadata block, close it off with 3 dashes again --- .
```

In the photo example, this would look as follows:

```
---
dimensions: 1200x1200
bit depth: 24
title: "Mandala Display Picture"
rating: 5
---
```

###### YAML Lists

You can add more than one value to each key using *lists* .
There are two notations you can use:

###### 1. Inline

```
foods: [apples, pears, oranges]
```

###### 2. Indented

```
foods:
  - apples
  - pears
  - oranges
```

**Note the spacing!**

##### Types of Metadata

You can find this information on the [Dataview reference page](https://blacksmithgu.github.io/obsidian-dataview/#/README).

```
number: 3.6
string: "Foo all the bars"
list:
  - 1
  - -2
  - 3.5
  - 1.61803

date:
  - 2021-04
  - "2021-04-09"
  - 2021-04-09T12:12:54

link: [[2021-04-09 Daily Note]]
```

##### Implicit Metadata in all notes

| Property | Value | Type |
| --- | --- | --- |
| file.name | File **title** | string |
| file.path | Full file **path** | string |
| file.link | **Link** to the file | link |
| file.size | **Size** (in bytes) of the file | number |
| file.ctime | Date that the file was **created** | date |
| file.mtime | Date that the file was last **modified** | date |
| file.day | The **date** contained in the note title | date |
| file.tags | An array of all **tags** in the note. | array |

Subtags are broken down by each level, so #Tag/1/A will be stored in the array as [#Tag, #Tag/1, #Tag/1/A]

#### Dataview Queries

##### List

Creates a *list* of the specified notes

```
list
```

##### From

Determines **where** to get notes *from* .

###### From #Tag

You can get all notes *from* a specified **tag** :

```
list
from #MOC
```

###### From "Folder"

All notes from a **folder** :

```
list
from "1. Projects"
```

###### From [[Links]]

And even all notes with links coming *into* a note:

```
list
from [[Yoga MOC]]
```

Or going *out of* a note:

```
list
from outgoing([[yoga MOC]])
```

```
*  This syntax may change in an upcoming release.
```

###### Combining Sources

You can use the 3 basic logical operators to create more complex from queries:
\* list from #A and #B
\* list from "University" or "Work"
\* list from -#Personal
\* list from [[CSS]] and -#HTML

###### String Concatenation

In the results of a list , you can include metadata fields joined with strings

```
list "File Path: " + file.path + " :)"
from #SN
```

###### Lists of lists

A list can also display indented sublists of metadata:

```
list authors
from #SN/Blog
```

##### Task

Task searches for all checkboxes - [ ] in your vault.
It returns a list of all tasks, grouped by their parent note

```
task from #MOC
```

##### Where

After choosing *which* notes to use, you can narrow down the list further using a where block.
This lets you use the various *comparison operators* on the metadata fields in your notes. > , >= , < , <= , = , != where {condition}

###### Examples

```
*  where file.size > 1000
*  where file.name != "2021-04-09 Daily Note"
*  where file.mtime >= date(today) - dur(1 day)
*  where !complete
```

##### Table

Table can show you a *table* of various metadata fields linked to each note. Table {field 1}, {field 2}, ...

###### Examples

```
table intensity
from #Uni/2021/Asg
```

```
table title, type
from #SN
```

```
table file.tags
from Kw/Yoga
```

##### Sort

You can use sort to define which order to list the results in, and which field to sort by: sort field asc/desc
Give multiple fields to decide ties sort field1 asc/desc, field2 asc/desc, ...

##### Flatten

Use flatten to "unroll" lists into their own rows.

```
table authors from #SN
```

versus

```
table authors from #SN
flatten authors
```

##### Group by

Group by lets do gather together results based on the value of a field.
You may group:
\* tasks by completed
\* games by rating
\* assignments by intensity
First, gather all the assignments: from #Uni/2021/Asg
Then, group by intensity : group by intensity

###### rows Object

By grouping the notes, we've created a **new object** .
This is a **nested list** of all the assignments grouped by intensity.
Something like:

```
[
	[A1, A2, A6], // Green
	[A3, A4], // Yellow
	[A5, A7], // Red
];
```

To access this new list, we use the rows object.
\* Get the file name of every note in the array: rows.file.name
\* Get the due date of every note: rows.dueDate

```
table intensity, rows.title
from #Uni/2021/Asg
group by intensity
```

###### Group by tags

```
table rows.file.tags, rows.file.link
from #Fi/Yoga
group by file.tags
```

###### Limitations

It will only consider two notes to be in the same group if they have **exactly the same tags** .
\* So even if two notes have #Note/Author , if the one has a tag that the other doesn't, they won't be grouped together.

#### Functions

##### Contains()

Used to see if:
\* a string *contains* a substring
\* a list *contains* a value where contains(file.name, "Daily Note") where contains(authors, "Robert Lamb")

##### Length()

Returns the *length* of a string or list where length(file.name) > 10

##### Sum()

Returns the *sum* of the numbers in a list where sum(minutesStudied) < 60

##### Many other Functions

For further info on implemented functions, head over to [the official documentation](https://blacksmithgu.github.io/obsidian-dataview/#/functions).

#### Neat Examples

People have come up with a lot of interesting ways of leveraging Dataview. Many have been shared in the central [Dataview Snippet Showcase](https://forum.obsidian.md/t/dataview-plugin-snippet-showcase/13673) on the Obsidian Forum.

##### Untagged Notes

For example, finding all untagged notes in your vault is as simple as: list where length(file.tags) = 0

##### Birthdays

If you track #People in separate notes and add their Birthday as a dataview property, you could compile a list of everyone whose birthday is today like this:

```
list from #People
where Dates.Birthday = "<% tp.date.now(format = "YYYY-MM-DD") %>"
```

### This note in GitHub

[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/04%20-%20Guides%2C%20Workflows%2C%20%26%20Courses/Guides/An%20Introduction%20to%20Dataview.md) | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/04%20-%20Guides%2C%20Workflows%2C%20%26%20Courses/Guides/An%20Introduction%20to%20Dataview.md) | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip)
Links to this page
[🗂 Guides](https://publish.obsidian.md/hub/04+-+Guides%2C+Workflows%2C+%26+Courses/Guides/%F0%9F%97%82%EF%B8%8F+Guides)
[An Introduction to Dataview Slides](https://publish.obsidian.md/hub/04+-+Guides%2C+Workflows%2C+%26+Courses/Guides/An+Introduction+to+Dataview+Slides)
[YT - An Introduction to Dataview](https://publish.obsidian.md/hub/04+-+Guides%2C+Workflows%2C+%26+Courses/Community+Talks/YT+-+An+Introduction+to+Dataview)
An Introduction to Dataview
Not found
This page does not exist
Interactive graph
On this page
[Powered by Obsidian Publish](https://publish.obsidian.md/)