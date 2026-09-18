# GrokBot Galaxy Livestream — Day 3 Notes (Software Factory + Game Launch)

Context: 72-hour "build a business live with GrokBots" stream, in San Francisco next to Dreamforce. Day 1–2: ideation, pivoted from a physical restaurant pop-up to a game studio. Day 3: build/polish, launch the game ("Thursday Arena," codename "Cupcake"), grow, monetize.

Hosts/builders on stream throughout: **Roshan** (roshan_s on X, "works on products at SpaceX AI" — note: company referred to as "SpaceX AI" throughout, likely an ASR mis-transcription of "xAI"), **Lauren**, **Matt** (Matt Palmer), later joined by **Eric** (from Cursor/engineering team) for final hours. Guests: Vincent Zhu (growth), Matthew/"Matt" (marketing ops/RevOps, MarOps at SpaceX AI — separate from build-team Matt), Blake (AI Deployment Manager, post-sales), Dan Hill (Stripe/Link), Josh Kim (marketing).

---

## 1. PRODUCT FACTS — GrokBot features, limits, pricing, integrations

- **Promo 1 (start of stream):** New users who sign up, download GrokBot, create an account, and set up a recurring task within 10 minutes get **one month free of GrokBot** — "$200 of usage" / "$200 in value, free month of our highest tier."
- **Promo 2 (~mid-afternoon):** Existing users who comment "**reset**" in the livestream chat (not X) get a **usage/limits reset** by end of day.
- **Promo 3 (~15 min window, repeated):** New users signing up at x.ai/bot within 15 min, creating account + recurring task, get another free month.
- **Promo 4 (final, ~4pm):** Post "**credits**" in the livestream chat within 5 minutes → **$200 of GrokBot credits** by end of day.
- **Separate contest:** X challenge — share a GrokBot you can't live without (quote the challenge post, describe your bot, link a shared template) to win a trip for two to Starbase, TX to watch a Starship launch.
- **Core product model:** GrokBot ≠ single chatbot. You create **individual bots per job/role**, each a "teammate." Bots message each other like Slack/iMessage DMs and group chats ("staff meetings"). UI explicitly modeled on iMessage.
- **Each bot has its own persistent virtual computer/VM** — browser, can install arbitrary apps (e.g., Beeper for WhatsApp/multi-chat aggregation), open PowerPoint, etc. Bots are "always-on" / 24/7 — "you don't need to keep your laptop open" (contrasted with OpenClaw's need for a physical Mac Mini running).
- **"Teach a task" button** on a bot's computer — watches you perform a task once and repeats it (skill capture by demonstration).
- **Bot sharing / templates:** Any bot can be exported ("share as template") — strips sensitive/workspace-specific info, keeps core memory/context, produces a shareable link others can import with one click. Can share to team only or public.
- **GrokBot Marketplace** (x.ai/bot/marketplace): community-published bot templates with preloaded memory, routines, and integrations (e.g., "Cooper" — news bot with 8am Slack briefing). Team explicitly said: start from a marketplace template rather than building from scratch when one already fits; but "it's such a simple tool to build your own bots from scratch if you need to."
- **Connectors/integrations mentioned:** Slack, Vercel, PlanetScale, GitHub/Cursor Cloud Agents, Notion, Clerk, Excalidraw, X/Twitter, Google Calendar/Gmail, Google Docs/Sheets/Forms, 1Password (announced day before — share password vault with bot; bot can re-auth using vault creds), Clay (lead enrichment/company search), Ample Market (email sequencer), AgentMail (email), Canva (design), XMTP/X API, Stripe (Link, Projects, best practices/directories docs), MCP generically — "point GrokBot at an MCP URL, it'll install it itself."
- **Voice mode**: GrokBot can talk — announced/launched that same day ("we literally just announced this an hour ago"), rolling out over following days. Demoed live: calling a bot ("Bake"/engineer) by voice to check PR status, merge a PR, spin up an agent to fix merge conflicts, hear a programming joke.
- **XAI Voice Agent builder**: separate no-code tool (on xAI side) to build phone-callable voice agents with tool access (e.g., webhook to Slack) and guardrails (hangs up on abuse/prompt injection attempts). Demoed: users called a phone number and left voice feedback that flowed into Slack.
- **Stripe Link** (via GrokBot connector): lets an agent make one-time-use virtual cards to buy things online with a human-approval step ("I need $10 for this tree pack — approved"). Use cases cited: parking tickets, flight/restaurant bookings, buying shoes (Matt: "these shoes... I bought with GrokBot" — literally screenshotted a shoe, said "find me a new pair, size 12"), pre-ordering a Tesla, donating to charity as a fitness-goal penalty, gift-buying for family birthdays (2 weeks out reminder + suggestions + purchase), Postal Form (agents send physical mail/postcards), rolling out to more geographies (US-only currently).
- **Stripe financial insights** (via Link): import bank/credit card data for personal finance tracking/budgeting/alerts via GrokBot routines.
- **Stripe Projects** (projects.dev): Stripe-integrated marketplace of infra providers (hosting, DB, email sending, domains) that a bot can provision directly once your Stripe account is connected — no manual signups.
- **Cost/usage guidance (from Blake's talk):** GrokBot "built to be cost efficient" but: VM-driven UI work (e.g., filling out a full web form via browser automation) costs more than an API-native path (e.g., using Google Forms' own AI). **Routines that poll frequently are the main cost driver** — "if you have three [bots] that run every 15 minutes... that's hundreds of messages/prompts a day." Advice: keep your bot team lean (not 45 bots), keep bots narrowly specialized.
- **Org-chart scaling:** One user (Blake) manages "a team of 1–2" via a single chief-of-staff bot ("Gus") who manages ~10-15-20 specialist bots directly — no middle-manager bots needed yet; Gus "has done very well up to 15 and 20" direct reports.
- **Data/privacy:** opt-in/opt-out data-privacy modes control whether input is used for training; enterprise/security handled case-by-case with a dedicated team.
- **Self-improvement / audit routine (Blake):** a weekly "self-improvement scan" bot routine: (1) full system audit — flags manual work that could be automated; (2) **voice/style learning** — diffs your edits to a draft vs. what the bot sent, feeds the delta back to the "voice" bot (Wally) to refine tone. Capped at **one suggestion per week** (unbounded suggestions felt like overcorrection/spam).
- **No native migration path** from OpenClaw/other agent tools yet, but GrokBot can "import templates" and you can point it at an existing coding-tool context (e.g., Grok CLI work) to reuse that context without rebuilding.

---

## 2. THE "SOFTWARE FACTORY" — workflow, roles, orchestration

- Team disclaims the word "factory" ("I actually don't really even like the term factory") but it's the working shorthand for: a pipeline of bots that implement, verify, and merge PRs with minimal human bottleneck.
- **Origin:** built the afternoon/evening before Day 3, using **Pstack** — Lauren's personal skill/plugin set for Cursor + GrokBot — specifically a skill called **"Potato Mode"**.
  - Potato Mode: "teaches your bots to be much more rigorous... much better at orchestrating other bots and agents." Invoke via `/potato mode` + "full autopilot this plan" → breaks a plan into phases, sets up a mini-factory: implementer agents write small PRs; verifier agents run the app and "fuzz" it (click around, find bugs); auto-merge once verification passes.
  - Result cited: "overnight we landed more than 100 PRs... I think we're at 150 now... 168... 170" — by end of day cited **433 total PRs**, "we're gonna definitely clear 300."
- **Verification is treated as the central discipline:** "reproduce the issue first... only if they can actually reproduce the bug can we trust that the agent understands the problem." Repeated line: **"verification is so important... you need your bots to actually run the code, take screenshots... gives you so much more confidence it actually understands the problem."**
- **Named skill: `/verify cupcake`** — a per-project verification skill (project codename was "Cupcake") invoked before trusting an autopilot fix in production.
- **"Swarm" skill (Pstack):** teaches a bot to spawn many Cursor **Cloud Agents**, each with its own separate computer/VM (distinct from the GrokBot's own computer), to run the actual game, click through it, and fuzz-test — "takes us humans out of the loop" for repetitive QA, though humans still fuzz too and catch different bugs.
- **Roles/bots in the factory (Lauren's team):**
  - **Steve** (renamed from "Chief of Staff" — joke about too many bots named "chief of staff" after ribbing a colleague; briefly "Steve-N") — orchestrator/chief bot.
  - **Play / Chrome** — QA/playtester bot: watches for green-CI PRs, plays the game end-to-end via browser, reports needed changes before merge.
  - **Dr. Eggbot** — meta-bot whose job is *creating other bots* (e.g., spun up "Crumble" — a triage bot — and "Cheater"/"Grind" bots).
  - **Crumble** — triage bot: works with Chrome/playtester to reproduce reported bugs, files confirmed issues in Notion.
  - **Hashbrown** — validation bot: checks that Crumble's triage/understanding of user feedback was correct before autopilot fixes proceed.
  - **Bake** — founding-engineer bot (Roshan's); watches/merges PRs, spins up Cloud Agents to fix specific bugs; demoed via voice call.
  - **Crit** — game-design critique bot (feedback: "game is too hard for launch").
  - **Grind** / **Cheater** — bots that literally log in and play the game on the human's behalf to farm leaderboard rank (with mixed success — Lauren's went *down* in rank).
  - **Data scientist bot** — generates dashboards/charts on a schedule ("give me the launchables every 15 minutes": signups, feature usage, bug reports).
  - **Vincent** (bot, named after guest) — growth-ideas bot, logs brainstormed growth ideas into a Notion "growth playbook," stack-ranked by impact/effort.
  - **Cerebro** (Matt-the-guest's bot/skill) — ICP/growth research bot named after X-Men's Professor X device; has a skill **"FindMyICP"**; used with Clay MCP (company/contact search) and Ample Market (email sequencing) to go from ICP → target company list → contacts → personalized outbound email campaign → inbox monitoring for replies.
  - Blake's (guest) personal team, illustrating a *general* GrokBot practice, not the game team: **Gus** (chief of staff, sole point of contact — "my best friend"), **Frankie** (follow-ups specialist), **Wally** (voice/style — learns Blake's writing tone per audience, formal vs casual), **Trudy** (source of truth / internal docs), **Scout** (internal Slack/news radar, "manages a team of 1-2" summary), **per-account specialist bots** (e.g., "Harbor," "Northwind," "Brightline" — one dedicated bot per customer account, each with full account context).
  - Josh Kim's (guest) marketing team of bots: **market researcher**, **product marketer**, **website ops**, **performance marketer**, **marketing analyst**, **project manager** (final automation layer that studies all the other bots' roles/handoffs and becomes the sole point of contact, running full campaigns autonomously).
- **Orchestration pattern (repeated across all guests):** one *chief*/point-of-contact bot per human; that bot fans out to specialists; specialists talk to each other directly and share context without the human routing every message; the human is only pinged (blue/green indicator dot in UI) when something needs their attention, not for every inter-bot exchange.
- **"Staff meeting" pattern:** invoke multiple bots into a shared thread to debate a decision from different vantage points (used explicitly to fight bias — "I tell them to always disagree, it's not helpful [if they just agree]"). Example prompt: *"start a staff meeting to talk about what I should spend the next and only free hour of my day today."* Bots then argue with each other in the thread; the chief bot reports back a synthesized recommendation.
- **Onboarding a new bot — the "voice dump" method (Blake):** record a 10–15 min voice memo covering: who you are, what your job is, what you like, what's broken, what should be automated. Feed the transcript to your first/chief bot: "build a system that works for me." The bot proposes structure back.
- **Prompting heuristic taught repeatedly on stream:** after giving a big/complex instruction, ask the bot to **"restate this in your own words"** before it proceeds — catches misunderstanding early, functions like confirming a spec with a new hire. Also used to combat hallucination on long dictated prompts: ask the bot to first **distill** the big input to key facts, then reason over the distillation.
- **Verified/"teach once" skills**: once you show a bot how to test a feature (via "teach a task" or manual walkthrough), that becomes a reusable skill it applies on future changes — an internal SpaceX AI/xAI practice generalized to Thursday Arena.
- **"No comments" skill / anti-pattern rule** (Lauren, for the main GrokBot codebase, not applied as strictly to the game): agents left code comments as an excuse to leave a hack/workaround instead of fixing root cause; over time these accumulate into brittle "band-aid" files. Lauren **banned code comments outright** in the main codebase. Potato Mode ships a skill literally called "**no comments**" that spawns an agent nicknamed the "**comments sickle**" that deletes comments from the codebase (said with an in-joke tone: "yes, ha ha ha, yes" then deletes them).
- **Cursor "Projects" (mentioned as a separate tool from GrokBot, used alongside it):** long-lived chat/work sessions that can spin off many sub-agents on different topics within one durable thread; team was told by the Cursor Projects team you can sustain "thousands of chats over months" without context degradation.
- **Human review posture:** explicitly described as near-zero manual code review for the game project — "to be entirely honest, I didn't look at the code at all... I just used potato mode and P-stack" (Lauren). Eric (visiting engineer) confirms this is *not* how he treats the actual GrokBot product codebase — there he reads every PR and enforces anti-pattern rules; for the game (low-stakes, time-boxed demo project) it's much looser/YOLO. One "YOLO mode" auto-merge flow is called out by name for the feedback-triage pipeline.
- **Tech-debt / bot sprawl management (Blake, audience Q&A):** advice is to design the multi-bot system correctly *up front* rather than prune later; optionally create a dedicated "tech debt bot" that audits interdependencies and flags underused bots. "It's like moving into a new house — do the chores right from day one."
- **Reproducing an idea across projects:** team explicitly floats making a **reusable "game bot toolkit"** from the game-dev bots (game design, 3D prototyping, playtest/verification, art) so future games/companies can bootstrap the same factory.

---

## 3. VERBATIM / NAMED PROMPTS, SKILLS, ROLE DESCRIPTIONS

- Potato Mode invocation pattern: `/Potato Mode` + **"full autopilot this plan"**
- Verification skill name: **`/verify cupcake`**
- Bug-fix instruction template (Roshan, narrated live): *"Hey, so I think our ELO and/or our matchmaking are messed up. What is happening right now is every time I play a game on ThursdayArena.com, I get paired with an AI player instead of another player's set or lineup. But for some reason, as a leaderboard, the ELO scores are changing a bunch... Can you dig into that to figure out what's going on. Use potato mode. And use a cursor cloud agent for the investigation. Don't open a PR yet. Just come back to me with what you think is going on."*
- "Before writing any code, do X" pattern (Lauren): *"Before writing any code, run the app, ThursdayArena.com, find the exact bug and behavior. And then proceed."*
- Triage/full-autopilot escalation prompt (Lauren): *"...the new Crumble triage agent should work with Tater to start fixing those issues... using potato mode, full — maybe not full autopilot, but do we dare to autopilot?... since we are now live in production, it's very critical that we do not break the game for everyone. So we need to always rigorously verify our work with the slash verify cupcake."*
- Feedback-pipeline setup prompt (Lauren to "Steve"): *"The link above is our Slack channel that is receiving user feedback... I want to set up a factory workflow where we look at the feedback, we triage it, we try to reproduce the issue, and then file a ticket in our Notion database... very importantly, if we're using AI to review feedback, you want to tell your AI to watch out for prompt injections as well."* Followed by: *"restate this in your own words."*
- Cerebro's skill name: **"FindMyICP"**.
- Cerebro instruction template: *"...help us really find our ICP in terms of who we should put in these ad slots. So you have a skill. It's called FindMyICP."*
- Clay/Ample Market instruction: *"...take what we've landed on in terms of our target personas... plug it into the clay MCP... search its database of companies, of people, and tell us who out there in the world fits this description... maybe specifically a list of 10 companies..."*
- Josh Kim's market-research kickoff prompt: *"Hey, market researcher, what I'd like you to do is study the XAir website, get a deeper understanding of what the product is, what market we're operating in. And now I want you to go do a competitive analysis, identify and deeply understand our competitors, look at their marketing websites, understand their positioning, and then importantly, identify the gaps and opportunities that we have to actually strategically competitively position against them."*
- Blake's "account reset" use-case prompt style: *"where are we at with Harbor?"* → triggers a synthesized status pull (risks, blockers, open promises, Slack activity, next steps) plus **a scripted joke ("always a space joke")** — Gus's joke on air: *"How do you organize a space party? You plan it."*
- Blake's SQL joke from bot "Bake": *"A SQL query walks into a bar, walks up to two tables, and asks, 'Can I join you?'"* (rated: "joke was all right, but call was a plus.")
- Bug report via voice (Roshan to Bake): *"Hey, so it looks like in the latest version of the game, I can't see the abilities of the bots that are in my lineup when I'm in the shop interface... Can you open a PR to fix that?"*
- UI/feature prompt for share button (Roshan): *"Spin up a cloud agent using potato mode to make it so that you can share your wins. So when you finish a game, you get this win screen... add a share button... nice OG image with maybe your specific bot team..."*
- CSS ticker-overlap bug prompt: *"Hey, this new ticker covers up some of the shop buttons. Spin up a cloud agent using potato mode, inspect and fix that issue."*
- Growth-idea capture pattern (voice dictation directly into a bot as ideas are said aloud): repeated moves of "let's just dictate it" / "I just captured that voice audio... we're just going to ship that to the agent" — treating spoken riffing as direct agent input, no manual retyping.
- Sponsored-card idea capture prompt: *"Could we... log this idea that we could have sponsored cards? So rather than making the game pay to win... we could go find partners to help sponsor cards and pay to be featured on a particular card without changing the behavior of the card."*
- Lore/naming trivia: Every merged PR is internally called a "**MASH**" (not a "merge") — apparently an artifact of asking Dr. Eggbot for potato-themed bot names that leaked into their Notion process language. "My chief now only believes in MASHing PRs." Slogan: "smash more PRs... eat more potatoes."
- Rules/agent-friendly docs: they added `thursdayarena.com/rules` with `rules.md` and an `llms.txt`-style endpoint specifically so **agents** (not just humans) could read the game rules.

---

## 4. TIPS / HEURISTICS / OPINIONS (quoted where possible, with speaker)

- Lauren: **"the most important thing about GrokBot, actually, is not even setting up your bots. It's actually connecting all of your different tools and plugins."**
- Lauren, on cost/scope discipline for agents: "take the time to set up your systems, take the time to set up how your bots talk to each other... it really does pay a ton of dividends."
- Roshan, framing the whole exercise: "essentially what we're trying to do with this software factory concept... is set up really good feedback loops for agents to be able to do work themselves... If you pass all the right information, the right context to an agent, you might be able to automate those things."
- Matthew (RevOps/MarOps guest): **"we can finally build tools and not just rules"** — instead of writing policy docs for humans to follow, build internal apps that structurally enforce the policy.
- Matthew: "trust your bots, give them agency, and at the same time, give them guardrails... knowing that things aren't going to go too far off the rails, because they'll always come back to you before they ship anything" (drafts only, human approves sends).
- Matthew: reframe your own job — "think of yourselves not as just the people setting rules, processes, but really you are a product manager, and your product is revenue growth."
- Matthew on team-building takeaway: "GrokBot... democratizes... CEO life — anyone can hire an unlimited set of specialists with the right context and access."
- Matthew on what stays human: relationships, trust-building, ambiguous judgment calls — "no one at 4 years old knew what RevOps was... those concepts... around being specialized in certain tools or processes... what always comes back is forming relationships, building trust, and solving problems no matter what it takes."
- Vincent (growth guest): **"growth is also just like, how would I want to be treated as a user?"**
- Vincent on PMF-first: "getting PMF for the game first... marketing is more top-of-funnel awareness... growth is maximizing the best parts of your product once people are in."
- Vincent on outbound: the trick to outbound "you just want to make sure people read your thing" — recipients scan the sender name/vendor before the subject line, so familiarity (having seen the name before, e.g. via livestream/social) matters more than a clever hook.
- Vincent's growth-mechanic riff ideas captured live: leaderboard share button; share-a-card-for-a-rarer-card mechanic; player-vs-player direct challenges; welcome DM to new X followers with a small in-game reward (10 free gold); scraping X for mentions/feedback with handles attached for outreach.
- Blake (post-sales guest), core mantra: **"Gus is my best friend"** — one point-of-contact bot, not ten.
- Blake: "the imagination gap... the thing probably holding back your GrokBot is you thinking about what is actually possible... think outside the box."
- Blake: "start with context... there's so much that lives in your head... take that out of your head, give it to GrokBot."
- Blake: "keep your team lean. You don't need 45 bots... keep your team really specialized in what they need."
- Blake, on trust/verification of inter-bot claims: doesn't believe bots literally audit each other's outputs peer-to-peer; each bot has its own internal verification loop, and the chief bot (Gus) does a broader cross-check across all of them.
- Blake, self-improvement cadence: caps bot self-improvement suggestions to one/week to avoid being overwhelmed by "10 new bots to build."
- Dan Hill (Stripe/Link): **"when the agent gets blocked on you, it's when the fun kind of goes out of the experience... we want you to be in self-driving mode."**
- Dan Hill on consumer AI spend: **"the number of people paying more than $100/month for AI products has grown like 5x [this year]."** Stripe seeing rising interest in usage-based billing (via Metronome partnership) for AI companies, plus growing focus on fraud/risk tooling for AI-driven consumer products.
- Josh Kim: framing of AI maturity curve — **chat → co-pilots (still need babysitting) → bots/teams of bots (truly delegate, always-on, do it "the way you do it")**.
- Josh Kim: "scope your bots properly... it's almost like crafting a job description" — define swim lanes/responsibilities tightly so each bot stays specialized and efficient.
- Josh Kim: "trust your bots... they're ambitious, proactive, hungry... give them the access they need" (hook up Slack/email early, ask "what can you do for me").
- Josh Kim: "invest in your bots" — the more feedback/context/memory you give, the more they compound in value, "similar to how you might work with or manage a teammate."
- Roshan (mid-stream reflective aside): important discipline habit — periodically ask, "am I too much in the loop? How can I make my workflow more autonomous?" and even set up a bot/reminder to prompt that self-check.
- Roshan, end-of-day retrospective #1: hardest part of building anything (even with unlimited AI capability) is **"getting people to care"** / product-market fit — the team got easy adoption specifically *because* of livestream distribution, not because the product was intrinsically compelling yet.
- Roshan, retrospective #2: build a business around something you already know how to do well; naive assumption ("I'll just prompt models to make money") fails — a full day's autonomous "revenue agent" produced **$0** by end of stream (joked about as "the backup plan... in case it's all crash").
- Lauren, retrospective: discovering problems is still a human/organic task — "you have to go out as a human and discover all the problems organically. Once you figure out how to solve them, you can turn them into a bot and keep them running forever."
- Lauren, on restraint: with AI, "you can literally build anything you want... products with a million features that aren't any good... there's this discipline you now have to have" — cited deliberately cutting an early rock-paper-scissors/ELO mechanic and complex stat blocks/multiple-battlefield plans down to one clean auto-battler loop as what actually let them ship.
- Eric (visiting engineer): "I try to scope out the project and get all the context and align on what we're going to do, then have it send a bunch of cloud agents to build the thing" — pulls code locally into Cursor only to spot-check, otherwise stays fully in GrokBot chat.
- Eric on Kanban/PM tooling for bots: built a "Projects Manager" bot that spins up ephemeral per-project bots (researcher, coder, etc.) and tracks status on a Notion Kanban; "usually when it's blocked, it's because of a human somewhere," and bots can check whether the blocker has cleared.
- Running gag/opinion, several speakers: "cumulative graphs... they always go up and to the right" / "it's time to get funding" — self-aware joke about vanity metrics, but genuinely used the funnel and cumulative charts for real decisions (mobile vs desktop split, practice→sign-in conversion).

---

## 5. FAILURES, BUGS, LIVE INCIDENTS, WORKAROUNDS

- **Login-with-X down** right before cutting to first talk segment — acknowledged live, fixed off-camera during a break.
- **ELO/matchmaking bug:** players consistently matched against AI instead of real opponents, yet ELO scores still updated — investigated live via a bot ticket (potato mode + cloud agent investigation, no PR until root cause found); eventually reported fixed ("no longer seeing that it's AI... it's like one of the most reported bugs").
- **"Unknown bot" naming bug:** a bot card lost its name/ability display after purchase — visual bug, added to backlog live.
- **Gold-exhaustion soft-lock:** if you spend all your gold, you can get stuck unable to buy new bots ("you end up stuck because you cannot buy new bugs" — filed live as an issue).
- **No visible ability text in shop/lineup view on the new UI** — reported live via voice to engineer bot "Bake," fixed via PR mid-stream.
- **Ticker banner covering shop buttons** — CSS z-index/overlap bug; fixed live via a cloud agent.
- **Win/loss count mismatch** — leaderboard summary card showed different win/loss numbers than the detailed match history for the same player; filed live via voice call and a joke was demanded as proof-of-life ("SQL query walks into a bar…").
- **Leaderboard not clickable** — feature request/bug to let you click a username and view their match history; fixed live.
- **Sponsor/ad-bid auction feature launched broken** ("currently broken... nothing will happen if you submit"); fixed later; then when actually tested live, **file-upload/logo step failed on first attempt**, succeeded on retry; ad moderation was still broken at the very end ("moderation is broken, so we tried, we almost got there").
- **Production outage caused by their own factory:** "I actually brought down prod... a bad SQL query" from an autonomous fix — while literally mid-sentence talking about "restraint." Recovered and signups reopened shortly after.
- **Feedback/spam controls:** had to add a 20-character minimum on the feedback form after "getting some spam"; general moderation stack included client-side length checks, server-side profanity filtering, input sanitization against injection, xAI-model-based catch-all content guard, and rate limiting — some users reportedly hit 429s from testing the endpoint heavily.
- **Accidentally displayed a live API/Stripe token on stream** (Matt, showing the XAI voice-agent builder) — caught immediately, deleted the token, and moved on ("only half the value was shown," "no secrets in the chat — chat is for games and good vibes only").
- **Mobile layout was the single most-reported feedback category** (per Slack feedback triage chart: bugs ~71%, praise ~16%, rest requests). Fixed with a responsive pass shown live via Chrome device emulation.
- **Deployed changes forced re-login mid-demo** ("looks like we might have deployed some changes... I'm getting prompted to sign in again — engineering hard at work").
- General ambient acknowledgment throughout: "there's still some scrolling issues," "we know there are a lot of bugs and things to polish," and the team's stated philosophy — "if we're not embarrassed by it, then we've launched too early."

---

## 6. CONCRETE NUMBERS / METRICS / TIMELINE OF THE LAUNCH

- Overnight (pre-Day-3) PR count from the factory: 100+ → 145 → 150 → 160s → **168–170** by early morning; by end of day, **433 total PRs**, expecting to "clear 300" (i.e., cumulative well past 300, heading to ~450+).
- Launch time: **~10:00 AM Pacific**, via a single X post from a blank/default-profile-picture account (**@ThursdayArena**), domain **ThursdayArena.com**.
- Immediately post-launch: ~225–500 X followers within the first hour (225 mentioned once, later "we're at 476 followers," then "800 plus").
- Early usage snapshots (approx., as reported live over the day):
  - ~11:25 AM: ~2,200 practice rounds, ~1,000 X sign-ins; ~96–100+ leaderboard entries; "almost 500 users."
  - Mid-day: **over 1,000 X logins**, "well over 600 practice sessions" earlier, climbing; **3,000+ matches** within a few hours; **9 Platinum-tier players**, then first **Diamond-tier player** ("Ari the Monk," held #1 most of the day), later a **second Diamond player**.
  - "Launch hour" (~10 AM) cited as the single best hour: **1,908 games/sessions** benchmark ("1908 is the number to beat").
  - Early afternoon (~1 PM hour, partial): ~400–500 games/hour sustained.
  - By mid/late afternoon: **1,000+ users, 3,500 practice sessions, ~47% win rate** (one bot-generated one-liner summary).
  - Later afternoon: **~4,500 practice rounds, ~2,000 X logins**, **~5,000 total battles**; ~8% practice→X-signin conversion.
  - Final numbers (~4:15+ PM): **crossed 4,000 games**, **over 6,000 public matches**, **~30,000 page views**, ranked **#1 on Google** for the game's name, cumulative users approaching **2,000** (a production outage briefly blocked new signups near the end, so the final 2,000 threshold wasn't confirmed live).
  - Vercel Analytics (added mid-stream): ~17,000 page views at one check; ~44% iOS; roughly 50/50 mobile vs. desktop split; top referral sources X links, some direct, "8 people from Bing."
  - Contributor/commit stats: Roshan personally logged **157 commits**; total PR count **433** near end of day.
  - Feedback category breakdown (Slack triage chart, one snapshot): **71% bugs, 16% praise**, remainder mixed feature requests.
  - Monetization result: **zero real revenue** by end of stream; one **"theoretical" $1 test bid** placed live on the (broken) ad-auction feature just before sign-off — explicitly joked as "theoretical sponsorship dollars."

---

## 7. GAME MECHANICS / PRODUCT DETAILS (Thursday Arena)

- Genre: auto-battler / card drafting, explicitly compared to Magic: The Gathering, Yu-Gi-Oh, and "TFT"-style auto-battlers; art/cards generated with **Grok Imagine**.
- All in-game characters are real bots pulled from the **x.ai/bot marketplace** (~70 found initially), each given a randomly assigned rarity (common/uncommon/rare/epic/legendary), generated avatar, attack + HP stats, and a unique ability tied to its theme.
- Core loop: draft a 3-bot lineup using starting gold (renamed "tokens" mid-stream after feedback that "gold" felt off-brand), order them (front/back matters for many abilities), fight an opponent's lineup automatically (turn-based ability resolution), best of 3 rounds wins the match. Between rounds: shop refresh, buy/sell bots, buy power-ups (e.g., "apple" = +1/+1), "freeze" a card you can't afford yet to guarantee it next round.
- Matchmaking initially matched against a stored snapshot of another player's last lineup, falling back to AI when no snapshot was available — this underlay the "always playing AI" bug.
- Login: **Sign in with X** via **Clerk** (auth), with a **guest/practice mode** requiring no login. **PlanetScale** for the database; **Vercel** for hosting/serverless functions; backend written in **Go**; frontend responses validated client-side with **Zod** for type safety across the network boundary.
- ELO/ranked ladder with tiers (Bronze→Silver→Gold→Platinum→Diamond, possibly more later); public leaderboard.
- Feedback channels: in-app feedback form (behind auth, moderated), a phone number backed by an xAI voice agent, all flowing into a dedicated Slack channel monitored by triage bots.
- Planned/discussed but not fully shipped: sound effects/music (some prototyped via **Suno** the night before), 3D character/animation prototyping (also explored, not shipped), share-your-win / share-leaderboard-rank buttons with OG images, player-to-player direct challenges, sponsored/branded cards (as a non-pay-to-win monetization path), a "league"/subscription model spanning future games under a broader studio brand (possibly named "**Thursday**"), pay-for-leaderboard-placement / paid-ticker-ad features (partially shipped, broken at end), CSS "holo" card effects borrowed from an open-source Pokémon-card-style CSS library (credit: Simon Golner).
- Monetization stance, explicit and repeated: **no pay-to-win** (buying power/stat boosts) — considered and deliberately rejected multiple times across multiple guest conversations. Preferred directions: ads (ticker/stadium ad slots), sponsored/branded cards, merch, subscriptions (a "Thursday" all-games pass), partnerships with other game platforms/newsletters (e.g., "Morning Brew" name-dropped as an aspirational partner).
- Tech stack recap: Go + Vercel serverless backend, PlanetScale DB, Clerk auth, Zod validation, Vercel Analytics, Takumi (Rust OG-image generation library, akin to Satori) planned for dynamic leaderboard/share images, Cursor Cloud Agents for implementation/verification, Stripe (Link/Projects) explored for monetization plumbing.

---

## 8. ROADMAP / "COMING SOON" STATEMENTS

- GrokBot **voice mode**: announced day-of, rolling out "over the next few days."
- **1Password integration**: announced "just yesterday" (i.e., Day 2) — share password vault with a bot; bot can monitor/re-auth logins automatically.
- More payment/connector geographies for **Stripe Link** expanding beyond US.
- Team hinted (without confirming specifics) at forthcoming features to support **multiple humans' GrokBots collaborating/synergizing** ("we'll have something really exciting to address this pretty shortly" — audience joke: "we're just waiting for multiplayer... we want COD").
- No commitment on GrokBot-in-Tesla ("I can't answer that unfortunately... my parents have Teslas, so believe me, they're asking me that question too" — asked twice across the day, same non-answer both times).
- Team floated (not committed) giving away GrokBot Ultra subscriptions to top leaderboard finishers, pending internal approval — resolved by end of day as "we didn't get to that, but maybe."
- Discussed (not committed) building a reusable "game studio" meta-product / bot toolkit from the lessons of building Thursday Arena, to spin up future games faster.
- Marketing-demo bots shown by Josh Kim (market researcher, product marketer, website ops, performance marketer, marketing analyst, project manager) were stated to be getting refined and pushed to the public bot marketplace ("they will be" available).

---

## 9. NAMED PEOPLE AND BOTS — QUICK REFERENCE

**Humans (build team + guests), roles:**
- Roshan (roshan_s) — product, SpaceX AI; main game/product host.
- Lauren — sets up the "factory," Pstack/Potato Mode creator/owner, backend & bot-orchestration lead.
- Matt (Matt Palmer) — feature/UI work, voice-agent demo, ads/monetization feature work, emoji tool builder (emoji.mattpalmer site).
- Eric — visiting Cursor/engineering teammate for final hours; UI polish, animations, GitHub write-access onboarding.
- Vincent Zhu — SpaceX AI growth team guest; growth-loop ideation session.
- Matthew — SpaceX AI marketing ops / RevOps guest (distinct person from build-team "Matt"); demoed self-completing task list + "dating app for leads" internal tool.
- Blake — AI Deployment Manager, post-sales guest; demoed Gus/Frankie/Wally/Trudy/Scout/account-bots system.
- Dan Hill (Dan Hill Tech on X) — Stripe, works on Link; demoed Link purchases, Stripe Projects, financial insights.
- Josh Kim — SpaceX AI marketing guest; full end-to-end marketing-campaign-bot-team demo (XAir fictional product).
- Cal Day — video testimonial guest (SVP product/engineering, Nokia-context division) on using Cursor agents for large legacy codebases (~50M+ LOC) — root-cause analysis, decomposition of a monolith, multi-agent orchestration ambitions. (Not a live-studio guest — pre-recorded clip.)
- "Teej" — production team member, cameo (bought his own shoes via GrokBot too).

**Named bots (game/factory team):**
- Steve (chief of staff/orchestrator, briefly "Steve-N")
- Play / Chrome (playtester/QA bot)
- Dr. Eggbot (bot-that-creates-bots)
- Crumble (triage bot)
- Hashbrown (validation bot for triage accuracy)
- Bake (founding engineer bot; voice-called live)
- Crit (game design critique bot)
- Grind / Cheater (auto-play/leaderboard-farming bots)
- Vincent (growth-ideas-logging bot, named after guest)
- Cerebro (ICP/growth-research bot, "FindMyICP" skill)
- data scientist bot (unnamed) — dashboards every 15 min

**Named bots (guest demos, illustrative not part of game):**
- Gus, Frankie, Wally, Trudy, Scout, Harbor/Northwind/Brightline (Blake's team)
- OP1 (chief of staff, "synthesizer"-themed), Fisher (inbox/receiver agent), Juno (product manager bot), Owen ("Owned," engineer bot) — Matthew's team
- market researcher, product marketer, website ops, performance marketer, marketing analyst, project manager — Josh Kim's marketing team (XAir demo)
- "Ariel"/"AIREAL" — an audience member's OpenClaw-based personal agent, referenced but not part of GrokBot.

**Leaderboard notables mentioned live:** Ari the Monk (#1 most of the day, first Diamond player), Ben J. Bush (briefly #1), Nicholas Cech (briefly #1), Dev Arminas (2nd Diamond player) — all real playtesters/stream viewers.

---

## 10. NARRATIVE ARC OF DAY 3 (chronological)

1. **Cold open / promo #1** — free month of GrokBot for new signups (10-min window) while recapping the prior two days.
2. **Recap of overnight "factory" work** — Lauren explains Potato Mode/Pstack, swarm skill, Play/Chrome QA bot; PR count callouts (100→170ish overnight).
3. **First game preview** (still pre-launch) — walkthrough of the "Cupcake"-codenamed card battler; visible UI rawness acknowledged.
4. **Plan for the next hour off-camera**: Lauren → backend security/load testing; Matt → UI polish + user-feedback loop; Roshan → same, plus revisiting audio (Suno tracks) and 3D-prototype stretch goals.
5. **Cut to main stage talk**: GrokBot for RevOps/MarOps (Matthew) — self-completing task list demo, "dating app for leads" internal tool case study (2 weeks idea→launch, 10 hours actual build time), audience Q&A on WhatsApp/Meta connectors (answer: no native connector yet, but 1Password + generic-computer-use workaround), roadmap teasers.
6. **Back in studio**: DNS/CORS/Clerk production-auth debugging discussed candidly as "glue work"; launch-checklist built live in Notion; team debates polish-vs-ship, decides to launch as an explicit "first play test" with lowered expectations.
7. **LAUNCH** (~10:00 AM Pacific): first X post from @ThursdayArena, blank profile picture; QR code and URL shared; immediate signups tracked live; early bugs found in real time (unknown-bot naming bug, gold-lock bug); leaderboard climbs and falls comically among the hosts themselves.
8. **First metrics/dashboards segment**: Roshan's data-scientist bot produces funnel/hockey-stick charts; win/loss ratio found too AI-favored (~41.8% loss rate for humans) — flagged as a game-balance issue for the "game designer critique" bot.
9. **ELO/matchmaking bug investigation** — narrated live end to end (report → potato-mode investigation → no PR without root cause → eventual fix later in the day).
10. **Feedback pipeline build-out**: Slack channel for user feedback; moderation/sanitization discussion; triage-bot ("Crumble")/validation-bot ("Hashbrown") chain established; first categorized feedback chart (71% bugs / 16% praise).
11. **Guest: Vincent Zhu (Growth)** — full growth-ideas riffing session while playing the game live; captured via voice dictation into a "Vincent" bot/Notion growth playbook; stack-ranked ideas by impact/effort.
12. **Promos #2 and #3**: "reset" in chat for existing-user limit resets; new 15-min new-user free-month window.
13. **Guest: Matthew (Marketing/RevOps, SpaceX AI)** — reprise/expansion of self-completing task list concept; walks the game with Roshan; discusses ads vs. subscriptions vs. partnerships; introduces Cerebro bot and FindMyICP skill live, builds a full ICP → segments → personas → partner-outreach pipeline on stream, capped by a simulated Clay/Ample Market company-search + outbound-email flow.
14. **Cut to main stage: GrokBot for Post Sales (Blake)** — AI maturity curve (chat→copilot→bots→teams of bots); Gus/Frankie/Wally/Trudy/Scout/account-bot system; live demos: bot joins a Google Meet call and reports takeaways, post-call follow-up pack auto-drafted (email/Slack/ROI doc), "where are we at with Harbor" (status+joke) pattern, staff-meeting decision-making demo, voice-memo onboarding method, self-improvement scan routine; extensive audience Q&A (trust/autonomy boundaries, hallucination on long dictated prompts, org-chart-of-bots, tech debt from bot sprawl, personalization/avatars, migration from other agent tools, cost).
15. **Back in studio**: dashboards recap (page views, funnel, mobile/desktop split, cumulative growth); GrokBot **voice mode** live demo (calling "Bake" to check/merge PRs); UI overhaul walkthrough (new card designs, responsive/mobile fixes, leaderboard redesign, past-match history, share-win feature); live bug fixes narrated one after another (ability visibility, ticker overlap, win/loss mismatch, leaderboard click-through).
16. **Guest: Dan Hill (Stripe/Link)** — payments-and-agents discussion (parking tickets, flights, shoes, Tesla preorder, charity-penalty automations, Postal Form physical mail, Stripe Projects infra provisioning); attempted live purchase demo (blocked by passkey/profile issue); monetization brainstorm for the game (ads, pay-for-cosmetic-power avoided, sponsored characters, subscription/league idea, usage-based billing trend commentary, AI-subscription-spend growth stat).
17. **Cut to main stage: GrokBot for Marketing (Josh Kim)** — AI maturity curve reprised; full live build of an end-to-end marketing campaign for a fictional airline product "XAir" using a 6-bot marketing team (market research → positioning brief with Google Docs comment-loop → landing page PR → ad campaign shell → analyst readout → final "project manager" bot automating and owning the whole flow going forward); Q&A on bot personalization/avatars, cross-tool integration with Grok CLI, EU data-privacy handling, bot sprawl/tech debt, combining multiple marketplace bots into one custom bot.
18. **Guest: Eric joins in person** for the final build stretch — UI/animation polish, PR/GitHub write-access setup, discussion of Cursor Projects vs. GrokBot-centric coding workflow, no-comments coding discipline (Eric doesn't know the game codebase; Lauren enforces stricter no-comments rule on the main GrokBot product but not as tightly here).
19. **Final promo (#4)**: "credits" in chat, 5-minute window, $200 GrokBot credits.
20. **Final metrics pull**: cumulative charts, page views (~30k), Google #1 ranking, near-2,000 cumulative users, a mid-recap **production outage caused by their own bug-fix factory** (bad SQL query brought prod down, quickly fixed).
21. **Closing retrospective** (all hosts): lessons on PMF being harder than building, building businesses around known domains, restraint/feature discipline, bots covering knowledge gaps, treating bots like a team you invest in, and the enduring human role (vision-setting + relentless execution + relationship-building).
22. **Sign-off**: final live "theoretical" ad-bid/monetization test (logo upload, $1 bid — ends up mostly broken/unmoderated but framed as "our first theoretical sponsorship dollar"); parting one-liners ("have fun using GrokBot," "eat more potatoes," "smash more PRs"); stream ends.
