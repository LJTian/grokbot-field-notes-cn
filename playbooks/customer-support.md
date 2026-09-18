# Customer Support

**Session:** GrokBot for Customer Support — day 2
**Ran by:** David, software engineer in xAI's user-ops org.

Demo-heavy and the most operational of the nine: a ticketing system, a
knowledge base with public and internal sections, an SOP, Stripe, Slack, and
four bots working real tickets end to end — including executing a refund.

His caveat, twice: "The whole product is still so new. I don't think there's
one meta or one clear playbook. Make the bots fit into how you work, not vice
versa."

---

## The team

He is explicit that you should **not** start with four bots. Start with one
bot with a generic name, teach it one workflow, and split when scope grows or
you need two running at once. This is where he ended up:

| Bot | Job | Connected to |
|---|---|---|
| **Build** | Setup and infrastructure. Installs connectors, creates the evals and traces tables | Plane, Notion, Supabase (Postgres), Slack |
| **Reply** | Answers tickets in the ticketing system and questions in Slack, following a written process | Plane, Notion, Stripe, Slack |
| **Alert** | Pinged by Reply when something needs a human now. Posts in a Slack alerts channel and tags him | Slack |
| **Tune** | Self-improvement. Updates the knowledge base (with approval). Reviews last week's tickets for what could have gone better | Notion, traces |

Demo company: Flylo again. One SKU to keep it simple: an in-flight Wi-Fi
subscription, $20/month, billed monthly.

---

## The knowledge base (Notion, for the demo)

Three sections, and the split matters:

1. **Public docs** — what a user could find by searching: product, auth,
   billing, FAQ. Reply may quote these.
2. **Internal policies** — what a human billing agent should know but the
   public shouldn't see. The refund SOP: *subscribed ≤ 14 days → approve,
   cancel, refund. > 14 days → deny.*
3. **The agent's process** — the loop Reply runs on every ticket, which he
   told it to re-read every time so edits take effect immediately:

   > Read the ticket → look for the knowledge → decide: reply or hand off →
   > act → leave a note.

Add a step 7 to the process doc and it's live on the next ticket.

---

## The crawl → walk → run ladder

"It can be scary to let an agent reply to your customers. Build up to it."

1. **Crawl** — read tickets only. Summarise, name the root issue, maybe draft
   a response *for you.*
2. **Walk** — add the draft as an **internal note** on the ticket. You see it
   before anything goes out.
3. **Run** — reply to the user, and take real actions (Stripe).

Orthogonal to that: **read-only first, writes later, and per-bot
permissions.** One bot may post to Slack automatically; another must ask.
The knowledge base is the thing he keeps human-gated even at "run": if a
wrong entry goes out and 100 people ask the same thing, that's an incident.

---

## The four tickets, as run

**Alex — "I forgot my password."** Basic.

> Hi, can you reply to Alex in Plane?

Reply followed the loop and left a **thinking note** on the ticket: *can
reply with high confidence; root issue; source referenced* — then replied
with the exact steps from Public → Auth → Forgot your password.

**Ben — SSO / Okta.** Not in the toy knowledge base.

> Try replying to Ben in Plane.

*No public docs or internal policy → low confidence → hand off.* It left the
note **and messaged Alert**, because he'd set a rule: an enterprise customer
who looks locked out gets escalated. Alert posted to the Slack alerts
channel and tagged him. Real-time visibility on the tickets that matter,
without reading every ticket.

**Carter and Damon — refunds.** Two users; Carter subscribed today (renews in
a month), Damon renews in ~10 days (so ~20 days in). Per the SOP: approve
Carter, deny Damon.

> Now try to answer Carter and Damon. [customer IDs pasted]

Both replies went out. **Carter: cancelled and refunded — verified in Stripe
(active → cancelled, payment refunded).** Damon: refund denied, *without
quoting the internal 14-day rule* — kept vague, and offered to schedule a
cancellation at period end so he isn't billed again. Stripe unchanged for
Damon. Stripe actions can be approve-gated or not; "you can let it run
loose."

**Elena — "can I share my Wi-Fi pass?"** Not in the KB.

