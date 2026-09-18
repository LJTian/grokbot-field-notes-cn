# Product Management

**Session:** GrokBot for Product Managers — day 1
**Ran by:** Kevin De Parco and Roshan, xAI product team.

The framing is DHH's line, *software is product management*: what should it
do, who for, how, what does it look like, what are the priorities. Now that
building is cheap, every builder has to answer those. The session is "how we
build GrokBot with GrokBot" from the product org.

The stat they opened with: GrokBot accounts for a **double-digit percentage of
merged PRs** internally, and lets product people ship PRs to production
themselves.

---

## The four properties of a colleague (the design brief)

They built the product around what a good colleague does, and it's also how
they expect you to use it:

1. **Ties multiple tools together.** Linear/Jira, Salesforce, Notion, Figma —
   colleagues work across them, not inside one.
2. **Long-running context.** They learn on the job. Start with little context,
   get taught tasks, take feedback, get better.
3. **Independence.** They complete tasks on their own with their own access.
   Hence: every bot has its own computer.
4. **Messaging, not turn-taking.** Rapid-fire, interrupt-driven, threaded.
   You jump in and steer mid-task.

The two things to take away: bots you give **real work** to that come back
with **results**, not questions; and they **finish jobs** and come back when
they need approval.

---

## The team

Demo company: **Flylo**, a fictional boutique airline.

| Bot | Role | Notes |
|---|---|---|
| **Cora** | Chief of staff | Has email, calendar, listens on Slack. Builds a model of how you actually work. Grooms the inbox and only surfaces what matters. |
| **Emily** | Engineering manager | **Coached not to write code.** Manages five engineer bots. Takes a large chunk of work, deconstructs it, delegates, and runs the verification loops on what comes back. |
| Einstein, Igor, Nova, Larry, Eileen | IC engineers | Each spins up cloud agents with a copy of the repo when it's time to change code. |
| **Ashley** | Data science / analytics | Connected to the data warehouse (Databricks, Snowflake — "pick your favourite"). Writes and runs the SQL, returns numbers and charts. |
| **PMP** / "Pete" | Product assistant | Drafts PRDs, synthesises customer insight. Has a PRD skill: crisp P0/P1/P2 requirements, optimised for getting to code fast rather than document longevity. |
| **Pixel** | Designer | Loaded with "how to be an S-tier AI designer" material plus the company design system (in Figma) and reference files: fonts, colours, patterns, and no-no's learned over time ("never put X buttons in the left corner"). |
| **Ray** | Recruiter | Sourcing and pipeline. Not demoed. |

Sidebar groups: *Leadership* (pinned), *Engineering team*, and group chats
**EngPod** (run a standup on a project), **EPD** (eng/product/design
triumvirate), **War room** (incident triage).

Connected tools in the demo: Notion, Slack, Figma MCP, Gmail. The S-tier
design skill is stored alongside.

---

## Three PM use cases they named

1. **The attention list.** What have you been paying attention to this
   morning / week / month, diffed against your priority list. Cora does this
   by watching how you work.
2. **Research and customer context.** Data questions on demand instead of
   writing SQL and hunting for the trusted table.
3. **Shipping.** "You cannot be a PM in 2026 if you're not focused on
   delivering software to your customers."

---

## The workflow, as run on stream

The whole loop went from a data question to a cloud agent opening a PR.

**1. Ask the data bot a question.**

> How many people purchased tickets yesterday on mobile versus web?

Ashley: 1,400 tickets, ~58% web / 42% mobile.

> How many families were flying? Help us visualise these with charts.

Ashley returns charts of solo / couple / family / group, and that 25% of
flyers are families. Roshan's note: "I now get data queries and charts on
demand" is his favourite daily use. Make it a routine:

> Send me this as an update every morning at 6:00 a.m.

For major launches they've asked for **hourly reports** from the data store.

**2. Spot the problem in a funnel — and get corrected.**

