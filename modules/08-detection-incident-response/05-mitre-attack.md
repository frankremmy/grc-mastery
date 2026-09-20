# The MITRE ATT&CK framework

> Module 08, lesson 5. Where detection use cases should come from, and how far
> into it a GRC professional needs to go.

## Summary

Validating detection means checking the detection use cases are complete, tested
and current. Deploying a SIEM isn't enough — someone has to build use cases that
mimic real attacks and configure them in the platform.

And those use cases shouldn't be invented. The industry references frameworks
describing attacker **tactics, techniques and procedures (TTPs)**. The older one
was Lockheed Martin's **Cyber Kill Chain**; **MITRE ATT&CK** is now the de facto
standard.

**The GRC recommendation** is that detection use cases are aligned to ATT&CK, so
detections aren't random. A surprising number of organisations run a SIEM with poor
use cases built on arbitrary scenarios.

**But alignment isn't effectiveness.** Mapping to ATT&CK doesn't mean the
detections work. They still need constant testing and tuning — to keep false
positives down, and to confirm they actually fire on the activity they're meant to
catch.

**And the scope limit is explicit.** Don't go down the rabbit hole of becoming an
ATT&CK expert. That isn't the GRC job. The scope is advising organisations to align
their use cases to the framework, and reviewing some samples of that configuration
with them. GRC professionals are not detection engineers or incident response
engineers — the role is understanding it at a high level, and consulting someone
with deep expertise when that's what's needed.

## How ATT&CK is structured

Enough to assess alignment, which is the scope this lesson sets.

**Three matrices**, covering different technology domains:

| Matrix | Covers |
| --- | --- |
| **Enterprise** | IT environments — Windows, macOS, Linux, cloud, containers, network devices |
| **Mobile** | iOS and Android |
| **ICS** | Industrial control systems and operational technology |

The ICS matrix is worth knowing exists. A bioengineering firm with networked lab
instrumentation, or any manufacturer, has attack surface the Enterprise matrix
doesn't describe — which connects to the operational technology gap flagged back
in module 4.

**Three levels within a matrix:**

- **Tactics** — the adversary's objective at that stage. *Why* they're doing
  something. The Enterprise matrix has 14: Reconnaissance, Resource Development,
  Initial Access, Execution, Persistence, Privilege Escalation, Defense Evasion,
  Credential Access, Discovery, Lateral Movement, Collection, Command and Control,
  Exfiltration, Impact.
- **Techniques** — *how* the objective is achieved, each with an identifier such
  as T1566 for phishing.
- **Sub-techniques** — more specific variants of a technique.

A detection use case maps to one or more techniques. Coverage is therefore
expressible as which techniques have detections and which don't — which is the
whole reason alignment is worth recommending.

The catalogue is versioned and updated regularly, so an alignment mapping is a
point-in-time statement and goes stale like any other.

## Key concepts

| Concept | What it means | Why it matters in practice |
| --- | --- | --- |
| TTPs | Tactics, techniques and procedures used by attackers | The vocabulary detection is built against |
| Cyber Kill Chain | Lockheed Martin's earlier attack-phase model | Still referenced; largely superseded |
| MITRE ATT&CK | The current standard catalogue of adversary behaviour | What use cases should map to |
| Framework alignment | Detections mapped to a published catalogue rather than invented | Makes coverage reviewable and gaps visible |
| Alignment ≠ effectiveness | Mapped detections can still fail to fire | Testing and tuning remain necessary |
| Random use cases | Detections built on whatever occurred to someone | Common, and produces unknowable coverage |
| Scope of the GRC role | Advise on alignment, review samples, escalate to specialists | Knowing where your expertise ends is part of the job |

## Where this shows up in a real job

ATT&CK is the framework my CVE detection lab work sits closest to. Writing
detections means deciding what behaviour to look for, and having a catalogue of
techniques to map against is the difference between systematic coverage and a
collection of rules that reflect whatever I happened to read about that week.

That's also the honest boundary: I've written detections in a lab, which is enough
to understand what a use case is and ask sensible questions about one. It isn't
detection engineering at organisational scale, and this lesson is explicit that
becoming that expert isn't the GRC path anyway.

The Wazuh work is relevant in the same limited way — rules that fire on activity I
generated, in an environment with no real noise.

## My take

The scope instruction here mirrors the encryption lesson, and the repetition is
deliberate: **know the framework well enough to assess alignment, not well enough
to build the detections.** Both lessons draw the same line — understand what good
looks like, recognise a weak answer, and bring in the specialist rather than
attempting the specialist's work. For someone with technical instincts that's a
useful discipline, because the interesting rabbit hole is always available and it
isn't where the value is.

Three things:

**ATT&CK's real contribution to an assessment is that it makes absence visible.**
Any detection set can be described as comprehensive by whoever built it. Mapped to
ATT&CK, coverage becomes a picture — these techniques have detections, these have
none — and the gaps are the finding. Without a catalogue there's nothing to be
missing *from*. That's the same structural point as third line asking what nobody
has verified, and as module 2's threat libraries making identification reviewable
rather than dependent on who was in the room.

**Coverage should be weighted, not counted.** ATT&CK is large, and "we cover 40% of
techniques" is a number without meaning — techniques aren't equally likely or
equally damaging for a given organisation. The better question is whether
detections exist for the techniques associated with the threats that actually
apply: ransomware for a hospital, industrial espionage for a research firm. An
organisation detecting many low-relevance techniques and none of the ones in its
own threat profile has good-looking coverage and a real gap.

**Alignment is a design check; testing is the operating check.** The lesson makes
this distinction and it's the module 3 ladder again — a use case can exist, be
correctly mapped, cover the estate, and still not fire, because the log source it
depends on was never onboarded or the rule was written against a field that
changed. So the two questions are separate: is it mapped, and when did it last
actually fire on something. The second is harder to answer and worth more.

Worth noting for the next lesson: testing detections deliberately — running
technique simulations and confirming alerts fire — is what turns that second
question into evidence. That's adjacent to what cyber drills do for the response
side.

## Reference

- MITRE ATT&CK — <https://attack.mitre.org/>
- CrowdStrike, *MITRE ATT&CK Framework* explainer —
  <https://www.crowdstrike.com/cybersecurity-101/mitre-attack-framework>
