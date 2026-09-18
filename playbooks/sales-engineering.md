# Sales Engineering

**Session:** GrokBot for Sales Engineers — day 2
**Ran by:** Amrita, field engineer at xAI. Also ran the day-1 GrokBot 101 demo.

Three bots she uses day to day. Two live in the demo project (Flylo, the
fictional airline), one is her real slide bot. The recurring line: **"Finished
work is the best part."** You come back to a done thing, not a queue of
decisions.

---

## The team

| Bot | Job | Access |
|---|---|---|
| **Mimi** | Slide and customer-proof-point curator | A master Google Slides deck on her computer. Case studies, benchmarks, everything in one place. |
| **Sherlock** | Technical expert | The product repos (booking backend, booking frontend). Uses Cursor cloud agents under the hood. Steered to **never release IP** and to phrase answers for a non-technical customer. |
| **Serena Williams** | Competitive intel | Her own computer. Signs up for and uses competitor products. Named for a tennis player famous for studying opponents. |
| *Echo* (Krista's, shown in the Sales session) | Live deck curation during a call | See [`sales.md`](sales.md). |

Plus three bots that **Sherlock spun up on its own** when asked (below).

---

## Mimi — case-study slides from a blog post

Her case-study slides all share one template: **logo, then problem →
solution → impact → quote.** She gives Mimi a customer blog post (or notes
from a call) and says:

> I just want you to do your job for Jellyfish, and here is the blog post.

Live, with a Salesforce post ("cut legacy code coverage time by 85%"):

> Can you create another one of these slides for Salesforce for me? Blog post
> here: [link]

Mimi reads the post, extracts the four parts, **goes to the company's brand
page to get the right logo**, builds the slide on her own computer (you can
watch her cursor moving in Slides), inserts it into the deck, and sends
screenshots back. 10–15 minutes. Then:

> Great work. Can you do one for Grab?

Things she does with Mimi:

- Batch: "do Salesforce, do Grab, do this other one" in one message; Mimi
  works through them while the laptop is closed.
- Before a call: "hide the case studies that wouldn't be relevant for this
  customer" — Uber cares about Grab, not Salesforce.
- As a routine: *have there been any customer posts recently about us that
  would be good to highlight? If so, create a slide.* Companies publish
  these posts without telling you.

Why a template: "I don't want it to come up with anything too sloppy or too
wordy. I know exactly how I want my slide organised." The bot's job is the
content, not the layout. She makes slides for 15–20 customers a week.

Live incident: Mimi lost her Google login mid-demo (there'd been an outage
earlier). Fix: take over the bot's computer, log in, hand it back.

---

## Sherlock — answering technical questions without pinging an engineer

Description she gave it: *You're a technical expert on Flylo and you support
the website flyloair.com.* Repos attached. *If there's a customer issue, I
want you to investigate and communicate what could be wrong to a customer.*

Example question the day before:

> How do we handle a race condition — two people booking the same flight or
> the same seat at the same time?

Sherlock launched cloud agents in the backend and frontend repos and came
back with: the protection is in Postgres; two customers can't confirm the
same last cabin; and, separately, **what to tell the customer** — *we hold
the last remaining cabin space for 10 minutes when you start checkout; if
someone else started first you'll get a message.* From there: "draft this in
an email and send it to this customer," with send gated on her approval.

---

## Serena — competitive intel with hands on the product

She gave Serena only a description, no walkthrough. First prompt:

> What are some competitor products that you think are worth testing against
> Flylo?

Serena listed options and, unprompted, **messaged Sherlock** for a baseline:
"what can the current Flylo booking codebase support today — search, fare
selection, seats, bags, known gaps?" Sherlock pulled it from the code and
replied. Then:

> Let's go with Southwest and Spirit. Let's see how those booking experiences
> compare to Flylo.

Serena started running the Southwest booking flow on her own computer
(visible top-right). Mid-task, Amrita steered:

> Can you see if there are any AI travel agent capabilities in any of the
> competitor tools that we should be aware of?

Serena incorporated the second ask **without abandoning the first** — she
answered the AI-agent question while still clicking through Southwest. That
multitasking inside one thread is the point: "other tools forget the first
question the minute you ask the second."

Routine she suggested: *every week, summarise what's happened on the Expedia
and Skyscanner technical blogs and tell me if they shipped anything I should
know about.*

---

## Group chat: get the two of them to agree on the roadmap

She put Sherlock and Serena in a group chat (visible in one place instead of
clicking between threads) and asked:

> What have you found is the key differentiator in our competitors that
> would be significantly low effort to build in the product?

They argued it out with their respective context:

- Sherlock: managed booking (view/change trips) is table stakes everywhere —
  easy fix. And **a flexible-date calendar is already wired in the frontend
  but never called** — classic differentiator, very easy.
- Serena: round trip and bags look big but aren't low effort; asked Sherlock
  which of managed booking vs. calendar felt most painful to users.

Sherlock `@`-tagged Serena on its own to ask for something specific. Bots do
that unprompted once they know who holds what. From here: connect Google Docs
/ Confluence / whatever and have them write the product doc, or open a PR.

---

## Teach a task — recorded live

She took over Sherlock's screen, hit **Teach a task**, and recorded herself:
Google → "expedia technical blog post" → their Medium → scan for AI-related
posts → open one → scroll. Pause, done. Then a voice note over the recording:

> Notice that I specifically looked for AI-related blog posts in my
> competitor products, and I wanted to make sure that we are staying on top
> of our AI tooling inside of our own product. I'm going to try and apply
> this to as many competitors as possible.

Then: *do the same for Southwest, Spirit, Skyscanner, Google Flights.*
Skills are shared across all bots regardless of where you taught them.
"One of the biggest-leverage ways to use GrokBot."

---

## Bots spinning up bots

> Based on the work that you and @Serena are doing, what bots would be
> helpful for you to continue doing great work, specifically around
> competitive differentiation and sales engineering? Go ahead and spin up
> those bots for me.

Sherlock created three, with descriptions:

- **Battle Card Blair** — "combines Serena's hands-on competitor product
  findings with Sherlock's Flylo codebase to produce short SE-ready battle
  cards: competitor claims, Flylo reality."
- **Demo Drake** — "sales engineering demo and talk-track specialist. Build
  confident, no-hallucination demo scripts and call talk tracks that map
  customer pain to the Flylo live flow. Ground every claim in Sherlock."
- **AI Radar** — "track competitor AI tooling from public tech blogs." Reuses
  the skill she'd just taught. Always uses Sherlock as source of truth; hands
  testing and user flows to Serena.

Her verdict: keep Blair and Drake; AI Radar overlaps Serena and "doesn't have
a cute alliterative name." The useful thing isn't the three bots, it's that
each one **knows who is the source of truth for what.**

If you're starting cold: *I need to build a demo for a POC with my AE in a
couple of weeks for this customer. Spin up three bots you think would be
useful.* "GrokBot is not here to give you extra managerial
responsibilities."

---

## Numbers

- 15–20 customer decks a week — Mimi's workload.
- 10–15 minutes — one case-study slide from a blog post, logo included.
- $20–30 — a whole sales case-study deck, vs. 4–5 hours by hand (her figure
  from the day's Q&A).
- 10 minutes — the cabin hold Sherlock found in the code.

---

## Q&A worth keeping

- **Will sites ban the bot?** CAPTCHAs and bot detection can block it on
  some sites; no guaranteed workaround. Enterprise rule of thumb: "if you
  shouldn't be accessing Facebook, block it on the bot's computer" rather
  than try to evade detection.
- **MCP vs. computer use.** MCPs are "APIs for agents" — faster, easier to
  whitelist/blacklist. Computer use is the fallback when there's no MCP
  (Power BI, MongoDB were the examples). A tool with no MCP is not a blocker.
- **Tokens.** Adjust the bot's verbosity to control spend; computer-use
  compute itself isn't user-tunable.
- **Non-Linux tools with no MCP?** Can't be used right now. Straight "no."

---

## Copy this

1. A slide bot with your template baked in. Feed it sources, not
   instructions.
2. A technical-expert bot on your repos, steered to never leak IP and to
   answer in customer language. Ask it the question the customer asked you.
3. A competitor bot that uses the products, not just reads about them. Let
   it talk to the expert bot for a baseline.
4. Group chat the two when you need a roadmap opinion.
5. Record one workflow you do by hand. Say out loud what mattered.
6. Ask your bots what bots they need.

Related: [`sales.md`](sales.md), [`founders.md`](founders.md) (StockBot is the
founder-side competitor bot).
