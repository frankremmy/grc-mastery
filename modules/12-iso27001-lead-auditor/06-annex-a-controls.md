# Annex A controls

> Module 12, lesson 6. _The 93 controls, the four themes, and how selection
> actually works._

## Summary

Annex A is a reference list of **93 security controls** an organisation can
select from to treat the risks its assessment identified. Reading them after this
course is mostly recognition — they're the same controls covered across earlier
modules, occasionally in different words.

**Selection, not implementation.** Implementing all 93 is not mandatory and would
be absurd, the same way implementing every NIST 800-53 control would be. What *is*
mandatory is that the risk assessment selects controls from Annex A. Selected
controls become mandatory to implement. Unselected controls must be **justified**.
Both go in the **Statement of Applicability**, required by clause 6 and one of
the standard's mandatory documents.

**Purpose of Annex A:** a structured set of security best practices; a way to
address risks found in the assessment; a common language across industries and
audits; and support for building a comprehensive ISMS.

### The four themes

The 2022 revision reorganised the controls into four themes, replacing the
previous 14 domains.

| Theme | Clause | Covers | Examples |
| --- | --- | --- | --- |
| **Organisational** | A.5 | Policies, procedures, third-party management, business continuity | Information security policies; risk assessment and treatment; supplier relationships |
| **People** | A.6 | Human factors — training, awareness, responsibilities | Screening and onboarding; security responsibilities in job roles; awareness training |
| **Physical** | A.7 | Protection of premises and physical assets | Physical entry controls; secure disposal of equipment; environmental controls |
| **Technological** | A.8 | Protecting information through technology | Access control; cryptography; backup, monitoring, malware protection |

The mnemonic the course offers: people, process, technology — with *organisation*
standing in for process, plus physical security as the fourth. Not a memorisation
exercise; the standard is there to be referenced.

**On the official text.** The ISO publication isn't free, which is why it can't
be redistributed. Same reason the source documents in this repo are linked rather
than copied.

## Worth adding

**The control counts per theme**, since "93 across four themes" invites the
follow-up:

| Theme | Controls |
| --- | ---: |
| A.5 Organisational | 37 |
| A.6 People | 8 |
| A.7 Physical | 14 |
| A.8 Technological | 34 |
| **Total** | **93** |

**The eleven new controls in 2022** are the ones worth knowing by name, because
they're what distinguishes someone who knows the current standard from someone
who learned the 2013 version:

- A.5.7 Threat intelligence
- A.5.23 Information security for use of cloud services
- A.5.30 ICT readiness for business continuity
- A.7.4 Physical security monitoring
- A.8.9 Configuration management
- A.8.10 Information deletion
- A.8.11 Data masking
- A.8.12 Data leakage prevention
- A.8.16 Monitoring activities
- A.8.23 Web filtering
- A.8.28 Secure coding

The pattern is clear enough: cloud, monitoring, data protection and secure
development — the things that moved between 2013 and 2022.

**114 to 93 was consolidation, not deletion.** Controls were merged rather than
dropped, with a handful carried over unchanged, one split, and the eleven above
added. Nothing was removed for being unnecessary, which matters if you're ever
transitioning an organisation from the old structure and someone asks what they
can stop doing. The answer is nothing.

## A correction on the NIST comparison

The lesson says the four themes are "similar to NIST identify, detect, protect,
recover — just different naming." I don't think that holds, and the distinction
is worth keeping straight.

The NIST functions are **lifecycle phases** — what you do, in sequence, before
during and after an incident. Annex A's themes are **categories of control** —
what kind of thing the control is. They're orthogonal, not renamed versions of
each other. An access control is technological regardless of whether you're using
it to protect or to detect.

**But there is a real NIST link, and it's better than the one claimed.** The 2022
revision attaches five **attributes** to every Annex A control:

- **Control type** — preventive, detective, corrective
- **Information security properties** — confidentiality, integrity, availability
- **Cybersecurity concepts** — identify, protect, detect, respond, recover
- **Operational capabilities**
- **Security domains**

The third of those *is* the NIST CSF function set, used deliberately. So Annex A
can be pivoted into a NIST-style view — you can filter the 93 controls by which
CSF function they serve. The themes aren't the NIST functions; the attributes
include them, which is more useful because it lets the two frameworks be mapped
rather than confused.

## Where this shows up in my own work

The themes map neatly onto what this course has already covered, which is a
useful way to see how much of Annex A I've effectively already studied:

- **A.5 Organisational** — governance, risk management, audit, third-party risk
  (modules 1, 2, 3, 9)
- **A.6 People** — security awareness and training (module 6)
- **A.7 Physical** — the one area with no dedicated module
- **A.8 Technological** — IAM, data security and DLP, detection and incident
  response, vulnerability management (modules 5, 7, 8, 10)

Against Oscorp, the shape from the capstone comes straight back: strong on A.7
physical, weak across A.5 organisational, nothing meaningful in the detection and
response parts of A.8. If Oscorp built an SoA today, the physical controls would
be the only theme where inclusion was easy to evidence.

## My take

The selection-and-justification mechanism is what makes ISO different from a
checklist, and it's the part I'd want to get right in practice. A control set you
must implement entirely is a compliance exercise. A control set you select from,
where the selection has to trace back to assessed risk and every exclusion has to
be defended, forces the organisation to actually think about its own exposure.
That's the same argument as the NIST CSF assessment in the capstone — the
framework's value is that it makes you consider everything and justify what you
skip.

It also puts the SoA at the centre rather than the certificate, which is now the
third time this module has arrived at that point from a different direction. For
supplier assessment the practical version is: the certificate says an auditor was
satisfied, the scope says about what, and the SoA says which of the 93 they
decided they needed — and what they talked themselves out of.
