# Marketing

**Session:** GrokBot for Marketing — day 3
**Ran by:** Josh Kim, xAI marketing.

One campaign, from market research to a landing page in production to an
ads readout, run across six bots — and then a seventh bot told to study how
the human orchestrated it and take over the orchestration. "The context
management, the coordination, the trafficking of a campaign — that's truly
where the craft of the work happens, and it's the crux of our job." So that's
what gets delegated last.

His mental-model correction for marketers: chatbots are **thought partners**;
these are **doing partners**. "They'll do it the way that you do it."

---

## The team

Crowdsourced across the xAI team and the marketplace ("who has the best
positioning bot, who has the best ads bot"), then consolidated. Demo product:
**XAir**, a fictional airline with a landing page, route search, and some
existing positioning.

| Bot | Job | Access |
|---|---|---|
| **Market researcher** | Studies the product and market, finds competitors, reads their sites, names the gaps | Web / own browser |
| **Product marketer** | Positioning brief, one-liners, packaging, value statements, landing-page outline, ad copy variants | Google Docs, Google Sheets (MCP) |
| **Website ops** | Ships the landing page as a PR and pushes to prod | The marketing-site repo (write access); Cursor cloud agents underneath |
| **Performance marketer** | Builds the campaign shell and traffics copy | Google Ads account |
| **Marketing analyst** | Pulls results, analyses, recommends | Google Ads API |
| **Project manager** | Studies the other five and the human's interventions, then runs campaigns end to end as the only point of contact | Everything, via the others |

---

## The campaign, step by step

**1. Market research** (dictated):

> Hey, market researcher. Study the XAir website, get a deeper understanding
> of what the product is and what market we're operating in. Then go do a
> competitive analysis: identify and deeply understand our competitors, look
> at their marketing websites, understand their positioning, and —
> importantly — identify the gaps and opportunities we have to strategically
> position against them within our marketing strategy.

It scraped the site (showing a screenshot from its own browser as a progress
update), found the competitors (real airlines), and returned the gaps:
**useful time, day design, long hauls** — and a recommendation to lead
every message with *useful time.*

**2. Positioning brief — with a handoff.**

> Product marketer: go to the market researcher bot and do a handoff of the
> analysis it just performed. Draft a positioning brief: how we should go to
> market, our one-liners, positioning and packaging, value statements, and
> examples of how this comes to life across two or three marketing surfaces.

The bot messaged the researcher for the context ("I exchanged a few
messages with the market researcher"), then wrote the brief in a **Google
Doc**: research handoff, target audience (*long-haul travellers who want
useful time back*), positioning, GTM notes, one-liners by angle, value
statements, a drafted paid landing page. Over time, he says, bots start doing
this handoff proactively; early on, you tell them to.

**3. Feedback the way you'd give it to a person.** He left comments in the
doc (*"this is great, lean into this"*) and then:

> I've just left some comments inside the Google Doc. Go through them, take
> the feedback, incorporate it into an updated draft. While you're at it,
> build out a full outline of the landing page. And ideate and draft some
> Google search campaigns to do variant testing between the copy angles you
> drafted.

Result: comments resolved, fuller landing-page outline, and a **sheet of ad
variants** — variant name, hypothesis, ad group, URLs, copy — "because
that's how performance marketers work."

**4. Campaign shell, in parallel.**

> Performance marketer: start creating a shell campaign inside Google Ads.
> Build it to optimise for clicks, because we're going to do copy and
> messaging testing that the product marketer is drafting right now.

Bot had been connected to the Google Ads account beforehand. It found the
drafted copy and built the shell, sending screenshots of the platform as it
clicked.

**5. Ship the landing page.**

> Website ops: take the landing page from the latest brief the product
> marketer drafted and spin up a PR to push it as a new landing page on the
> website. Send me screenshots as you're working so I can monitor progress.

Pulled the brief, opened the PR, showed progress screenshots, then the
preview, then **pushed to prod** and returned the URL. "All from the one
place where all the work is happening."

**6. Analysis.** He didn't launch the new campaign live (that needs budget
and a card); he'd run one earlier in the week.

> Marketing analyst: go into Google Ads, pull down the data from our last
> messaging experiment, analyse it, tell me the TL;DR of the insights, and
> give me recommendations on how to incorporate it into our marketing
> strategy and update the other assets you've seen.

Returned: a clear winner across variants (brand, customer promise, hours in
between, cost per day…), the key metrics (spend, CTR, CVR), and
recommendations. "There's some debate about how much liberty you give the
agent to make those decisions. In this case it recommends; the team
discusses."

**7. Hand over the orchestration.** "You might have noticed that during
this entire demo, I've been the one orchestrating. That's the tax."

> Project manager: study and talk to each of the bots on my team and
> understand each of their roles in bringing a campaign to life. Look at our
> conversations and see where I had to interject, give guidance, or give
> feedback, and weave that into how you work with them. Then kick this off
> and automate it completely with three new campaigns. Send me screenshots
> and progress updates so I can stay in the loop. And most importantly: be
> my point of contact. I don't want to talk to any of the other bots. I only
> want to talk to you, to save myself the context switching.

It studied the five specialists, listed the three campaigns (research →
positioning → landing page → …) and queued them. "You no longer have to be
bombarded with five different messages from five bots."

---

## Share as a template

> Create a template of yourself that I can share with someone else.

Snapshots the bot — context, memory, routines — into something a teammate
(or anyone) pastes into their own instance. "They have access to literally
the way you work." This is how the six bots were assembled in the first
place, and he said the refined versions would go to the marketplace.

---

## Composing a bot from several sources (Q&A)

How he built the product-positioning bot, "a product of being lazy":

1. Dictated a couple of minutes of how he wants it to think.
2. Had it pull tone and voice from the existing website.
3. Found two or three marketplace bots he liked, **gave it their URLs**, and
   said: *scrape all that context and memory and replicate it into how you
   work.*
4. Connected it to **SuperMe** (an expert marketplace with a plugin) and
   said: *in lieu of scaled qualitative research, vet everything you do with
   experts there.*

---

## What we learned (his three)

1. **Scope your bots properly.** It's like writing a job description: a new
   teammate, clear swim lanes, tightly scoped so they're specialised. "That's
   how you squeeze the most efficiency out of a team of bots."
2. **Trust your bots.** They're ambitious, proactive, hungry. Give them
   access: hook up Slack and email first and ask, *study all the context and
   tell me what you can do for me. Take a job off my plate.*
3. **Invest in your bots.** Bot-to-bot collaboration gets more organic as you
   prompt it; feedback, context and memory compound.

---

## Q&A worth keeping

- **Where to keep a human in the loop?** Same as onboarding a junior: don't
  hand over the keys on day one. One simple task, one or two tools, watch it
  deliver, expand. You can tell it "always allow" for a permission once
  you're comfortable. End state exists: xAI engineers with "armies of bots
  pushing code to prod." Start small and low-risk.
- **Biggest blocker for marketers?** The mental model. If you treat it like
  search or another LLM you get nothing. Hook it to Slack and let it be the
  first line of triage: *message Josh when it's important, reply to the
  person otherwise.*
- **Roles or initiatives?** Roles are always-on and keep learning;
  initiatives start and stop. Put role bots in a **group chat per
  initiative** — a "tiger team" on website conversion.
- **Personality?** Each bot has its own memory: tell the PM bot to talk like
  Harry Potter and call you a wizard if you want. Avatars can be regenerated
  and animated from a word. You can point a bot at an agent you built
  elsewhere and say *replicate this.*
- **EU data / training?** Opt-in/opt-out data-privacy modes; enterprise
  security case by case with a dedicated team.
- **Existing coding-tool context?** Point the bot at your existing work; it
  uses it as the harness. Website ops is Cursor cloud agents underneath.

---

## Copy this

1. Six roles: research, positioning, web, performance, analysis, PM. Borrow
   the ones that exist.
2. Chain them by telling each to go get the handoff from the previous one.
3. Give feedback in the document, then tell the bot to go read it.
4. Parallelise: campaign shell while copy is still being written.
5. Screenshots as progress updates for anything that touches a live system.
6. When the loop works, ask a PM bot to learn where you intervened and take
   over.
7. Share the result as a template.

Related: [`post-sales.md`](post-sales.md) and [`sdr.md`](sdr.md) for the
other single-point-of-contact setups; [`product-management.md`](product-management.md)
for the same data → spec → design → ship chain on the product side.
