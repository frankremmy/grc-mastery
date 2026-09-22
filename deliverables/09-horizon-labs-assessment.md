# Supplier security assessment — Horizon Labs

**Module:** 09 — Third-Party Risk Management
**Type:** Practical assessment
**Status:** My own answer, written before seeing the course solution.

**Task.** Review Horizon Labs' questionnaire responses and summarise the key risk
items for escalation to Oscorp senior management.

**Assumption stated in the brief:** Horizon Labs supplied sufficient evidence for
their answers.

---

## Supplier summary

| Field | Detail |
| --- | --- |
| Supplier | Horizon Labs |
| Service | "Horizon X" — SaaS application for scientific research data analysis |
| Respondent | Peter Parker, IT Manager |
| Location | Queens, New York, USA |
| Data handled | Oscorp confidential data — research intellectual property |
| Tier | **Tier 1** — holds Oscorp's research IP |

---

## My answer

I reviewed the Horizon Labs questionnaire. Because Horizon X processes Oscorp's
confidential intellectual-property and scientific research data, I would focus
senior management on weaknesses that could materially affect the confidentiality
and security of that data.

### Key risks to escalate to Oscorp senior management

**1. Weak access control — High**

Horizon Labs confirmed that it does not use RBAC, does not follow least
privilege, does not implement segregation of duties, and does not perform
periodic user access reviews. This creates a significant risk of employees or
privileged users having unnecessary or excessive access to Oscorp's confidential
research data. MFA through Okta is a positive control, but it does not
compensate for excessive permissions.

**2. No established vulnerability management programme — High**

Horizon Labs does not have a vulnerability scanner or formal vulnerability
management programme. They rely on installing regular Windows updates. This may
leave vulnerabilities unidentified or unaddressed, particularly across systems
supporting Horizon X.

**3. No penetration testing — High**

Horizon Labs has never conducted a penetration test and only plans to perform one
in the future. There is therefore limited assurance that vulnerabilities in the
SaaS application and its supporting infrastructure have been independently
identified and tested.

**4. Weak security monitoring and incident response — High**

Their responses only state that the IT team handles IT issues and incidents.
There is no evidence in the questionnaire of a defined security monitoring
capability or formal incident response process. This raises concerns about
Horizon Labs' ability to quickly detect, contain and respond to an attack
affecting Oscorp.

**5. No recognised cyber security framework — Medium/High**

As a startup, Horizon Labs stated that it does not currently follow a cyber
security framework. This increases concern about whether security controls are
implemented and governed consistently across the organisation.

**6. No DLP capability — High**

Horizon Labs does not have Data Loss Prevention controls despite processing
Oscorp's confidential intellectual property. Their reference to regular backups
does not address this risk: backups support recovery, whereas DLP is intended to
help prevent or detect unauthorised disclosure or movement of sensitive
information.

**7. Limited ongoing security awareness — Medium**

Security training is mandatory only when employees join the company. There is no
indication of periodic refresher training or ongoing awareness campaigns.

### Management conclusion

I would escalate Horizon Labs as presenting material third-party security risk,
particularly because of the sensitivity of Oscorp's scientific intellectual
property. The strongest areas identified are database encryption and MFA, but
these do not offset the significant gaps in access governance, vulnerability
management, penetration testing, monitoring, incident response and DLP.

I would recommend that Oscorp agree a formal remediation plan with Horizon Labs,
with owners and target dates for the high-risk findings. The most serious issues
should be addressed as a condition of continued use of Horizon X, and Oscorp
should track the remediation through its TPRM process rather than simply
accepting the questionnaire responses.

---

## Points I would add on a second pass

Written after the answer above, reviewing my own work.

**The encryption answer deserves a finding of its own.** I listed database
encryption as a strength. On re-reading, "the Oracle database encrypts by
default" is narrower than it sounds — it addresses data at rest at the database
layer. It says nothing about encryption in transit, who holds the keys, or
whether Horizon Labs administrators can read plaintext. It protects against a
stolen disk and does nothing against an over-privileged authenticated user, which
is exactly the risk in finding 1. A control can be genuinely present and
irrelevant to the threat in front of it, and this is the answer most likely to be
over-read by a non-technical reader as reassurance.

**The three "no capability" findings compound into one story.** Access control,
monitoring and incident response are three findings in my list. Stated together
they describe something sharper than their sum: Oscorp's research IP sits with an
organisation that cannot limit who reaches it, cannot tell whether anyone has, and
has no process to respond or notify if they did. For a senior audience I would
lead with that sentence, then give the findings underneath it as evidence. Eight
equally weighted rows tell a manager there are problems; the compounding version
tells them what decision they are being asked to make.

**Incident response has a direct consequence for Oscorp's own obligations.** A
supplier that cannot detect or report an incident leaves Oscorp unable to meet its
own notification deadlines — Oscorp cannot start a clock it never learns has
begun. This connects the finding to the incident response plan Oscorp has just
adopted, which makes it concrete rather than generic.

