# Practical approach to asset management

> Module 04, lesson 7. Start with the crown jewels, share the ownership, and stop
> worrying about the tool.

## Summary

The lesson's answer to a problem that looks unsolvable: don't try to solve all of
it first.

**Start with the crown jewels.** Accept that comprehensive asset management is
hard, then prioritise. At all times, maintain a list of the key critical
assets — the crown jewels. Even in an organisation where a complete inventory
looks impossible, that list is achievable, and it's smaller than people expect.
Typically 20 to 30 for small, medium and even large organisations; the largest
seen was around 50, in a very large multinational.

The entry doesn't need to be atomised. An insurance company's claims application
might be several pieces of software and databases, and it's fine to record it as a
single asset with an owner and a classification, then list the serial numbers
beneath it. What matters is that a small spreadsheet of key critical assets exists
and is being watched.

And the sequencing is explicit: when engaged to do asset management, get the
critical asset list **first**. Network scans and cloud discovery with the IT team
are fine — later.

**Assign the responsibility, and share it.** What works in practice is shared
ownership between IT and security. Someone from security — ideally a GRC
consultant — drives the process; someone from IT supplies the lists and explains
what the applications and software actually are, feeding the CMDB. Larger
organisations occasionally have a dedicated asset management specialist, though
it's rare because nobody wants the job. More often it's a GRC analyst, GRC
consultant or security analyst who specialises in it and maintains it.

**Asset management is a process, not a software purchase.** Some organisations buy
the newest, most impressive tooling. Fine, but not the point. What matters is that
identification and classification happen periodically, and that the process is
comprehensive — or at minimum covers the key critical assets. A spreadsheet inside
a real process beats expensive software that lacks the data and that nobody
maintains.

## Key concepts

| Concept | What it means | Why it matters in practice |
| --- | --- | --- |
| Crown jewels | The key critical assets the business genuinely depends on | Makes an impossible task tractable; usually 20–30 items |
| Prioritised sequencing | Critical assets first, broad discovery afterwards | Delivers something useful in week one rather than month six |
| Asset grouping | Recording an application as one asset, with components beneath | Keeps the critical list readable instead of expanding into thousands of rows |
| Shared IT/security ownership | Security drives; IT supplies and explains the data | Neither function can do it alone — one has the remit, the other the knowledge |
| Dedicated asset management roles | Rare specialists; more often a GRC or security analyst who owns it | A realistic picture of where this work actually sits |
| Process over tooling | Periodic, comprehensive practice matters more than the system of record | Prevents a tool purchase from substituting for the work |

## Where this shows up in a real job

The crown jewels framing matches how triage already works for me. Not every
system gets equal attention; you learn which ones, if broken, mean the business
stops — and that shortlist is what you actually watch. The lesson is giving that
instinct a name and a spreadsheet.

The shared ownership model also reflects something I've lived from the IT side of
the divide. Whoever runs the systems knows what they are and what they're
connected to; they rarely know what the business would lose without them. Those are
two different kinds of knowledge and they sit with different people, which is
precisely why the model splits the roles rather than assigning it to one team.

The career detail is useful too: this work tends to belong to a GRC analyst or
consultant who takes it on, rather than a dedicated asset manager. That's a
concrete thing a first GRC role might involve, and unlike a lot of the course
content it's something I could contribute to early.

## My take

The crown jewels idea is the most immediately usable thing in the module, and the
reason it works is that it inverts the order of failure. The comprehensive
approach fails by producing nothing for months and then producing something
incomplete anyway. Starting with 20 critical assets produces something genuinely
useful in the first week — a list that can drive backup verification, access
review, monitoring coverage and recovery planning immediately — and it can grow
outward. Anything that gives you a defensible deliverable early is worth a lot in
a discipline where the usual outcome is an unfinished exercise.

Three things:

**The small number is the surprise, and it's the argument to lead with.** Telling a
sceptical executive "we need to inventory everything" invites a no. Telling them
"there are probably twenty systems this business cannot run without, and nobody can
currently name them" invites a very different conversation. The claim is testable,
cheap, and slightly alarming — which is what makes it move.

**Grouping is what keeps the list usable, and it needs a stated rule.** Recording
the claims application as one asset with components beneath it is right, but where
the line falls should be deliberate: group at the level the *business* recognises
and can assign an owner to, and put the technical components underneath. Group
inconsistently and the list becomes incomparable — one row a whole platform, the
next a single server.

**Shared ownership is right and it's also where these initiatives die.** Two teams
sharing responsibility can mean two teams each assuming the other has it. The model
works when the split is asymmetric and explicit — security accountable for the
process happening, IT responsible for supplying data within an agreed timeframe.
Named people and a deadline, not two departments and good intentions. That's the
same lesson as the risk register's owner column, one level up.

The process-over-tooling point is worth keeping calibrated rather than absolute. A
spreadsheet inside a working process genuinely does beat unmaintained software.
But tooling earns its place at the point the estate outgrows manual maintenance —
when discovery has to be continuous, when changes need an audit trail, when
multiple people maintain it at once. The lesson's framing is a corrective to
buying first and thinking later, not an argument that tools never help.
