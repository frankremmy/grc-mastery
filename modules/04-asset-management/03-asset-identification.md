# Asset identification

> Module 04, lesson 3. The first step: finding out what's actually there, by
> asking people.

## Summary

Asset identification is the step where you identify and document every asset the
organisation owns. The goal is a view of the key critical assets, which is
impossible without first knowing what exists at all.

The lesson is blunt about how badly this usually goes, and bigger organisations
are worse rather than better. Undocumented applications are routine. The image
that sticks: servers that have been running for years, nobody knows what they do,
and everyone is afraid to switch them off.

**The method is conversations.** For a small insurance company, you start with the
IT department, because IT can usually produce a list of applications, software and
some of the hardware. But that list is a starting point, not the deliverable —
names of software, names of databases, version numbers. That's an inventory of
stuff. Asset management means assigning value and meaning to it, which is the
categorisation and classification that comes next.

The lesson also widens the scope. For an insurance company, software and hardware
may genuinely be all there is. Other businesses have intellectual property — the
secret recipe. And "hardware" can mean far more than laptops and servers: **SCADA
and industrial control systems**, found in oil and gas, energy, manufacturing, food
and drink. Machinery in a vineyard, equipment in agriculture. The test offered is
simple — any machine connected to the local network is in scope.

Once the list is collected, it has to be documented somewhere, which is the CMDB
lesson.

## Key concepts

| Concept | What it means | Why it matters in practice |
| --- | --- | --- |
| Asset identification | Finding and documenting every asset the organisation owns | The first step of asset management, and the input to everything after |
| Interviews as the method | Starting with IT, then other teams, to build the picture | Discovery is a people problem before it's a tooling problem |
| A list is not asset management | Software names and versions without value or meaning attached | The raw list is where the work starts, not where it finishes |
| Undocumented assets | Applications and servers nobody has a record of | Extremely common, and worst in large organisations |
| The server nobody dares turn off | A running system with no known purpose and no owner | The clearest symptom of failed asset management |
| Industry-specific assets | Intellectual property; SCADA and industrial control systems | Scope depends on sector — an insurer and a winery need different lists |
| "Connected to the network" | The practical test for whether a machine is in scope | Keeps operational technology from falling outside the exercise |

## Where this shows up in a real job

The "nobody knows what it does, nobody will turn it off" pattern is completely
familiar. In WordPress work it's the plugin nobody recognises that can't be
deactivated because the last person who tried broke checkout. Same dynamic: an
asset with no documented purpose, no owner, and a change nobody wants to sign for.

Discovery-by-conversation also describes a lot of support escalation. Working out
what a site is actually running usually means asking the client, the agency, and
the previous developer, and getting three partial answers that have to be
reconciled. The technical tooling tells you what's installed; only people can tell
you what it's *for*.

The industrial control systems point is genuinely new to me. I have no OT
experience and wouldn't claim any — it's worth flagging as a gap, since energy and
manufacturing are exactly the regulated sectors where GRC roles concentrate.

## My take

The distinction I want to keep is between **an inventory and an asset register**.
IT can hand over a list of software, versions and databases in an afternoon. That
list can't tell you what to protect first, because it has no owner, no business
purpose, no data classification and no criticality against it. Turning the one
into the other is the actual job, and it's why this can't be fully automated —
scanning tools find what exists, but only a person can say what it's for and what
it would cost to lose.

Two things:

**The server nobody will switch off is an asset management failure and a risk
finding at once.** It's unpatched by default, monitored by nobody, owned by
nobody, and still connected. Both the artefact and the fear around it are evidence
— the fear exists precisely because no one can predict what breaks, which is the
absence of documentation showing itself. It's a good example to have ready, since
it makes the abstract case for inventory concrete in one sentence.

**Sector determines scope, so the first question is what business this is.** An
insurer's list is software and hardware. A manufacturer's includes control systems
that may be decades old, unpatchable, and safety-critical. A research company's
centre of gravity is intellectual property. Arriving with a generic asset checklist
and no sense of the business produces a list that misses whatever matters most —
which is the same lesson the Oscorp applicability analysis taught about
regulations.

**Interviews are the method, which means the output depends on who you ask.** IT
knows what it manages. It doesn't necessarily know about the SaaS tool a
department bought on a card, the spreadsheet the finance team runs on, or the
cloud account a developer opened for a trial. Starting with IT is right; stopping
there produces a confident list of everything IT already knew about.
