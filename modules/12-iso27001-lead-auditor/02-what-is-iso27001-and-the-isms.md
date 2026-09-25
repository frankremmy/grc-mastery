# What is ISO 27001 and the ISMS?

> Module 12, lesson 2. _The standard, the management system it asks for, and the
> thing that makes ISO different from every other framework in this course._

## Summary

ISO is the International Organization for Standardization — a body publishing
standards across an enormous range of subjects. ISO 27001 is the one for
information security, published jointly with the IEC, which is why it appears as
**ISO/IEC 27001**.

**Full title:** *ISO/IEC 27001:2022 — Information security, cybersecurity and
privacy protection — Information security management systems — Requirements.*
You'll see it written as ISO 27001, ISO 27001:2022 or ISO/IEC 27001; all the same
standard. **History:** published 2005, first major revision 2013, current version
2022.

**The purpose** is to help organisations of any size or sector identify and
assess information security risks, implement appropriate controls, meet
regulatory obligations, build trust with customers, partners and regulators, and
continually improve. All of it aimed at the CIA triad — confidentiality,
integrity and availability.

### The ISMS

An **Information Security Management System** is a systematic framework of
policies, processes, procedures, people and technologies used to manage and
protect an organisation's information assets. ISO/IEC 27000 clause 3.2 puts it
more tersely: *a management system for establishing, implementing, maintaining
and continually improving information security.*

It covers **people** (roles, responsibilities, awareness), **process** (secure
procedures, followed and kept current) and **technology** (the controls
themselves — encryption, firewalls, detection). Security is not an IT problem
with an IT solution, and treating it as one is the characteristic junior GRC
mistake.

**Core components:** scope; risk assessment; controls; policies and procedures;
training; monitoring and internal audit; improvement.

### Key elements of the standard

| Element | What it is |
| --- | --- |
| ISMS — clauses 4 to 10 | The management system requirements; the certifiable part |
| Risk-based approach | Identify, assess and treat information security risks |
| Annex A controls | 93 reference controls grouped into 4 themes |
| Statement of Applicability (SoA) | Declares which Annex A controls are in use, and why |
| Internal audits | Regular assessment of ISMS performance |
| Continual improvement | Feedback loops that evolve security maturity |

### What makes ISO different

Frameworks give a comprehensive view and reveal blind spots — an organisation can
have firewalls, penetration testing and a decent password policy and still be
missing whole categories of control. The standard forces you to consider every
Annex A control and **justify both the ones you selected and the ones you
didn't**, which is what the SoA records.

ISO then goes further than NIST CSF: **certification**. With NIST you assess,
implement and document. With ISO, once the ISMS is in order, an accredited
external auditor can certify the organisation. That gives assurance to customers
that their information is handled properly, and assurance to senior management
that critical assets have been assessed and protected.

**Who uses it:** SaaS companies, financial services, healthcare providers,
government agencies — any business handling sensitive or valuable information.

### The caveat that matters most

**Everything is subject to a scope.** When a GRC professional starts work with an
organisation running ISO 27001, the first thing to ask for is the ISMS — and the
first thing to read in it is what the scope actually covers.

### The ISMS cycle

The management system runs as a loop rather than a project:

```
        ┌──────────────► Scope ──────────────┐
        │        define what the ISMS covers  │
        │                                     ▼
   Improvement                          Risk Assessment
   correct nonconformities,             identify and evaluate
   update processes                     information security risks
        ▲                                     │
        │                                     ▼
        └────────────── Controls ─────────────┘
                 apply security measures
                   (e.g. Annex A controls)
```

Scope decides what is in. Risk assessment finds what threatens it. Controls treat
what was found. Improvement corrects what didn't work — and feeds back into
scope, because the organisation changes.

## Key concepts

| Concept | What it means | Why it matters in practice |
| --- | --- | --- |
| ISO 27001 | The international standard for information security management | The certifiable one; why it comes up in sales conversations |
| ISO 27001:2022 | Current version (2005 → 2013 → 2022) | Describing the 2013 structure dates you |
| ISMS | The management system, not just its paperwork | The artefact to ask for first |
| Scope | What the ISMS and any certificate actually cover | The single most important thing to check |
| Clauses 4–10 | The management system requirements | What certification is actually assessed against |
| Annex A | 93 reference controls in 4 themes | Selected from, not implemented wholesale |
| Statement of Applicability | Which controls are in use and why; exclusions justified | Mandatory document; tells you what was actually implemented |
| Risk-based approach | Controls follow from assessed risk | Stops the standard being a checklist |
| Internal audit | Regular self-assessment of the ISMS | Clause 9; a certification prerequisite |
| Continual improvement | Nonconformities corrected, controls updated | Clause 10; what auditors look for evidence of |

## Where this shows up in a real job

The scope point is one I've already hit from the other side. In the Horizon Labs
supplier assessment I flagged that an ISO 27001 certificate has to be read
alongside its scope statement, because a certificate can cover a different legal
entity, location or service line than the one you're buying. This lesson confirms
it from the practitioner's direction: scope is the first thing the standard's own
people check.

The people-and-process framing also lands against the capstone. Oscorp's biggest
problems weren't technical — no owner, no policy, no risk process, no defined
roles. If Oscorp pursued certification, the ISMS work would force exactly those
gaps into the open, which is a fair argument for certification as a forcing
function rather than only as a badge.

## My take

**"The ISMS is documentation" undersells it, and the distinction matters.** The
documentation is *evidence* of the management system; the management system is
the set of processes actually running. That gap is the difference between a real
ISMS and a paper one, and it's the same design-versus-operating-effectiveness
point from the audit module. An auditor doesn't only read the policy — they look
for records proving the process ran: meeting minutes, review dates, completed
risk assessments, closed corrective actions. An organisation can have a
beautifully written ISMS and fail an audit because nothing in it has happened for
a year.

**The SoA is the document I'd ask a supplier for, not the certificate.** The
certificate tells you they passed. The SoA tells you *what they implemented* and,
more revealingly, what they excluded and on what grounds. A supplier assessment
that stops at "they're ISO 27001 certified" has learned much less than it thinks.

**Certification quality depends on who issued it.** A certificate is only as good
as the certification body behind it, and bodies are meant to be accredited by a
national accreditation body. An unaccredited certificate is a document someone
sold. So reviewing a supplier's ISO 27001 claim means checking three things: the
scope statement, the accreditation mark, and the SoA.

**One caution on the material's framing.** It lists "ensure regulatory compliance
(e.g. GDPR, SOC 2)" as a purpose. ISO 27001 *supports* compliance and overlaps
substantially with both, but it does not deliver either — GDPR is law with
obligations ISO doesn't cover, and SOC 2 is a separate attestation under a
different framework with different criteria. Certification is evidence of good
practice, not a compliance certificate. Worth keeping straight, because
conflating them is a common sales claim.

**The cycle as drawn skips a step.** It runs Controls → Improvement, but you
cannot correct nonconformities you have not detected. Between applying controls
and improving them sits performance evaluation — monitoring, measurement and
internal audit, which is clause 9 and its own mandatory part of the standard. The
core components list includes monitoring; the diagram compresses it. Worth
holding onto, because "we implemented controls and we fix things when they go
wrong" describes most immature organisations, and what makes an ISMS a management
system rather than a set of controls is precisely the measurement step that finds
the problems before someone else does.

**A currency note.** ISO published Amendment 1 to ISO 27001:2022 in 2024, adding
climate change considerations to the context clauses. Minor in substance, but
knowing the standard has moved since 2022 signals that I follow it rather than
having read about it once.
