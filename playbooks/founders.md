# Founders

**Session:** GrokBot for Founders — day 1
**Ran by:** Shub, who works with founders on their GrokBot setups.

The frame: as a founder you have three execution jobs that make or break the
company — **preserve your focus**, **maintain velocity** across everything the
team ships, and **protect the quality of your insight** (decisions, planning).
Everything necessary-but-not-important is what you hand off. "The mental load
it saves you is probably more important than anything else I'm going to talk
about today."

The maturity curve he uses: chatbots → ephemeral agents you throw away after
one task → **bots that compound** (you keep them, invest in them, they get
better like an employee) → a fully automated staff function.

---

## The four founder use cases

1. **Closing customers** — "do things that don't scale," except you can scale
   them.
2. **Product changes** — staying across what's shipped and unshipped when
   engineers ship faster than you can follow. (His own story: demoing a
   feature that had been removed that morning, pointing at nothing.)
3. **Adapting to competitors** — bots can sign up and use competitor products
   as you.
4. **Shipping feedback quickly** — feedback → PR in hours.

---

## The team

| Bot | Job | Compounds on |
|---|---|---|
| **CloseBot** | Everything customer: call prep, post-call learning, support, activation, contracts, pipeline, calendar | Every call transcript |
| **ProdBot** | What's live: PRs, Linear issues, walks the product end-to-end on its own computer | Product decisions it's told about |
| **StockBot** | Competition: signs up, uses their product, reads changelogs, X, hiring | Every competitor it learns |
| **ProtoBot** | Prototypes, and turns customer feedback into PRs. Runs its own GrokBot account on its VM so it can drive the real product | Product context |
| **YapBot** | Talks like you. Learns from email, Slack, iMessage; re-learns weekly | Draft-vs-sent delta |
| **Misc bot** | Trash can for random requests so nothing pollutes the others' context | — |

Shared publicly after the talk: StockBot (via QR).

---

## CloseBot, in four parts

**Part 1 — Call prep.** Runs on a daily routine against his calendar. For each
meeting:

- Pulls product telemetry for that account: are they accelerating (find the
  feature to push) or declining (find the objection)?
- Researches who they are and what their product does.
- **Walks through their website and screenshots it** — and, without fail,
  finds a bug ("your cookie banner is on top of your submit button"). He
  opens calls with it. Actionable, and it shows he looked.
- Writes recommendations and risks for the call.

Output is a call-prep HTML file. "It doesn't look perfect and that doesn't
matter — I'm not sending it to anyone." Five minutes before the call, read
it. You have 15–20 minutes with a customer; get to the crux.

**Part 2 — After the call.** The bot reads the Granola transcript and records
what resonated and what didn't. If you pitched a note-taking feature and they
didn't care, the next prep doc won't lead with it. Give it two or three
weeks and it also lets you leverage *other people's* calls.

**Part 3 — Support.** Founders leave it to last and it crushes them. The thing
that makes it work: connect the bot to the risky pieces — your data, your
**billing** — because that's where support actually struggles.

**Part 4 — Activation.** You know your wow moment. When the activation event
fires (in the demo: a template shared with teammates), the bot automatically
sends the email with credits ("$1,000, which is a crazy example") so the user
feels rewarded in the moment. No monitoring every journey, no building a tool.

Plus: contract back-and-forth, pipeline generation, calendar. "I no longer
need to worry about 99% of this journey." He steals some of it back
deliberately because he likes talking to customers.

---

## ProdBot

> Give me a daily rundown of Flylo.

For the demo airline. It reads PRs and Linear issues, then **logs into the
product and walks it** on its own computer, mapping changes to what it sees.
Output: what shipped, what was unshipped, and **decisions worth being
intentional about** — micro-decisions the team made implicitly by shipping
fast. Attached: screenshots and a video of the bot walking the site
("the fastest way to verify if something is done well"). Connect it to
metrics and it shows you the results of ships instead of you watching a
dashboard.

---

## StockBot

> Run a competitor pulse on Notion and Craft.

For each competitor: finds them, signs up with a throwaway email, goes
through onboarding, uses the product ("it will write in Craft"), reads the
changelog, X posts, who they're hiring for ("a really good way to get signal
on what people are building"), who the team is. Output: an HTML teardown plus
a video. Craft isn't hiring; Notion is hiring a lot (he asked it to
truncate).

Routines run every few days. **If nothing relevant, it stays silent.**
"One of those ambient bots that's really important to just have around."

