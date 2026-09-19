# Why organisations fail at asset management

> Module 04, lesson 6. Five reasons the foundation stays broken, and the one that
> gets organisations breached.

## Summary

Asset management matters because you can't sensibly protect what you haven't
identified — the firewalls and the antivirus are being bought to defend something,
and it's fair to ask what. Yet most organisations fail at it. The lesson works
through why.

**It's genuinely hard.** A multinational bank with many branches and separate IT
departments cannot easily maintain one central record. Large organisations
routinely have hundreds of thousands of assets across software, hardware,
applications and people. The scale alone defeats casual effort.

**Nobody wants to own it.** The security team is busy with tickets and attacks,
underfunded, and has no visibility across the whole business anyway. The IT team
often doesn't see the value, and even where it keeps a list of IT assets, it has
no idea what marketing or HR are running. Add politics between departments that
don't communicate well, and the work has no natural home.

**Over-reliance on automation.** Rather than talking to departments, teams run a
network scanner, get a list of everything responding on the network, and call it
asset management. Scanning is useful and incomplete — and a hostname or serial
number still carries no context. Assets have to be classified by criticality and
sensitivity, and the owner and the person responsible for maintaining each asset
must be recorded. Large organisations do stop at the scan and call it done.

**It isn't a one-off.** Organisations continuously buy software and hardware,
decommission things, and acquire whole estates through mergers. Asset
identification has to be repeated — every six to twelve months, or eighteen at the
outside — or the record decays.

**Completeness is the hardest part.** Even with consultants interviewing across
the organisation, did they reach the branches in other locations? Did they capture
the cloud instances the marketing department spun up? This is where the real
failure lives — and it's how organisations get breached: someone in some
department buys something, forgets about it, nobody secures it, and that's the way
in.

The closing advice: treat this as ongoing, keep having the conversations, and
don't hesitate to bring in external help, because it's a difficult process.

## Key concepts

| Concept | What it means | Why it matters in practice |
| --- | --- | --- |
| Scale | Hundreds of thousands of assets across dispersed business units | Explains why effort alone doesn't solve it |
| Ownership vacuum | Security lacks visibility, IT lacks the remit, neither wants the job | Without an owner it's nobody's deadline |
| Departmental politics | Teams that don't share information readily | A discovery process that depends on cooperation fails where cooperation is absent |
| Scanner ≠ inventory | Network discovery returns what responds, without meaning | Finds unknown devices; can't tell you value, owner or purpose |
| Asset owner | The named person accountable for an asset, and whoever maintains it | Missing from technical discovery, and essential to everything downstream |
| Periodic re-identification | Repeating the exercise every 6–18 months | The estate changes constantly through purchases, decommissioning and acquisitions |
| Completeness | Whether the exercise actually reached the whole organisation | The failure mode that leads to breaches |
| Shadow purchases | Systems bought by a department outside IT's knowledge | Unsecured, unmonitored, and a common initial access route |

## Where this shows up in a real job

The shadow purchase pattern is one I've seen the small version of repeatedly. A
department wants something the official route doesn't provide quickly, buys a tool
or spins up a site, and it exists outside every process — no patching, no
monitoring, and often no one who remembers the login. In WordPress terms it's the
staging site someone stood up two years ago, still public, still running the
plugin versions of the day it was built.

The ownership vacuum also matches something I've observed from the support side.
When a problem sits between two teams' remits, it doesn't get half-solved by both
— it gets ignored by both, and resurfaces indefinitely. Asset management is that
dynamic at organisational scale.

I'd be honest in an interview that my exposure is to small estates, not to
hundreds of thousands of assets across a bank's branch network. The dynamics
described here I recognise; the scale I've only read about.

## My take

The most important claim is the one made almost in passing: **this is how
organisations get breached.** That connects asset management to something people
care about. A forgotten system is unpatched by default, unmonitored by default,
excluded from every access review, and absent from the risk assessment — not
because anyone decided that, but because none of those processes knew it existed.
An attacker needs one of those. That's the argument to make when asking for
funding, and it's far stronger than an appeal to good practice.

Three things:

**The scanner limitation is worth stating precisely, because scanners are still
valuable.** A network scan answers "what is responding on this network" — which is
genuinely useful and finds things nobody declared. It cannot answer what something
is for, who owns it, what it would cost to lose, or whether it's sensitive. And
it's blind to whatever isn't on the network it scans: SaaS subscriptions, cloud
accounts on someone's card, an office it can't reach. The right use is as one
input to be reconciled against the interview findings, with the *differences*
being the interesting part. Assets the scan found that nobody claimed are the
highest-value finding available.

**The ownership vacuum is the root cause, and the others follow from it.** Scale
makes the job hard, but organisations do hard things when someone is accountable
for them. Nobody owns this, so it's done badly by whoever has least ability to
refuse. Any realistic recommendation has to name an owner with the authority to
ask other departments for answers — which usually means it sits above the security
team rather than inside it.

**Periodic isn't quite enough on its own.** A twelve-month cycle means a system
bought in month two spends ten months invisible. The cycle is the safety net; the
better control is catching assets at the point they're created — procurement
requiring an owner and classification before purchase, cloud accounts provisioned
centrally, a joiner-mover-leaver process that covers systems and not only people.
Periodic review then finds what slipped through, rather than being the only
mechanism.

There's a candid point in the lesson worth noticing too: the advice to bring in
external consultants comes from a consultant. It's still probably right — an
outsider can ask across departmental lines in a way an internal team can't, and
politics is one of the stated obstacles. Worth recognising the shape of the
recommendation regardless.
