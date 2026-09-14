# Cyber security audit in the real world

> Module 03, lesson 3. What audit is for, and where the work actually sits
> depending on how big the organisation is.

## Summary

Audit exists for two reasons.

**Assurance.** The board isn't involved in the daily running of IT and security,
so it needs a summary it can trust — reports from first, second and third line
setting out not just what the controls are but how the work was validated. The
audit trail *is* the credibility.

**Compliance validation.** The other reason audit appears is a standard that has
to be met. A financial services firm handling credit card data has to comply with
PCI DSS, and auditors come in to confirm the controls and processes genuinely
meet it.

Where that work lives depends almost entirely on organisation size.

**Large organisations** — multinational banks especially, but also big government
bodies in the US and parts of Europe, and large healthcare organisations — build
it in. There'll be a substantial second-line audit team doing nothing but auditing
first line, all year. Inside the security team itself there may be someone whose
entire job is first-line audit; it's a specialism in its own right. And there'll
be an internal audit function, which isn't only cyber — it covers financial and
accounting audit too — with cyber-skilled people inside it auditing lines one and
two.

**Smaller and mid-sized organisations** can't staff that. Their security teams are
small and mostly doing technical work: penetration testing, incident response.
Self-auditing isn't done well because nobody has the time or the remit. So they
buy it — typically an annual engagement from a consulting firm, often one of the
Big Four (Deloitte, PwC, EY, KPMG). An auditor embeds for a month or two, works
alongside the team while belonging to a different company, and produces a report
of findings.

And in practice, the word "audit" tends to surface whenever a standard is in
play — privacy law, the ISO standards, CPS 234 in Australia, GDPR in Europe.
Auditors both help organisations get compliant, and get hired to confirm that they
are.

## Where the work sits, by organisation size

| | Large / regulated | Small to mid-sized |
| --- | --- | --- |
| First-line audit | Often a dedicated role inside the security team | Rarely happens; the team is busy on technical work |
| Second line | A standing team auditing first line year-round | Thin or absent |
| Third line | Internal audit function covering finance, accounting and cyber | Usually none |
| External help | Used for specific mandates | The main source of audit — an annual engagement |
| What triggers it | Continuous, plus regulatory cycles | A standard, a customer requirement, or a renewal date |

## Key concepts

| Concept | What it means | Why it matters in practice |
| --- | --- | --- |
| Assurance reporting | Summarising control status and how it was validated, for the board | The board can't inspect; the report is the whole channel |
| Compliance validation | Auditing against a named standard rather than in general | Changes the question from "is this good?" to "does this meet the clause?" |
| Audit as a specialism | A distinct career track within security, not a task people do on the side | Doing it properly needs dedicated time and a defined remit |
| Internal audit's breadth | Covers financial and operational audit as well as cyber | Cyber auditors sit inside a much older profession with its own standards |
| Embedded external auditor | A consultant working alongside the team but employed elsewhere | Independence comes from the employer, not the desk they sit at |
| Standards as the trigger | PCI DSS, ISO, GDPR, CPS 234 and similar | Audit demand follows regulation more than it follows risk |

## Where this shows up in a real job

Helium Health had the shape this lesson describes for a mid-sized organisation.
The ISO 27001 work was first-line effort plus outside help, with the certification
body providing the independent validation at the end. There was no standing second
line and no internal audit function, which at that size is normal rather than a
failing — but it means the assurance arrives once a year in a burst, rather than
continuously.

This lesson is also the most directly useful one yet for the pivot I'm making,
because it's a map of where these jobs exist. Dedicated cyber audit roles cluster
in regulated industries — financial services, healthcare, government — and in the
consultancies that sell audit to everyone else. Malta's economy leans heavily on
financial services and iGaming, both regulated, and the Big Four all operate here.
That's worth knowing when deciding what to apply for.

What I can't claim is audit experience. I've been audited, and I've prepared
evidence for an auditor, which gives me a working sense of what good evidence
looks like from the receiving end. That's a starting position, not a qualification.

## My take

The two purposes aren't equally weighted in practice, and the lesson quietly says
so: audit demand follows *regulation* more than it follows risk. That's worth
understanding without being cynical about it. Compliance is often the forcing
function that gets security funded at all, which is the same point module 1 made
about compliance generally. But it means the controls that get audited most
thoroughly are the ones a standard names, not necessarily the ones carrying the
most risk — so an organisation can have beautifully audited card handling and an
unexamined supplier estate.

Two more things:

**Independence comes from the employer, not the seating plan.** An embedded
consultant who sits with the team for two months and eats lunch with them is still
independent in the way that matters, because their pay and their professional
standing come from elsewhere. Conversely, an internal team that reports to the
person whose work it reviews isn't independent no matter how far away its desks
are.

**The recurring pattern: the same firms help you comply and check that you
complied.** This is the third time the course has circled this — advisory versus
assessment in consulting, advise-and-challenge inside second line, and now
consultancies on both sides of a standard. It seems to be a structural feature of
the industry rather than an occasional lapse, and the professional answer is
separation of engagements and of teams rather than pretending the tension isn't
there. Worth being able to talk about, since it's the kind of thing an interviewer
asks to see whether you've thought about the business you're joining.

**The size split is a career map.** Large regulated organisations have dedicated
audit roles and a route from first line into second and third. Smaller
organisations have no such ladder but far broader exposure, because one person
covers everything. Both are reasonable entry points into GRC, and they lead to
quite different second jobs.
