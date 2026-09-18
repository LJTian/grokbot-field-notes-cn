# Roster

A catalogue of the agent roles described across the three days — sixty-nine
of them, deduplicated by *role*, not by bot name. Steve, Cora, Gus, Craig,
Simon-bot and Olive are one role (chief of staff) with six names.

Every file has the same sections:

| Section | What it answers |
|---|---|
| **Seen on stream as** | The named bots that played this role, and whose |
| **Owns / Does not own** | The swim lane. The *does not own* list is the part people skip and the part that stops sprawl |
| **Source of truth** | Where it gets facts. If it isn't there, the bot says so |
| **Needs approval for** | The human gates. Start stricter than this and relax |
| **Triggers / Outputs** | What starts it, what it hands back |
| **Routines** | Cadence, where the stream stated one |
| **Role description** | A paste-ready description with `{PLACEHOLDERS}`. This is the "soul" / system prompt |
| **From the stream** | The incident or quote it came from |

## How to use one

1. Copy the description block into a new bot. Fill the placeholders.
2. Cut the *owns* list down to what you actually need today. Don't build
   the four-bot support team on day one — David didn't.
3. Keep the *needs approval* list as written until it has earned trust.
4. When you correct it, add the general rule to its description — not the
   story. See [`../AGENTS.md`](../AGENTS.md).

Most setups on stream were 5–10 of these. Blake: "You don't need 45 bots."
Simon: "I've had way too many at some points. It's more chaotic."

---

## Orchestration

| Role | One line |
|---|---|
| [`Bot Factory (meta-bot)`](bot-factory.md) | Creates other bots: writes their descriptions, picks names, reviews and health-checks the existing team, and diagnoses workflow bottlenecks. |
| [`Chief of Staff`](chief-of-staff.md) | The one bot the human talks to. Routes every request to the right specialist, holds who-is-working-on-what, and is the only thread that pings the human. |
| [`Engineering Manager`](engineering-manager.md) | Takes a large chunk of work, decomposes it into scoped tasks, delegates to engineer bots, and runs the verification loop on what comes back. Coached not to write code. |
| [`Knowledge Base Manager`](knowledge-base-manager.md) | Watches the other bots' conversations passively and selectively writes durable facts to the team knowledge base — with the human's say-so, treating it like a git log, not a dump. |
| [`Miscellaneous Bot (trash can)`](misc-bot.md) | A catch-all for random requests so they don't pollute the specialists' context. Can hand a learning to the right bot when it turns out to matter. |
| [`Playbook Owner (head of operations)`](playbook-owner.md) | Owns the living document of team standards. Other bots read it and may not edit it. Every new rule goes in once and is announced to every bot. |
| [`Project Manager`](project-manager.md) | Learns how a multi-bot workflow was orchestrated by the human, then runs it end to end without them. Becomes the single point of contact for that workflow. |
| [`Self-Improvement Scan (bot optimiser)`](self-improvement-scan.md) | Audits how the human and the bots actually worked this week, proposes one automation, and feeds the draft-vs-sent delta back into the voice bot. |
| [`Source of Truth`](source-of-truth.md) | Answers questions from the canonical documentation with sources attached. Other bots ground their claims in it; the chief goes to it when an answer must be right. |
| [`Sub-Agent Army (soldier)`](sub-agent-army.md) | A pool of low-context, identical sub-bots that a parent bot fans a batch job across, reporting back to the parent in a shared group chat — never to the human. |

## Engineering

