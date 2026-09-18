# Sales

**Session:** GrokBot for Sales — day 2
**Ran by:** Krista (rendered "Crystal" in the captions) and Mark Wright, xAI
go-to-market. Krista is the team's power user; her templates are what the rest
of the sales team started from.

The maturity curve, sales edition: ask a question → "clean up my files" tasks
→ **"build me pipeline" / "get me a meeting with X company"** as a single
delegated objective → a staff function of bots working together.

The pitch is aimed at the parts of sales nobody enjoys: pipeline generation,
engineering questions you can't answer on the call, Salesforce hygiene,
forecasting.

---

## The team

| Bot | Job | Connected to |
|---|---|---|
| **Olive** (her dog) | Chief of staff. Day-to-day: morning prep, prep for the 9 a.m., drafts email replies as cards | Gmail, Slack, calendar |
| **PG** | Outbound prospecting. The PG skill is on the marketplace | Salesforce, X API, Gmail |
| **Echo** | Updates a deck live from what the customer said on the call | Granola (or Gong), Google Slides |
| **Customer Expert** | Knows her strategic accounts inside out. Updates the account plan after every call | Notion (database of record), Slack channels, usage data, changelog |
| **Engineer** | Answers technical questions live on a call, customer-ready | The codebase, Slack |
| Salesforce next-steps updater | Turns call transcripts into pipeline updates in her format | Granola, Gong, Gmail, Slack, Salesforce |
| Travel & expense, X bot, "learning" chat | Utility | — |

---

## Olive — the chief of staff

"The bus to the office is my most anxiety-prone time: not at my laptop, but
Slacks and emails flowing in." Olive preps the day and the 9 a.m. meeting and
drafts replies. A customer asks for a one-pager → Olive drafts the email as a
card; she edits, sends, or discards.

Routine: morning inbox scan. Her cadence is deliberate: **once or twice a
day, not more** — "otherwise I find it really noisy." Mark is the opposite
(chief of staff + heavy routines, higher spend) and offsets it by asking the
bot itself for optimisation tips.

Olive can also orchestrate: working on a deck, it calls the deck bot; working
on a customer, it calls that customer's bot for account data. Krista mostly
talks to the specialists directly and finds that uses fewer tokens.

---

## PG — prospecting with personal hooks

The workflow, run overnight:

1. Pick **five accounts** from her book in Salesforce (or she names them). You
   can do 100; she does five a day.
2. Pick **five contacts** per account.
3. For each contact, pull **personal hooks**, not company events. "Your
   company raised funding" — they're getting that from a thousand vendors.
   Instead: the CTO posted on X about building a software factory; the CEO
   posted about a product launch. Connect the **X API** — "X is where a lot
   of leaders and companies post."
4. Pull intent data: company growth, job openings, whatever you ask for.
5. Find podcasts and webinars the contact appeared in and **watch them**,
   pulling quotes that relate to what you sell. She used to try to listen on
   the way to work; a 45-minute webinar per prospect doesn't scale.
6. Rank contacts by who to reach out to first.
7. Draft the outreach in Gmail, as editable cards.

Before any of this sends: **de-slop.** Give the bot writing you're proud of —
scan your sent Gmail, Slack, your X — so it writes in your voice. "I'm very
picky that things sound like me."

Then build on it: "you drafted these emails, great — now draft LinkedIn
responses, now find 10 more people." Every day add ~20 more. Result: "I've
booked a lot more meetings with executive buyers because I understand what's
important to them based on what they've posted."

---

## Echo — a deck that updates itself during the call

Run discovery with Granola recording. Stop Granola, run Echo. It pulls the
transcript and updates the slides — use cases discussed, next steps — so you
leave the discovery call with a deck that reflects it. About two minutes.
Also: "translate this slide to Japanese" for international customers.

Granola is fast; Gong takes a couple of minutes to load after the call, so
Gong is better for the *next* call or the follow-up email.

---

## Salesforce next steps

"Does anyone enjoy updating Salesforce?" (One person did.)

