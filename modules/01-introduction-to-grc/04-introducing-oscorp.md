# Introducing Oscorp

> Module 01, lesson 4. The case-study org the rest of the course runs on, and how
> little we actually know about it yet.

## Summary

The framing device for the course: I've been hired as a cyber security consultant
at a Big 4 firm, and my first client is Oscorp, a bioengineering research company.
The CEO and founder, Norman Osborn, cares about security because he's planning a
secret project, and he wants Oscorp to pass every cyber security legal and
compliance obligation that applies to it.

That's genuinely all we're given. Sector, a CEO with a motive, and a stated goal.
No headcount, no jurisdiction, no revenue, no systems inventory, no statement of
what data Oscorp actually holds. Every practical assessment from module 2 onwards
builds on this org, so rather than wait for the details to arrive one lesson at a
time I've started a running profile at
[`../../capstone-nist-program/oscorp-profile.md`](../../capstone-nist-program/oscorp-profile.md),
which separates what the course has stated from what I'm assuming and why.

The gap is useful rather than annoying. Starting an engagement with a sector, a
sponsor and a vague goal is exactly what a real first client meeting looks like.
The work is turning that into scope.

## Key concepts

| Concept | What it means | Why it matters in practice |
| --- | --- | --- |
| Oscorp | Bioengineering research company; the course's running client | Every later assessment assumes this context, so the profile needs to be consistent |
| Norman Osborn | CEO and founder; the engagement sponsor | The sponsor sets scope and budget, and has their own reasons for wanting the work done |
| The "secret project" | An unnamed high-value initiative driving the CEO's interest in security | Signals that confidentiality of research IP is the crown-jewel asset, not availability or payment data |
| Engagement scoping | Turning a sector and a sponsor's goal into a defined assessment | The step between being hired and doing anything useful; the course skips it |

## Where this shows up in a real job

Nothing in my background is bioengineering, and I'm not going to pretend
otherwise. What does transfer is the shape of the problem: at Helium Health the
regulated data was health data, and the question of *which* obligations actually
bit was answered by where the data sat and who it belonged to, not by listing
every standard we'd heard of. Oscorp is the same question with different data.

The habit worth carrying over from support is asking what the system actually
holds before deciding how to handle it. A ticket about "the site is down" and a
ticket about "customer data looks wrong" get triaged differently, and the
difference isn't the severity field — it's what's inside.

## Gotchas / what most orgs get wrong

- **"Pass all cyber security legal and compliance regulations" is the wrong
  goal, and it's the client's own words.** You don't comply with all regulations;
  you comply with the ones triggered by your data, your jurisdictions and your
  business activities. The course's compliance examples list Australian Privacy
  Act, GDPR, China Privacy Act, PCI DSS, ISO 27001 and CPS 234 — for a
  bioengineering research firm, several of those almost certainly don't apply.
  PCI DSS is triggered by handling cardholder data; CPS 234 by being an APRA
  regulated entity. A consultant who nods along and assesses against all six is
  billing for work the client doesn't need. The first deliverable of a real
  engagement is the applicability analysis, not the assessment.
- **The sponsor is also the risk.** Norman wants security because of a secret
  project he owns. That makes him the engagement sponsor, the crown-jewel data
  owner, and the person with the strongest incentive to route around any control
  that slows the project down. The course presents his interest as an unqualified
  positive. In practice a CEO-owned confidential project is a textbook setup for
  exception-by-authority, and any access model for that project needs to survive
  its own sponsor. (The course is naming a comic-book villain as the client's
  CEO, which I assume is a joke, but the org design point stands on its own.)
- **A profile assembled lesson by lesson will drift.** If each assessment invents
  the Oscorp facts it needs, module 4's asset inventory won't match module 9's
  supplier list. One profile file, updated as facts land, with assumptions marked
  as assumptions.
- **Course images stay out of the repo.** The lesson's Oscorp render and the GRC
  diagrams are the course's own assets. Same rule as the transcripts — described,
  not reproduced.
