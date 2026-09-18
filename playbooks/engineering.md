# Engineering

**Session:** GrokBot for Engineers — day 1
**Ran by:** Ling Shi, software engineer at xAI. Built the first version of the
GrokBot mobile app solo in three weeks. Before GrokBot existed as an
orchestration layer, was managing 15 Cursor cloud agents by hand.

The premise: agentic coding is already good. The bottleneck moved to the human
who writes the prompts, watches the transcripts, nudges the agent when it
drifts, and re-explains the same standard to every new agent. The whole
session is about pushing that layer down to bots too.

---

## The team

| Bot | Role | What it holds |
|---|---|---|
| **Craig** (also "Ling Xixi") | Chief of staff / head of engineering | Who is working on what. Routes every request. Onboards new bots agent-to-agent. Does *not* hold engineering workflow details — that's Jenny's job. |
| **Cray** | UI engineer | Everything ever said about UI work, persisted in its own memory. |
| **Steve** | DevX engineer | Onboarded live from the marketplace template *Nightly audit engineer*, then renamed. Runs the nightly cleanup. |
| **Hogan1QR** | Infra engineer | Infra instructions, persisted in its own memory. |
| **Jenny** | Head of operations | **Owns the playbook** in Notion. Other engineer bots may read it, not edit it. Announces every change to every engineer bot. |
| **Fleet DB** (Notion database, not a bot) | Task ledger | Every task plus the stage it's at. A bot managing 20 cloud agents checks this instead of holding 20 agents in its context. |

**Why three engineer bots on the same model instead of one.** Any of them
could do any task. The split is about context, not capability: each bot has
its own context limit and its own memory. What you tell Hogan stays in Hogan
and is applied next time Hogan starts a task, without re-pulling
instructions. Switching one bot between too many kinds of task blows its
context. And you mostly never talk to the engineers directly — you talk to
Craig.

---

## Workflows, as run on stream

### 1. Unblock a teammate while you're asleep or on a flight

You're the only code owner on a service. A teammate pings you in Slack.

1. Bot monitors Slack for pings at you.
2. Reads the message, decides whether it's a review case.
3. Checks the PR against **your stated review criteria** — e.g. "must have a
   screenshot attached", "tests must not be fake tests".
4. Kicks off a code-scan / code-research skill, run inside a cloud agent in
   the repo.
5. Acknowledges back in Slack.

If it actually needs you, you look on your phone and reply to your bot:
*"this looks good, approve it."* The bot sends the approval and notifies the
sender. Human touches it once, from a phone.

### 2. Bug reports on X → PR

Bug reports about the product get posted on X. A bot watches (via the Slack
sync of the X feed), and for each report: checks whether the reproducer is
still valid on `main`; if it is, fixes it and sends a PR. Same shape for
security reviews and "find the right reviewer" requests. "Bots contacting
bots; humans only contact humans when absolutely needed."

### 3. Nightly code cleanup — 3 a.m.

Available as a marketplace template ("Nightly audit engineer").

- Every night at 3 a.m. (Ling says 4 a.m. in one place — either works), the
  bot starts a research cloud agent that reviews the whole monorepo surface.
- It looks for: code quality, things that should be modularised and aren't,
  comments that should be condensed, security audit items ("things we forgot
  are very important to prevent someone else stealing something").
- It opens PRs. Cloud agents may merge them **only if the PR includes a clear
  end-to-end proof.** Otherwise they wait.
- You wake up to a set of PRs.

Why nightly: nobody is shipping, so conflicts are unlikely, and the changes
are low-risk slop removal.

### 4. Internal tooling via a Slack mention instead of a dashboard

Problem: adding people to TestFlight by email. The old answer: build a
dashboard, add auth, add a DB, deploy behind a login, distribute. Takes an
hour or two with agents, which is fast — but why?

The new answer: anyone in the org `@mentions` the bot in Slack with the email
address. A routine (or webhook on the Slack signal) adds them to TestFlight.
The only setup: give the bot safe access to TestFlight, and one prompt
describing what to do.

### 5. Auto-fix everything: CI, deploys, alerts

- CI goes red → bot examines what's red → spins a cloud agent to fix → uses
  your instructions to decide whether it may merge → merges.
- Same hook for deployment errors, flaky tests, anything with a signal.
- **On-call is only paged if it's unresolved after 10 minutes.** "Most of the
  time GrokBot can get it done within 10 minutes."

### 6. Verify the product on its own computer

A user reports they can't see previously booked flights on flyloair.com (the
fictional demo airline). Craig navigates the site on its own VM, clicks
through, and reports back: `/trips` is a stub while navigation still links
there. Confirmed before any code is touched.

### 7. P0 escalation, defined once

Telling an agent "urgent" repeatedly is counter-productive: it starts
skipping steps and guessing to finish faster. Instead, define a standing P0
policy:

> A routine checks the cloud agents every five minutes. If an agent is off
> track — running a long sleep like `sleep 300`, drifting from the goal,
> being too conservative — interrupt it and nudge it immediately.

You never write a prompt to the cloud agent yourself after that. The bot
writes the follow-ups.

