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

## My take

The interesting part is how little we're given: a sector, a sponsor and a goal.
That's roughly what a real first client meeting hands you, and the work is turning
it into scope. So rather than let each assessment invent the Oscorp facts it
needs, everything lands in one profile with assumptions marked as assumptions.

The goal as stated — pass all cyber security legal and compliance regulations —
is worth reframing early with a client. You comply with what your data, your
jurisdictions and your activities trigger, not with everything on a list. Working
out which regimes actually apply is the first deliverable, and for Oscorp several
of the course's examples almost certainly don't.

Worth noting for later: Norman is the sponsor, the owner of the crown-jewel data,
and the person with the strongest reason to want an exception when a control slows
his project down. Any access model for that project has to hold against him.