| Role | One line |
|---|---|
| [`CI / Alert Auto-Fix (on-call bot)`](ci-autofix.md) | First responder for red CI, failed deploys and alerts. Investigates, spins a cloud agent to fix, merges per policy, and pages a human only if unresolved after a timeout. |
| [`Comment Cleanup`](comment-cleanup.md) | Deletes unnecessary code comments. Exists because agents use comments as a crutch for workarounds instead of fixing root causes. |
| [`Domain Engineer (UI / DevX / infra / …)`](domain-engineer.md) | One engineer bot per domain, with its own memory, that turns a scoped task into a cloud-agent run and returns a PR with proof. |
| [`Feedback → PR`](feedback-to-pr.md) | Takes a confirmed piece of customer feedback and turns it into a PR, using the real product for context and verification, within hours. |
| [`Founding Engineer (PR watcher)`](founding-engineer.md) | The first engineer on a new repo: watches every PR, merges what's ready, spins up cloud agents for specific bugs, and can be called by voice for status. |
| [`Kanban / Task-Board Updater`](kanban-updater.md) | Keeps the task board true: moves cards when PRs land, creates cards from decisions, and lets other bots pick up work by watching the board. |
| [`Nightly Audit Engineer`](nightly-audit-engineer.md) | Runs a research cloud agent over the whole codebase every night, finds slop, modularisation gaps, comment bloat and security issues, and leaves PRs for the morning. |
| [`Playtester / QA`](playtester.md) | Actually uses the product — clicks through it, plays it, breaks it on purpose — on its own computer, and reports what's wrong before a PR merges or after a deploy. |
| [`PR Reviewer`](pr-reviewer.md) | Reviews every PR for correctness, risk and missing tests, checks that the required proof is attached, and either auto-merges or sends it back. |
| [`Prototyper`](prototyper.md) | Builds throwaway prototypes fast — inline HTML in chat, or a cloud agent on a scratch branch — to answer a design question, not to ship. |
| [`Slack Mention Responder`](slack-mention-responder.md) | Listens for @-mentions and DMs in Slack and processes them — a lightweight internal tool with no dashboard, or a triage layer in front of the human. |
| [`Triage Validator`](triage-validator.md) | Checks that the triage bot's understanding of a piece of feedback is correct before any autopilot fix proceeds. A second pair of eyes between users and code. |
| [`Triage`](triage.md) | Reads incoming feedback, reproduces the reported issue, and files a confirmed ticket — or discards it. Watches for prompt injection in the feedback. |

## Product & design

| Role | One line |
|---|---|
| [`Creative Director / Media Explorer`](creative-director.md) | Explores creative directions — music, motion, ad assets — as code where possible, and drops candidates somewhere the team can react (Notion, a playground). |
| [`Critic`](critic.md) | Reviews a piece of work against a rubric and says what's wrong, in plain English, before it ships. Feedback only; never edits the thing. |
| [`Data Scientist / Analyst`](data-scientist.md) | Answers data questions in plain English by writing and running the SQL against the warehouse, returns numbers and charts, and corrects the humans when they misread a chart. |
| [`Designer`](designer.md) | Produces on-brand mocks fast because it carries the design system, reference files and the team's accumulated no-no's. Delivers options, not one answer. |
| [`Prioritizer`](prioritizer.md) | Keeps a stack-ranked list of what to do next, scored by impact and effort, and re-ranks as new ideas and feedback arrive. |
| [`Product Changes Tracker`](product-changes-tracker.md) | Tells you what shipped, what was unshipped, and which implicit decisions got made, by reading PRs and issues *and* walking the live product on its own computer. |
| [`Recruiter`](recruiter.md) | Sources candidates, manages the hiring pipeline, and drafts outreach — or, flipped around, finds the recruiters and warm contacts for a job seeker. |
| [`Spec / PRD Writer`](spec-writer.md) | Turns an insight plus product context into a crisp P0/P1/P2 spec optimised for getting to code fast, and iterates from comments in the doc. |

## Sales & sales engineering

