# SDR

**Session:** GrokBot for SDRs — day 2
**Ran by:** Simon, xAI go-to-market, SDR team.

The most *systems*-minded of the nine sessions. His argument: single-task
prompting is easy and pointless; the value is an end-to-end pipeline —
prospect → enrich → context → sequence → outbound — that runs on routines,
with **one bot you actually talk to.** "What's working for us today was not
working three months ago." So the setup has to be cheap to change and cheap
to share.

---

## Setup rules he stated up front

1. **Chief of staff first.** It's the first bot you create.
2. **Build every other bot *through* the chief of staff.** When you create a
   bot via the chief, the chief knows its purpose and end goal, so later it
   knows who to delegate to — and when a task needs two bots talking to each
   other.
3. **One bot per platform, not per task.** Bots are things that run in
   parallel. One email bot does all of email (draft, send, inbox). A second
   outbound bot only if you outbound on a second platform.
4. **Colour-code by function.** Orange = research, another colour =
   Shakespeare / copy, green = account-research army. "When my chief of
   staff messages an orange bot, I know at a glance it's in the research
   phase." Everything is delegated from the chief, so the colours are how he
   reads the pipeline.
5. **Don't sprawl.** "I promise you I've had way too many at some points. It's
   more chaotic and does more harm than good." Before a new bot: *why can't
   the email bot also be the inbox manager? Should this be a routine
   instead?*

---

## The team

| Bot | Colour | Job | Tools |
|---|---|---|---|
| **Simon-bot** | — | Chief of staff. **The only bot he talks to.** Every other bot was built from it | Calendar, everything below via delegation |
| **Shakespeare** | copy | Email. Meticulously trained on his voice | Gmail |
| **Web Search** | orange | Public signals: funding, job postings, news | Exa |
| **Simon soldiers** (an army) | green | Low-context sub-bots. Web Search splits a batch across them | — |
| **Army huddle** | — | Group chat: Web Search giving orders, soldiers reporting back | — |
| **Customer / Voice of Customer** | orange | Context from closed-won and closed-lost: why they bought, what pain, what product areas | Salesforce, call recordings |
| **PLG bot** | orange | Internal usage: who signed up, power users, what they use, closed-lost | Salesforce, product data |
| **Ample Market** | orange | Enrichment: find and **verify** emails so nothing bounces and deliverability stays clean | Ample Market |
| **Company research** | orange | Tech stack, job postings, org chart ("who leads their SDR team") | Sumble |
| **Inbox manager** | — | Ranks overnight Slack, meeting invites, external email into an action order | Slack, Gmail, calendar |

Everything ends up in a **CSV** — the sequencer, the prospect queue, the
board, and "what I need to action today." "A hideous UI. You shouldn't be
looking at this much, if at all. It's GrokBot's brain. Trust it to have the
context and only look when you really need to."

---

## The pipeline

**ICP first.** For an early-stage company: ask the chief which titles carry
deals past stage 1, which title/industry is most responsive to a first
meeting, and how that differs from the economic buyer. Reverse-engineer from
your own goal ("how many S1s can I get").

**Prospect.** Web Search + soldiers scan 100–200 accounts for net-new
signals. PLG bot pulls sign-ups and usage. Company research pulls stack and
org.

**Enrich.** Ample Market finds and tests emails.

**Context.** The nuance he says he hasn't seen elsewhere: your AE had a call
with the account *yesterday*. That transcript is gold and should shape
today's message. The bot has it: "they mentioned tool fatigue, AI fatigue" —
or "Simon on the AI team is investigating exactly this, reach out to him."
Most of those never get actioned. Here they get sequenced automatically.

Cross-bot example he walked through: a prospect account is closed-lost.
Chief asks Voice of Customer why → "we didn't support a critical function
then." Chief notices from recent closed-won that **now we do**. Account gets
**ranked higher** in the sequence — re-engage on the exact thing they care
about. Then chief hands to Shakespeare with the FinTech-specific context to
draft.

**Sequence.** Each day's actions come with Gmail draft IDs. He reviews in
Gmail one by one. Or asks the chief:

> Can you give me a score on how confident you are that this email is
> accurate, solid, and that they might actually respond?

He's now at the point of somewhat trusting it — but says: early on,
thoroughly read every draft and give honest feedback.

