# Identify cybersecurity threats

> Module 02, lesson 2. The vocabulary, the two levels threat identification
> happens at, and why it isn't meant to be a brainstorm.

## Summary

Step one of the risk management process, prefaced with the three definitions the
rest of the module leans on. A **vulnerability** is a weakness — in a system, a
design or a process — that can be exploited. A **threat** is the malicious actor
or negative event that could exploit it. **Risk** is the exposure that results
when the two meet — how likely it is that a threat exploits the weakness, and how
much it would cost the organisation if it did. Likelihood on its own doesn't get
you there: lesson 1's whole budget argument depended on some findings ending in
harmed patients and others not.

Threat identification happens at two levels. Organisation-wide, you're cataloguing
what the whole entity is exposed to: for a hospital, external attackers after
patient records, a disgruntled employee walking off with data, malware, and
non-malicious events like fire or earthquake. Project or application level, you
ask the same question of one system, and the answers get more specific — this OS,
this framework, this class of attack against this application.

The point I want to hold onto is the closing one: threat identification is not a
brainstorm. Industry frameworks and standards publish threat libraries, and the
job is mapping the organisation or the system against an established catalogue
rather than assembling a list from imagination and whoever happens to be in the
room.

## Key concepts

| Concept | What it means | Why it matters in practice |
| --- | --- | --- |
| Vulnerability | A weakness in a system, design or process that can be exploited | The thing you fix; on its own it says nothing about how much it matters |
| Threat | The actor or event that could exploit a weakness | What you can't remove — you control exposure to it, not its existence |
| Risk | The combination of how likely a threat is to exploit a weakness and what the consequence would be | Both terms are needed — ranking on likelihood alone puts a near-certain trivial issue above an unlikely catastrophic one |
| Organisation-level threats | What the whole entity faces: attackers, insiders, malware, natural events | Sets the baseline every system inherits |
| Application-level threats | What one system faces, given its stack and exposure | Where the specifics live, and where generic org-level lists stop being useful |
| Threat libraries | Published catalogues of threats in frameworks and standards | Makes identification repeatable and reviewable instead of dependent on who's in the room |

## Where this shows up in a real job

The vulnerability-versus-risk distinction is one I already work with, just without
the vocabulary. A published CVE in a WordPress plugin is a vulnerability. Whether
it's a *risk* to a given site depends on whether the plugin is installed, whether
the vulnerable path is reachable, and what the site holds. Most of the triage
work is deciding that second question, and my CVE detection lab is essentially an
exercise in the same gap — a feed of vulnerabilities is not a list of risks.

The insider threat example is the one I'd flag from my own seat rather than take
on faith. Support engineers routinely hold broad access to customer data because
the job needs it, and that access is rarely scoped as tightly as an equivalent
engineering role's would be. When the hospital example reaches for "disgruntled
employee", the version I picture is someone with a legitimate support tool and no
particular need to break anything.

I haven't done formal threat modeling — no STRIDE sessions, no attack trees. The
Wazuh lab is detection of threat *events* after the fact, which is a different
activity from enumerating them beforehand.

## My take

The distinction I already use without the vocabulary: a published CVE is a
vulnerability, and whether it's a risk depends on whether the thing is installed,
reachable, and holding anything worth taking. A feed of vulnerabilities is not a
list of risks.

Worth keeping the two senses of "threat" apart when writing them down. A malicious
actor is a *source* — it has intent and capability, and you can profile it. A fire
is an *event* — it has a probability and no motive. They end up in the same
column and they need different treatment, so I'd rather separate them than blur
them.

Threat libraries are the right default because they make the exercise repeatable
and reviewable instead of dependent on who's in the room. The thing to stay awake
to is that you'll find what's in the catalogue, and catalogues lag — hardest on
supply chain, third-party and identity-driven attacks. Treat the library as the
floor.
