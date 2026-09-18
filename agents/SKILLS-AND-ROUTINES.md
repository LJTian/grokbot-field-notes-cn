# SKILLS-AND-ROUTINES.md

**Use when:** you want an agent to stop needing the same instruction twice.

Two building blocks. A **skill** captures *how* something is done. A **routine**
decides *when* it happens. Always in that order, and never before the work has
been done by hand at least once.

```
Do it by hand  →  Get a reliable result  →  Save it as a skill  →  Give it a routine
```

Skipping straight to automation encodes a process nobody has validated.

---

## Three ways a skill gets made

### 1. By demonstration

Record yourself doing the task once; the agent turns the recording into a
reusable skill.

Works well for: UI-heavy workflows, anything in a tool with no API, "click here
then here then export."

**One demonstration is not enough on its own.** It captures the happy path and
nothing else. After the recording, add by hand:
- the decision logic (what to do when the case differs)
- error handling (what to do when the step fails)
- approval checkpoints (what requires a human before proceeding)

### 2. By correction — the highest-value source

> "Any time you see the agent think incorrectly, that's probably a good
> opportunity to build a skill to fix it."

Not re-prompt around it. Not silently fix it yourself — that loses the loop
entirely. The compounding only happens if the correction lands somewhere
permanent.

> "If you do that over and over, you actually get agents that compound and get
> better over time — versus 'I'll just fix it,' where you lose the feedback
> loop."

### 3. By writing it

When the process is mostly judgment, write it directly. Reading an agent's
reasoning is a good source of material: *"a lot of the skills I made were
inspired by just looking through these thinking blocks."*

---

## The overfitting trap

This is the single most common way a skill goes bad, and it happens precisely
*because* you wrote it at the right moment — right after something went wrong.

> "Whenever that rule or skill change comes from a problem that happened in that
> chat session, agents tend to put all the details of that session in the rule.
> Then it makes the skill less feasible, because it's overfitted."

**Write the principle. Delete the story.**

| Overfit | General |
|---|---|
| "When the invoice export fails with error 502 on the March batch, retry twice then email Dana." | "On a transient upstream failure, retry with backoff; escalate to the named owner after the retry budget." |
| "Don't put the banner above the buy button on the product page." | "After any layout change, verify no interactive element is covered." |
| "Use the v3 endpoint because v2 broke last Tuesday." | "Use the current documented endpoint; check the docs before assuming a version." |

A useful test: **would this rule still make sense to someone who wasn't there?**
If it only makes sense with the backstory, it is overfit.

---

## What a good skill describes

- when the skill applies — and when it does *not*
- the inputs and system access it needs
- the sequence of steps
- how the result gets checked
- the expected output format
- which actions require approval

---

## Routines

### What a routine needs defined

- which agent owns it
- the schedule and time zone — **or an event trigger, preferred**
- where its input comes from
- the expected output format
- approval boundaries
- what happens on failure
- **what to do when there is nothing to report**

That last one is underrated. Tell the routine that on a no-op it should handle
it silently or stay quiet. Otherwise you train yourself to ignore it, and then
you ignore it on the day it matters.

### Frequency is a budget

The dominant cost driver in every practitioner's setup. Three routines at every
15 minutes is hundreds of runs a day.

- Prefer an **event or webhook trigger** over a schedule, always
- Once or twice a day is enough for most reporting
- Five-minute polling is for actively supervising running work, not for watching
  for something that happens twice a week
- **Audit them on a schedule.** Put a recurring reminder in your own calendar to
  look at the list and kill what isn't earning its keep

### Connector or browser

A connector (an MCP, an API plugin) is faster than the bot driving a browser,
cheaper per task, and easier to whitelist or blacklist. Filling a web form by
clicking through it costs more than the same form's own API. Use a connector
when one exists; the browser is the fallback for anything that has no
connector, not the default.

### Test on safe data

A test run performs real work. It can change real files and hit real sites.
Point it somewhere disposable the first time.

---

## Self-improvement routines

A weekly routine where an agent audits its own operation:

1. **System audit** — what manual work happened this week that could have been
   automated?
2. **Voice/style learning** — diff what you edited against what the agent
   produced, and feed the delta back so the next draft is closer.

**Cap the output at one suggestion per week.** Unbounded self-improvement
suggestions feel like spam and get ignored, which defeats the point.

---

## Checklist for a new skill

- [ ] The work was done by hand at least once first
- [ ] It states when it applies and when it doesn't
- [ ] It includes error handling and approval gates, not just the happy path
- [ ] Nothing in it references a specific past incident
- [ ] Someone who wasn't there would understand every line
- [ ] It names how the result gets checked
