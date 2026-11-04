# 05 — Internal audit: secure development lifecycle

A first-party audit of the Refunds API's SDLC, carried out after the technical work. It answers a different question: whether the *process* would have prevented these flaws, and whether Kestrel can prove that to an assessor.

## Audit plan (summary)

| Item | Detail |
|---|---|
| Objective | Determine conformity of the SDLC with ISO 27001:2022 A.8.25–A.8.29 and the PCI DSS Req 6 / Secure SLC expectations; evaluate effectiveness |
| Scope | Refunds & Card Lookup API: last 6 months of changes (Apr–Oct) |
| Criteria | ISO 27001 A.8.25–8.29, A.8.8; PCI DSS 6.2–6.4; Kestrel Secure Development Procedure v1.2 |
| Methods | Interviews (team lead, 2 developers, DevOps); review of the procedure, PR history and CI config; sampling of merged changes |
| Sampling | Judgement sample of **15 of 64** merged PRs, weighted to changes touching auth, payments or card data. Judgement samples can't be extrapolated; this is stated in the report |
| Independence | The auditor took no part in designing the pipeline under review. The new CI gate (built during this engagement) is **excluded** from conformity conclusions because I built it, and the certification body or a peer will assess it |

## Findings

| ID | Criterion | Evidence | Finding | Classification |
|---|---|---|---|---|
| AF-01 | A.8.28 / PCI DSS 6.2.3 (code reviewed before release) | Procedure requires a security-focused peer review. **6 of 15** sampled PRs were merged with no approving review, including the PR that introduced the refund endpoint | Requirement not met on a recurring basis, including the change behind KP-04 | **Major NC.** Systematic failure of a control the organisation defined itself, with critical consequences |
| AF-02 | A.8.29 / PCI DSS 6.2.4 (testing for common vulnerabilities) | No SAST, SCA or DAST in CI before this engagement. Testing was functional only | Security testing not performed in the lifecycle | **Minor NC.** The new gate is in place and needs time to show effectiveness |
| AF-03 | A.8.25 / A.8.27 (secure design) | No threat model existed for the API before T1–T8 | Secure design principles not applied to a card-data service | **Minor NC** |
| AF-04 | A.6.3 / PCI DSS 6.2.2 (secure coding training, at least every 12 months) | Training records exist for 9 of 11 API developers. 2 recent joiners have none | Records incomplete for new starters | **Minor NC** |
| AF-05 | — | Dependency pinning is consistent and documented | Positive practice. The process existed; only the cadence of updates was missing | **Good practice / OFI:** add scheduled updates |

## Conclusion

The documented SDLC is reasonable, but it is **not operating effectively**. The control most likely to have caught the refund and logging flaws (a reviewed PR) was skipped in 40% of the sampled changes. One major and three minor nonconformities were raised. Correction and corrective action are owned by the Head of Engineering. Corrective actions due in 30 days include branch protection so that "no review, no merge" is enforced, not just written down. Effectiveness will be re-tested on a fresh sample of PRs merged *after* the change.

## Why AF-01 is major

The organisation's own procedure defines the control. The failure recurs (6 of 15), and it directly let a critical defect into production. The [Brunel](../../../deliverables/12-brunel-iso27001-documentation-audit.md) and lesson notes cover the minor/major reasoning in more depth.
