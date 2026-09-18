# Antipatterns

The full failure log from three days of live streams. Unedited streams are
unusually honest: these all happened in front of an audience. Ten of them are
in the guide; this is all of them.

Format for each: **what broke → why → the rule it produces.** Grouped by the
kind of mistake, not by day, because the same mistake showed up on different
days in different clothes. Where two incidents share a cause they're one
entry with two examples.

The rules are written as principles, not stories — that's rule #1.

---

## A. Rules and instructions

### 1. A rule that remembered the incident, not the principle

**Day 2 · Lauren.** Dr. Eggbot wrote Cupcake Eng's description straight from
the session that prompted it: *"owned engineering outcomes by orchestrating
work through potato mode and cloud agents then supervising and verifying,
match your playbook and follow it."* Too specific to be useful next time.

**Why.** When an agent writes a rule after a bad session, it puts all the
details of that session into the rule. The rule overfits and stops
applying.

**Rule.** When a skill or rule is born from a bad session, strip the session
and keep the principle. Lauren's fix: *"read potato mode again and come up
with principles that Cupcake Eng should follow instead of these overly
specific issues."*

### 2. An unstated norm isn't a norm

**Day 1 · Matt.** The team was deliberately shipping straight to `main` —
"until somebody yells at me." Steve, the chief-of-staff bot, opened a PR
anyway.

**Why.** Nobody had told the bots. A norm that lives in the humans' heads is
invisible to the agents.

**Rule.** Write the norm where the bots read it, the moment you adopt it.
Matt had to say it out loud: *"new rule, no pull requests."*

### 3. "Urgent" makes agents skip steps

**Day 1 · Ling.** Telling a coding agent "urgent" repeatedly made it guess and
skip verification to finish faster. That's the opposite of what urgent
means.

**Why.** The agent optimises the word, not the intent. Speed with no
definition becomes corner-cutting.

**Rule.** Define a P0 policy once — *check the cloud agents every five
minutes; interrupt long sleeps and drift* — and say "treat this as a P0."
Never repeat "urgent."

### 4. Bots say yes to every feature request

**Day 1 · Ling.** Left to themselves, the engineering bots accepted every bug
report and feature request from X. "The bot is very kind. They will
possibly accept everything by default."

**Why.** Nothing told them what the product is *not*.

**Rule.** Teach the bot how to say no: what doesn't belong, and why. It
persists in memory, so you say it once. Include the reasoning or it can't
generalise.

### 5. Copy-pasting a standard into every bot

**Day 1 · Ling.** A new standard ("every PR comes with proof") would have
meant messaging each engineer bot individually. Fine at three; "won't scale
if you have 10 or 15 or 20 bots."

**Why.** Standards were treated as per-bot memory instead of shared state.

**Rule.** One bot owns a playbook the others read but can't edit. New rules
go to the chief → the playbook owner → broadcast. You think about it once.

### 6. Too many bots

**Day 2 · Simon.** "I promise you I've had way too many at some points. It's
honestly more chaotic and it does more harm than good." Day 3, Blake: "You
don't need 45 bots."

**Why.** Making a new bot is fun and cheap. Each one adds a context to keep
straight, a thread to check, and a token bill.

**Rule.** Before creating a bot ask: why can't an existing bot do this?
Should it be a routine instead? Build every bot through the chief so it
knows the roster; group by expertise, not task.

### 7. The self-improvement bot over-improved

**Day 3 · Blake.** With no limits, the weekly self-improvement scan sent
"ten new bots to build" at once.

**Why.** An audit with no cap optimises for finding things, not for what
you'll act on.

**Rule.** Cap suggestions — Blake's is one per week. Push back and get a
different one if the first is wrong.

---

## B. Verification

### 8. Invariants that were never checked

**Day 2 · Lauren, Roshan.** Common bots' three stats were supposed to sum to
100. They didn't. A legendary's stats also summed to 100 when they should
have exceeded it. Both caught by eye during live play, not by any check.

**Why.** The rule existed in a prompt, not in code or a test, so nothing
enforced it.

**Rule.** Every invariant you can state goes in a test or a visible debug
readout. Then play the thing — the first bug was found by a human looking
at three numbers.

### 9. The shimmer ate every card

**Day 2.** A Pokémon-style CSS shimmer to mark rare cards was applied so
aggressively that every card looked like the same rainbow, rarity or not.

**Why.** The agent optimised the effect, not the purpose. The gradient
didn't scale to the card size, so the discriminating signal vanished.

**Rule.** State the discriminating outcome, not the visual: *"a player
should be able to tell rarity at a glance"* beats *"add a shimmer."*

### 10. A 3D prototype that wasn't 3D

