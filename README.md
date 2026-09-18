![Grok Bot Guide by SpaceX Engineers](guide/cover.png)

# Grok Bot Field Notes

The xAI Grok Bot team built and launched a product from an empty repo in 72
hours, live on stream, using their own agent platform. This repo is what I
pulled out of those three days: a designed guide, rules you can drop into
your own agents, nine role playbooks, a catalogue of bot roles, and a log of
everything that broke.

## What's here

| Path | What it is |
|---|---|
| `AGENTS.md` | House rules for a coding agent. Put it in your repo root and your agent reads it. |
| `ANTIPATTERNS.md` | Forty things that broke on air. Each one: what broke, why, and the rule that came out of it. |
| `agents/` | The longer references `AGENTS.md` points at: verification, orchestration, skills and routines, prompts. |
| `roster/` | Sixty-nine agent roles, one file each. What the role owns, what it doesn't, where it gets its facts, what needs approval, and a description you can paste. |
| `playbooks/` | Nine role workshops: engineering, PM, founders, sales engineering, sales, SDR, support, post-sales, marketing. Each has the team of bots, the workflow as it ran, the prompts, the routines and the numbers. |
| `guide/` | *Grok Bot Guide by SpaceX Engineers*, a 24-page PDF that tells the three days as a story: mental model, software factory, case study, failure log, economics. |
| `notes/` | Structured notes, one per day. Product facts, workflows, prompts, failures, numbers, who was who. Everything else was built from these. |

## Where to start

- You want rules for your agent now: copy `AGENTS.md` into your repo root.
- Your agents keep asking you to test their work: `agents/VERIFICATION.md`.
- You are designing a team of agents rather than prompting one: `agents/ORCHESTRATION.md`.
- You want the wording that worked: `agents/PROMPTS.md`.
- You want a bot's job description to paste: `roster/`, starting with `roster/README.md`.
- You want a setup for your own role, say support or sales: `playbooks/`, starting with `playbooks/README.md`.
- You want to know what goes wrong: `ANTIPATTERNS.md`.
- You want the whole story: `guide/`.
- You want to check a claim: `notes/`.

## In one paragraph

Give each agent one narrow job and a name. Build a verification loop before
you build the second agent. Make the agent reproduce a bug before it fixes
one, and attach proof to everything. When it's wrong, write down the general
principle, never the specific story. Audit your routines weekly, because
frequency is where the money goes. Keep a human gate on migrations, deploys,
money and permissions, no matter how well the loop has been working.

## Roadmap

### Done

- [x] `playbooks/`: nine role workshops, one file per session.
- [x] `roster/`: sixty-nine roles with paste-ready descriptions.
- [x] `ANTIPATTERNS.md`: the full failure log, grouped by cause.

### Next

- [ ] `reference/PRODUCT.md`: features, limits, how memory works, what does
      and doesn't transfer when a template is shared. A dated snapshot.
- [ ] `reference/INTEGRATIONS.md`: every connector named on stream, and when
      to use a connector versus driving a browser.
- [ ] `reference/STACK.md`: what they built with and why. Go, Vercel,
      PlanetScale, Clerk, Zod, Remotion, Strudel, Suno, tldraw.
- [ ] `reference/ECONOMICS.md`: every cost and metric quoted, in one place.
- [ ] `case-study/`: the full Thursday Arena build log and a three-day
      timeline of what was announced and what broke, and when.
- [ ] `guide/src/`: the HTML and CSS the PDF is generated from, so the
      layout can be reused.