---

## Training Shakespeare — the voice

Everyone says "sync your email." He pushed further, in this order:

1. Look at **my sent email to external companies that match a Salesforce
   account where I'm the assigned SDR.** (Not all sent mail.)
2. From that set, look at the ones that **got positive responses**, not
   negative ones.
3. Put a **heavier weight on recent positive responses.** The product
   changes every few months; three-month-old messaging may be dead.
4. Still pull inspiration from older messages for the human aspect.

Then the critique loop. The first drafts came back templated — same email
with the name and company swapped. So:

> Give me examples of these emails.

And on each one: *this is why this email sucks and here's how to make it
better.* Repeatedly, until it broke out of the standard format.

> Not a single one of your emails should look like a template.

---

## Routines

| Routine | When | What |
|---|---|---|
| **50 new prospects** | daily | Ranked. **Top 5** are the ones to action first thing: someone who contacted sales and nobody replied, someone who downloaded content that matches a live conversation. |
| Calendar blocking | daily | Chief has calendar access: blocks **15 minutes at 9 a.m.** for the top 5, and **an hour at 1 p.m.** for the other 45. It learned how he likes to split his time. |
| Inbox ranking | every morning | Slack, new meeting invites, external email → ordered by what to action now. |
| Account signal scan | **8 a.m. every weekday** | All accounts, net-new signals: sign-ups, content downloads, inbound. "Speed to lead. Even a weak signal actioned while it's warm gets the most receptive responses." |
| **Salesforce trigger** | on stage change | If an account moves stage 0 → 1, **un-sequence** those contacts. Runs in parallel with the sequencer so you stop outbounding a deal that's moving. |

Alternative cadence he offered in Q&A: 250 prospects delivered Monday
morning for the week, if 50/day is more than your outbound needs.

---

## Skills

- **Prospecting skill** — everything he wants for a one-off account: title,
  ICP persona, owner, why, enrichment, LinkedIn, location. Run for net-new
  accounts mid-day; the rest runs on routines.
- **ICP skill** — their own evolving understanding of who buys GrokBot,
  fed by stage-1+ deals and Voice of Customer. Kept as a **skill rather than
  memory** deliberately: it will change drastically, and a skill can be
  updated once and called by every system.

---

## The army pattern

Web Search needs to check 200 companies. It won't do that in one context.
So: an **army huddle** group chat where Web Search says "40 each, run in
parallel," the soldiers do it, and results flow back to Web Search — not to
the chief, not to Simon.

Why a group chat instead of direct messages (Q&A): he can open the huddle
and check each sub-agent's output is accurate and flowing; and it scales
from 5 soldiers to 20 on a whim because the soldiers are **low-context** —
Web Search hands off exactly what each needs.

---

## Takeaways (his three)

1. **Go end to end.** It's a lot of pain up front to prompt back and forth
   and build the system. Stick through it, train it on your style, and the
   payoff is the full workflow running without you.
2. **Be intentional.** Build through the chief. Bots should talk to each
   other. "You shouldn't be focusing even harder and messaging even more
   bots — that's exhausting."
3. **Think systematically.** Question every new bot. Turn repeated chats
   into routines.

---

## Q&A worth keeping

- **Token cost of 50/day?** "It very much depends" — how many Gong calls
  you pull, how much Databricks context, how many fresh enrichments vs.
  Salesforce records you already have. Ask the bot where the spend is and
  how to optimise. Consider 250/week.
- **Fastest time-to-value if I know nothing?** Talk to the chief at a high
  level about what your workflow is. It will tell you where separate bots
  make sense.

---

## Copy this

1. Chief of staff. Build everything else from it. Talk only to it.
2. One bot per platform. Colour-code.
3. A voice bot trained on *positive-response, recent, in-territory* sent
   mail — then critique it until nothing looks templated.
4. Daily ranked batch with a small "action now" tier; let the chief block
   the calendar.
5. A signal scan every morning. A CRM trigger to un-sequence.
6. An army for batch research, reporting to its parent bot in a group chat.
7. Put anything that will change (your ICP) in a skill, not in memory.

Related: [`sales.md`](sales.md) (PG is the AE-scale version of this),
[`post-sales.md`](post-sales.md) (the same "one bot I talk to" discipline,
after the sale).
