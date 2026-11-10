---
tags:
  - notebooklm-import
notebook: "B_Science - Physics - Space - Earth - Quantum Theory Misc"
category: "research"
---

https://www.youtube.com/watch?v=8JuWdXrCmWg
8JuWdXrCmWg
Just a few months ago, a scientist showed a pretty
astounding relationship between space  and time — “an earthquake of a result.”
But it’s not about *this* kind  of space and time — instead,
it’s about the space and time  of computation. Like, how long
does it take to compute something?  And how much memory does it use?
Computational time gets a lot of attention. Like,
one of the most famous unsolved problems in  computer science — P versus NP — is about
distinguishing certain types of problems which  can or cannot be solved quickly. But the next
chapter is all about space — which is full of  its own fascinating and fundamental questions.
Recently, computer scientist  Ryan Williams made an unexpected discovery
that forced him to rethink  the rules of computational space and time
that he described it as “disturbing”.  He found a way to trade in space for
time in any program — like, a lot of  space. Some programs seem
like they shouldn’t be able to give up any space — they're using all of it. But, he proved that it's possible.
It's the first breakthrough  of its kind in 50 years,
and it’s pretty unbelievable — “unbelievable”  in a literal sense. Many computer scientists,
including Williams himself, did not  believe it was true… until he proved it.
Here’s one obvious, but very important,  difference between space and time:
space is reusable, whereas time is not. You’re probably aware of that. You can’t
redo yesterday, but you could turn your  living room into an office — using the
space for something else entirely. And  sometimes, you can trade in space for time.
Like, if you live in a tiny house — or  you can’t leave your apartment because of
a global pandemic — you might be reusing  the same space over and over again. You
put away the breakfast dishes, converting  the table to your kids’ school classroom,
pushing the couch aside to create a yoga studio.  But this efficient use of space can cost time,
cause you’re repeatedly rearranging the furniture.
Space and time are fundamental constraints  — both in our lives and in computer science. It’s
still true that you can reuse space on a  computer, but not computational time.
So, on a computer, when and how can you trade in  space for time? And what’s the “exchange rate”?
Often, when people talk about  computational space or time,
they’re using physical units — like  gigabytes or seconds. But these things
are constantly in flux — changing with  advances in technology and engineering.
In order to talk more fundamentally about  the space and time of a computation,
computer scientists use a Turing machine  — invented by the prolific Alan Turing.
He wanted to study the any possible “computing  machine” — not just the very limited technology
of the day. So, he devised the Turing  machine, which is a computer of the mind.
A Turing machine has an infinitely long strip of  paper — referred to as the “tape” — separated into
boxes. There’s a “head”, which reads and writes on  the tape, and then moves one square left or right.
A Turing machine is entirely theoretical — it’s  a mathematical construct. But it sort of reminds
me of a typewriter — which makes sense, because  the Turing machine was invented in the 1930s.
A human controls a typewriter — decides the  next keystroke. By contrast, a Turing machine
decides what to do using a very specific set  of instructions, which are laid out in advance.
On a Turing machine, the definitions of time and  space are more straightforward than they are in
the real world. We can measure time with a little  ticker. Every time the head moves — reading a new
square — the time ticker goes up. So the total  time is the number of steps the head takes.
To measure the space — or memory — that a program  uses, we’ll use another ticker. Similarly,
the ticker goes up every time the  head reads another square — but
only if it hasn’t read from that same  square before — it’s a new square.
If you no longer need an earlier  part of your computation,
then you can just write over that  part of the tape — you can reuse
that space. But the time you took to  do that earlier computation is gone.
So, right away, we can see that the amount of  space a program uses will be less than the time
it runs for. The time ticker is always  running, but the space ticker isn’t. So,
if the time is 100, then the space is  definitely some number less than 100.
But how much less space than time does a program require?
Some programs use just use a little bit of space — way less than  the 100 bound — but we want to an answer that
applies to all algorithms. And some programs  seem to store lots of information
— a huge table — which would essentially  require new space at every time step. So,
the space would seem to be very close to 100.
But, is it possible to create another program, which simulates the current one
— meaning, the same outputs from the same inputs — but uses significantly less space?
It would seem unlikely, given how much information some algorithms seem to store.
But, pretty early on in the study  of computational complexity,
researchers noticed that Turing machines  can be quite wasteful with their time.
Like, let’s say that you want to check if two  numbers are equal.
One option is  to go back through the tape — left, left, left —
to find the other number. Look at the first digit. Then go back — right, right, right. The first digits match.
Now let’s compare the second digit — left, left, left… and so on.
When it’s walking back and forth, the  Turing machine is racking up time,
but not space. And, if it’s not walking  back and forth, then the Turing machine
doesn’t need to store all that information,  so it can just write over it — saving space.
By exploiting these bottlenecks, researchers  proved in 1968 that it is possible to trade
in space for time. In the original program, the space was a number less than 100. But,
they showed that it’s possible to create another  program, which accomplishes the same thing,
whose space is less than the square  root of the original time — 10.
The square root of a number is way smaller  than a number — like, way, way smaller.
Instead of focusing on 100 and 10, let’s  move it to a general graph — showing the
original time of the program and the bound on the amount of space. In the original program,
we only knew that the space was less than  the time — it’s below the blue line. But,
in the simulated program, we know that  it’s below the yellow line — way further down.
But, not all Turing machines are so  inefficient. This graph — it applies
to single-tape Turing machines — but not to the more powerful multitape Turing machines.
These work similarly to a single-tape  machine, except there are multiple tapes,
each with its own head. It’s all controlled by a central logic — the state of the machine — but,
at every time step, the state can direct  each head to do something separate.
In some ways, a multitape machine  and a single-tape machine are
similar — they’re ultimately capable  of performing the same computations.
But a multitape Turing machine is way  faster — even if it just has two tapes.
It can simultaneously read information  off the two or more tapes, and that saves
a lot of time wandering back and forth. For example, to check that two numbers are equal,
you can put one tape head at the beginning of each one. No wandering back and forth required.
So, the multitape machine is way more  time-efficient than a single-tape machine.
You wouldn’t expect to see a graph like  *this* for the multitape machine.
In 1975, computer scientists proved that
this graph could be reduced slightly — but then, fifty years since,
no one has made any more progress. And most people thought it would be impossible to dramatically push that curve down.
In fact, this intuition is  so strong that last year,
when Ryan Williams did find a way to greatly reduce the space on a multitape machine,
he didn’t initially believe his proof. He just set it aside, figuring he would pick it up later,
find the error, and learn something in the process. But, when he returned to the proof,
he realized that there was no error — he had actually proved something that seems unprovable:
Any computation — which was originally constrained in time, but not constrained in space — could be
simulated using much, much less space. Specifically, in SQRT(TlogT) space, where T is the time of the original computation.
This is only slightly bigger than the SQRT(T)  we saw for the single-tape machine — although
it’s mighty close — which is remarkable given how much more efficient the multitape machine seems.
Creating this space-saving simulation is a two step process: First, you map out the computation,
unrolling the connections between different parts. And second, you recombine these pieces:
you need to create the same final outcome, but using way less space than before.
And to push that red line so low will require some surprising — nearly magical — mathematics.
First, let’s map the computation — specifically, how information from the past affects the future
steps. This is one way that physicists sometimes distinguish time from space — by thinking about
causality — the way one thing influences another. Influence only happens in one
direction — an event in the future cannot cause something to happen in the past.
We can imagine time as a long line — like a  ruler, marking each time the Turing machine
ticks along during the computation. Let’s  look at *this* moment in time — which I’ll
color green. We could draw arrows from all  the past moments which directly affect the
green part of the computation. But, this  will very quickly become unwieldy. There
are lots of time points and lots of arrows. Instead, we’ll break the computation into
intervals — into little time chunks, which  — for visual convenience — correspond to the
rainbow colors. So, our computation starts at red and it goes up to the purple interval.
We can still think about how these  intervals influence each other. For example,
if I want to simulate the computation  during the green time interval,
I need information from previous time  intervals — but which ones? Well,
I certainly need to know what was happening directly beforehand, so there is an arrow from
yellow to green — the information in the yellow time interval influences the green time interval.
But we might also need other information — for example, from the red interval — which
isn’t really represented in the yellow.  Then, we draw an arrow from red to green.
Now, to reproduce the little chunk  of the computation that happened
during the green interval, all we  need to do is follow those arrows
backward to get the information  from the end of the previous time intervals.
We only did this for green, but  you do the same for every time
interval — connecting it to the previous  ones to show the flow of information.
This is a graph — each time interval is  a node, and they are connected by edges.
We can unroll this graph to reveal exactly how each time interval depends on the others. For
example, the purple depends on green, blue, and yellow. But green depends on red and yellow,
which in turn depends on orange. We can similarly trace back the blue and yellow intervals.
This tree shows the flow of information  — it’s like a map of the connections.
What’s necessary to compute what?  Each node contains all the relevant
information from that time interval  — mostly what’s printed on the tape.
To figure out what happens at the end of the computation — that’s the purple dot — we need
to work our way up — recombining the  chunks, doing partial calculations
along the way. Our goal is to do this  in the most space-efficient way possible.
We wouldn’t want to compute everything in parallel — that would take a lot of space. Instead,
we want to compute things successively — in a clever order. But, what's that?
Well, the most reasonable  strategy seems to come from
a silly little game involving pebbles.
In fact, this pebbling game is so simple that I made a little website where you can play it
— it's linked in the description.
On each turn, you’re allowed to do one of  three things: You can place a pebble on a
leaf — those are the bottom nodes. If both nodes below a node have a pebble on them,
then you can slide one of those pebbles  up. So, *here* we can slide one up,
but *here* we can't. And you  can remove a pebble anywhere.
Your goal is to get a pebble to the  root of the tree — the top node.
Well, you could put pebbles  on all the leaves — the bottom
row — and then slowly move them up, row by row.
But that’s too easy. Let’s make it  harder. Here’s your new challenge:
Get a pebble to the root of the tree using the least total number of pebbles. That’s
why the third rule is useful: You  can remove pebbles and reuse them.
Last time, we used 8 pebbles. But, let’s push it. If you only have 7 pebbles, could you still reach
the root? What about 6? Or 5? 4? 3 pebbles? You can also change the tree’s height
— that's the number of layers, and see what happens then. Give it a try yourself — and let us know the results in the comments.
The best strategy here — this “pebbling strategy” — seems to also be the best way to solve Williams’
problem — the most space-efficient way to combine the little pieces of the computation to get the
final result. And just as you can reuse pebbles in the pebbling game, you can efficiently reuse
space — memory — when working your way up the causal tree. Like, you might be recomputing
the same thing many times — there's a bunch of orange nodes — but that's okay. We're trying to conserve space, not time.
The efficiency of this pebbling strategy is  part of a formal conjecture made in 2018.
The general version is called the “tree  evaluation problem”. You’re given numbers
on the leaves — the bottom of the tree — and functions on the other nodes. Each function takes
as input the two numbers below it and spits out a new one, which can be fed into
the function above that — until, all the way at the root, you end up with a single number.
The goal is to do this using the least amount of total space — or memory —possible.
You want to find the best way to solve all these functions, so that you can efficiently reuse space.
Since you need to work your way up to  solve for the root, it seems that a
pebbling-type strategy is the best. In other words, treating each pebble as a piece of
memory — and using and reusing them in the same pattern — is optimal.
In fact, the computer scientists that created the tree
evaluation problem bet $100 that you couldn’t substantially beat the pebbling strategy.
And, if that bet were right, it would be kind of a bummer
for Williams. Because it wouldn’t actually save him any space.
The calculation could take as much space as the original — which was not the goal.
Luckily for him, numbers are not pebbles.  And the inventors of the tree evaluation
problem would eventually lose that  $100 bet to a young duo of computer
scientists — including the son of one  of the original authors — who found a
very clever way to use the same space in  a computer’s memory to store information
and calculate things — like, the same bits  are serving multiple functions all at once.
Here’s one clever thing that you can do with  numbers that you cannot do with pebbles.
Let’s say we have two variables — a=9  and b=30. And we want to switch them:
a=30 and b=9. How do we do it? Computers  aren’t magic — we need to give it a set
of instructions. We could try saying,  “Set the value of a to be the value
of b — 30,” but the then the value  of a disappears — we’ve lost the 9.
The standard solution would be  to create a temporary variable,
set equal to a. Then, when we set  a equal to b — 30 — we haven’t lost
the value of a. We can set b equal to the  temporary variable, and they’re swapped.
But, is it possible to swap a and b  without creating an extra variable?
Here’s one way to start: First, let’s  switch everything to binary. So 9 is
1001 and 30 is 11110. (I put the extra zero  in front of a so they are the same length,
but it doesn’t change the value.) We put them in binary because we want
to XOR them — that stands for “exclusive or” — which means "one or the other, but not both."
Another way to think about it is 1 is “flip” and 0 means “leave it alone”. So, if you  flip and then leave it, the light is on.
Or, if you leave it and then flip, the light  is also on. But, if you flip it twice,
the light is back to off — just like  if you didn’t do anything at all.
Now, we’re ready to swap the  variables. (You can pause here,
if you want to try it on your own.) First, set a to be a XOR b — that is, we take each of the
bits separately and XOR them — then we set that to a. Now, set b to be a XOR b. But, of course,
a is different than it was in the beginning, so we’ll get something different. Finally, set a to
be a XOR b — again. This swaps the two variables. We can also convert them back to base 10.
In practice, this is often not the best way to  swap variables. But it’s cool that it’s possible,
and the intuition behind it reveals some  surprising mathematical possibilities.
So, why does it work? Well, XOR resets  itself every cycle of two — it cancels
itself out — a XOR a is always 0. And even if  you do some things in the middle — a XOR b XOR  a
— those a s still cancel out. Because  of the cancellations, you can continue
to store the value of the variable while also modifying it.
In general, that’s the magic technique: The same part of memory can be used for multiple
purposes — storage and computation — because of some clever tricks where things cancel.
When we swapped two variables using XOR, we did something twice and we ended up back
where we started — that’s where the  cancellation was. But there are other
systems in math with similar properties — including the roots of unity. For example,
the fifth roots of unity are these five points around a circle. They represent sweeping a dial
a fifth of the way around, two-fifths of the  way around, three-fifths of the way around,
and so on. If you pick any of these points and repeat that same sweeping motion five times,
you’ll always end up back at the  started. In other words, they cancel.
Last year, James Cook and Ian Mertz used these number systems — the roots of unity — to find a
shockingly space-efficient way to solve the tree evaluation problem. Instead of always using new
space — new memory — to compute the functions on the tree and store their values, their new
technique used the same chunks of memory over and over again to both store and calculate the values.
Their procedure for solving this  tree evaluation problem doesn’t even
really compute all these intermediate  values — they’re all sort of scrambled
together — the values strangely layered and intertwined. But, at the very top root node,
because the roots of unity cancel, these scrambled numbers straighten out
and produce the correct value. The original authors didn't anticipate this
because you can't XOR pebbles or manipulate them like the roots of unity.
But, Cook and Mertz took advantage of the strange properties of numbers.
In the  end, it was enough to win them $100.
And that, in turn, was enough for Ryan  Williams to simulate any algorithm using
much less space than expected. After breaking down the whole computation into this massive
tree — showing the flow of information  — he could apply Cook and Mertz’s super
efficient algorithm to compute the top  node — the end of the computation. But,
actually, the whole tree is really big  — and the goal is to save space — so he
only computes little pieces of the tree  — branches — on an “as needed” basis.
So, ultimately, any computation can be performed using way less space than the original time
estimate. But, the route to get there is pretty strange. It requires taking off little interwoven
chunks of the original computation — these branches of a tree — and then layering these on top of
each other, using wild XOR-style tricks to  super efficiently compute the final answer.
And, in the end, this takes way  less space — sqrt(T log T). But,
can we do better? Is it possible to push  the red curve even lower? No one knows.
But, unexpected breakthroughs often snowball — they build on themselves, spreading in new
directions. Last year, computer scientists found a strange and remarkably efficient way
to solve the tree evaluation problem. And then this year, that led to a startling separate
discovery — a way to trade in space for time. What could come next? Anything is possible.