| Role | One line |
|---|---|
| [`Account Specialist (one per account)`](account-specialist.md) | A dedicated bot with the full context of one account: plan, stakeholders, renewal, signals, promises. Updates the account plan after every call and flags what needs you. |
| [`Battle Card Writer`](battle-card-writer.md) | Combines the competitor bot's hands-on findings with the technical expert's codebase truth into short, SE-ready battle cards: competitor claim vs. our reality. |
| [`Call Prep / Close`](call-prep.md) | 15–20 minutes before a call (or the night before), hands you who's on it, what happened last time, their usage, what shipped since, a suggestion, and any bug on their site to open with. |
| [`Case-Study / Slides Curator`](case-study-curator.md) | Turns a customer blog post or call notes into a slide in your fixed template, fetches the right logo, inserts it into the master deck, and hides what's irrelevant for the next call. |
| [`Competitive Intel`](competitive-intel.md) | Signs up for and uses competitor products on its own computer, reads their changelogs, blogs, X and job posts, and reports what's different and what you should react to. |
| [`CRM Updater (next steps)`](crm-updater.md) | Listens to the call, reads the thread, and writes the next-steps update in your exact format for you to approve and push — and reacts to stage changes. |
| [`Demo Scripter / Talk Track`](demo-scripter.md) | Builds no-hallucination demo scripts and call talk tracks that map a specific customer's pain to the live product flow, grounded in the technical expert. |
| [`Enrichment & Company Research`](enrichment.md) | Turns a name into a verified email, and a company into a tech stack, job postings and an org chart — so the sequencer doesn't bounce and the message lands with the right person. |
| [`ICP Researcher`](icp-researcher.md) | Works out who actually buys — from won deals, VoC and product data — turns it into segments and personas, and keeps that as a skill because it will change. |
| [`Live Deck Curator`](live-deck-curator.md) | After (or during) a discovery call, pulls the transcript and updates the deck with the use cases and next steps the customer actually said. |
| [`Prospector (outbound)`](prospector.md) | Picks accounts and contacts, finds personal hooks (X posts, podcasts, webinars — watched, not skimmed), ranks who to reach out to, and drafts the outreach in your voice. |
| [`Signal Scanner (web research)`](signal-scanner.md) | Scans the outside world for changes across your whole account list — funding, job posts, news, blog posts — every day, at scale, by fanning out to sub-agents. |
| [`Technical Expert (repo-grounded)`](technical-expert.md) | Answers "how does the product actually do X" from the codebase, via cloud agents, and rephrases it for a customer — without leaking IP. |
| [`Usage Signals (PLG)`](usage-signals.md) | Reads product usage to find who signed up, who the power users are, which teams adopted what, and which accounts are warm right now. |
| [`Voice of Customer`](voice-of-customer.md) | Holds why deals were won and lost — from call recordings and the CRM — so outreach and ranking can be tailored to what similar customers actually cared about. |
| [`Voice (writes as you)`](voice.md) | Learns how you actually write from what you actually sent — filtered, weighted to recent and successful — and drafts everything external in that voice, per audience. |

## Post-sales & personal ops

| Role | One line |
|---|---|
| [`Commitment Tracker (promise keeper + ask watch)`](commitment-tracker.md) | Two lists: what you said you'd do, and what you asked others for. Reminds you of the first and chases the second, so nothing falls into the abyss of email and Slack. |
| [`Daily Digest`](daily-digest.md) | Reads the newsletters, podcasts and feeds you subscribed to and can't keep up with, and posts one summary a morning where you'll see it. |
| [`Follow-Up Desk`](follow-up-desk.md) | The second a call ends: reads the transcript, drafts the replies, Slacks the AE, and builds whatever was promised on the call — as drafts, in your voice. |
| [`Inbox Manager`](inbox-manager.md) | Ranks overnight email, Slack and meeting invites into an action order every morning, drafts replies to the routine ones, and only escalates what matters. |
| [`Internal Radar`](internal-radar.md) | Watches the 30–40 internal channels and update emails you can't, and sends one daily digest of what's new, what you need to know, with links. |
| [`Meeting Attendee / Note Taker`](meeting-attendee.md) | Joins a call on your behalf (muted, camera off, announces itself), sends takeaways and decisions afterwards, and routes action items to the right bots. |

## Customer support

