# Insider threat program design — Oscorp

**Module:** 07 — Data Security and DLP
**Type:** Practical assessment
**Status:** My own answer, written before seeing the course solution, followed by a comparison written afterwards.
**Role:** External cyber security consultant advising Oscorp.

---

## Situation

Reports of serious side effects of Oscorp's new medication have reached the press.
Norman and Harry Osborn suspect an employee leaked the information. Oscorp wants a
comprehensive insider threat programme to monitor and stop employees stealing and
leaking sensitive data.

Environment: Microsoft 365, Microsoft Azure, SharePoint internally.

---

## My answer (as submitted)

I would recommend that Oscorp establish an Insider Threat Programme combining
people, process and technology controls rather than relying on monitoring alone.

The first step is to identify and classify sensitive information. Data such as the
medication formula, research results, patient information and confidential business
documents should be labelled according to sensitivity. Access should follow least
privilege and need-to-know principles, with regular reviews to ensure employees
only have access required for their roles.

Since Oscorp already uses Microsoft 365, Azure and SharePoint, it should consider
implementing Microsoft Purview Data Loss Prevention (DLP) and sensitivity labels.
DLP policies can help detect and restrict attempts to send sensitive information
through email, share it externally through SharePoint or OneDrive, or transfer
protected information through other controlled channels.

Policies should be risk-based. For example, sharing highly confidential research
externally could be blocked, while lower-risk activities could generate a warning
or require justification. Alerts should be sent to the security team when
suspicious activity occurs.

Oscorp should also establish monitoring for unusual behaviour, such as excessive
downloading of confidential documents, unusual external sharing, repeated attempts
to access restricted information or significant data activity before an employee
leaves the company. Alerts should be investigated using a documented
incident-response process rather than automatically assuming malicious intent.

A strong joiner, mover and leaver process should ensure access is granted
appropriately, reviewed when employees change roles and removed promptly when they
leave. Privileged and high-risk access should receive additional monitoring.

Employees should receive regular security awareness training covering confidential
information, acceptable use, phishing and secure data sharing. Clear policies
should explain how company information may be accessed, stored and shared.

Finally, the programme should be regularly reviewed using DLP incidents,
investigation outcomes and false-positive rates. Monitoring should also comply with
applicable privacy, employment and legal requirements.

This layered approach would help Oscorp prevent data leakage while also improving
its ability to detect, investigate and respond to potential insider threats.

---

## Additions on review

### 1. What was leaked matters, and it changes the engagement

The disclosure concerns **serious side effects of a medication that is on the
market**. Before designing anything, that has to be said plainly to Norman and
Harry, because it carries three consequences my answer didn't address.

**It may be a protected disclosure.** In many jurisdictions, reporting genuine
public-health or safety concerns is protected by whistleblowing law, and
retaliating against or attempting to identify a protected whistleblower creates
liability independent of whether the disclosure breached a confidentiality
obligation. A programme designed and deployed immediately after a safety leak, with
the stated purpose of finding who talked to the press, is exactly the fact pattern
that turns a reasonable security control into a legal exposure.

**The underlying issue may not be a security issue.** If the side effects are real
and were known internally, Oscorp has a product safety and regulatory problem, and
the leak is a symptom. Building surveillance in response addresses the symptom and
leaves the cause — which is the more serious risk to the business by a wide margin.

**Design the programme, don't design the manhunt.** A standing insider threat
programme protecting research IP and commercial data is defensible. A monitoring
capability stood up to identify one suspected individual is a targeted
investigation, and it belongs to a separate process run with HR and legal counsel,
under a documented basis, not to a security programme being built in the same
week.

My recommendation to Oscorp: keep the two strictly separate, get legal advice on
the disclosure before any monitoring is aimed at it, and confirm that internal
routes exist for raising safety concerns — because if they don't, the leak is also
telling you something about the governance.

This isn't a reason to decline the work. It's the thing a consultant is being paid
to notice, and raising it protects Oscorp more than the programme does.

### 2. Name the Microsoft capabilities precisely

My answer proposed Purview DLP and sensitivity labels, which is right but partial
for this platform.

| Capability | What it does for Oscorp |
| --- | --- |
| **Purview Information Protection** | Sensitivity labels on documents and email; labels travel with the file and drive downstream enforcement |
| **Purview Data Loss Prevention** | Policy enforcement across Exchange, SharePoint, OneDrive, Teams and endpoints |
| **Purview Insider Risk Management** | The capability actually designed for this brief — behavioural sequence detection, departing-employee indicators, risky activity scoring |
| **Endpoint DLP** | USB, print, clipboard and local copy controls on managed devices |
| **Defender for Cloud Apps** | Visibility over unsanctioned SaaS and personal cloud storage |
| **Entra ID conditional access** | Blocking downloads to unmanaged devices; restricting access by device compliance |
| **Unified audit log and eDiscovery** | The evidence layer — what an investigation actually runs on |

Insider Risk Management is the one worth naming explicitly: it detects *sequences*
rather than single events — access, then download, then external share, then
departure — which is closer to how a leak actually looks than any single-rule DLP
policy.

### 3. Phase the rollout; don't start in block mode

My answer set risk-based tiers but not a sequence. From the module: policies start
in monitor mode, generate a false positive baseline, get tuned, and only then move
to blocking for the narrow categories where confidence is high. An organisation
that blocks on day one either has excellent classification or is about to
accumulate exceptions until the control is decorative.

Concretely: monitor for 60–90 days, measure alert volume against the capacity of
whoever will triage it, tune, then enforce.

