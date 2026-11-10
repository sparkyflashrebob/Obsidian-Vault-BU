---
tags:
  - notebooklm-import
notebook: "C_Obsidian info"
category: "research"
---

Structure of a Query - Dataview [-] [-]
[Skip to content](https://blacksmithgu.github.io/obsidian-dataview/queries/structure/#structure-of-a-query)
Dataview
Structure of a Query
Type to start searching
[GitHub
\* 0.5.70
\* 8.9k
\* 514](https://github.com/blacksmithgu/obsidian-dataview)
Dataview
[GitHub
\* 0.5.70
\* 8.9k
\* 514](https://github.com/blacksmithgu/obsidian-dataview)
\* [Overview](https://blacksmithgu.github.io/obsidian-dataview/) [-] Metadata Metadata
\* [Adding Metadata](https://blacksmithgu.github.io/obsidian-dataview/annotation/add-metadata/)
\* [Data Types](https://blacksmithgu.github.io/obsidian-dataview/annotation/types-of-metadata/)
\* [Metadata on Pages](https://blacksmithgu.github.io/obsidian-dataview/annotation/metadata-pages/)
\* [Metadata on Tasks and Lists](https://blacksmithgu.github.io/obsidian-dataview/annotation/metadata-tasks/)
\* [DQL, JS and Inlines](https://blacksmithgu.github.io/obsidian-dataview/queries/dql-js-inline/) [x] Query Language Reference Query Language Reference
[-] Structure of a Query [Structure of a Query](https://blacksmithgu.github.io/obsidian-dataview/queries/structure/) Table of contents
\* [General Format of a DQL Query](https://blacksmithgu.github.io/obsidian-dataview/queries/structure/#general-format-of-a-dql-query)
\* [Choose a Output Format](https://blacksmithgu.github.io/obsidian-dataview/queries/structure/#choose-a-output-format)
\* [Choose your source](https://blacksmithgu.github.io/obsidian-dataview/queries/structure/#choose-your-source)
\* [Filter, sort, group or limit results](https://blacksmithgu.github.io/obsidian-dataview/queries/structure/#filter-sort-group-or-limit-results)
\* [Examples](https://blacksmithgu.github.io/obsidian-dataview/queries/structure/#examples)
\* [Query Types](https://blacksmithgu.github.io/obsidian-dataview/queries/query-types/)
\* [Data Commands](https://blacksmithgu.github.io/obsidian-dataview/queries/data-commands/)
\* [Differences to SQL](https://blacksmithgu.github.io/obsidian-dataview/queries/differences-to-sql/)
\* [Sources](https://blacksmithgu.github.io/obsidian-dataview/reference/sources/)
\* [Expressions](https://blacksmithgu.github.io/obsidian-dataview/reference/expressions/)
\* [Literals](https://blacksmithgu.github.io/obsidian-dataview/reference/literals/)
\* [Functions](https://blacksmithgu.github.io/obsidian-dataview/reference/functions/) [-] JavaScript Reference JavaScript Reference
\* [Overview](https://blacksmithgu.github.io/obsidian-dataview/api/intro/)
\* [Data Arrays](https://blacksmithgu.github.io/obsidian-dataview/api/data-array/)
\* [Codeblock Reference](https://blacksmithgu.github.io/obsidian-dataview/api/code-reference/)
\* [Codeblock Examples](https://blacksmithgu.github.io/obsidian-dataview/api/code-examples/) [-] FAQ and Resources FAQ and Resources
\* [Frequently Asked Questions](https://blacksmithgu.github.io/obsidian-dataview/resources/faq/)
\* [Examples](https://blacksmithgu.github.io/obsidian-dataview/resources/examples/)
\* [Developing Against Dataview](https://blacksmithgu.github.io/obsidian-dataview/resources/develop-against-dataview/)
\* [Resources and Support](https://blacksmithgu.github.io/obsidian-dataview/resources/resources-and-support/)
\* [Friends of Dataview](https://blacksmithgu.github.io/obsidian-dataview/friends/)
\* [Changelog](https://blacksmithgu.github.io/obsidian-dataview/changelog/)
Table of contents
\* [General Format of a DQL Query](https://blacksmithgu.github.io/obsidian-dataview/queries/structure/#general-format-of-a-dql-query)
\* [Choose a Output Format](https://blacksmithgu.github.io/obsidian-dataview/queries/structure/#choose-a-output-format)
\* [Choose your source](https://blacksmithgu.github.io/obsidian-dataview/queries/structure/#choose-your-source)
\* [Filter, sort, group or limit results](https://blacksmithgu.github.io/obsidian-dataview/queries/structure/#filter-sort-group-or-limit-results)
\* [Examples](https://blacksmithgu.github.io/obsidian-dataview/queries/structure/#examples)

### Structure of a Query

Dataview offers [multiple ways](https://blacksmithgu.github.io/obsidian-dataview/queries/dql-js-inline/) to write queries and the syntax differs for each.
This page provides information on how to write a **Dataview Query Language** ( **DQL** ) query. If you're interested in how to write Inline Queries, refer to the [inline section on DQL, JS and Inlines](https://blacksmithgu.github.io/obsidian-dataview/queries/dql-js-inline/#inline-dql). You'll find more information about **Javascript Queries** on the [Javascript Reference](https://blacksmithgu.github.io/obsidian-dataview/api/intro/).
**DQL** is a SQL like query language for creating different views or calculations on your data. It supports:
\* Choosing an **output format** of your output (the [Query Type](https://blacksmithgu.github.io/obsidian-dataview/queries/query-types/))
\* Fetch pages **from a certain source** , i.e. a tag, folder or link
\* **Filtering pages/data** by simple operations on fields, like comparison, existence checks, and so on
\* **Transforming fields** for displaying, i.e. with calculations or splitting up multi-value fields
\* **Sorting** results based on fields
\* **Grouping** results based on fields
\* **Limiting** your result count
Warning
If you are familiar with SQL, please read [Differences to SQL](https://blacksmithgu.github.io/obsidian-dataview/queries/differences-to-sql/) to avoid confusing DQL with SQL.
Let's have a look at how we can put DQL to use.

#### General Format of a DQL Query

Every query follows the same structure and consists of
\* exactly one **Query Type** with zero, one or many [fields](https://blacksmithgu.github.io/obsidian-dataview/annotation/add-metadata/), depending on query type
\* zero or one **FROM** data commands with one to many [sources](https://blacksmithgu.github.io/obsidian-dataview/reference/sources/)
\* zero to many other **data commands** with one to many [expressions](https://blacksmithgu.github.io/obsidian-dataview/reference/expressions/) and/or other infos depending on the data command
At a high level, a query conforms to the following pattern:

```
```dataview
 
FROM 
 
 
          ...
```

```
Only the Query Type is mandatory.

The following sections will explain the theory in further detail.

## Choose a Output Format

The output format of a query is determined by its **Query Type**. There are four available:

1. **TABLE**: A table of results with one row per result and one or many columns of field data.
2. **LIST**: A bullet point list of pages which match the query. You can output one field for each page alongside their file links.
3. **TASK**: An interactive task list of tasks that match the given query.
4. **CALENDAR**: A calendar view displaying each hit via a dot on its referred date.

The Query Type is the **only mandatory command in a query**. Everything else is optional.

Possibly memory intense examples

Depending on the size of your vault, executing the following examples can take long and even freeze Obsidian in extreme cases. It's recommended that you specify a `FROM` to restrict the query execution to a specific subset of your vaults' files. See next section.
```

Lists all pages in your vault as a bullet point list

```
LIST
```

Lists all tasks (completed or not) in your vault

```
TASK
```

Renders a Calendar view where each page is represented as a dot on its creation date.

```
CALENDAR file.cday
```

Shows a table with all pages of your vault, their field value of due, the files' tags and an average of the values of multi-value field working-hours

```
TABLE due, file.tags AS "tags", average(working-hours)
```

```
Read more about the available Query Types and how to use them [here](https://blacksmithgu.github.io/obsidian-dataview/queries/query-types/).

## Choose your source

Additionally to the Query Types, you have several **Data Commands** available that help you restrict, refine, sort or group your query. One of these query commands is the **FROM** statement. `FROM` takes a [source](https://blacksmithgu.github.io/obsidian-dataview/reference/sources/) or a combination of [sources](https://blacksmithgu.github.io/obsidian-dataview/reference/sources/) as an argument and restricts the query to a set of pages that match your source.

It behaves differently from the other Data Commands: You can add **zero or one** `FROM` data command to your query, right after your Query Type. You cannot add multiple FROM statements and you cannot add it after other Data Commands.
```

Lists all pages inside the folder Books and its sub folders

```
LIST
FROM "Books"
```

Lists all pages that include the tag #status/open or #status/wip

```
LIST
FROM #status/open OR #status/wip
```

Lists all pages that have either the tag #assignment and are inside folder "30 School" (or its sub folders), or are inside folder "30 School/32 Homeworks" and are linked on the page School Dashboard Current To Dos

```
LIST
FROM (#assignment AND "30 School") OR ("30 School/32 Homeworks" AND outgoing([[School Dashboard Current To Dos]]))
```

```
Read more about `FROM` [here](https://blacksmithgu.github.io/obsidian-dataview/queries/data-commands/#from).

## Filter, sort, group or limit results

In addition to the Query Types and the **Data command** `FROM` that's explained above, you have several other **Data Commands** available that help you restrict, refine, sort or group your query results.

All data commands except the `FROM` command can be used **multiple times in any order** (as long as they come after the Query Type and `FROM` , if `FROM` is used at all). They'll be executed in the order they are written.

Available are:

1. **FROM** like explained [above](https://blacksmithgu.github.io/obsidian-dataview/queries/structure/#choose-your-source).
2. **WHERE**: Filter notes based on information **inside** notes, the meta data fields.
3. **SORT**: Sorts your results depending on a field and a direction.
4. **GROUP BY**: Bundles up several results into one result row per group.
5. **LIMIT**: Limits the result count of your query to the given number.
6. **FLATTEN**: Splits up one result into multiple results based on a field or calculation.
```

Lists all pages that have a metadata field due and where due is before today

```
LIST
WHERE due AND due < date(today)
```

Lists the 10 most recently created pages in your vault that have the tag #status/open

```
LIST
FROM #status/open
SORT file.ctime DESC
LIMIT 10
```

Lists the 10 oldest and incomplete tasks of your vault as an interactive task list, grouped by their containing file and sorted from oldest to newest file.

```
TASK
WHERE !completed
SORT created ASC
LIMIT 10
GROUP BY file.link
SORT rows.file.ctime ASC
```

```
Find out more about available [data commands](https://blacksmithgu.github.io/obsidian-dataview/queries/data-commands/).

## Examples

Following are some example queries. Find more examples [here](https://blacksmithgu.github.io/obsidian-dataview/resources/examples/).
```

```
TASK
```

```

```

```
TABLE recipe-type AS "type", portions, length
FROM #recipes
```

```

```

```
LIST
FROM #assignments
WHERE status = "open"
```

```

```

```
TABLE file.ctime, appointment.type, appointment.time, follow-ups
FROM "30 Protocols/32 Management"
WHERE follow-ups
SORT appointment.time
```

```

```

```
TABLE L.text AS "My lists"
FROM "dailys"
FLATTEN file.lists AS L
WHERE contains(L.author, "Surname")
```

```

```

```
LIST rows.c
WHERE typeof(contacts) = "array" AND contains(contacts, [[Mr. L]])
SORT length(contacts)
FLATTEN contacts as c
SORT link(c).age ASC
```

```
Made with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
```