| Role | One line |
|---|---|
| [`Support Alert`](support-alert.md) | Pinged by the reply bot (or on its own hourly scan) when a ticket matches an escalation rule; posts to a shared Slack channel and tags the human. |
| [`Support Infra (build)`](support-infra.md) | Sets up the support system: installs connectors, creates the evals and traces tables, wires the KB, and builds a missing connector with a cloud agent when there isn't one. |
| [`Support Reply`](support-reply.md) | Works tickets through a written loop — read, look up, decide reply-or-handoff, act, leave a note — with confidence gating, and answers internal questions from the same KB. |
| [`Support Tuner (self-improvement)`](support-tuner.md) | Proposes KB additions when the reply bot can't answer, reviews last week's tickets and traces for what could have gone better, and — with approval — makes the change. |

## Marketing & growth

| Role | One line |
|---|---|
| [`Growth Ideas Logger`](growth-ideas-logger.md) | Captures growth ideas as they're said aloud, logs them to a growth playbook doc, and stack-ranks them by impact and effort. |
| [`Market Researcher`](market-researcher.md) | Studies your product and market, finds competitors' marketing sites, and names the positioning gaps and opportunities — the first bot in a campaign chain. |
| [`Marketing Analyst`](marketing-analyst.md) | Pulls the results of the last experiment from the ads platform, names the winner and the key metrics, and recommends how to update strategy and assets. |
| [`Performance Marketer`](performance-marketer.md) | Builds campaign shells in the ads platform, traffics the copy variants into them, and sends screenshots as it clicks — stopping short of spend without you. |
| [`Product Marketer`](product-marketer.md) | Takes the research and writes the positioning brief — one-liners, packaging, value statements — then the landing-page outline and ad-copy variants, iterating from your comments in the doc. |
| [`Website Ops`](website-ops.md) | Takes an approved landing-page outline and ships it: opens a PR against the marketing site, sends progress screenshots, and pushes to production. |

## Operations, events & finance

| Role | One line |
|---|---|
| [`Bookkeeper / CFO`](bookkeeper.md) | Tracks receipts and expenses, keeps the books current, and alerts on budget — with no ability to move money. |
| [`Contract / Policy Reviewer`](contract-reviewer.md) | First-pass review of a venue contract or policy: flags unusual terms, missing protections and market-rate outliers — explicitly a draft for a human expert to finish. |
| [`Event Planner`](event-planner.md) | Owns a production budget for an event — venue, F&B, staffing, AV, marketing as a separate line — and sends the sub-bots (venue, permits, contracts) their parameters. |
| [`Negotiator / Reseller`](negotiator.md) | Lists items or requests quotes, and negotiates with counterparties inside a framework you set — floor price, walk-away rules — reporting back for anything outside it. |
| [`Permit / Red-Tape Researcher`](permit-researcher.md) | Researches the permits, licences and regulations for an event type in a specific jurisdiction, and produces a checklist with lead times. |
| [`Venue Scout`](venue-scout.md) | Finds venues that meet the event's criteria, sends RFPs by email, and negotiates within the budget you set. |

---

## Roles that were on stream and are *not* here

- **Grind / Cheater** — bots that logged in and played the game to farm
  leaderboard rank for the hosts. A joke; Lauren's went *down* in rank.
- **Personal trackers** (Karen Cheng's package tracker, back-in-stock,
  shows tracker; Matthew Berman's PG&E plan optimiser) — personal-life
  automations, not team roles. The pattern is `daily-digest` +
  `signal-scanner` pointed at your own life.
- **The xAI voice agent** on the feedback phone line — a product feature,
  not a bot in this sense.

## Caveats

Names, quotes and cadences are as stated on stream. Demo accounts (Harbor,
Northwind, Brightline, Flylo, XAir) are fictional. The descriptions are
written from what the presenters said their bots do; none of them were
published verbatim, so treat each block as a reconstruction to edit, not a
template that was tested as-is.
