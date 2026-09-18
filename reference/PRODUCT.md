# PRODUCT.md

The parts of Grok Bot that change how you design a bot. Not a feature list;
the marketplace and xAI's own docs are the source of truth for those. This is
a snapshot of what was said on stream in September 2026, kept to the things
that affect memory, isolation, sharing and permissions. Where speakers
contradicted each other, the resolution is noted.

---

## The model

A bot is a named colleague with one job, not a chat thread. You come back to
the same bot. It has its own memory, its own context limit, and its own
computer. Every design rule in this repo follows from those three facts.

---

## Memory

- Per-bot, long-lived, editable. Stored in S3. Nothing is shared between bots
  unless one messages another.
- Steering sticks. "Never use my last name" said once is kept forever.
- You can tell a bot to forget something and it does. Do it: memory it no
  longer needs costs tokens on every turn.
- Each bot has its own context limit. That is the reason to split roles rather
  than grow one bot: a bot switching between too many tasks runs out of
  context, a narrow one doesn't.
- Multitasking inside one thread works; a bot holds two asks at once without
  dropping the first.

---

## What transfers, and what doesn't

Three operations sound similar and behave differently.

| Operation | Instructions | Memory | Skills | Credentials, chat history |
|---|---|---|---|---|
| **Duplicate** a bot | copied | **empty** | shared anyway | no |
| **Share as template** (team or public) | copied | core memory copied, workspace-specific data stripped | copied with first-party plugins | no |
| **Teach a skill** in any bot | — | — | **available to every bot in the org** | — |

Day 1 said sharing copies "memories, context, instructions, first-party
plugins"; day 3 said it "strips sensitive and workspace-specific info, keeps
core memory." Both hold: the template carries what the bot knows about its
job, not what it knows about you.

Consequence: put job knowledge in the description and skills, not in memory
accumulated through chat. Memory is what you lose on duplicate and what gets
filtered on share.

---

## Isolation

- Each bot runs on its own Linux VM. One bot cannot touch another bot's
  computer. Two bots editing different slides of the same deck don't collide.
- Bots on one account share a file system but not memory or context.
- Cross-account bot-to-bot messaging did not exist as of the stream.
- Local execution is a per-account toggle. The team's bias is the cloud VM:
  parallelism, nothing stealing focus on your laptop, keeps running when the
  lid is closed.

---

## Permissions

- A built-in classifier rates each action and asks before risky ones. On
  stream it refused to build a form until it had checked the form wasn't
  collecting PII.
- You layer explicit rules on top, per action type: "never send email without
  asking", "create slides freely", "deploy to production: always ask first."
- Enterprise admins can whitelist and blacklist sites and MCPs per bot.
- Credentials go through a secure form or 1Password. The bot never sees the
  password; neither does xAI. A demoed competitor printed passwords in plain
  text.
- You can take over a bot's screen for logins and CAPTCHAs. The recommended
  answer to CAPTCHAs is to block the site, not to evade the check.

---

## Description is the system prompt

The description field is the bot's persona and instructions in one. A
bot-factory bot writes it for new bots and tends to overfit it to the one
scenario it was created for; correct that early. Labels are cosmetic tags for
remembering what "Tater" does.

---

## Limits that bit on stream

- Linux only. A tool that is neither Linux-compatible nor exposed as an MCP
  cannot be used at all.
- Multi-machine bots got confused, acknowledged as being fixed.
- Voice was transcribe-only on day 1, two-way by day 3.
- No migration path from other agent tools beyond importing templates and
  pointing a bot at an existing context.
- Group chats work but every bot answers every message. See `ECONOMICS.md`.
