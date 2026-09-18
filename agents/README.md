# Agent Pack

Drop-in rules for coding and orchestration agents, distilled from three days of
the xAI Grok Bot team building and launching a product live on stream.

Not product documentation. These are the working practices — what they actually
did under time pressure, including the parts that broke.

---

## What's in here

| File | Use it when |
|---|---|
| **`../AGENTS.md`** | Always. The core rules for an agent working in a repo. Start here. It lives in the repo root so agents pick it up automatically. |
| **`VERIFICATION.md`** | Setting up a project so agents can check their own work. The highest-leverage file in the pack. |
| **`ORCHESTRATION.md`** | You're designing a *team* of agents, not prompting one. |
| **`SKILLS-AND-ROUTINES.md`** | You want an agent to stop needing the same instruction twice. |
| **`PROMPTS.md`** | You want the phrasing that actually worked. Patterns plus a copy-paste library. |

Pick what you need. `AGENTS.md` stands alone; the files in this folder are the
references it points at.

---

## Install

**Claude Code** — drop `AGENTS.md` (or `CLAUDE.md`) in your repo root. Put this
folder in `.claude/` or `docs/agents/` and reference it from the core file.

**Cursor** — `AGENTS.md` in the repo root, or split the sections into
`.cursor/rules/*.mdc`.

**Codex / Copilot / Windsurf / Cline** — `AGENTS.md` in the repo root is read by
most of them. Check your tool's docs for the exact filename it expects.

**Any agent with a system prompt** — paste `AGENTS.md` in. It's written to be
read cold, with no other context.

---

## Adapt before you ship it

This pack is opinionated on purpose. Two things to change for your own setup:

1. **Set the autonomy level from your blast radius.** The throughput numbers
   behind these practices came from a 72-hour throwaway project where nobody
   read the code. The same team reads every PR on their real product. Read
   `VERIFICATION.md` → *The caveat, stated honestly* before granting
   auto-merge.

2. **Fill in your own verification commands.** `VERIFICATION.md` describes the
   shape of the loop, not your specific CLI. Nothing else in the pack works
   properly until that exists.

---

## The one-paragraph version

Give each agent one narrow job and a name. Build a verification loop before you
build the second agent. Make the agent reproduce a bug before it fixes one, and
attach proof to everything. When it's wrong, write down the general principle —
never the specific story. Audit your routines weekly, because frequency is where
the money goes. Keep a human gate on migrations, deploys, money and permissions,
however well the loop has been working.

---

## Provenance

Assembled from transcripts of three consecutive livestreams (~24 hours of
material) in which three people built and shipped a product from an empty repo
using their own agent platform. Quotes are theirs. Figures were stated live and
were moving targets on the day.

The companion PDF in `../guide/` covers the same material as narrative,
including the case study, the failure log and the economics. Structured extraction notes are in `../notes/`.
