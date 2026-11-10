---
tags:
  - notebooklm-import
notebook: "C_AI_AI Prompting - Agents - Computer - Tips"
category: "research"
---

In part one, we got Gemma 4 installed and running
on your computer using Lama. And while the OMA
app works great for basic chat, there's so much
more you can do with this model once you give
it a better interface. Today, I'm going to show
you how to set up Open Web UI. It's a free open-
source tool that turns your Gemma 4 into a full
chat GPT like experience right on your machine.
We're talking document uploads, knowledge
bases, image analysis, custom AI assistance,
and more. Everything still runs locally. It's
still free, still completely private. If you
haven't seen part one, I'll leave a link down
below in the description and up here in the card,
and you'll want to have Alama and Gemma
installed before we get started here.
Hi, I'm Jamie and welcome to Teachers Tech.
So, what exactly is Open Web UI? It's a free
open-source web interface that sits on top of
Alama and gives you a much more powerful way to
interact with your local AI models. Think of it
like this. Alama is the engine and open web UI
is the dashboard. The Alama app gives you basic
chat, image uploads, and web search, which is
great for getting started, but Open Web UI takes
it further. It lets you upload documents like PDFs
and spreadsheets and ask questions about them. You
can build knowledge bases, permanent collections
of files that your AI can reference across any
conversation. You can create custom AI personas
with safe system prompts and it gives you a full
conversation history with search so you never lose
a chat. The best part is that everything still
runs locally. Open WebUI is just the front end.
Your data stays on your machine. Your models stay
on your machine. Nothing is sent to the cloud. Let
me show you how to set this up. It's easier than
you might think. To install Open Web UI, we're
going to use something called Docker. If you've
never heard of Docker, don't worry. You don't
need to understand how it works. You just need to
install one app, then paste one command. That's
it. I'll put the link to this down below in the
description. But once you're here, you can see you
can just go download, pick what operating system
you're on, and then just go through the normal
install. On Windows, Docker Desktop uses something
called WSL 2 in the background. If it asks you to
enable WSL 2 during installation, just follow
the prompts and let it do its thing. You may
need to restart your computer after that step. On
Mac, you just install and run it. No extra steps.
Once Docker Desktop is installed and running, you
should see the icon down below in the taskbar or
menu bar. I want to point out that it will prompt
you to sign in, but you can skip it. By default,
members can use Docker Desktop without signing in.
Go ahead and open up terminal. So on Windows, this
is going to be the command prompt or PowerShell
or on Mac, this is terminal. So on mine, I'm using
Windows today. I'm going to go open up just my
command prompt. And I want to point out something
right away. So this is an update. If you get a
message like this, what you would do, you can go
and copy it, then go back over to command prompt,
and you can just paste it in, hit enter, and then
it will do the update for you. Now, you can see
it's all updated. Now, we're going to paste this
one command right here. I know this looks long,
but you just need to copy and paste it once. I'll
put this command down below in the description, so
you can just grab it from there. This is going to
be uh to download everything Open Web UI needs.
It will take a few minutes depending on your
internet connection. So, I'll speed up this part.
And that is it. Open web UI is installed. Now,
we're going to go and open a web browser. And
just go and put this in localhost 3000. And
you're here. The first time you open it, you'll
need to create an account. This is just a local
account on your machine. It doesn't go anywhere.
It's not going to connect to any service. So,
we're going to just pick a name, email, password,
and you're in. And look at that. Because the llama
is already running on my computer, open web UI
found it automatically. You can see Gemma 4 right
up here in the model dropdown ready to go. If you
don't see your model, just make sure that Alama
app is running in the background. If you need to
start the service, you can just go back to your
command prompt and put this llama space serve.
This should feel familiar if you've ever used
chat GPT or Claude. You have your chat area in
the center here, the model selector over here, and
your conversation history in the sidebar. You can
rename chats, search through old conversations,
and organize things with folders. So, let me fire
off a quick prompt to see this in action. Let's
keep this pretty simple. So, we have the same
Gemma model wept from part one, the same quality
answers, but now this is a much more polished
interface. Now, if you've watched part one, you
already know you can drag and drop files into the
Alama app, like PDFs, images, and even multiple
files at once, like this, and I can ask a question
like this. Let's sum up the main points. And it
works. But here's the catch. If I go and start a
new conversation and just say, "What was in that
PDF I uploaded earlier?" See, it has no idea.
Every time you start a new fresh conversation,
you're starting from scratch. Now, if you're
just doing a quick one-off question about a
single document, that's fine. But what if you
have a collection of policy documents or course
materials or product guides that you want your AI
to always have access to? Re-uploading five or 10
files every single time is not practical. Now,
that's the problem that Open Web UI solves. It
lets you build what are called knowledge bases.
So, these are permanent collections of documents
that Gemma 4 can access in any conversation at
any time without you uploading anything again.
Let me show you how this works. We're going to
go to workspace here and then look across the
top. We have knowledge and then we're going
to go to add new knowledge. In this demo,
I'm just going to say this is called school
policies and I'm just going to add what am I
trying to achieve? A collection of school district
policy documents including grading grading. I'm
not going to change any of this here. I'm going to
go and create knowledge. Now I'm going to go ahead
and click this content. I'm going to upload files.
I have these three files right here, PDFs that I'm
going to add. But you can also see how you can add
text content, even web page, but you would need to
be online to be able to do that also. So, these
documents are processed and stored permanently,
uploaded once, and they're there forever or until
you decide to remove them. Now, here's how you
use it. You start a brand new chat, and notice
I'm not uploading anything. In the message box,
I can go and do this a couple different ways. I
can either hit the more and attach the knowledge
and you're going to see school policies here or
else you can just hit the pound key and this will
give you a shortcut and you can pick school
policies. So now I can go ahead and ask can
a teacher use their personal phone to take photos
on a field trip and it's going to be grounded in
the knowledge that I uploaded. So look at that.
It pulled information from uh multiple documents.
It give me to give me a complete answer. I
didn't upload a single file in the conversation.
It's pulling from the knowledge base that I built
once. And just to prove that we're truly just
running on this machine, I'm going to go and turn
off my Wi-Fi. So, I have no connection at all. I'm
just going to go to settings and turn this off.
And let's keep with the knowledge base again. So,
let's put our pound key and we'll go back. Select
school policy. We'll ask a different question this
time. What are all the rules around student
photos and social media across our policies?
And it works perfectly. Everything, the model,
the documents, the knowledge base is all running
right here on this computer. Nothing's going to
the cloud. Now, let me explain what's happening
behind the scenes. When you upload documents
to a knowledge base, Open Web UI breaks them
into smaller chunks and indexes them. So, when you
ask a question, it searches through those chunks,
finds the pieces that are relevant, and feeds just
those pieces back to Gemma 4. So, the model is
answering based on your actual documents instead
of general training. You don't need to understand
how it works to use it. Just upload your files and
ask questions. And the privacy angle here is huge.
If you work with sensitive documents like student
records, legal files, financial data, medical
information, this lets you use AI to search,
summarize, and analyze without anything ever
leaving your computer. This is something that you
can't do with Chat GPT or any cloud-based tool.
Now, here's another thing Open Web UI makes easy
with Gemma 4. And I used this with a llama last
time to show you how Gemma 4 is multimodal, which
means it can understand and interpret images,
not just text. So, I have this image right here,
and I'm going to go and just drag it into here.
And I'm just going to give it a prompt. What do
you see in this image? Describe everything in
detail. All right. This is pretty impressive for
a model running right here on my computer. it was
able to pull the information from this picture
right here and just bring out all those details
from it. Now, you could use this to extract text
from screenshots, analyze charts and graphs,
read handwritten notes, describe photos, all kind
of practical things. Now, let me show you one of
my favorite features, custom personas. And you
can create a specialized version of Gemma that
are tailored for a specific task and save them so
you can use them at any time. This works through
something called a system prompt. basically a set
of instructions that shapes how the model behaves
for every message in a conversation. Now, let me
build you one so you can see what I mean. We're
going to go to workspace again and we're going to
stay in models right here and we're going to just
click new model. I'm going to go give it a name,
select my base model. I'm going to pick J Gemma
4 and my system prompt. So, I'm a prof you're
a professional email assistant. When given a
few rough notes or bullet points about what the
email should say, it's going to write me a good
email. That's pretty much what this is saying.
Also notice I could select knowledge. I could
upload files. And down below we have capabilities,
default features, bulletin tools. I'm just going
to go save and create. Let's go test it out now.
I'm going to go up and select my models. Here it
is right here. Email writer. And let's give
it this right here. Complaint to my internet
provider. Been down three times this month. want a
credit on my bill. Now, see how different this is
just from giving it this information. It's giving
me this detailed email that I can just simply copy
and paste over. It already knows based on how
I told it to write it, how to answer it just
by switching that model. Now, I can create as
many as these as I want. It could be, you know,
uh coding assistant, the quiz generator, meeting
notes summarizers, whatever you use regularly,
build a persona for it. And also don't forget
about the knowledge base how you can add documents
to this as well. Open web UI also has features
like skills or tools and these can even make it
even more powerful. I'll cover those in the next
video. Everything that I was showing you today I
was using the E4B model that I downloaded in
the part one video. Now, this is the default
Gemma 4 model and it runs well on most computers
with 8 to 16 gigs of RAM, but Gemma 4 comes in
a larger sizes and if your machine can handle
it, the quality of difference is notable. Uh,
the one I would recommend trying is the 26B. This
is a mixture of experts model. It has around 26
billion total parameters, but only activates about
4 billion at a time. So, it's smarter than the E4B
without needing as much power as you'd expect.
The download's about 18 GB and you'll want to
have at least 16 gigs of RAM to run it. Now, you
can pull it right from inside Open Web UI without
the terminal. The only thing is maybe the Gemma
Force might not be available yet, but I'll show
you where this is. If I go to just click on my
name, I'm going to go to the admin panel and I'm
going to go across the top to the settings and I'm
going to take a look at models right here. So, you
can see I'm using Gemma 4. I did use uh terminal
when I downloaded this last time and then Alama
picked it up and I can go to manage here and this
is where I can go ahead and enter the model number
and it can do a pull from Olama. The only thing
is if I click on here and I take a look, you won't
find Gemma 4 yet on the list here. So maybe that's
just not updated yet. So how you could do that is
just to go to uh terminal. So whether you're on
Mac or you're on your Windows. So if I go ahead
and just open up command prompt and I could go
ahead and put this in just so llama pull Gemma 4
26B and then this will pull it and then everything
will be connected through it that way. So it just
hasn't been updated yet on the list from Lama. So
let's step back and look at what you have now. You
have a completely private AI setup running on your
computer with a proper chat GPT style interface,
document uploads, searchable knowledge bases,
image understanding, and custom AI personas,
and all for free with nothing sent to the
cloud. I'd love to know in the comments,
what documents are you going to upload first?
What kind of knowledge base are you going to
build? Let me know. And that helps me figure out
what to cover for the next video as well. Thanks
for watching this time on Teachers Tech. I'll see
you next time with more tech tips and tutorials.