# Lesson 18 — Types of ISO 27001 auditors

## Summary

There are four auditor roles in an ISO 27001 context. Three of them describe who the audit is for: the organisation itself, a customer, or a certification body. The fourth, the lead auditor, describes who runs the audit. Any audit, internal or certification, needs someone leading it, even when that person is the only auditor.

## Key concepts

| Role | Audit party | Who they work for | Output |
|---|---|---|---|
| Internal auditor | First party | The organisation (staff or contracted) | Findings for management review (clause 9.2 → 9.3) |
| Customer / supplier auditor | Second party | A customer or other interested party | Assurance for a contract or supply-chain decision |
| Certification auditor | Third party | An accredited certification body | Certification decision |
| Lead auditor (audit team leader) | Any of the above | Whoever commissioned the audit | Audit plan, team direction, consolidated report |

- **Internal auditor.** This audit is mandatory under clause 9.2. Objectivity and impartiality are what count, not being from outside the company: the auditor must not audit their own work. A consultancy doing a pre-certification readiness audit is still doing a first-party audit, because it acts on the organisation's behalf.
- **Second-party auditor.** A customer checks you against *their* requirements, usually only the controls the contract cares about. When I ran the Horizon Labs vendor assessment in module 9, I was acting as a second-party auditor.
- **Third-party auditor.** Works for a certification body, which is accredited against ISO/IEC 17021-1 and 27006. The audit runs as Stage 1, then Stage 2, then annual surveillance audits, with recertification every three years.
- **Lead auditor.** Plans the audit, assigns work, consolidates findings and reports them. ISO 19011 calls this role the *audit team leader*.

## Where this shows up in a real job

- Entry-level GRC roles usually start by preparing for audits: building evidence, maintaining the SoA, and sitting in on the certification body's interviews. The next step is joining an audit team. Leading one comes only after several audits.
- When a vendor sends an ISO certificate, check two things: who issued it, and whether that issuer is accredited. Then read the scope and the SoA (see module 9).
- On the customer side, second-party audit rights belong in the contract (a right-to-audit clause). Without that clause, you get only what the vendor chooses to share.

## Where I'd push back

- **"External auditor" and "second party" are not synonyms.** In ISO 19011 terms, *external* audits include both second-party audits (by customers) and third-party audits (by certification bodies). A cleaner split is first, second and third party, defined by who the audit serves, not where the auditor sits.
- **Accreditation applies to the certification body, not the individual auditor.** National accreditation bodies that are members of the IAF (UKAS in the UK, ANAB in the US, NAB-Malta here) accredit the certification body. The certification body then has to show its auditors are competent under 17021-1 and 27006. This also explains the "questionable certificates" warning: a certificate from an *unaccredited* body proves very little. **IAF CertSearch** is the database to check.
- **Stage 1 is more than document review.** It also confirms scope, readiness and site specifics, and plans Stage 2. A Stage 1 finding can delay Stage 2.
- **"Must be a trained ISO 27001 Lead Auditor" is industry practice, not something the standard requires.** No clause demands a lead auditor course certificate, especially for internal audits. Certification bodies set their own competence criteria. In practice, though, the credential plus logged audit experience is what gets you hired.
- **Brand note:** SAI Global's assurance business now trades as Intertek SAI Global.

## My take

The useful question is who the audit is for. That one answer tells you what the auditor is checking against, who receives the report, and what happens with the findings. "Lead auditor" is a role on any of those audits, not a fourth kind of audit. The lesson's point about experience holds: this course qualifies me to sit on an audit team, and audit hours are what will qualify me to lead one.
