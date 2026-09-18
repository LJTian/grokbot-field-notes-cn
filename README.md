# Grok Bot Field Notes

Everything useful extracted from three consecutive livestreams in which the
xAI Grok Bot team built and launched a product from an empty repo — live, in
72 hours, using their own agent platform.

Roughly 24 hours of material, turned into things you can actually use: a
designed guide, drop-in rules for your own agents, and the raw source so every
claim is checkable.

---

## What's here

| Path | What it is |
|---|---|
| **`AGENTS.md`** | Drop-in house rules for a coding agent. Put it in your repo root and your agent reads it. |
| **`agents/`** | The deeper references `AGENTS.md` points at — verification, orchestration, skills and routines, prompts. |
| **`playbooks/`** | Nine role-based workshops — engineering, PM, founders, sales engineering, sales, SDR, support, post-sales, marketing. Each one: the real team of bots, the workflow as it ran, the prompts, the routines, the numbers. |
| **`guide/`** | *Grok Bot Guide by SpaceX Engineers* — a 24-page designed PDF covering the whole three days as narrative: mental model, software factory, case study, failure log, economics. |
| **`notes/`** | Structured extraction notes, one per day. Product facts, workflows, verbatim prompts, failures, numbers, roster, chronology. This is the working source everything else was built from. |
| **`transcripts/`** | The raw transcripts. Cleaned plain text, plus the original timestamped SRT for day 2. |

## Start here

- **You want rules for your agent right now** → copy `AGENTS.md` into your repo root.
- **Your agents keep asking you to test their work** → `agents/VERIFICATION.md`. Highest-leverage file in the repo.
- **You're designing a team of agents, not prompting one** → `agents/ORCHESTRATION.md`.
- **You want the phrasing that actually worked** → `agents/PROMPTS.md`.
- **You want to set this up for your own role** — support, sales, marketing, PM… → `playbooks/`. Start with `playbooks/README.md`.
- **You want the whole story** → `guide/`.
- **You want to check a claim or dig for something I missed** → `notes/` then `transcripts/`.

---

## The one-paragraph version

Give each agent one narrow job and a name. Build a verification loop before you
build the second agent. Make the agent reproduce a bug before it fixes one, and
attach proof to everything. When it's wrong, write down the general principle —
never the specific story. Audit your routines weekly, because frequency is where
the money goes. Keep a human gate on migrations, deploys, money and permissions,
however well the loop has been working.

---

## Roadmap

There is a lot still sitting in the transcripts. Ranked by how much material
exists and how useful it would be.

### Done

- [x] **`playbooks/` — nine role-based workshops.** One file per session:
      the team of bots, the workflow as it ran on stream, the prompts, the
      routines, the numbers, and a copy-this checklist. See
      `playbooks/README.md` for the cross-session patterns.

### Next up

- [ ] **`roster/` — a catalog of agent roles.**
      Forty-plus named agents are described across the three days with real
      roles: chief of staff, triage, triage validator, playtester, voice/tone,
      one-per-account, self-improvement scan, comment cleanup, data scientist,
      ICP researcher. One file per role: what it owns, what it explicitly does
      *not* own, its source of truth, what needs approval, and a ready-to-paste
      role description with placeholders. The thing people take out of a repo
      most often.

- [ ] **`ANTIPATTERNS.md` — the full failure log.**
      Ten made it into the guide; there are roughly twenty-five distinct
      failures in the transcripts. Format: what broke → why → the rule it
      produces. Cheap to build and usually the most-read file in a repo like
      this.

### After that

- [ ] **`reference/PRODUCT.md`** — features, limits, memory semantics, what
      does and doesn't transfer when a template is shared. A dated snapshot.
- [ ] **`reference/INTEGRATIONS.md`** — every connector named on stream, plus
      the rule for when to use a connector versus driving a browser.
- [ ] **`reference/STACK.md`** — what they actually built with and why:
      Go, Vercel, PlanetScale, Clerk, Zod, Remotion, Strudel, Suno, tldraw.
- [ ] **`reference/ECONOMICS.md`** — every cost and metric quoted, in one place.
- [ ] **`case-study/`** — the full Thursday Arena build log plus a three-day
      chronology: what was announced when, what broke when. The guide condenses
      this to two pages; there is four times as much.
- [ ] **`guide/src/`** — the HTML and CSS the PDF is generated from, so the
      layout can be reused for other documents.

---

## Notes on the material

The transcripts are auto-captioned, so the product name appears as "GrokBot,"
"Rockbot" and "Brockbot," and the company as "SpaceX AI." They all mean the same
thing.

Every figure was stated live and was a moving target on the day. Features and
limits are as described during the streams and will have changed since. Treat
the reference material as a shape, not a specification — check anything
load-bearing against current documentation before building on it.

Quotes belong to the people who said them. Links to the original streams are in
`transcripts/README.md`.