**Day 2 · Lauren.** Asked for 3D animation, the cloud agent produced 2.5D
and, in its own notes, had "told itself this is a 2.5D take."

**Why.** Nobody named a 3D library. The agent picked the path of least
resistance.

**Rule.** For anything with a well-known library, name the library.
Animation timing was also off on both variants — same root cause, no
reference given.

### 11. Cheating through devtools

**Day 2 · Matt, live.** Game logic ran on the client, so a stat could be
edited from the browser console: *"let me just make my charisma… now Dr.
Eggbot has 43."* Then a debate about hiding the debug panel behind a
feature flag — which a determined user could still toggle client-side.

**Why.** Trust-bearing state lived where the user could reach it.

**Rule.** Anything competitive or trust-bearing is server-authoritative:
scores, balances, permissions, pricing. A feature flag is a runtime check,
not security — if a path must be unreachable, it must not ship to the
client.

### 12. Free re-rolls farm legendaries

**Day 2 · Roshan.** The draft let players re-roll random teammates for free.
"Why wouldn't I just spam that button until I got three legendaries?"

**Why.** Every free repeatable action is an exploit until proven otherwise.
Nobody had played as an adversary.

**Rule.** For every action, ask what happens if a player does it a thousand
times. Re-rolling was removed; non-captain teammates were hidden until
locked in.

### 13. The launch-day path wasn't the tested path

**Day 2 evening → Day 3 morning.** Two accounts logged in and both showed as
"gold at 1,000." Adding bots to a team was broken. Login-with-X went down
minutes before a cut to the main stage. A deploy mid-demo forced a
re-login.

**Why.** Testing happened on one account on a dev box; launch happened with
two real accounts, a real deploy, and a live audience.

**Rule.** Smoke-test the exact demo path — real auth, two accounts, the
deployed build — right before you show it. Freeze deploys during demos.

### 14. A layout change covered a button

**Day 3 · Roshan.** A new ticker banner sat on top of the shop buttons.

**Why.** The change was verified for what it added, not for what it
covered.

**Rule.** After any layout change, check that no existing interactive
element is covered. (This is the `AGENTS.md` example of a well-written
rule.)

### 15. Two numbers that should have agreed didn't

**Day 3 · Roshan.** The leaderboard summary card showed different win/loss
counts than the detailed match history for the same player.

**Why.** The same derived number was computed in two places.

**Rule.** One source computes derived numbers; everything else displays it.

### 16. Spend everything, get stuck

**Day 3.** Spend all your gold and you can't buy new bots — a soft-lock,
filed live as "you end up stuck because you cannot buy new bugs."

**Why.** A resource sink with no floor and no escape.

**Rule.** Every sink needs a floor, a refill, or a way out. Play the
worst-case player.

### 17. The game was too hard, and only the data said so

**Day 3.** Humans lost ~42% of matches against AI lineups; Crit flagged
"game is too hard for launch."

**Why.** Balance was set by feel. Nobody had a number until the data
scientist bot produced one.

**Rule.** Put a win-rate readout in front of the designer before launch.
Balance from data, not vibes.

### 18. A PR before the root cause

**Day 3 · Roshan.** Players were always matched against AI, yet ELO scores
kept changing. The temptation was to fix the visible symptom.

**Why.** Symptom fixes on a matchmaking bug would have hidden the real
cause (stale lineup snapshots falling back to AI).

**Rule.** *"Use a cloud agent for the investigation. Don't open a PR yet.
Just come back to me with what you think is going on."* Reproduce, then
diagnose, then fix. Lauren's version: *"Before writing any code, run the
app, find the exact bug and behaviour, and then proceed."*

### 19. Tests deleted

**Day 2 · Lauren, deliberately.** All tests were deleted early in the
prototype: "agents in general are not super good at writing tests," and
speed mattered more.