**Absent controls are not unverified claims.** The brief says to assume evidence
was sufficient. That applies to answers asserting a control. Questions 7 and 8
assert nothing — "the IT team manages all incidents" names a team and describes
no capability. No evidence could make that a control, so it is recorded as absent
rather than unverified.

**Four questions Oscorp never asked.** These are findings against Oscorp's own
TPRM process rather than against Horizon Labs, and for a tier 1 supplier they are
material:

- **Hosting and subprocessors** — where Horizon X runs and who else touches the
  data. Horizon Labs' suppliers are Oscorp's fourth parties
- **Data location and jurisdiction** — the supplier is US-based; Oscorp needs to
  know where research IP resides and under whose legal reach
- **Business continuity and exit** — no questions on backup testing, recovery
  objectives, or what happens to Oscorp's data if a startup supplier fails
- **Data return and deletion at contract end** — nothing establishes what happens
  to Oscorp's IP when the relationship ends

**Compensating controls Oscorp can apply itself.** My conclusion puts the
remediation entirely on Horizon Labs, which leaves Oscorp exposed for as long as
the supplier takes. Oscorp can act within its own authority immediately: minimise
what research data goes into Horizon X, restrict which Oscorp users can send data
to it, and monitor egress from Oscorp's environment. These do not depend on a
supplier who has not yet demonstrated they can deliver.

**One immediate contractual action.** A breach notification clause. Oscorp
currently has no contractual right to be told that its research IP has been
exposed — and given finding 4, no practical prospect of learning it another way.

---

## Design notes

Not part of the assessment — my reasoning.

**Startup candour cuts both ways.** Horizon Labs answered honestly where they
could have been evasive, which makes remediation more plausible than with a
supplier claiming controls it does not have. Worth noting to management, but it
does not soften a rating — the exposure is identical either way.

**The tier assessment is doing work the questionnaire does not.** Nothing in the
responses establishes criticality; I assigned tier 1 on the sensitivity criterion
alone, because for a pharmaceutical business the research data *is* the asset.
Stating the tier at the top is what justifies treating these findings as material
rather than as the ordinary weaknesses of a small supplier.

---

## Comparison with the course solution

The course solution rates six items:

| Course finding | Rating | In my answer? |
| --- | :---: | --- |
| No cyber security team or capability; IT manages security; no framework followed | High | Partly — I raised the framework gap (Medium/High) but did not name the absence of a security function |
| No vulnerability management or penetration testing programme | High | Yes — findings 2 and 3 |
| No detection and monitoring capability | High | Yes — finding 4 |
| Not capable of responding to incidents | High | Yes — finding 4 |
| Significant deficiency in identity and access management | High | Yes — finding 1 |
| No DLP monitoring | Medium | Rated High |

### What I missed

**The absence of a security function is the root cause, and I treated it as a
framework question.** The solution groups "no security team, IT manages security,
no framework" into a single High finding. That grouping is better than my
framing. I rated the missing framework Medium/High as a governance concern, but
the sharper point is that **nobody at Horizon Labs owns security as their job.**
Every other finding follows from that: there is no vulnerability programme, no
monitoring and no incident response because there is no one whose responsibility
those are. Naming the root cause changes the remediation conversation too —
asking a supplier to buy a scanner is a different request from asking them to
establish a security function, and the second is what actually fixes the pattern.

I had the evidence for this in front of me. The respondent is the IT Manager, and
questions 7 and 8 both answer "the IT team". I read those as evidence of absent
capabilities rather than as evidence of an absent function.

### Where I rated differently

**DLP: I said High, the solution says Medium**, on the basis that encryption and
backups exist and their absence would have made it High.

I would defend my rating, but the disagreement is a definitional one worth being
precise about. "Data loss" carries two meanings. Loss of *availability* — data
destroyed or unrecoverable — is genuinely mitigated by backups. Loss of
*confidentiality* — data leaving the organisation without authorisation — is what
DLP as a control category addresses, and neither backups nor encryption at rest
reduces it. An authorised user exporting Oscorp's research IP reads it decrypted
and leaves the backups intact.

Given Oscorp's data here is research intellectual property, exfiltration is the
consequence that matters, which is why I rated it High. If the concern were
accidental destruction, Medium would be right. The lesson I take is not that one
rating is correct but that **the rating depends on which loss you mean**, and a
report should say so rather than leaving the reader to guess.

### Where I went further

Not scored by the solution, but I would keep all of it:

- Encryption at rest does not mitigate the access control finding
- The compounding effect of the access, monitoring and response gaps
- The consequence for Oscorp's own incident notification obligations
- Compensating controls Oscorp can apply without waiting for the supplier
- The four questions Oscorp's questionnaire never asked
- Tiering Horizon Labs as tier 1, which is what makes these findings material