She gave the bot her format — **initials, date, customer outcomes, next
steps** — and it listens to her Granola and Gong calls, pulls from email and
Slack, drafts the next-steps update, she reviews, it pushes to Salesforce.

---

## Customer Expert — one bot per strategic account

She works a few strategic accounts across many departments, internal and
external Slack channels, email threads. Notion is the database of record.
After every call the bot updates the **account plan**: signals, upcoming
renewal, stakeholders to reach, calls had, projects in flight, next steps.
Pull usage: "who are the top 20 power users?" — so the team can get feedback
before renewal or offer a new feature.

The feature she loves: **changelog ↔ feature requests.** A customer asked for
something a month ago; she'd have forgotten. When it ships, the bot flags:
*we just shipped this, reach out to the customer who asked.* "Feels like we
built a feature for them."

Per-client bot vs. one expert for all clients? Preference. She has one per
strategic account because she only has a few; AEs with hundreds of accounts
do it differently. Mark: per-customer bots for intent and notes, a chief of
staff directing them, plus an "intent" bot that builds demos on the fly.

---

## Engineer — answering on the call, not after

> Can you send me a customer-facing answer on how to set up cloud agents?
> Also send me a few outcomes that Amplitude and Fair achieved.

Without it: bring an engineer onto the call, or go find the Amplitude and
Fair account managers. With it: steps pulled from the codebase, outcomes
pulled from other accounts, formatted paste-ready for Slack because "it
already knows how I work." Mark: "how many times have we all said *let me
find the answer and get back to you* — now we answer on the call and speed
up the next step."

---

## The mindset shift, in her words

"When I first started, I mistakenly used it like a chat interface. I said *go
do this research* and it gave me links to go watch the webinars myself. I
pushed back: **no, go watch those webinars for me and draft an email.**"

Think of it as a **doing partner**, not a thinking partner. It has its own
computer. It can work overnight. Have the prospecting bot chew through a long
list while you sleep and wake up to drafts.

---

## Three tips (Mark's close)

1. **Connect your stack.** Whatever you use day to day, get it connected
   first. That's where the "aha" moments come from fastest.
2. **One bot, one job.** Engineer, pipeline, travel & expense. Onboard them
   as team members; give each all the material to be great at that job.
3. **Routines.** "Set it and forget it" — but see Krista's cadence.

---

## Q&A worth keeping

- **Tokens.** Run fewer routines (someone ran one every 15 minutes). Use
  specialists directly rather than routing everything through a chief of
  staff. **Use MCPs where they exist** — Gong, Granola, Salesforce shipped
  out of the box — and save computer use for tools without one. "A lot of
  sales tools don't have great MCPs."
- **Knowledge base as it grows?** Meet where you are. For them everything
  lives in Notion and Slack, so connect those. Salesforce is the source of
  truth for deals. GrokBot is the **orchestration layer** over Databricks,
  Salesforce, Notion, Slack — "no company is good at keeping data in one
  place."
- **Delegating to Cursor?** Just say "spin up cloud agents" in natural
  language; your Cursor account is connected.
- **Talking to other departments?** Slack, as before — but the bot can track
  the marketing channel for you.
- **Standardised setup for a team?** Take the power user's templates and
  share them so a new rep gets five bots on day one. Role-based onboarding
  (GrokBot asks your role and pre-loads templates) was rolling out.

---

## Copy this

1. Chief of staff for the morning: prep, inbox, reply drafts. One or two
   routine runs a day.
2. Prospecting bot: small daily batch, personal hooks from X, watch the
   webinars, rank, draft. Train the voice first.
3. Post-call bot that updates the CRM in *your* format from the transcript.
4. One account-expert bot per strategic account, with the account plan in
   your doc tool, updated after every call, watching the changelog.
5. An engineer bot on the codebase for live technical answers.
6. Push back the first time it hands you links.

Related: [`sales-engineering.md`](sales-engineering.md) (Sherlock is the SE
version of the engineer bot), [`sdr.md`](sdr.md) (the top-of-funnel version
of PG, at scale).
