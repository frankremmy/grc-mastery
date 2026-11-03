# Lesson 22 — The seven audit principles (ISO 19011)

## Summary

ISO 19011 sets out seven principles that keep audit results reliable, objective and consistent. They describe how a good security professional behaves in general, not only how an auditor behaves. The lead auditor has to follow them personally and make sure the team does too. In practice that means picking competent, impartial people, managing conflicts of interest, protecting evidence, checking that evidence is sufficient, reporting the audit's limitations, and putting effort where the risk is.

## Key concepts

| # | Principle | In one line | What it looks like in practice |
|---|---|---|---|
| 1 | Integrity | Work honestly within your competence and stand by your findings under pressure | Refuse to downgrade a nonconformity that the evidence supports |
| 2 | Fair presentation | Report what actually happened, including limitations and disagreements that weren't resolved | State "records X were unavailable" instead of implying full coverage |
| 3 | Due professional care | Be diligent, investigate contradictions, call in specialists | Bring in an expert on a legacy banking application |
| 4 | Confidentiality | Access only what the audit needs, store it on approved systems, dispose of it securely | Keep screenshots in the audit repository, never in personal email |
| 5 | Independence | Never audit your own work. Apply safeguards where full independence isn't possible | Move a team member off a process they used to manage |
| 6 | Evidence-based approach | Findings must rest on evidence that is relevant, reliable, sufficient and verifiable | Sample access reviews instead of accepting a manager's word |
| 7 | Risk-based approach | Spend audit effort according to risk, and manage the risks to the audit itself | Add time and sampling for a system with recent incidents |

The pair worth memorising: **risk-based decides where to look; evidence-based decides whether the finding holds.**

## Where this shows up in a real job

- **Confidentiality covers AI tools.** Client evidence must not go into an AI assistant the engagement hasn't approved. I hold that line for my own work as well: course material and client data stay out of this repo.
- **Sampling choices need to be stated.** For the lesson's offboarding example, a random sample tests whether the process works in general. A sample of privileged accounts tests the cases where a failure hurts most. Both are valid, but the report has to say which approach was used, because a judgement-based sample can't be extrapolated to the whole population.
- **Integrity under pressure.** I know this from support work: a customer wants a ticket marked resolved before it is. An auditor faces the same pressure, with more at stake.

## Where I'd push back

- **"Get rid of the data after the audit" needs qualifying.** Copies of the client's sensitive data should be disposed of. Audit records are a different matter: working papers, the evidence behind findings, and the report itself have to be **retained**. Certification bodies are required to keep records (ISO/IEC 17021-1), and internal audit results are documented information under clause 9.2. Dispose according to the agreed retention schedule, not as soon as the audit ends.
- **Confidentiality has legal limits.** Disclosure required by law or regulation (a regulator's request, a court order) overrides it. Read the engagement letter, not just the principle.
- **Independence in 19011 is guidance, but for internal audits 27001 makes it a requirement.** Clause 9.2.2 requires auditors to be selected so the audit is objective and impartial. A small organisation that can't achieve full independence needs documented safeguards, such as an external auditor for the areas where conflicts exist. Otherwise the certification body will raise a finding.
- **Edition.** The course material cites ISO 19011:2026. The seven principles are unchanged from the 2018 edition, so the content here holds either way. The citation in my lesson 17 note still needs checking.

## My take

Principles 1, 2 and 6 together amount to this: say what you saw, how you saw it, and what you didn't get to see. Most bad audit reports I can imagine fail on the last part. They imply coverage the audit never had. If I write the limitations section first, the rest of the report stays honest.
