# Brunel University London — ISO 27001 documentation audit

**Module:** 12 (ISO 27001 Lead Auditor) · **Role:** Lead auditor · **Result:** 10/10

## Engagement

The course asked for a documentation audit of Brunel University London's ISMS policy set, which is publicly available, against ISO/IEC 27001:2013. The policy set covered governance, the ISMS roles and responsibilities, information asset owners, remote working, cryptography, acceptable use, information classification, and the information risk management policy and methodology (IRM01/IRM02). The documents are Brunel's own; [Brunel publishes them](https://www.brunel.ac.uk/) and they are not reproduced here.

The course assessed this as a ten-question quiz. Below are my answers and the audit point behind each. After that I note the findings I would raise in a real engagement.

## Answers and audit reasoning

| # | Question area | Answer | Why it matters to an auditor |
|---|---|---|---|
| 1 | Aim of the Information Security Policy | Protect information assets from all threats | The top-level policy sets direction (clause 5.2). Narrower documents handle specific topics. |
| 2 | What IAOs are *not* responsible for | Developing encryption algorithms | IAOs handle labelling, handling, risk management and reporting to the SIRO. Approved cryptography comes from the Cryptographic Policy, and nobody writes their own algorithms. |
| 3 | A principle of the policy | Defined roles and responsibilities | Clause 5.3, supported by BUL-POL-6.1.1 |
| 4 | Policy governing encryption | Cryptographic Policy | A.10.1 (2013) → A.8.24 (2022) |
| 5 | Basis of risk assessment | Confidentiality, integrity, availability | IRM02 scores impact against C, I and A |
| 6 | Ultimate accountability | Executive Board | Top management stays accountable (clause 5.1). Others carry out the work. |
| 7 | What to do with an identified risk | Record it in the register and apply controls | Clause 6.1.3. Applying controls is only one treatment; accepting a risk within appetite is valid if the acceptance is recorded. |
| 8 | Remote access from non-Brunel computers | Connect Portal VPN only | A.6.2.2 (2013) → A.6.7 (2022) |
| 9 | IAO delegating | Keeps accountability | Tasks can be delegated, accountability cannot. Look for a delegation record. |
| 10 | Standard aligned to | ISO/IEC 27001:2013 | Document numbering follows the 2013 Annex A |

## Findings I would raise

The quiz only covers what the policies *say*. An audit also needs evidence that they are followed. From the documents alone I would raise the following, and verify each one in fieldwork:

1. **Transition to 27001:2022 (potential major NC if certification is in scope).** The policy set is structured around the 2013 standard, and 2013 certificates expired on 31 October 2025. I would check:
   - whether the SoA has been rebuilt against the 93 controls;
   - whether the 11 new controls were assessed, including threat intelligence, cloud services, data masking and secure coding;
   - whether the new clause 6.3 (planning of changes) is addressed.

   If none of that has been done, and the university claims conformity to the 2022 standard, this is a systemic gap.
2. **Document control (clause 7.5).** Several documents are at v1.0 or v1.1. Each needs evidence of a recent review, an owner and an approval date. A policy that has not been reviewed since 2013-era alignment would fail the "reviewed at planned intervals" expectation.
3. **Remote working depends on the VPN alone.** A VPN protects the connection, not the endpoint. For non-Brunel computers I would ask for evidence of device posture checks, restrictions on downloading data, or virtual desktop use. Without one of these, data classified as confidential can end up on unmanaged devices. I would raise this as an OFI, or as a minor NC if the risk register rates the risk higher than its treatment covers.
4. **Accountability chain from the Executive Board to the IAOs.** The governance chain is well defined on paper. I would sample:
   - Executive Board minutes, for clause 9.3 management review inputs and outputs;
   - SIRO reports, to confirm the IAO reporting route actually runs;
   - IAO delegation records, to back up question 9.
5. **Risk acceptance.** I would sample the risk register for low risks that were accepted, and check each has a named risk owner who signed off and a review date. Without these, "ignore it if it's low" becomes the practice even though the policy says otherwise.

## Lessons

- Document numbering is evidence. You can spot a 2013-aligned ISMS before reading a word of the content.
- Reviewing documents shows the design. Conformity also needs records, interviews and samples, so a documentation-only audit should be labelled that way in its scope.