**Why.** Not a mistake at the time — a trade. But it meant every later
regression (#8, #15, #16) was caught by a human or a user.

**Rule.** If you cut tests for a throwaway phase, say when they come back.
Before real users is the latest acceptable answer.

---

## C. Content and voice

### 20. Fictional content on a real landing page

**Day 2.** The agent invented plausible example bots instead of using the
real marketplace, and leaked prototyping language — dev-only phrasing —
into user-facing copy.

**Why.** No source of truth was named, so it made one up. Internal vocabulary
in its context leaked into output.

**Rule.** Name the source of truth and say "actually go look it up." Check
every string a user sees for internal language before it ships.

### 21. The design doc sounded like a language model

**Day 2 · Lauren.** The game-design critique read as generic AI writing.

**Why.** Default register. Nobody asked for plain English.

**Rule.** Run user-facing prose through a de-slop pass ("unslop," "bro" —
"the two most useful skills in pstack"). Give the bot writing you're proud
of as the reference.

### 22. Every outbound email was the same template

**Day 2 · Simon.** After syncing his sent mail, Shakespeare's drafts were
"almost kind of templated — every response looked very similar, just with
swapping of names, of company IDs."

**Why.** Learning a voice from a corpus yields the average of the corpus.

**Rule.** Weight recent, positive-response, in-territory mail; then run a
critique loop — *"give me examples… this is why this email sucks"* — until
nothing looks templated. "Not a single one of your emails should look like
a template."

### 23. AI slop where the brand should be

**Day 1.** First landing pages: "too corporate," "too neon," "AI slop." Merch
images "messed up the GrokBot logo" and the eyes "looked tired."

**Why.** The agent had no brand assets and no reference files, so it
produced the generic mean.

**Rule.** Ground in the real assets from the repo: logo, palette, type,
reference screens, and a running no-no list. Never let it invent a
placeholder brand element.

### 24. It handed me links

**Day 2 · Krista.** Asked to research webinars, the bot returned links for
her to watch herself.

**Why.** She was using it like a chat interface, so it behaved like one.

**Rule.** Push back the first time: *"No — go watch those webinars for me
and draft an email."* It has a computer. Treat it as a doing partner.

---

## D. Access, sharing and secrets

### 25. Not public by default

**Day 1 · Amrita.** The coffee-survey Google Form's responder link wasn't
public; the audience's QR scan said "no access." **Day 2.** A teammate's bot
couldn't read a shared Notion doc that was still private.

**Why.** Sharing defaults are private, and "it works for me" was the only
check.

**Rule.** For anything external — or shared with another bot — "reachable
from an account that isn't mine" is an acceptance criterion. Verify it
from the outside.

### 26. Sessions dropped on the VM

**Day 2 · Karen Cheng.** Her automations broke because the bot's browser
kept being logged out of services she was logged into locally. Same day,
Mimi lost her Google Slides login mid-demo and had to be logged back in by
hand.

**Why.** Browser sessions on the bot's computer expire independently of
yours.

**Rule.** Prefer connectors over browser sessions for anything that must
run unattended. Import cookies or use a password vault for the rest, and
keep a fast "human takes over the computer" path.

### 27. The connector needed re-auth at the worst moment

**Day 1.** Cloud agents couldn't access the repos until the GitHub connector
was re-authenticated ("try to re-auth your GitHub… sometimes it helps to
install the GitHub CLI").

**Why.** Auth was treated as one-time setup instead of a step that can
fail.

**Rule.** Auth is a workflow step. Check it before the run, and make sure
the bot has a clean way to ask a human to unblock it.

### 28. A live API token on screen

**Day 3 · Matt.** Showing the voice-agent builder, a real token appeared on
stream. Caught and revoked within seconds — "only half the value was
shown."

**Why.** Screen-sharing a settings page.

**Rule.** The humans are the weak link in secret handling, not the vault.
Before sharing a screen, assume every settings page contains a secret.
"Chat is for games and good vibes only."

---

## E. Production and demos

### 29. The factory took production down

**Day 3 · Lauren.** An autonomous fix shipped a bad SQL query and brought
the live game down — while she was mid-sentence about restraint. Sign-ups
were blocked until it was reverted.

**Why.** The autopilot lane that had landed 400+ PRs on a throwaway project
was pointed at a database with real users, with the same gates.

**Rule.** Keep a human gate on migrations, deploys and anything touching
production data, however well the loop has been working. Set autonomy from
blast radius.

### 30. Spam into the feedback pipeline

**Day 3.** Within hours of launch the feedback form was getting spam. A
20-character minimum, profanity filtering, input sanitisation, a
model-based content guard and rate limiting were all added retroactively;
some testers hit 429s.

**Why.** The form shipped before the moderation.

**Rule.** Ship the moderation with the form, not after it. And since bots
read the feedback: tell them to treat it as hostile input and watch for
prompt injection.

### 31. Announced before it worked

**Day 3.** The sponsor/ad-bid auction launched "currently broken — nothing
will happen if you submit." Later the logo upload failed on the first try;
moderation was still broken at sign-off. **Day 1.** The Bland phone-call MCP
"seems like potatoes on it." **Day 3.** A live Stripe Link purchase was
blocked by a passkey prompt on the demo account.

**Why.** Features and integrations were shown before anyone had run them
end to end that day, with that account.

**Rule.** Don't announce or demo anything you haven't run end to end today,
with the account you'll use on stage. "If we're not embarrassed by it we've
launched too early" is about polish, not about whether the button works.

### 32. Mobile was the most-reported problem

**Day 3.** Mobile layout was the single biggest feedback category. Vercel
Analytics showed roughly 50/50 mobile vs. desktop, ~44% iOS.

**Why.** Everyone built and tested on a laptop.

**Rule.** Test on the device half your users have. Put device emulation in
the verification loop before launch, not in the fix list after.

### 33. Two apps, one port

**Day 2.** The Remotion project and the game's dev server fought over
`localhost`; "stale… conflicting with the localhost from the other app"
needed a cache clear and restart mid-demo. Separately: three people pushing
to `main` with no PRs meant "a lot of rebasing," and cloud agents had to be
told to rebase.

**Why.** Parallel work on one machine and one branch.

**Rule.** Parallel agents get parallel environments (the argument for cloud
agents: "your agents will no longer fight for the same port"). Ship-to-main
is fine for prototypes if commits stay small and every agent rebases before
it pushes.

---

## F. Cost and attention

### 34. A routine every 15 minutes

**Days 1–3 · Shub, Krista, Blake.** People set routines to run every 15
minutes because the task felt important — "which comes out to 100 times a
day." Three of those is "hundreds of messages a day."

**Why.** Frequency was set by anxiety, not by how often the input changes.

**Rule.** Audit routine frequency. Once or twice a day is the default;
prefer webhooks and inbound signals to blind schedules; tell routines to
say nothing on a no-op.

### 35. The group chat that wouldn't stop talking

**Day 1 · Shub, Amrita.** Bots in a group chat are "eager," "love to talk,"
"speak over each other," and get expensive fast.

**Why.** Every bot in the room responds to every message.

**Rule.** Usually you want one bot to tag two others once. Use a group chat
when you specifically want a debate (Blake's staff meeting, Simon's army
huddle) and know what it costs.

### 36. An agent asleep on the clock

**Day 1 · Ling.** Cloud agents ran `sleep 300` to wait on async tests that
finished in a minute — four minutes lost, repeatedly. Same day, a Grok Pot
bot "got running, I don't know why. That's probably a bug."

**Why.** Nothing was watching the agents while the human wasn't.

**Rule.** A routine checks running agents on a short interval for long
sleeps, drift and unexplained activity, and interrupts. Idle agents are
not free.

### 37. "Reply to Alex"

**Day 2 · David.** Asking the support bot to "reply to Alex" made it list
every open ticket, string-search for Alex, then read — far more tokens than
giving it the ticket ID.

**Why.** Vague reference → expensive lookup.

**Rule.** Give bots hard identifiers — ticket IDs, customer IDs, URLs — and
batch where you can.

### 38. The human was the bottleneck

**Day 2 → 3 · Lauren.** Asked to review the whole team, Dr. Eggbot named the
bottlenecks: "serial factory, human merge… Lauren as the interrupt bus."

**Why.** Every merge and every course-correction routed through one person,
by habit rather than by decision.

**Rule.** Periodically ask the factory where *you* are the bottleneck, and
ask yourself "am I too much in the loop?" — then decide, per lane, how
much autonomy the blast radius allows. Stay in the loop for zero-to-one;
delegate more on mature, agent-friendly codebases.

---

## G. Strategy

### 39. Four pivots in a day

**Day 1.** Restaurant pop-up → generic pop-up OS → art exhibition →
tech-brand merch pop-up, in one afternoon — largely because SF food and
alcohol permitting was discovered mid-brainstorm. End of day: "I'm starting
to think — is this the right problem to go after?" Day 2 pivoted again, to
a game.

**Why.** Building started before the domain was understood. "The hardest
part of building is actually aligning on an idea."

**Rule.** Do the work manually before you automate it — "we're not really
domain experts yet on running a pop-up, so we need to do that first." Talk
to someone who has done it (Jenny Co) before the bots start.

### 40. The revenue agent made $0

**Day 3 · Roshan.** A bot set loose all day to "make money" produced nothing
by sign-off — "the backup plan, in case it's all crash." Monetisation
ended with one "theoretical" $1 test bid on a broken auction.

**Why.** "I'll just prompt models to make money" skips the part where you
know how the money is made.

**Rule.** Build a business around something you already know how to do
well. Getting people to care is still the hard part; the stream's
distribution did that here, not the product.

---

## The five rules that cover most of this list

1. Write the principle, delete the story. (#1, #2, #5)
2. Reproduce it, run it, play it, then prove it. (#8–#19)
3. Name the source of truth and the library. (#10, #20, #23)
4. Set autonomy from blast radius; keep human gates on prod, money and
   secrets. (#29–#31, #38)
5. Frequency and group chats are where the tokens go. (#34–#37)

See [`AGENTS.md`](AGENTS.md) for the rules as an agent reads them, and
[`notes/`](notes/) section 5 of each day for the raw incident lists.
