# Post-Sales

**Session:** GrokBot for Post Sales — day 3
**Ran by:** Blake, AI Deployment Manager at xAI. After the sale closes, makes
sure customers see ROI: "lots of emails, lots of Slack, Teams messages,
meetings, conversations."

The most personal setup of the nine, and the clearest statement of the
*one-bot-in-front* model. Line of the session: **"Gus is my best friend."**
He talks to one bot. Gus manages the other ten to twenty.

---

## Six use cases

| Use case | What it does |
|---|---|
| **Morning status board** | Same time every day: fires overnight, meetings today, what he said he'd do yesterday and didn't. |
| **Call prep** | 15–20 minutes before a call: who's on it, titles, what was discussed last time, something that launched since, a suggestion to bring up, anything he needs unblocked. Just-in-time, not a morning dump. |
| **Follow-up desk** | The second a call ends: bots get the Granola transcript, pull context, draft replies, create the materials. Handles "the work in between meetings." |
| **Promise keeper** | Watches for things he said he'd do and reminds him. |
| **Ask watch** | Watches for things he asked *others* to do that haven't come back — instead of losing them in the abyss of email and Slack. |
| **Account reset** | "Where are we at with Harbor?" → one pack: risks, people, blockers, open promises, Slack activity, next steps. Preceded by a space joke, because he only sends it when stressed. |

"I could have made 20 of these slides."

---

## The team

| Bot | Role | Notes |
|---|---|---|
| **Gus** | Chief of staff | Sole point of contact. "I'm very distractible. I didn't want to manage a team of ten. Gus manages a team of ten. I manage a team of one to two, depending on the day." |
| **Frankie** | Follow-ups | Drafts post-call materials, e.g. an ROI doc in the customer's branding. |
| **Wally** | Voice | Trained on his sent email and Slack. Knows **personas**: internal Slack is lowercase, casual, maybe an emoji; an exec email is short, to the point, formal. Knows he's "an exclamation-point person." |
| **Trudy** | Source of truth | Internal docs across many platforms. Gus goes to Trudy when an answer needs sources. |
| **Scout** | Internal radar | He used to juggle 30–40 Slack channels plus email updates. Scout sends one daily update with links. This is the "second" bot he sometimes hears from directly. |
| **Franny** | Forms / VM work | Builds Google Forms through the UI on its own computer. |
| **Harbor, Northwind, Brightline** | One bot per account | Each has the full context of that account. "Your own employee dialled in on that account." Recommended for small-to-medium books; "if you have 1,500 there's a better way." |
| **Staff meeting** | Group chat | Gus convenes the specialists to argue a decision. |

**Notification discipline.** None of the specialists ping him. Gus messages
Wally, Frankie, Harbor; they reply to Gus; only Gus's thread lights up
(the green/blue dot). "I don't want to be bothered with my ten-person team.
I want to be bothered with who I'm talking to." Franny only talks to him
directly if he talks to Franny directly.

---

## The demo, step by step

**1. Send Gus to a meeting.**

> Can you join the internal learnings call for me right now? Send takeaways
> when it's done.

Gus opened Google Meet on its computer, muted, camera off, entered his name,
and typed in the chat: *hey everybody, this is Gus, Blake's bot.* Afterwards
it sent the decisions (new branding, link), asks, and owners. He wouldn't do
this for just any call — "be protective over what it does for this."

**2. Post-call pack.**

> I'm done with the Harbor call.

(Normally automatic on the transcript landing; prompted for the demo.) Gus
messaged **Wally** (voice), **Frankie** (follow-up), **Harbor** (account).
Back came *"Harbor post-call pack is ready. Drafts only."* — three things:

- Gmail drafts to Maya and Priya, in his voice ("Hey Maya! — that's clearly
  me").
- A Slack draft to Alex, the AE on the account, in the post-sales channel:
  *just chatted with Harbor, meeting the new champions next week, working on
  an ROI PDF.*
- The **ROI one-pager** they'd asked for on the call, built by Frankie in
  Flylo branding.

He tweaks, presses send. "Probably used to take at least 45 minutes."

**Drafts only** is a hard rule: "I've made it very clear I never want it to
send anything on its own."

**3. VM work.** Directly to Franny:

> Make me an ROI form for Northwind.

Franny opened Google Forms and clicked through building it — team and role,
primary use cases, what does done look like — then returned the share link
and edit link and asked if he wanted it sent. His note: speed depends on the
task, and if you do a form often, use *Teach a task* so it doesn't guess the
steps.

**4. Account reset.**

> Where are we at with Harbor?

Gus messaged Harbor, Frankie, and Scout, told him "still waiting on Frankie
and Scout," then "now just Scout," then delivered: the joke (*How do you
organise a space party? You plan it.*), then what's at risk, who the people
are, blockers, open promises, Slack, what to do next.

