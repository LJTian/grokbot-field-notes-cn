# VERIFICATION.md

**Use when:** setting up a project so agents can check their own work, or when
an agent keeps finishing tasks with "you can run it and tell me if it works."

That sentence is the symptom. This file is the cure.

---

## Why this is the first thing to build

Without a verification loop, every task ends in a round trip through you. You
become the test suite. With one, the agent closes its own loop and you only see
finished work.

The general test for whether a job is safe to hand to an agent at all:

> **Is the loop verifiable?** Is there a signal, readable by a machine, that
> says this succeeded or failed?

Coding is the easy case — tests, builds and a running app all produce that
signal. Anything without one needs a signal invented before autonomy is safe.

---

## What a verification skill actually contains

### 1. A CLI the agents can drive

Not ad-hoc scripts written fresh each time. Those cost tokens, differ between
runs, and cannot be reasoned about.

> "You want a CLI, or a script, or some tool that allows the bots to reliably
> and deterministically interact with your application. I'd rather it just have
> a standard set of tools."

Build one command per meaningful action, with stable names and stable output:

```
./verify seed              # put the app in a known state
./verify run <flow>        # exercise a named flow end to end
./verify screenshot <page> # capture proof
./verify check             # assert invariants, exit non-zero on failure
```

Rules for the CLI:
- deterministic — same input, same result
- exits non-zero on failure, always
- prints what it did, not just whether it passed
- safe to run repeatedly

### 2. A feature map

A machine-readable description of what the app has and how to get there, so an
agent navigating it doesn't guess.

```yaml
# feature-map.yaml
checkout:
  path: /checkout
  requires_auth: true
  entry: click "Buy" on any product page
  flows:
    - happy_path: add item -> checkout -> pay -> confirmation
    - declined_card: add item -> checkout -> pay(declined) -> error state
  invariants:
    - order total always equals sum of line items
    - no order is created before payment succeeds
```

Consider also shipping an agent-readable version of your product's own rules —
a `/rules` page, or an `llms.txt`-style endpoint. If agents are going to use
your product, document it for them the way you document it for humans.

### 3. Named invocation

Give it a name and use the name. Something like `/verify <project>`. Once it
exists, cite it in every instruction that grants autonomy:

> "...using autopilot. Since we are now live in production, it is critical that
> we do not break this for everyone. So always rigorously verify with
> `/verify <project>` before merging."

---

## The three rules to enforce

1. **Reproduce before you fix.** Only once the agent can reproduce the bug can
   you trust that it understood the problem. Standing instruction:

   > *"Before writing any code, run the app, find the exact bug and behaviour,
   > and then proceed."*

2. **Proof goes in the PR.** Screenshots or video for UI. Numbers for backend.
   The reproduction, then the same steps passing, for bug fixes. Agents that
   can record their own runs should attach the recording.

3. **Verification is the merge gate.** Not a human reading the diff. That is
   what makes throughput possible — but see the caveat below.

---

## Fuzzing and swarms

Once the CLI exists, you can point many agents at it in parallel: each runs the
app, clicks around, and tries to break it. This finds a different class of bug
than a human does, and costs you nothing but tokens.

Two things to know:
- humans still find bugs the swarm misses, and vice versa — run both
- a fuzzing run does **real work** against whatever it is pointed at. Point it
  at a disposable environment, never production

---

## The caveat, stated honestly

Auto-merge on green is appropriate in proportion to blast radius.

The team that shipped 433 PRs this way said plainly: *"To be entirely honest, I
didn't look at the code at all."* That was a 72-hour throwaway game. On the
actual product, the same team reads every PR and enforces anti-pattern rules by
hand.

Set the autonomy level from the cost of being wrong, not from how well the loop
has been working lately. And keep a human gate on migrations and deploys
regardless — an autonomous fix took their production down with a bad SQL query
mid-stream.

---

## Checklist

- [ ] There is one command that puts the app in a known state
- [ ] There is one command that exercises each critical flow
- [ ] Every command exits non-zero on failure
- [ ] There is a feature map, and it is current
- [ ] The skill has a name, and instructions cite it by name
- [ ] Fuzzing runs against a disposable environment
- [ ] Migrations and deploys still require a human