### 8. Broadcast a standard once — the playbook chain

1. Tell **Craig** the new rule.
2. Craig tells **Jenny**.
3. Jenny writes it into the Notion playbook and **announces it to every
   engineer bot.**

Next time you add a workflow ("do this step before you trigger a deploy"),
same chain. You think about it once. "Very similar to how a human
organization is shaped, at agent scale."

### 9. Proof on every PR

Told to Craig once, baked into the playbook by Jenny:

> Every single PR comes with proofs — screenshots for UI changes, perf metrics
> for performance improvements.

Ling doesn't watch the cloud agents any more. He checks results and proof.
Cloud agents attach screenshots (and can attach a video of their run) to the
PR description. Bug-bot and security-comment features run on the PR on top.

---

## Prompts that were used

Onboarding a new bot through an existing one:

> Hello, I have a new member in the team called Nightly. Rename them to Steve
> and tell them how the engineering workflows are enforced.

Craig then messages Steve with: how the Notion board works, the definition of
clean, how work ladders through the stages. Steve acknowledges and absorbs
into memory. You don't copy-paste anything between bots.

Investigate before fixing:

> I think there is an issue with flyloair.com that users cannot check their
> previously booked flight. Can you check if it's true?

The P0 definition (near verbatim):

> You need to set up a routine that checks cloud agents every five minutes.
> Check if they are off the track, such as running a sleep, running a long
> sleep like sleep 300, or going off our goal, being too conservative. We
> sometimes just need things moving a little faster. Interrupt and nudge them
> at the time you find them going off.

Then, replying to the confirmed bug (reply-quoting so the bot has the
context):

> Fix this issue urgently. Treat it as a P0.

Creating the playbook owner:

> Onboard a new member called Jenny, head of operations. Jenny needs to
> manage a playbook for my engineering team, own the playbook, and avoid other
> engineers updating it.

Adding a standard:

> Another requirement for the playbook is to make sure every single PR comes
> with proofs, like screenshots for UI changes and perf metrics for
> performance improvements.

Teaching the bot to say no (paraphrased from the talk): bots accept every
bug report and feature request by default. Tell them *why* something doesn't
belong in the product, what should not be done, and the reasoning. It's
stored in memory; you don't repeat "I don't want this, this is not simple
enough, we need to simplify."

---

## Routines and cadences

| Routine | Cadence |
|---|---|
| Nightly audit / cleanup | 3 a.m. daily |
| P0 cloud-agent check | every 5 minutes, while a P0 is open |
| CI / deploy auto-fix | on signal (red CI, failed deploy, alert) |
| On-call page | only if auto-fix hasn't resolved it in 10 minutes |
| Slack-mention tooling | on webhook / Slack signal |
| Scheduled deploy | "deploy 6 a.m. tomorrow" — the bot knows the time and calls the tools then |

---

## Numbers

- 15 — cloud agents Ling managed manually before an orchestration bot existed.
- 3 weeks — first GrokBot mobile app, built solo.
- 10 minutes — grace period before a human is paged for red CI.
- 5 minutes — P0 polling interval.
- 10–20 — the bot-count at which copy-pasting a standard into every bot
  stops scaling (hence the playbook chain).
- 20 — cloud agents one bot can manage without holding them in context, using
  the fleet DB.

---

## What still needs a human

Stated explicitly, because "where is the human?" was the obvious question:

- Product direction.
- Design details.
- Hard things bots couldn't finish: performance issues, the architecture of
  the next version "so we won't get sloppy code along the horizon."
- Teaching the bot how to say no.
- Making sure the bot is never blocked on auth — every auth step in the chain
  needs a smooth "human unblocks the bot" path.

---

## The three takeaways, in Ling's words

1. **Treat them like interns.** When you're struggling to communicate, don't
   reach for skills and formal invocation. Chat with them like a talented
   intern who doesn't know what to do yet but will be extremely capable once
   told.
2. **Sink one level further rather than fix the sink.** If you've typed the
   same prompt ten times, that's a waste. Work out what actually needs to be
   done and extract it — into a playbook, or into a bot that nudges another
   bot at the right time.
3. **Have a complete feedback loop.** Any engineering task needs a signal for
   success versus failure, or the agent can't know when to push further and
   when to stop and merge. The easiest loop is letting the agent drive the
   website via computer use. Hardware has its own signals.

---

## Copy this

1. One chief-of-staff bot. Talk to it, not to the engineers.
2. One engineer bot per domain (UI / DevX / infra). Their memories stay
   separate on purpose.
3. One ops bot that owns a playbook document the others can read but not
   edit. New standards go to the chief → ops → broadcast.
4. A task ledger outside any bot's context.
5. Define P0 once. Define proof requirements once. Define merge conditions
   once.
6. Nightly cleanup with a proof-gated auto-merge.
7. Hook every signal you have (CI, deploys, alerts, Slack mentions) to a bot
   first, a human second, with a timeout.

Related: [`../agents/VERIFICATION.md`](../agents/VERIFICATION.md),
[`../agents/ORCHESTRATION.md`](../agents/ORCHESTRATION.md).
