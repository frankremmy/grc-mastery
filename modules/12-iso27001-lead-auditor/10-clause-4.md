# Clause 4 — context of the organisation

> Module 12, lesson 10. _First document of the ISMS, and the one place I'd
> disagree with the model answer._

## The method

Work the spreadsheet clause by clause: read the requirement, then either create
the document it needs or perform the process it describes.

Clause 4 has four requirements — 4.1 internal and external issues, 4.2 interested
parties, 4.3 the ISMS scope, and 4.4 the ISMS itself. **They go into a single
document: the ISMS Scope.**

Worth being clear why that's allowed. **ISO tells you what must be satisfied, not
how many documents to write or how to organise them.** Document structure is the
implementer's choice. One document per clause is a methodology, not a
requirement — and combining clause 4 into one artefact works because the four
requirements are genuinely one idea: what are we certifying, and in what context.

Clause 4.4 needs no separate artefact. It's satisfied by building the ISMS.

## The document

**Document control table on the front page:** date, version, author, description,
approved by, last updated, review frequency, next review. Every ISMS document
carries it.

This isn't just tidiness. The standard requires continual review and improvement,
so a document has to record who reviewed it, who approved it, and — the part
people forget — **when it will be reviewed again**. Review frequency is an
explicit expectation.

**Purpose section**, stating plainly what the document does. The methodology
behind it is clarity: a reader should be in no doubt what the document covers.
That's a good general habit for security writing, not just for ISO.

**Scope statement**, built in widening layers:

1. The activity — design, development, deployment and maintenance of the
   cloud-based SaaS marketing platform
2. The resources — all processes, personnel, systems, infrastructure and
   information assets directly involved in delivering the service
3. The environments — development environments, production systems hosted on
   AWS, supporting internal tools
4. The third parties — relevant third-party services and vendors supporting the
   operation and security of the platform

Each layer could have been the end of the sentence. Continuing is the point:
specificity over breadth. Layer 4 matters particularly because both the clauses
and Annex A call out outsourced services, and Stark runs on AWS.

**Context — internal issues:** a small team and limited budget, which *may*
impact the ability to dedicate resources to security initiatives. The hedging is
deliberate — it's a constraint, not a catastrophe.

**Interested stakeholders**, as a table of role and requirement. CEO,
Information Security Manager, Information Security Analyst, Cyber Security GRC
Analyst, Software Developer, IT Infrastructure Engineer, plus **AWS** and
**customers** as external parties.

**Job titles, not names.** People resign and new people are hired; the role
persists. The document stays accurate without being reissued every time someone
leaves.

**A deliberate trap in the roles:** the project has both an "Information Security
Analyst" and a "Cyber Security GRC Analyst", which is confusing on purpose.
Titles in this industry are inconsistent and frequently interchangeable, so the
stakeholder table states what each role actually does rather than relying on the
title to convey it. Read the responsibilities, not the job title.

**External issues:** no legal, regulatory or contractual obligations applicable
to the scope — because the platform handles public marketing data.

## Where I'd push back

The external issues section is a single sentence saying nothing applies, and the
lesson itself flags this as "slightly unusual". I think it's more than unusual —
I'd have written it differently, for three reasons.

**Contractual obligations exist and the same document names them.** The
stakeholder table records that customers "may require ISO 27001 certification for
procurement", and the project brief says certification is a *condition* of
procurement. That is a contractual obligation. So is the AWS Customer Agreement,
which carries security-relevant terms and defines the shared responsibility
boundary. A document that lists customer requirements on one page and declares no
contractual obligations on the next is internally inconsistent.

**Regulatory obligations are unlikely to be genuinely zero for a New York SaaS
company.** New York's SHIELD Act requires reasonable safeguards for private
information of NY residents. A marketing automation platform sending email
engages CAN-SPAM. And if any client operates in the EU or UK, GDPR can reach
Stark as a processor through that client — which loops back to the untested "no
PII" assumption I flagged in the project profile.

**This section feeds two things downstream.** Clause 4.2's requirements flow into
the clause 6.1 risk assessment, and **A.5.31 covers legal, statutory, regulatory
and contractual requirements** — a control that will be hard to evidence if the
context document says there are none. An empty legal and regulatory register is
an easy thing for an auditor to probe, and "we determined none apply" needs to
show the determination was made rather than assumed.

**What I'd write instead:** the same conclusion, but arrived at visibly. List the
obligations considered — privacy law in the states where customers operate,
email marketing regulation, the AWS agreement, customer contractual security
requirements — and record the assessment against each. If most genuinely don't
apply at this scope, saying so explicitly is stronger than saying nothing
applies, and it demonstrates the analysis the clause is actually asking for.

## Two things I'd add to the document

**State what is out of scope, not only what is in.** The scope statement is
precise about inclusions and silent on exclusions. For a deliberately narrow
scope, the exclusions are the half that prevents misreading — corporate IT,
finance and HR systems, the company's own internal network. This is the same
issue I read from the outside in the Monash certificate: it names two platforms,
and the reader has to infer that the rest of the university isn't covered. Naming
the exclusions removes the inference.

**Keep a title-to-person register somewhere.** Using job titles is right, but in
a six-person company an auditor will want to know who currently holds each role.
That mapping belongs in a maintained register — logically in the roles and
responsibilities document under clause 5.3 — so the scope document stays stable
while the names stay traceable.

## My take

The reusable thing here is the **scope statement pattern**: activity → resources
→ environments → third parties. Four layers, each narrowing ambiguity, ending
with the outsourced services that every framework cares about and most scope
statements forget. That transfers to any organisation.

The deeper point is that clause 4 is where a certification either becomes
meaningful or becomes decoration. Everything downstream — the risk assessment,
the control selection, the exclusions in the SoA, what the certificate ultimately
attests to — inherits the boundary drawn here. Which is why a thin external
issues section bothers me: it's cheap to write, it's read by an auditor, and it's
the foundation for a control the organisation will have to evidence later.

**Repo note:** the course's Clause 4 document is its own material and stays out of
the repo. My version for Stark Industries, written from scratch, goes in
`deliverables/`.