Looking at a mobile purchase funnel Ashley had pulled earlier, they read it as
"big fall-off at seat selection." They replied in the thread:

> Looks like a big fall off when people are choosing seats on mobile. Work
> with @PMP to generate a product spec to optimize our mobile funnel.

Ashley messaged PMP — and **corrected the humans**: the big leak is
*search → fare selection*, not seat selection. They'd misread the chart. The
bot caught it before the spec was written.

**3. PRD.** PMP produced a Notion PRD with P0s and P1s: mobile fare results
need a redesign, faster compare section, honest fare proof on the card.

They one-shot it for the demo, but said plainly: normally there's human
review and iteration here. You can leave comments in Notion (or Google Docs)
and tag the bot — bots read the comments. "That number feels off" as a
comment is a real instruction.

**4. Hand off to design and engineering in parallel.**

> Hand the PRD to Emily and have the engineering team prototype these ideas.
> Also get Pixel to design each of the P0s.

Two handoffs fire. Pixel comes back with Option A and Option B. Room votes A.

> Hand the first mock over to Emily to update the prototype.

**5. Engineering manager decomposes.** Emily split the priorities into scoped
work per engineer and had **direct conversations with each one**, adding
context. Their observation: "agents are really good at prompting — often
better than we are at figuring out what context to give an agent." Give the
team the goal and let them work out the context and decomposition.

**6. Cloud agents.** Nova asked whether to create a PR; they said yes. Nova
launched a cloud agent on a local copy of the repo (setup scripts included so
it's runnable and testable) and monitors it.

**7. Verification loop.** The IC engineer reviews the cloud agent's output,
then hands to QA or to Emily for a second layer of checks against the
original goal.

**How much human to put in the loop:** choose by stakes. A docs-site change
or resizing something in the app — let it run. Implementing a design as
spec'd — jump in and ask for a demo or prototype. Two things that help:
giving agents an environment to verify their own output, *and* giving them
the tools to help you verify it (screenshots, recordings).

---

## Alternative team shapes they suggested

The Flylo team is one example. Others they've seen:

- A team whose job is keeping a **knowledge base of requirements** up to date
  and feeding it into the product — for complex systems where each small
  requirement has knock-on effects.
- A team that keeps **many repos in sync** in a convoluted codebase.
- A single **builder bot** that is eng + product + design in one. It works;
  they separate roles for the complex cases.

---

## Hard-learned lessons (their list)

1. **Named agents with separate memory, learning on the job.** They are not
   great on day zero. There's an onboarding phase where you give them skills,
   context, and teaching. Over time they take on more.
2. **Reduce noise.** When you set up a routine, tell the agent: *if this is a
   no-op — nothing important or urgent — handle it yourself or don't update
   me.* Cora grooms the inbox and only escalates.
3. **Agents all the way down.** Managers of agents. Agents coordinating cloud
   agents. Don't feel you have to be the one holding it together.

Also from Q&A: each bot has its **own memory pool**, plus a **shared memory
pool** bots write to when something is worth the whole team remembering. The
role-based split gives you strong memories per role ("how to be a really
good engineer over time"); group chats bring them together when needed. And
the goal is that you stop doing the "what does this agent know, do I need to
compact" mental work entirely.

---

## Copy this

1. A data bot on your warehouse. Ask it questions in plain English; make the
   good ones morning routines.
2. A spec bot with one skill: crisp P0/P1/P2, short, optimised for getting to
   code.
3. A designer bot loaded with your design system and your accumulated
   no-no's.
4. An EM bot that does not code. It decomposes, delegates, and verifies.
5. Thread your feedback: reply to the data message with the ask, tag the
   next bot, let them talk.
6. Tell every routine what to do on a no-op: nothing.

Related: [`founders.md`](founders.md) for the founder's version of ProdBot
and feedback → PR; [`engineering.md`](engineering.md) for the other end of
the same pipeline.
