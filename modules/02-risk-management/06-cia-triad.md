# The CIA triad in the real world

> Module 02, lesson 6. Three properties of information, used as a question
> generator rather than a definition to memorise.

## Summary

The first "framework" in the course isn't really a framework — it's a model, a set
of principles describing three properties that information needs to hold.

**Confidentiality**: only authorised individuals can access the data.
**Integrity**: the data is accurate, complete and hasn't been tampered with.
**Availability**: authorised individuals can get to the data when they need it.

Stated like that it's almost too simple to be useful. What makes it work is using
it as a set of prompts during an assessment. The lesson's example is a web
application at an insurance company, and the triad turns into three lines of
questioning.

For confidentiality: what data does this application handle, who has access to it,
and what protects it from people who shouldn't. For integrity: what stops the data
being altered by someone who isn't authorised to change it — authentication,
password strength, multi-factor. For availability: is this meant to be up
twenty-four hours a day, is there high availability, what happens when it goes
down, are there backups, how long does a restore take, and has the restore ever
actually been tested.

That last question is the one that gives the whole model away. Nobody asks
"has the backup been tested" unless they've been handed a checklist that forces
the question. The triad's value is that it's very hard to skip a category once
you're walking it deliberately.

## Key concepts

| Concept | What it means | Why it matters in practice |
| --- | --- | --- |
| CIA triad | Three properties information should hold: confidentiality, integrity, availability | A reference model for assessments, not a control catalogue |
| Confidentiality | Only authorised people can see the data | Failure looks like a leak — an open storage bucket, shared credentials, a successful phish |
| Integrity | The data is accurate, complete and unaltered | Failure means decisions get made on wrong data; altered transaction logs, a pricing bug, an audit record changed without detection |
| Availability | Authorised users can reach the data when they need it | Failure means the data may be perfect and still useless — DDoS, a server with no failover, ransomware |
| Model, not framework | A way of structuring thinking, not a list of controls to implement | Tells you what questions to ask; the answers come from elsewhere |
| Assessment prompts | Using each leg to generate questions about a scoped system | The practical way the triad gets used day to day |

## Where this shows up in a real job

The triad describes a split I've lived on one side of. In support, availability is
the property that gets all the attention — the site is down, checkout is broken,
nobody can log in. Confidentiality incidents are rarer and get escalated away
quickly, and integrity almost never comes up by name even though it's what's
happening when data syncs wrong or an order total is incorrect.

So my instinct when assessing a system is to reach for availability first, because
that's where four years of tickets have pointed me. That's exactly the bias the
model is there to correct, and it's useful to know which leg I'll under-weight
rather than assume I'm even-handed.

The Helium Health ISO 27001 work touched all three, but the one I remember
arguing about was availability — backup and restore evidence, and whether a
restore had been demonstrated rather than just configured.

## My take

The triad earns its place as a question generator. "What are the risks to this
application" produces a blank page; "who can read this, who can change it, and
what happens when it's gone" produces a list. It's the same move as risk scenarios
in lesson 3, one level up.

Three things I want to carry forward:

**It gives me an impact axis.** When rating a risk, asking which property is
harmed makes the impact statement concrete. "Confidentiality breach of customer
records" and "eight hours of downtime" are different kinds of damage, and they
reach different parts of the business.

**Integrity fails without an attacker.** The examples that stay with me are the
software bug that modifies pricing data and the audit record changed without
detection. No adversary required in the first case, and no visibility in the
second. Integrity is the leg most likely to be broken quietly, which is why
"who would notice, and how" belongs next to "who could change it".

**The three pull against each other.** The spreadsheet fallback from lesson 3 buys
availability with confidentiality — payment data ends up on an unprotected machine
beside the till. Every meaningful control decision is a trade between the legs,
and the triad is most useful when it names the trade rather than implying all
three can be maximised at once.