And size the rule set to the team. Oscorp's security team is small. Two rules that
get investigated beat twenty that generate noise nobody reads.

### 4. Govern the monitoring itself

My answer said monitoring should comply with privacy and employment requirements.
The specific controls that make that real:

- **Pseudonymisation by default**, with a documented dual-approval process before
  an individual's identity is revealed — Purview Insider Risk Management supports
  this natively.
- **Role-based access to the monitoring data**, with the security team seeing
  alerts and only a named investigation role seeing content.
- **Defined retention** for monitoring data, and deletion when it expires.
- **Disclosure** in employment terms and acceptable use policy, plus employee
  consultation where local law requires it.
- **A documented lawful basis** for the processing, and a privacy impact
  assessment — which, per module 2, is not mine to conduct.

Without these, the programme is itself a compliance finding.

### 5. Acknowledge the channels this cannot cover

Worth telling the executives directly, so the programme isn't oversold. DLP and
Insider Risk Management cover managed devices and corporate channels. They do not
cover a photograph of a screen taken on a personal phone, a conversation, printed
material removed from a building, or anything on an unmanaged personal device.

For a determined insider — as opposed to the negligent one, which is the more
common case — technical controls raise effort and produce evidence. They don't
prevent. The honest framing: this reduces likelihood and improves detection; it
does not guarantee that nothing leaves.

### 6. Fix the access problem, because it caps everything else

Oscorp's known IAM findings sit underneath this: the whole research lab has read
access to the formula, and the formula database uses authentication outside the
directory. Least privilege isn't just one component of the insider threat
programme — it's the control that decides how many people *could* leak in the first
place. Monitoring a hundred people who shouldn't have access is a far worse
position than monitoring the eight who should.

That also makes the programme cheaper: fewer people in scope, fewer alerts, less
tuning, less surveillance.

---

## Recommendation in short

1. Separate the investigation of this disclosure from the programme design, and
   take legal advice on the former before any monitoring is pointed at it.
2. Reduce access to the crown jewels first — least privilege caps the population
   that could leak.
3. Classify and label the sensitive data, since nothing downstream works without it.
4. Deploy Purview Information Protection, DLP and Insider Risk Management, phased:
   monitor, tune, then enforce narrowly.
5. Govern the monitoring — pseudonymisation, dual approval, retention, disclosure,
   lawful basis.
6. Keep the rule set within the team's capacity to investigate.
7. Tell the executives what it cannot cover, before they assume it covers
   everything.

---

## Comparing against the course solution

The solution sets IAM aside as already covered in the previous module's assessment
and focuses narrowly on data security. Its sequence:

1. **Block USB storage** — a simple, effective, essentially free control.
2. **Data discovery, scoped to the drug** — start with the SQL database known from
   the earlier assessment, then search SharePoint for related files.
3. **Label everything drug-related as Highly Sensitive** using Microsoft's
   information protection tooling.
4. **Deploy Microsoft Purview DLP** as the natural fit for a Microsoft estate, with
   strict rules preventing sending or copying anything tagged Highly Sensitive.
5. **Physically search desks** for printed material related to the drug, and store
   it in a secure cabinet to reduce the risk of employees photographing documents.

### What the solution had that I didn't

**USB blocking as the immediate first move.** I covered removable media inside
Endpoint DLP without singling it out. The solution is right to lead with it: it's
a single policy change, costs nothing, closes a major exfiltration channel, and can
be done today — before discovery, labelling or any platform work. When a client is
in an emergency meeting, the control you can implement this afternoon has value
the perfect one doesn't.

**Scoping discovery to the drug rather than the enterprise.** My answer proposed
classifying sensitive data broadly. The solution narrows to the data that matters
right now, which is both faster and proportionate to the situation. Enterprise-wide
classification is the right long-term programme; it is not what an urgent response
looks like.

**Physical documents.** Neither my answer nor the module's lessons addressed paper.
I noted that a photograph of a screen defeats technical controls and stopped there
— the solution goes further and secures the physical source. Printed research in an
unlocked desk is outside every control we'd discussed, and a locked cabinet is
another control that costs nothing.

### Where the solution and I differ

**Straight to strict blocking.** The solution configures rules to prevent sending
or copying Highly Sensitive files immediately, with no monitoring period. Module 7
lesson 6 warns that blocking without a tuning phase breaks legitimate work and
generates exceptions.

Both can be right, and the reconciling factor is **scope**. Blanket blocking across
all sensitive categories needs a baseline first. Blocking a narrow, newly labelled
set — the drug files, where the population is small and the classification
confidence high — is defensible on day one, because the false positive surface is
tiny and the urgency is real. The principle to carry: block early where scope is
narrow and confidence is high; monitor first where it's broad.

**Product naming.** The solution links Azure Information Protection, which has
since folded into Microsoft Purview Information Protection. The capability is the
same; the current name is what appears in documentation now.

### What I had that the solution didn't

Behavioural detection through Insider Risk Management — sequence-based rather than
single-event; joiner-mover-leaver; governance of the monitoring itself
(pseudonymisation, dual approval to unmask, retention, disclosure, lawful basis);
programme review metrics; and telling the executives which channels this cannot
cover.

And the framing issue: the solution treats the brief as purely technical. It
doesn't address that the disclosure concerned drug safety, that this may be a
protected disclosure, or that a surveillance programme built to find the person who
raised it carries legal exposure of its own. That's the judgement I'd still want in
the answer — the technical design is the easy half.
