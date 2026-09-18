# Playbooks

Nine role-based workshops from the three days, one file each. Every session
was an xAI employee showing the bots they actually run, live, on a demo
company. Each playbook has the same shape:

**the team** (who owns what, connected to what) → **the workflow as it ran on
stream** → **the prompts, verbatim where the transcript allows** →
**routines and cadences** → **numbers** → **what they said they learned** →
**copy this** (a setup checklist).

These are the most directly copyable thing in the repo. The guide compresses
six of them into three paragraphs each; here they get the full treatment.

---

## The nine

| Playbook | Who ran it | Day | The one idea |
|---|---|---|---|
| [`engineering.md`](engineering.md) | Ling Shi, engineer | 1 | A playbook-owner bot broadcasts standards; P0 defined once; nightly cleanup with proof-gated merge |
| [`product-management.md`](product-management.md) | Kevin De Parco + Roshan, product | 1 | Data → spec → design → EM decomposes → cloud agents, with the bot correcting the humans' read of the funnel |
| [`founders.md`](founders.md) | Shub, founder success | 1 | Four bots for four founder jobs; compound, don't discard; audit routine frequency |
| [`sales-engineering.md`](sales-engineering.md) | Amrita, field engineer | 2 | A repo-expert bot and a competitor bot that argue in a group chat; teach a task by recording |
| [`sales.md`](sales.md) | Krista + Mark Wright, GTM | 2 | Prospecting with personal hooks from X; a bot that watches the webinars for you; CRM updates from transcripts |
| [`sdr.md`](sdr.md) | Simon, SDR | 2 | Chief of staff first, build everything through it; one bot per platform; an army of low-context sub-bots |
| [`customer-support.md`](customer-support.md) | David, user ops | 2 | Crawl → walk → run; public / internal / process KB split; traces and evals tables; $0.20–$2 per ticket |
| [`post-sales.md`](post-sales.md) | Blake, AI deployment | 3 | One bot in front, nothing else pings you; voice dump to bootstrap; weekly self-improvement capped at one suggestion |
| [`marketing.md`](marketing.md) | Josh Kim, marketing | 3 | Six bots run a campaign to prod; then a PM bot learns where you intervened and takes over |

Not included: the day-3 RevOps / MarOps talk (Matthew, "build tools, not
rules"). It's covered in [`../notes/day-3-notes.md`](../notes/day-3-notes.md)
and the transcript; it wasn't one of the nine role workshops.

---

## What every session said

Read across the nine, the same rules come up in different vocabulary. If you
only take the intersection:

1. **One bot, one job.** Every presenter. Scope it like a job description.
   Split when scope grows, not before.
2. **One bot you talk to.** Simon, Blake, Josh, Ling, Kevin all end up with a
   chief-of-staff / point-of-contact bot and specialists behind it. Shub is
   the lone dissenter — he prefers talking to experts directly — and calls
   it personal preference.
3. **Build the specialists *through* the chief** so it knows who does what.
   (Simon, most explicitly.)
4. **Say it once.** Ling's playbook chain, Blake's self-improvement scan,
   Shub's "sink one level further," Roshan's "when it thinks wrong, build a
   skill." Repeating a prompt is the signal that a rule or routine is missing.
5. **Voice first.** Krista, Simon, Shub, Blake all train a voice bot on real
   sent mail before letting anything go out. Simon's recipe is the most
   precise: in-territory, positive-response, recency-weighted, then critique
   until nothing looks templated.
6. **Drafts, then sends.** David's crawl → walk → run; Blake's "drafts only,
   never send"; Josh's "start small and low-risk." Writes are earned.
7. **Routines: fewer than you think.** Krista: once or twice a day. Blake:
   three 15-minute routines is hundreds of messages a day. Shub: every 15
   minutes is 100 runs a day; use webhooks. Kevin: on a no-op, say nothing.
8. **Bots talk to bots; you get pinged when it matters.** Threads between
   specialists shouldn't light up your sidebar.
9. **Let it use the product.** Serena books a Southwest flight. ProdBot walks
   the site. Reply reads the actual ticket. Craig clicks through
   flyloair.com. The bot's own computer is the verification loop.
10. **Ask the bot to design the bots.** "What bots would help you?" (Amrita),
    "help me build a system" (Blake), "where are our bottlenecks?" (Lauren,
    in the build sessions).

---

## Bots by name, across sessions

Useful when a name comes up in the notes or transcripts and you want the
session it belongs to.

| Bot | Session | Role |
|---|---|---|
| Craig / Ling Xixi, Cray, Steve, Hogan1QR, Jenny | engineering | chief, UI, DevX, infra, playbook owner |
| Cora, Emily, Einstein/Igor/Nova/Larry/Eileen, Ashley, PMP/Pete, Pixel, Ray | product-management | chief, EM, engineers, data, spec, design, recruiting |
| CloseBot, ProdBot, StockBot, ProtoBot, YapBot, misc | founders | customers, product state, competitors, feedback→PR, voice, trash can |
| Mimi, Sherlock, Serena Williams, Battle Card Blair, Demo Drake, AI Radar | sales-engineering | slides, repo expert, competitor tester, and three spawned by Sherlock |
| Olive, PG, Echo, Customer Expert, Engineer | sales | chief, prospecting, live deck, account plan, technical answers |
| Simon-bot, Shakespeare, Web Search, Simon soldiers, Customer, PLG, Ample Market, Company research, Inbox manager | sdr | chief, email voice, research, army, VoC, usage, enrichment, stack/org, triage |
| Build, Reply, Alert, Tune | customer-support | infra, tickets, escalation, self-improvement |
| Gus, Frankie, Wally, Trudy, Scout, Franny, Harbor/Northwind/Brightline | post-sales | chief, follow-ups, voice, source of truth, radar, forms, per-account |
| market researcher, product marketer, website ops, performance marketer, marketing analyst, project manager | marketing | the campaign team |

---

## Caveats

- **Flylo, XAir, Northwind, Harbor, Brightline, Craft** are demo companies
  and accounts. Prices, metrics and ticket contents in those demos are
  fabricated for the stage.
- Prompts marked verbatim are as the auto-captioner heard them; dictated
  prompts were lightly repunctuated. Where a prompt is reconstructed from
  narration it's marked paraphrased.
- Product names in the captions are mangled (GrokBot / Rockbot / Brockbot /
  Grock-Bot; "SpaceX AI"). They're normalised here.
- Every number was stated live and was a moving target on the day.
