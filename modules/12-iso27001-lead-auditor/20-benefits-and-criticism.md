# Lesson 20 — Benefits and criticism of ISO 27001 certification

## Summary

Getting certified pushes an organisation into habits it should have anyway: it thinks about risk, runs risk assessments consistently, follows treatment through to closure, and builds governance the board can see. Security teams also use certification as a lever to get budget. The lesson covers three common criticisms:

- **Implementers and auditors make mistakes.** The instructor says this applies to everything humans do, so it is not a reason to avoid the standard.
- **"We're too busy for paperwork."** This is fair for an immature organisation that still lacks basics like MFA: fix those first. It stops being an excuse once the organisation wants a mature, end-to-end programme it can report to the board and customers.
- **Certificates vary in quality.** Inexperienced auditors, one-person firms and "certified in two weeks" offers mean a certificate on its own proves little.

The takeaway: ISO 27001 is worth doing for organisations that take security seriously, and any certificate still gets trust-but-verify treatment.

## Key concepts

| Benefit | Mechanism |
|---|---|
| Risk-based thinking | Clauses 6.1.2 and 6.1.3 require repeatable assessment and treatment |
| Risks get closed | Risk owners approve the treatment plan and accept residual risk |
| Board-level visibility | Management review (9.3) and top-management accountability (5.1) |
| Funding lever | An external deadline and a customer requirement justify spending |
| Market access | Customer, tender and supply-chain requirements |

## Where this shows up in a real job

- Vendor due diligence (module 9). A certificate starts the conversation; it doesn't end it. Check that:
  - the issuing body is accredited (IAF CertSearch);
  - the scope covers the service you are actually buying;
  - the SoA shows which controls apply, and the dates are current.
- Advising a startup. If MFA, backups and patching aren't in place, spend the first budget there. The NIST CSF is a reasonable way to structure that work before certification.

## Where I'd push back

- **The strongest criticism is structural, not about people.** A certificate shows the *management system* conforms. It does not show the organisation is *secure*. Audits are sampled, happen at a point in time, and cover only the declared scope, and a scope can be cut down to the easy parts. Certified organisations still get breached. This is why "read the scope and SoA" matters more than "check the logo".
- **Much of the documentation burden is self-imposed.** Clause 7.5.1 says the amount of documented information depends on the organisation's size, complexity and competence. The standard does not require meeting agendas. It requires evidence of results, for example management review outputs (9.3.3). An organisation that says it's drowning in paperwork has often documented to what an auditor expects, not to what the standard requires.
- **The two-week certificates are usually unaccredited, not just poor quality.** An accredited body can only certify after a Stage 1 and a Stage 2 audit with records of the ISMS in operation (internal audit and management review included), so it physically can't certify in two weeks. Checking accreditation filters out most of these mills.
- **NIST CSF and ISO 27001 are not alternatives.** The CSF can't be certified against. It is a good way to structure and measure the programme. ISO 27001 is the management system you can certify. Many organisations map one to the other.
- **SOC 2 is not a standard or a certification.** It is an attestation report issued by a CPA firm under AICPA criteria. It is still useful, and it answers a different question: did these controls operate over a period?

## My take

"Certified" means "has a working management system, as sampled by someone accredited to sample it." That is valuable, and it is narrower than it sounds. From the buyer's side, I read the scope, SoA and dates before I trust the badge. From the implementer's side, I document to the standard's requirements, not to an auditor's wish list, and I don't let certification work delay a basic control that's missing.