Reply classified the root issue (pass sharing), searched, couldn't answer,
left a hand-off note, and **recommended asking Tune to add it to the
knowledge base** — it asked rather than editing. He approved:

> Add pass-sharing to the FAQ. Say this is not allowed. Do it in green.

Tune added it. Then:

> Can you try again now that the information is added?

Reply answered with high confidence and linked the new section.

**Internal Q&A in Slack.** A teammate on billing asks the same bot:

> What is the refund SOP?

It answers with the *internal* policy, because the asker is internal. Same
KB, same bot, different audience. "Other support agents are focused on
customer replies; using the KB you already built to answer your own team is
surprisingly cumbersome." Use cases: GTM prepping for a call on today's
release; a manager checking how the refund policy changed over time.

Side note from the run: the bot asked permission to post in Slack. He set
"always allow." Also, "it was even more protective than I wanted at the end —
that's probably better for writes."

---

## Alerting as a use case

Anyone on the team with a bot connected to the ticketing system can say:

> Create a routine that looks through tickets every hour, classifies whether
> a user is threatening to churn and has been a customer for six months or
> more, and sends an alert to this Slack channel.

No engineer needed.

---

## Evals and traces — how you debug it

Set up with a Supabase connector on Build:

> You have access to Postgres now. Create a traces table and an evals table.
> Write to those tables every time I ask you to run an eval or create a new
> eval, and every time you run a trace or answer a ticket — internal,
> external, even a dry run, even if you're only leaving a note.

Per run: how long it took, which files it looked at, which files it ended up
using (usually a filtered-down list). From that you can see where it went
wrong. Evals are the things you want to re-test every time you change
something. And Tune reads the traces to find improvements — "a big unlock."

---

## Numbers

- **$1–2 per ticket** for medium-to-complex tickets, the way he runs it
  (classifiers before every ticket, traces and evals written).
- **~$0.20 per ticket** for low-complexity billing tickets ("user just asks
  for a refund," "user asks about an email they got") once you bucket them:
  run a script to find them first, then reply to the bucket at once.
- Competing support-agent products charge per resolution, "$1 to $10, order
  of magnitude." Humans: noticeably higher.
- "That's with half a day of trying to improve it."

---

## Q&A worth keeping

- **Non-technical users writing to production?** Whoever sets it up first
  (slightly more technical, or just architecture-aware) gives others a
  **template** with the guardrails baked in — e.g. "you can't update the
  knowledge base yourself." Stronger: put the KB in **GitHub** instead of
  Notion. You get branches, PRs, code owners. The self-improvement bot must
  open a PR, a bug bot reviews it, it pings the owner, **evals run against
  the PR branch** before approval. Same building blocks, real gates.
- **Is it cheaper to batch?** Yes, and be specific. "Reply to Alex" makes it
  list all open tickets, string-search for Alex, then read. Give it ticket
  IDs. "More hard details it can look up easily."
- **Phone support?** He hasn't; Matt on the stream had given a bot a phone
  number (see the day-3 voice-agent feedback line in
  [`../notes/day-3-notes.md`](../notes/day-3-notes.md)).
- **Where to start, for the stream's new company?** 80/20: 20% of use cases
  create 80% of ticket volume. Identify those, get them into the KB with
  SOPs, run evals until it handles them, *then* put the bot in front of
  tickets.
- **Missing connector?** Have GrokBot spin up a cloud agent and build it. Don't
  wait on a roadmap or a vendor.

---

## Copy this

1. One bot, one workflow, then split.
2. KB with three sections: public, internal, and the agent's own process.
   Make it re-read the process every run.
3. Crawl → walk → run. Read-only → notes → replies → actions.
4. An alert rule for the tickets that actually need a human, into a shared
   channel.
5. Human gate on KB edits. If your KB can live in git, put it there and use
   PRs as the gate.
6. Traces on every run from day one; evals for every change.
7. Bucket the cheap tickets and batch them.
8. Point the same bot at your team's internal questions.

Related: [`../agents/VERIFICATION.md`](../agents/VERIFICATION.md) — the
traces/evals idea is the support-shaped version of the verification loop.