How he built that prompt (Q&A): he told Gus where he gets stuck and
overwhelmed, then listed what he needs to know — risks, etc. — and Gus built
the rest. "Get a first prompt and build from there."

**5. Staff meeting.**

> Start a staff meeting to talk about what I should spend the next and only
> free hour of my day today.

Gus posted the question to the group. He's told them to **always disagree**
— "it's not helpful if they just agree, especially with AI." Northwind:
*don't spend it on us, there was a usage dip but it's fine.* Brightline:
*not us.* Harbor: *SSO.* Frankie: *protect the cap, this needs to go out
now; then SSO.* Scout agreed. Gus returned the synthesis: SSO first, then
send Maya the next-steps email (already drafted), park the rest.

Also useful for bias: "I don't want you to always bias towards a specific
customer. Bring all the voices into the room."

---

## How to get to this from a blank page — the voice dump

He recorded a **10–15 minute voice memo** on his phone while pacing: *my name
is Blake, this is my job, here's what I like about it, here's what I'm
struggling with, here are the processes that are broken, here's what we
could do better.* Pasted the transcript to his first bot:

> I need a system that's going to work for me. Help me build it.

It came back with structure: *you love talking to customers directly — let's
protect calendar time for that. This process is broken. You're constantly
checking Slack — let's take that off your plate.*

"Start with context. There's so much that lives in your head. Take it out of
your head, give it to GrokBot, and it will do the rest." If it gets stuck:
*don't stop until you figure this solution out.*

---

## Routines

| Routine | When |
|---|---|
| Daily brief | 8:30 |
| Unfinished promises | 9 a.m. and 1 p.m. |
| Friday dashboard | Fridays |
| **Self-improvement scan** | **Wednesdays** |

The self-improvement scan has two parts:

1. **Full system audit.** Watches what he does manually — sending things,
   checking Slack himself, things he never asks a bot for — and proposes an
   automation.
2. **Voice learning.** Takes the **delta between what a bot drafted and what
   he actually sent**, and sends it to Wally, which updates its rules.
   "Continuously gets better and better."

He originally gave it no limits and it sent "ten new bots to build" —
overcorrection. Now: **one suggestion per week.** If he disagrees, he pushes
back and gets a different one. "I self-improve at least once a week."

---

## Numbers

- 75% of a nine-to-five in meetings, by choice.
- Before: ~6 hours of meetings plus 3–4 hours of in-between work = 9–10 hour
  days. Now: same calls, close to fitting in 8 hours.
- Gus "has done very well up to 15 and 20" direct reports. No
  middle-manager layer needed yet. If it strains, add one — and talk about
  the org shape during the voice dump.
- Three routines on a 15-minute schedule = "hundreds of messages a day."
  Don't.
- "You don't need 45 bots."

---

## Q&A worth keeping

- **Cost.** Built to be efficient, but: driving a full UI on the VM (building
  a form by clicking) costs more than an API-native path (Google Forms' own
  AI with the questions pasted in). Routines that poll often are the main
  driver. Keep the team lean and specialised.
- **Other software?** MCPs/APIs where they exist; otherwise install it on
  the VM.
- **Will the bot own the account?** "Hopefully never." Humans are good at
  customer-facing work. The goal is to remove the work that doesn't need a
  human and make the human hours count.
- **Has it improved retention?** It catches things he didn't have time to:
  a micro-ship a customer was waiting for → email drafted and flagged →
  sent → trust. Harbor-bot always watching Harbor means issues surface
  earlier. Customers feel more tailored because he has the time.
- **Do bots verify each other?** Not peer-to-peer. Each bot has its own
  verification loop; Gus does the broader cross-check over all of them.
- **Layers of managers?** Not yet needed; see the 15–20 number.

---

## Copy this

1. Voice-dump your job for 15 minutes. Ask for a system.
2. One bot in front. Nothing else pings you.
3. A voice bot with personas per audience.
4. One bot per account for a small book.
5. Drafts only, forever, for anything customer-facing.
6. Promise keeper + ask watch as morning and afternoon routines.
7. A weekly self-improvement scan capped at one suggestion, with the
   draft-vs-sent delta feeding the voice bot.
8. A staff meeting when you need a decision; tell them to disagree.

Related: [`sdr.md`](sdr.md) and [`marketing.md`](marketing.md) for the other
two "single point of contact" setups; [`founders.md`](founders.md) for
YapBot, the founder version of Wally.
