# ECONOMICS.md

Every cost and metric quoted on stream, in one place, with the rule each one
supports. Figures are what speakers said out loud in September 2026; treat
them as order-of-magnitude, not a price list.

---

## What work cost

| Work | Cost | Manual equivalent | Source |
|---|---|---|---|
| Full sales case-study slide deck | $20–30 | 4–5 hours | Amrita, day 2 |
| Mid/complex support ticket resolved | $1–2 | more than that for a human | David, day 2 |
| Low-complexity billing ticket, after bucketing and batch scripts | ~$0.20 | — | David, day 2 |
| Comparable support-agent products | $1–10 per ticket | — | David, day 2 |
| Finding a cheaper PG&E plan | ~60 seconds of attention | ~$1,000/year saved | Matthew Berman, day 2 |

The support numbers are the useful pair: the same job went from $1–2 to
$0.20 once low-complexity tickets were sorted into a bucket and handled by a
script instead of a reasoning pass. Cost is a property of the setup, not of
the tool.

---

## What made the bills go up

| Driver | Quoted | Rule |
|---|---|---|
| A routine every 15 minutes | "comes out to 100 times a day"; three of those is "hundreds of messages a day" | Once or twice a day is the default. Prefer webhooks and inbound signals to blind polling. |
| Bots in a group chat | "eager", "love to talk", "speak over each other", get expensive fast | One bot tags two others once. Group chats only when you want a debate. |
| UI work through the bot's browser | filling a web form by clicking costs more than an API-native path | Use a connector when one exists. The browser is the fallback. |
| Too many bots | keep the team lean, "not 45 bots" | One chief of staff over 10–20 narrow specialists worked; nobody needed middle managers. |
| Throwaway verification scripts | rewritten every run, token-costly, non-reproducible | Build one CLI the agents call instead. |
| Agents that `sleep 300` | four minutes lost per wait on tests that finish in one | Watch running agents; a 5-minute check routine is for this, not for reporting. |

Frequency and group chats are where the tokens go. Everything else is second
order.

---

## Throughput

| Metric | Number | Source |
|---|---|---|
| PStack PRs merged to production in one month | 2,500 (~83/day) | Lauren, day 1 |
| Share of merged PRs at the company coming through Grok Bot | double-digit percent | PM session, day 1 |
| First mobile app version, one engineer | 3 weeks | Ling, day 1 |
| Cloud agents one engineer managed by hand before orchestration | 15 | Ling, day 1 |
| CI auto-fix: page a human only after | 10 minutes unresolved | day 1 |
| PRs in the 72-hour build | 433 | day 3 |
| Commits from one host in three days | 157 | Roshan, day 3 |
| Bot employees across 7 businesses | 22 | Jenny Co, day 1 |
| SDR prospects per day | 50, top 5 actioned each morning | Simon, day 2 |

---

## Launch day, for scale

Thursday Arena went live at ~10:00 AM Pacific from one X post.

| When | Number |
|---|---|
| Launch hour | 1,908 games — the best hour of the day |
| Sustained afternoon | 400–500 games/hour |
| End of day | ~4,000 games, 6,000+ public matches, ~30,000 page views, ~2,000 users |
| Practice → X sign-in conversion | ~8% |
| Feedback mix | 71% bugs, 16% praise |
| Revenue | $0 (one theoretical $1 test bid on a broken ad auction) |

Traffic: roughly 50/50 mobile and desktop, 44% iOS, referrals almost all from
X. Eight people came from Bing.
