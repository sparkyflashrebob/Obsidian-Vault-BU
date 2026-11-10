---
tags:
  - notebooklm-import
notebook: "C_Obsidian info"
category: "research"
---

DataviewJS Snippet Showcase - Share & showcase - Obsidian Forum
[Obsidian Forum](https://forum.obsidian.md/)

### [DataviewJS Snippet Showcase](https://forum.obsidian.md/t/dataviewjs-snippet-showcase/17847)

[Share & showcase](https://forum.obsidian.md/c/share-showcase/9)
[dataview](https://forum.obsidian.md/tag/dataview)
[Moonbase59](https://forum.obsidian.md/u/Moonbase59) May 8, 2021, 8:02am 1
*Dataview* plugin versions 0.3.0+ offer enhanced, *javascript-enabled* dataviewjs code blocks. [@blacksmithgu](https://forum.obsidian.md/u/blacksmithgu) is constantly adding features and functions to it.
Since the [Dataview plugin snippet showcase](https://forum.obsidian.md/t/dataview-plugin-snippet-showcase/13673) is getting *huge* , I thought we start a new— *DataviewJS* \*\*\*\*-only— snippet showcase here.

#### With great power comes great responsibility …

*DataviewJS* has a steeper learning curve and is not for the faint of heart—you do have full Javascript access but must adhere to the rules, or you'll debug forever and get real frustrated. But it's *worth* it.
*If you're unsure, start out with the “normal” dataview codeblocks and syntax.*

#### … and endless new possibilities!

Almost everything you ever wanted can now be done.
If not, …
\* [open an issue on GitHub](https://github.com/blacksmithgu/obsidian-dataview/issues) *(please check for similar issues before posting!)* ,
\* always *test with the latest version* , and
\* [read the docs!](https://blacksmithgu.github.io/obsidian-dataview/docs/intro)

#### Sharing is progress!

So please …
\* *share* your findings and code snippets with us,
\* *help others* , and
\* let us know about *your creative new ideas!*
If the forum lets me, I'll edit this first post from time to time, to include new information.
41 Likes
[DataviewJs - Code reuse: common place for scripts](https://forum.obsidian.md/t/dataviewjs-code-reuse-common-place-for-scripts/18611/2)
[Designing notes with types and links with types](https://forum.obsidian.md/t/designing-notes-with-types-and-links-with-types/20109/6)
[Obsidian commands, hotkeys and duplicate hotkey assignments](https://forum.obsidian.md/t/obsidian-commands-hotkeys-and-duplicate-hotkey-assignments/55193)
[Moonbase59](https://forum.obsidian.md/u/Moonbase59) May 8, 2021, 9:42am 2

#### Show family members, friends and places that are *nearby*

I love location data, maps, and visualizing stuff. When I plan to travel or visit a friend or family member, I *love* to see “what's near” in each person or location note. Automatically linking places and people together, so to say.
 [obsidian-dataview-nearby-preview-km 788×606 66.1 KB](https://forum.obsidian.md/uploads/default/original/2X/c/cd1e190d4115a6935a5429fee51683d41cc34739.png)
“Nearby” with German setting, in kilometres (text untranslated; check 'km' and the decimal *comma* )
\* If I visit a friend, I can check if there are other friends or places of interest nearby, and we could maybe visit them together.
\* I can check if other friends are near enough to do something together, maybe meet for a barbeque.
\* When sightseeing, I won't miss nearby friends, business contacts, favourite restaurants or other sights anymore.

#### Goals

```
*  Never miss anything  *nearby*  anymore.
*  Have this dataview available as a template so it can be  *in every person, business contact, and place-of-interest note*  and automatically show me  *what's near this place* .
*   *No more people and location notes without location data*  (easily be copied from Google Maps or the like).
```

#### Requirements

```
*   *All people/location notes*  must have a
```

```
location: [lat, lon]
```

entry in the YAML frontmatter. (This syntax has something to do with YAML & JS data structure and easy parsing. The sequence [lat, lon] has been chosen for practical reasons: People are used to it and it can easily be copied from Google Maps and others.)
\* *Dataview 0.3.0+* installed.
\* moment.js available (it currently is).
\* Distance units of **m** , **km** , **yd** and **mi** must be usable and easy to switch.
\* Distances must be calculated as correct straight-line distances, taking into account that Earth is not a perfect sphere but a rotational ellipsoid.
\* Distances must also be available as (approximate; for speed and offline use) driving distances.
\* Distances shall be shown with the unit appended but internally numeric, for easy calculation/comparison.
\* Numbers shall be formatted *according to the language currently set in Obsidian* ( 4,096.1 vs 4.096,1 ). The OS's system setting shall only be used if all else fails.
\* Date & time strings must be easily formatable however I wish, defaulting to *ISO-8601* ( 2021-05-08T10:34:05+02:00 ).
\* Very long note title links shall optionally be shortened in Dataview table views, using my [dataview-shorten-links.css snippet](https://forum.obsidian.md/t/how-to-achieve-css-code-snippets/8474/152).
\* Tags (from frontmatter only, a current Dataview restriction) shall be shown in one (comma- or blank-)separated string, *not* as a list.
\* The list shall be sorted by distance from “here” (i.e., this note).
\* The distance values shall be clickable and lead to the Google Maps Route Planner, destination already filled in, and start point taken from the current location.
\* Above the table, a text line shall show the currently set “nearby” radius as well as the selected unit of measurement ( within 100 km driving distance , within 50 mi straight-line distance ), so we later know what's actually shown in the table.

#### Current status

```
*  Proof-of-concept, working but params have to be set in the codeblock (instead of being taken from YAML).
*  It is still already usable, and should have no major bugs.
```

[obsidian-dataview-nearby-preview-mi 784×590 64.4 KB](https://forum.obsidian.md/uploads/default/original/2X/8/83f1804319827f15a3dba51edb2e78f06e99b0a7.png)
“Nearby” with English setting, in miles (check 'mi' and the decimal *point* )

##### To-Do

```
*  [x] ~~Wait for new Dataview version that allows reading from “this” note, and other things.~~
*  [x] ~~Make unit and radius readable from “this” note, most probably by using something like:~~
```

```
nearby: 50 km
```

~~or~~

```
nearby: 50 mi
```

~~which would split the string and use the numeric part as radius, the textual part as the desired unit for calculating & showing in the table.~~
\* [x] ~~Read origin (starting point) from “this” note so all can be automatic, even when the location changes.~~
\* [x] ~~Possibly make the searchterm for dv.pages() available in YAML. Don't know yet.~~

#### Current Code

This is surely the part you've been waiting for!
*Note: I might change the code here when updating it, so check more often.* It's easier than to keep a zillion copies down below.
This is the dataviewjs code block only. You'll have to type your own header.

```
// Nearby Family Members, Friends and Places
// 2021-05-15 - Matthias C. Hormann (Moonbase59)

// set parameters (to be supplied via YAML frontmatter, eventually)
// DV 0.3.3 interprets "500000 m" as a Luxon duration,
// so we have to put nearby: '"500000 m"' and remove the ".
let nearby = dv.current().nearby.replace(/['"]+/g, '');
let unit = nearby.split(' ')[1];
let radius = nearby.split(' ')[0];
let origin = dv.current().location;

// search term as used in dv.pages()
// use "#tags" or '"folder/subfolder"' for a folder
let searchterm = dv.current().searchterm;

//======================================================================

function getDistance(origin, destination, unit='m') {
    // return distance in selected unit (m,km,yd,mi)
    var factor = 1.0;
    switch (unit) {
      case 'm':
        factor = 1.0;
        break;
      case 'km':
        factor = 1000.0;
        break;
      case 'yd':
        factor = 0.9144;
        break;
      case 'mi':
        factor = 1609.344;
        break;
      default:
        factor = 1.0;
        console.warn("getDistance: Invalid unit '%s', using 'm'. Valid units are: m,km,yd,mi.",unit);
    }

    var lon1 = toRadian(origin[1]),
        lat1 = toRadian(origin[0]),
        lon2 = toRadian(destination[1]),
        lat2 = toRadian(destination[0]);

    var deltaLat = lat2 - lat1;
    var deltaLon = lon2 - lon1;

    var a = Math.pow(Math.sin(deltaLat/2), 2) + Math.cos(lat1) * Math.cos(lat2) * Math.pow(Math.sin(deltaLon/2), 2);
    var c = 2 * Math.asin(Math.sqrt(a));
    var EARTH_RADIUS = 6371000; // 6,371 km in metres
    return c * EARTH_RADIUS / factor;
}

function toRadian(degree) {
    return degree*Math.PI/180;
}

function getDrivingDistance(origin, destination, unit='m') {
    // PREDICTED, using a factor.
    // Much faster, and no need for Internet access.
    // The U.S. predict 1.417, based on statistical analysis.
    // For Germany, I’ve found 1.3 a good value (comparing w/ Google Maps "best route")
    var factor = 1.3;
    return getDistance(origin, destination, unit) * factor;
}

//======================================================================

// Show what we will display.
dv.paragraph("List shows nearby places (within " + radius + " " + unit + " driving distance).");
dv.paragraph("  
  
");

// get the pages
let pages = dv.pages(searchterm)
  .where(p => p.location &&
    // must be >0 so we don’t catch ourselves!
    getDrivingDistance(origin, p.location, unit) > 0.0 &&
    getDrivingDistance(origin, p.location, unit) <= radius)
  .sort(p => getDistance(origin, p.location, unit));

// create table
dv.table(["Name", "Tags", "Distance*"],
  pages.map(p => [
    // The name
    p.file.link,
    // tags (show '–' if none defined)
    (p.file.etags ? p.file.etags.join(' ') : '–'),
    // straight-line distance
    /*
    getDistance(origin, p.location, unit)
      .toLocaleString(moment.locale(), {maximumFractionDigits: 1}) + " " + unit,
    */
    // predicted driving distance and Google Maps Route Planner Link
    (getDrivingDistance(origin, p.location, unit)
      .toLocaleString(moment.locale(), {maximumFractionDigits: 1}) + " " + unit)
      .link('https://www.google.com/maps/dir/?api=1&dir_action=navigate&destination=' + p.location[0] + ',' + p.location[1]),
  ])
);

// show a small legend
dv.paragraph("* Approximate driving distance; when clicked, opens a new Google Maps Route Planner window.");
```

#### Changelog

```
*   **2021-05-08**  — Original version.
*   **2021-05-15**  — Fixed To-Dos, add YAML features:
    *  nearby:   in YAML frontmatter now allows specifying how near it shall be, and the units to display. Knows  **m** ,  **km** ,  **mi**  and  **yd** .
    *  location: [, ] in YAML specifies the starting point (i.e. “here”) for distance calculations.
    *  searchterm: … in YAML is a normal Dataview from type search term. Examples:
```

```
searchterm: "#family or #friends or #location"
```

or

```
searchterm: '"People"'
```

```
*  Make tags inline and clickable.  *Note:*  Using my [dataview-shorten-links.css snippet](https://forum.obsidian.md/t/how-to-achieve-css-code-snippets/8474/152) will work but display one line per tag. Adapt the CSS to select a.internal-link only, or  *not*  to select a.tag if you want more than one tag per line.
    *  Code above updated .
```

#### Questions, Help

```
1. If anyone knows how I can optimize the overuse of getDistance() and getDrivingDistance() ,  *please let me know!*
1. What's the performace/memory hit creating a new pages variable? I mainly did it to decouple, not creating even longer spaghetti code. Or should I string it all together and  *not*  use an extra variable?
1. If anyone knows about an easy (and  *working!* ) way to get at “this” notes YAML frontmatter  *inside*  the code block, let me know.
1. Is it possible to ![[nearby]]  *embed*  this within other notes and have it read its YAML frontmatter  *from the including parent?*  Because that would be truly dynamic—only keep it in  *one*  place and just include it! Would save the hassle of changing it in hundreds of existing people/location notes, eventually!
```

#### Have fun & Keep 'em coming!

14 Likes
[How to work with geolocations](https://forum.obsidian.md/t/how-to-work-with-geolocations/16818/8)
[Moonbase59](https://forum.obsidian.md/u/Moonbase59) May 8, 2021, 11:31am 3
So *Dataview 0.3.3* is here and we got dv.current() . Im just testing reading data from YAML frontmatter instead of hardcoding it into the codeblock.
**Caveat:** Dataview seems to pre-interpret the YAML, and so my entry

```
nearby: 500000 m
```

is “interpreted” as a Luxon duration of 500,000 *minutes* ! Which means, I can't access the string 500000 m and work on it in my function. (It's meant to mean “500,000 metres”.) Argh.
See also: [0.3.3: Interprets YAML frontmatter string as Luxon Duration! Argh! · Issue #189 · blacksmithgu/obsidian-dataview · GitHub](https://github.com/blacksmithgu/obsidian-dataview/issues/189)
Hope our friend will come up with a good fix.
1 Like
[Rishi](https://forum.obsidian.md/u/Rishi) May 8, 2021, 4:19pm 4
This is a lot of amazing work. Although, I am not going to use something like this myself, I still think it is gold!
P.S. Good thought on updating the code as opposed to adding newer ones below. We should make that a movement and make things on the forum simpler!
1 Like
[davecan](https://forum.obsidian.md/u/davecan) May 8, 2021, 9:59pm 5
Moonbase59:
Is it possible to ![[nearby]] *embed* this within other notes and have it read its YAML frontmatter *from the including parent?* Because that would be truly dynamic—only keep it in *one* place and just include it! Would save the hassle of changing it in hundreds of existing people/location notes, eventually!
I submitted a feature request a few weeks ago to add stored queries and the dev agreed it would be a useful add-on. Hopefully its coming soon because I have the same problem.
My recommendation was along the lines of creating a folder where each query is defined in a separate file and then including them with syntax like this:

```

```

An implementation in the JS API would presumably look something like:

```
dv.include('file_path', [key_val_pairs])
```

Using dv.current() seems to be a move towards supporting this type of feature.
2 Likes
[Moonbase59](https://forum.obsidian.md/u/Moonbase59) May 9, 2021, 7:13pm 6

#### Upcoming Birthdays (robust & flexible)

Here's a rather robust and flexible list of upcoming birthdays that
\* shows **link** , **next birthday** , and **age** someone will turn to
\* has a configurabe **date range** (from today, for a “natural language” duration)
\* sorts by **next birthday**
\* uses **locale settings** from the language *Obsidian is set to*
\* doesn't choke when crossing the year boundary
\* has YAML **searchterm** configuration
\* has YAML “natural language” **duration** configuration; “odd” data like duration: 0.5 years will be auto-translated to 6 months (or 6 Monate in German)
\* has YAML **date format** configuration (yay!)
\* has a configurable **info line** above the table (can be disabled)
 [obsidian-dataview-upcoming-birthdays 789×558 64.9 KB](https://forum.obsidian.md/uploads/default/original/2X/4/4f70d33649d6c45a7ac9c86b3226b0cb3f021dc0.png)
Upcoming birthdays with English settings, custom date format and info line
**The technically-minded** may also find interesting:
\* utility functions that can be used for table data
\* custom function for “where”
\* comparator function for “sort”
\* easily translatable “info line” with parameters
\* how I need to *undo* Dataview's YAML pre-parsing of dates and durations
 [obsidian-dataview-upcoming-birthdays-de 789×553 64 KB](https://forum.obsidian.md/uploads/default/original/2X/5/5d6ccde0ae290500f38c930b2c91142f45f27304.png)
Upcoming birthdays with German settings, custom date format and info line

#### Requirements

```
*   *Dataview 0.3.3+*
*  moment.js (comes with Obsidian)
*  Notes to be included must have a birthday as YYYY-MM-DD in the frontmatter:
```

```
birthday: 1959-07-19
```

```
*  The note  *using*  this script  **must**  have the parameters searchterm and a (more or less) “natural language” duration in the frontmatter:
```

```
#searchterm: "#family or #friends"
searchterm: '"People"'
duration: 1 year
```

```
*  The note using this script  *can*  have an additional dateformat in the frontmatter:
```

```
dateformat: "ddd, D MMMM YYYY"
```

If left out or empty, it will default to YYYY-MM-DD .

#### Code

##### YAML frontmatter example

```
#searchterm: "#family or #friends"
searchterm: '"People"'
duration: 1 year
dateformat: "ddd, D MMMM YYYY"
```

##### dataviewjs code

This contains some utility functions that can be used in your table, like nextBirthday() , turns() .

```
var start = moment().startOf('day');
var end = moment(start).add(dv.current().duration);
var dateformat = "YYYY-MM-DD";
if (dv.current().dateformat) { dateformat = dv.current().dateformat; }

// info text above table, {0}=duration, {1}=start date, {2}=end date
// parameters can be left out, or the string empty
var infotext = "Upcoming birthdays for {0} from now ({1} – {2})  
  
";

//======================================================================

function nextBirthday(birthday) {
    // Get person’s next birthday on or after "start"
    // returns a moment
    
    // need to "unparse" because DV has already converted YAML birthday to DateTime object
    // shouldn’t harm if already a string
    var bday = moment(birthday.toString());
    var bdayNext = moment(bday).year(start.year());
    if (bdayNext.isBefore(start, 'day')) {
        bdayNext.add(1, "year");
    }
    return bdayNext;
}

function turns(birthday) {
    // Get the age in years a person will turn to on their next birthday

    // need to "unparse" because DV has already converted YAML birthday to DateTime object
    // shouldn’t harm if already a string
    var bday = moment(birthday.toString());
    return nextBirthday(birthday).diff(bday, 'years');
}

function showBirthday(birthday) {
    // Determine if this birthday is in the range to be shown
    // including the start date, excluding the end date
    // because that comes from a duration calculation
    // for use with "where", returns true or false
    
    if (birthday) {
        // need to "unparse" because DV has already converted YAML birthday to DateTime object
        // shouldn’t harm if already a string
        var bday = moment(birthday.toString());
        var bdayNext = nextBirthday(birthday);
        if (bdayNext.isBetween(start, end, 'day', '[)')) {
            return true;
        } else {
            return false;
        }
    } else {
        return false;
    }
}

function sortByNextBirthday(a, b) {
    // comparator function for "sort"
    
  if (nextBirthday(a).isBefore(nextBirthday(b))) {
    return -1;
  }
  if (nextBirthday(a).isAfter(nextBirthday(b))) {
    return 1;
  }
  // they’re equal
  return 0;
}

//======================================================================

dv.paragraph(infotext.format(moment.duration(dv.current().duration.toString()).humanize(), start.format(dateformat), end.format(dateformat)));

dv.table(
    ["Name", "Birthday", "Turns"],
    dv.pages(dv.current().searchterm)
        // use a function to see if this birthday is in range to be shown
        .where(p => showBirthday(p.birthday))
        // use a comparator function to sort by next birthday
        .sort(p => p.birthday, 'asc', sortByNextBirthday)
        .map(p => [
            p.file.link,
            p.birthday ? nextBirthday(p.birthday).format(dateformat) : '–',
            turns(p.birthday)
        ])
);
```

#### Notes

```
*  Dataview actually  *parses*  the cell content, so if you for example set the date format to D. MMMM , you'll get large vertical spacing. This is because DV  *thinks*  something like 17. May must be an  *ordered list item*  and parses it accordingly. Which in turn will ruin your vertical spacing. See [0.3.3: table item converts to ordered list, ruining vertical spacing · Issue #199 · blacksmithgu/obsidian-dataview · GitHub](https://github.com/blacksmithgu/obsidian-dataview/issues/199).
*  Using durations > 1 year (like 2 years )  *work* , but don't make much sense. The table will only display a person's  *next*  birthday. So no duplicates.
```

24 Likes
[Dataview question about formatting date](https://forum.obsidian.md/t/dataview-question-about-formatting-date/18071/2)
[Dataview plugin snippet showcase](https://forum.obsidian.md/t/dataview-plugin-snippet-showcase/13673/275)
[Birthday algorithm with dataviewjs](https://forum.obsidian.md/t/birthday-algorithm-with-dataviewjs/42246/10)
[Dataview plugin snippet showcase](https://forum.obsidian.md/t/dataview-plugin-snippet-showcase/13673/728)
[kastyb](https://forum.obsidian.md/u/kastyb) May 9, 2021, 9:09pm 7
Hello! I have a “How-to” question.

```
for (let group of dv.pages("#test1").groupBy(p => p.subject)) {
    dv.header(5, group.key);
    dv.table(["Name", "Author", "Link"],
        group.rows	
          
            .map(k => [k.file.link, k.author, 
			k.URL]
))
}
```

This is the output of the code.
 [Capture 908×385 31.1 KB](https://forum.obsidian.md/uploads/default/original/2X/f/ff3a246886aaf4ed4e700fe959d4f27e1090e6bd.jpeg)
How do we get a hyperlink instead of the long URL. With the “normal” dataview we could wrap the URL with a desired sting using elink() function. How do we emulate that in dataviewjs?
2 Likes
[Creating a table of notes grouped by other notes](https://forum.obsidian.md/t/creating-a-table-of-notes-grouped-by-other-notes/28377)
[Moonbase59](https://forum.obsidian.md/u/Moonbase59) May 9, 2021, 9:22pm 8
Well, instead of k.URL you could use something like

```
"Link".link(k.URL)
```

where "Link" could even come from a variable or calculation, enclosed in parentheses, like

```
(k.author).link(k.URL)
```

effectively making the author clickable and saving a column.
I use this technique in my [Show family members, friends and places that are nearby](https://forum.obsidian.md/t/dataviewjs-snippet-showcase/17847/2) example above.
*Note:* In olden times, .link wasn't supported too well in each and every browser. Fortunately, Electron (and thus Obsidian) handles it well.
5 Likes
[kastyb](https://forum.obsidian.md/u/kastyb) May 10, 2021, 1:08pm 9
Thank you so much! This will save unnecessary horizontal scrolling to view all the rows.
[Rishi](https://forum.obsidian.md/u/Rishi) May 10, 2021, 3:47pm 10
Moonbase59:

```

```

#searchterm: “#family or #friends”
searchterm: '“People”'

```

```

Why does the YAML have both these?
[Moonbase59](https://forum.obsidian.md/u/Moonbase59) May 11, 2021, 5:17am 11
Because I'm currently testing and it's much easier just to comment/uncomment things.
I also wanted to show how a tag search and a folder search would look like.
1 Like
[Rishi](https://forum.obsidian.md/u/Rishi) May 11, 2021, 6:12am 12
Oh I figured it after posting this! I was getting some weird error and was eliminating all possible options that might cause it. Thanks for sharing the code.
Do you happen to know if we can use DataviewJS inline like we could Dataview queries? I've been using Templater to have inline “Next Birthday” in individual People note but Templater dynamic templates break all table formatting right now.
[Moonbase59](https://forum.obsidian.md/u/Moonbase59) May 16, 2021, 2:02am 13

#### List(s) of Obsidian Commands

**EDIT:** *A newer and better version is down in post #37!*
I needed a list of currently enabled Obsidian Commands (those in the Command Palette, internal plus plugins). So I thought »Why not do it using Obsidian itself (and Dataview)?«

##### Commands sorted by internal Command ID

```
const getNestedObject = (nestedObj, pathArr) => {
    return pathArr.reduce((obj, key) =>
        (obj && obj[key] !== 'undefined') ? obj[key] : undefined, nestedObj);
}

function getHotkey(arr) {
    return arr.hotkeys ? [[getNestedObject(arr.hotkeys, [0, 'modifiers'])],
    [getNestedObject(arr.hotkeys, [0, 'key'])]].flat(2).join('+').replace('Mod', 'Ctrl') : '–';
}

let cmds = dv.array(Object.entries(app.commands.commands))
    .sort(v => v[1].id, 'asc');

dv.paragraph(cmds.length + " commands currently enabled.  
  
");

dv.table(["Command ID", "Name in current locale", "Hotkeys"],
  cmds.map(v => [
    v[1].id,
    v[1].name,
    getHotkey(v[1]),
    ])
  );
```

Result:
 [obsidian-dataview-command-list-by-id 792×820 69.2 KB](https://forum.obsidian.md/uploads/default/original/2X/9/941d1ddfba27d5caab7bc258634ac95fb017525d.png)

##### Commands sorted by assigned hotkey

This I missed the most. Just to check if a planned hotkey combo is already taken …

```
const getNestedObject = (nestedObj, pathArr) => {
    return pathArr.reduce((obj, key) =>
        (obj && obj[key] !== 'undefined') ? obj[key] : undefined, nestedObj);
}

function getHotkey(arr) {
    return arr.hotkeys ? [[getNestedObject(arr.hotkeys, [0, 'modifiers'])],
    [getNestedObject(arr.hotkeys, [0, 'key'])]].flat(2).join('+').replace('Mod', 'Ctrl') : '–';
}

let cmds = dv.array(Object.entries(app.commands.commands))
    .where(v => getHotkey(v[1]) != '–')
    .sort(v => v[1].id, 'asc')
    .sort(v => getHotkey(v[1]), 'asc');

dv.paragraph(cmds.length + " commands with assigned hotkeys.  
  
");

dv.table(["Command ID", "Name in current locale", "Hotkeys"],
  cmds.map(v => [
    v[1].id,
    v[1].name,
    getHotkey(v[1]),
    ])
  );
```

Result:
 [obsidian-dataview-command-list-by-hotkey 789×822 76.5 KB](https://forum.obsidian.md/uploads/default/original/2X/8/86470033b38fd2b4ca5ec117606d210f2c4d349b.png)

#### Notes

I'm on Linux and this is good enough for me. I leave remapping MacOS keys and/or adding nice `…` tags around the keys (but not the plus signs in between!) as an exercise for the reader.
Anyway, it's a good check what we have, and could well be a starting point for the [Buttons](https://github.com/shabegom/buttons) and [Obsidian Leaflet](https://github.com/valentine195/obsidian-leaflet-plugin) plugins to maybe invoke commands *language-independently* , using their *ID* . Because now we know it an can make a list!
(Bi- and multilingual people switch Obsidian's language often, and it sucks that commands called up by their (locale-specific!) *name* suddenly stop working.)
18 Likes
[Unclear how to get list of commands and their currently assigned hotkeys](https://forum.obsidian.md/t/unclear-how-to-get-list-of-commands-and-their-currently-assigned-hotkeys/18836)
[Rishi](https://forum.obsidian.md/u/Rishi) May 16, 2021, 8:33am 14
This is a very thoughtful snippet from [@Moonbase59](https://forum.obsidian.md/u/moonbase59) like always! I've added some symbols in this for the Mac Shortcuts,

```
const getNestedObject = (nestedObj, pathArr) => {
    return pathArr.reduce((obj, key) =>
        (obj && obj[key] !== 'undefined') ? obj[key] : undefined, nestedObj);
}

function getHotkey(arr) {
    return arr.hotkeys ? [[getNestedObject(arr.hotkeys, [0, 'modifiers'])],
    [getNestedObject(arr.hotkeys, [0, 'key'])]].flat(2)
	.join(' ')
	.replace('Mod', '⌘')
	.replace('Shift', '⇧')
	.replace('Alt', '⌥')
	.replace('Ctrl', '⌃')
	.replace('ArrowRight', '→')
	.replace('ArrowLeft', '←')
	.replace('ArrowUp', '↑')
	.replace('ArrowDown', '↓')
	.replace('Enter', '⏎')
	.replace('Tab', '⇥'): '–';
}

let cmds = dv.array(Object.entries(app.commands.commands))
    .where(v => getHotkey(v[1]) != '–')
    .sort(v => v[1].name, 'asc')
    .sort(v => getHotkey(v[1]), 'asc');

dv.paragraph(cmds.length + " commands with assigned hotkeys.  
  
");

dv.table(["Command ID", "Name in current locale", "Hotkeys"],
  cmds.map(v => [
    v[1].id,
    v[1].name,
    getHotkey(v[1]),
    ])
  );
```

Although it works fine for me right now, except for sorting which needs some fixing, I'm sure I'm missing other symbols people might use,
 [image 1574×1614 300 KB](https://forum.obsidian.md/uploads/default/original/2X/a/a8df6efa3da551a26e7d70d0034beebb86765373.png)
[This](https://gist.github.com/Zenexer/c5243c4216f1f8cd2251) is a good place to find some of the common symbols if the built-in character viewer seems too much.
10 Likes
[Productive](https://forum.obsidian.md/u/Productive) May 21, 2021, 1:58pm 15
Hi I built a quick script with dataviewjs to collate my daily note lists for my weekly note. It's using regular expressions and the obsidian API to accomplish this. I'm pretty new to using javascript so any feedback will be appreciated.

```
//Set the beginning and end of the week
const beg = moment("2021-05-16")
const end = moment("2021-05-22")

//The RegEx that does the heavy lifting
const er = new RegExp(/##.Lists\n([\s|\S]*)##.[I|D]/g);
const re = new RegExp(/(?:####.*\n)(?:[-|\d.].*\n)*/g);

/*
My Lists look like this
## Lists
#### a list
- markdown
#### another list
- [ ] it catches these too
*/

//Obsidian's API has allows you to grab a file's parent
const par = app.vault.getAbstractFileByPath("Daily/2021-05-13.md").parent;

//Get the files for the week as a Map 
const week = par.children.reduce((acc,chil) => {
	let name = chil.basename;
	let date = moment(name);
	if (date >= beg && date <= end){
		acc.set(name,chil)	
	}
	return acc
},new Map())

const sortWeek = new Map([...week].sort((a,b) => String(a[0]).localeCompare(b[0])))

sortWeek.forEach((v,k,m) => {
	let path = app.vault.getAbstractFileByPath(v.path)
	app.vault.read(path)
	.then( fileText => {
		let listText = fileText.match(er)
		return new Promise((resolve,reject) =>{resolve(...listText)})
	})
	.then(listText => {
		const lists = listText.match(re);
		if (lists !== null){
			dv.header(4,k)
			dv.list(lists)
		}
	})
});
```

10 Likes
[Moonbase59](https://forum.obsidian.md/u/Moonbase59) May 22, 2021, 6:18am 16

#### Sortable columns—Note to myself

I'm using the really helpful [Sortable Plugin](https://github.com/alexandru-dinu/obsidian-sortable), so columns in my tables can be easily sorted in preview mode. It it in its early stages, but already quite practical to use.
Of course it won't be able to sort columns with “odd” contents, like user-formatted dates, for instance.
Nevertheless, since we could write a **sort comparator function** in Javascript for these, within the code block, it should be a snap if the author of *Sortable* could provide us with a hook to add our own comparator functions per column. And if we could access this within the “Dataview Javascript”.
I opened a [feature request for this](https://github.com/alexandru-dinu/obsidian-sortable/issues/12) on *Sortable's* GitHub page. Maybe you'd like to support it.
Related:
\* [About table sorting · Discussion #136 · blacksmithgu/obsidian-dataview · GitHub](https://github.com/blacksmithgu/obsidian-dataview/discussions/136)
\* [Check integration with obsidian-dataview · Issue #6 · alexandru-dinu/obsidian-sortable · GitHub](https://github.com/alexandru-dinu/obsidian-sortable/issues/6)
5 Likes
[hstagner](https://forum.obsidian.md/u/hstagner) May 28, 2021, 2:37pm 17
I'm looking to create a dataview table that I think can only be accomplished with Dataviewjs.
I have Literature Notes that look like this:
 [image 675×529 33.9 KB](https://forum.obsidian.md/uploads/default/original/2X/8/8ae6fb0f5c00559a6e97def0622b7cd9b36c2ec4.png)
I would like to show ALL Literature Notes in a table sorted descending by their “secondary tag” frequency. The secondary tags are all tags that are not “#litnote”. In this example the only secondary tag is “#writing” but some notes have more.
This is so I can find clusters of “Literature Notes” that belong to the same tag. I am at a loss at the moment to figure out how to associate the tags with the notes. I can grab the tags themselves and the notes themselves in js, but not the correlation between the two.
I hope this is clear. Thank you in advance for any help.
[torantine](https://forum.obsidian.md/u/torantine) June 3, 2021, 1:15am 18
[@Azulaloi](https://forum.obsidian.md/u/azulaloi) was looking for a dataview snippet that would give the word count of all pages in a vault with a specific tag. Uses the guts of the Better Word Count Plugin by [@lukeleppan](https://forum.obsidian.md/u/lukeleppan). Works really well with MetaEdit to change the search term. Here is what I came up with: [dataviewjs.wordcountfromtag · GitHub](https://gist.github.com/gblakehl/af639cba3c32762576d64c34effaf614)
 [dataviewjs-wordCountOtherPages-003 1106×626 542 KB](https://forum.obsidian.md/uploads/default/original/2X/d/d1bc9832ec9e0bf00562a0ea532657c4ff200199.gif)
6 Likes
[cristian](https://forum.obsidian.md/u/cristian) June 4, 2021, 12:51pm 19
Thanks for this!, one question.
Where I can know more about those 'inline metadata fields'? they look simple and amazing
[Moonbase59](https://forum.obsidian.md/u/Moonbase59) June 11, 2021, 11:47pm 20
Here's another thread that shows how an idea evolves and *DataviewJS* is used: [@FiekeB](https://forum.obsidian.md/u/fiekeb) and I were talking about how a recipe data collection could be set up.
[Help: #howto Build Recipe "database" in Obsidian (complex)](https://forum.obsidian.md/t/help-howto-build-recipe-database-in-obsidian-complex/19548) [Share & showcase](https://forum.obsidian.md/c/share-showcase/9)
Build Recipe “database” in Obsidian \*I usually write in Dutch, but for the sake of being able to ask help on the Obsidian Forum, this one's in English. I will translate it into Dutch to keep in my vault under “Culinair”, once I know how to set this up according to my wishes. #remindertoself \* Why I want to build this “database” of interlinked recipe and ingredient notes I have thousands of PDF Recipe books and also thousands of TXT recipes and lots of them in a recipe manager called Paprika. …
4 Likes
**next page →**
\* [Home](https://forum.obsidian.md/)
\* [Categories](https://forum.obsidian.md/categories)
\* [Guidelines](https://forum.obsidian.md/guidelines)
\* [Terms of Service](https://obsidian.md/terms)
\* [Privacy Policy](https://obsidian.md/privacy)
Powered by [Discourse](https://www.discourse.org/), best viewed with JavaScript enabled