The optional part ("might be corporate espionage, do what you want with it
and be responsible"): if you know from your CRM that a customer churned to
competitor Y, have the bot email them and ask why. Don't try to win them back
in that message. Just get the signal.

---

## ProtoBot

> Pull the most recent customer feedback.

It pulls the feedback and starts working on it — in the demo, "the share
button for bot templates isn't exciting enough, they want it to pop" → a
cloud agent kicks off. The vision: every feedback channel (X, support inbox,
email) piped into one bot that opens PRs. "You'll see the full feedback →
ship → deploy loop happen in hours." Your job becomes the decision — which
feedback to take. "The main bottleneck should be your decision-making."

Because ProtoBot has its own GrokBot account on its VM, it can drive the real
product to QA what it shipped. Verification without leaving the loop.

---

## YapBot

One purpose: talk like him. It reads everything he's sent and learns his
voice — **weekly**, not once. Other bots proactively loop it in when they need
to write as him ("after they do this a few times where I encourage them, they
learn to loop in the other bots as needed"). Sensitive email stays as drafts;
the bot learns from the difference between its draft and what he actually
sent. "The end vision being that you don't need to think about it at all."

---

## What we learned (his slide)

- **Let your bots run free.** Give them as much access as you're comfortable
  with. It's the only way they do work end-to-end.
- **Don't throw them away after a course-correction.** The instinct from
  ephemeral agents is "context is polluted, start fresh." Here the context
  you "wasted" is the investment. Believe in them like employees.
- **Intentionality repays.** "Make this cooler" as a prompt will get stuck.
  The more intent you put into a task the first time, the more you can
  repeat it without hitches.
- **Spend one to two hours thinking about your day** and what to delegate.
  "I know that sounds dumb." Do it anyway.

---

## Power-user tips (the token section)

- **Browser use is expensive.** Watch the bot do a task once in the browser,
  ask it to inspect the network requests it made, then have it hit those
  APIs directly from then on. Faster and far cheaper. General rule: ask the
  bot how to optimise; it'll figure it out.
- **Audit your routines.** People run a routine every 15 minutes "because
  it's important" — that's 100 runs a day. Have a bot audit routine
  frequency. Prefer webhooks and inbound signals over blind schedules.
- **Make a voice bot.** Most underrated.
- **Import your cookies** so the bot stays signed in and you stop taking over
  its computer.
- **Group bots by expertise, not task.** Compounding happens inside a domain
  in ways you can't predict, so everything customer-shaped goes to the
  customer bot.
- **A bot whose only job is to optimise the other bots** — better routines,
  where you had to ask twice, why. Set it once.
- **Tell a bot to forget things.** "Forget all things about how we generated
  your profile picture. Don't ever think about that again." Clears it out
  and improves token efficiency.

---

## Q&A worth keeping

- **How do I set them up intentionally?** Inventory every single thing you
  need to do, then group. Give each bot a domain it's the expert in; let it
  expand as you ask it things outside that. Chief-of-staff-on-top is
  personal preference — he doesn't use one ("I like being a control freak in
  the weeds"). If you want the work abstracted away, use one.
- **Deterministic decisions for enterprise?** Models aren't. Have a cloud
  agent write code with a decision tree, then tell the bot: every time you
  need to make this decision, look at this flowchart and execute it. Code
  "cosplays being deterministic."
- **Group chats.** Pro: eager bots collaborating on a complex task. Con: they
  all love to talk, speak over each other, and get expensive. Usually you
  want a bot to tag two others once, not a room.
- **Marketplace quality.** Hand-audited by the team, and reviewed by bots
  that review bots. To evaluate one yourself: ask it "what do you do and how
  do you do it" before running the whole flow.
- **Do bots share memory?** No. They share a **file system** (one VM, one
  instance per bot, like desktops), so they can read each other's files and
  will do so proactively. Context windows are separate.
- **Cloud agent vs. GrokBot?** Anything complicated you want to ship, where
  you want control of the model: cloud agent. GrokBot passes it only the
  relevant context and can QA the result. "Try it a few times and you'll get
  the intuition."
- **Cross-account bot-to-bot messaging?** Doesn't exist yet.
- **Local execution?** Settings → local execution. Works. They bias to cloud
  because local apps steal focus and eat your machine.

---

## Copy this

1. One bot per founder responsibility: customers, product state,
   competition, feedback-to-PR, your voice, misc.
2. Call prep on a calendar routine; include a walk of *their* site.
3. Post-call learning from the transcript, every call.
4. Competitor pulse every few days, silent unless relevant.
5. Feedback channels → one bot → PRs. You decide which ones ship.
6. Weekly voice re-learning from what you actually sent.
7. Audit routine frequency; convert schedules to webhooks.

Related: [`product-management.md`](product-management.md),
[`sales-engineering.md`](sales-engineering.md) for the SE version of a
competitor bot.
