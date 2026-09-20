# Two real ways we can protect data

> Module 07, lesson 1. Narrowing a very broad term down to the two things people
> mean by it.

## Summary

"Data security" is broad to the point of being unhelpful. Technically the goal of
all of cyber security is to secure data — firewalls, passwords, identity and access
management all share that purpose. But when the industry says *data security* or
*data protection*, it usually means two specific methods.

**Encryption.** Scrambling data so it's only readable by the intended audience.
The data is encrypted with a key, and reading it requires decrypting it, which
requires the key. Its role is to **reduce the impact** of an attack: if an
attacker gets hold of encrypted data, reading it becomes much harder, so the
damage they can do is smaller.

Note the wording — *harder*, not impossible. There are techniques for reading
encrypted data. Depending on the algorithm some are extremely expensive in
computing resources, and some take a very long time. The point to hold: **encryption
is not a guarantee that data can never be read.**

The lesson is emphatic about this because it keeps coming up with senior people.
CIOs and CTOs have questioned the need for other security measures on the grounds
that "our data is encrypted so nobody can read it." That belief is common and it's
wrong.

**DLP — data loss protection.** Also rendered historically as data loss prevention
or data leakage protection; same thing. As a GRC professional you'll ask questions
about DLP and assess the effectiveness of DLP controls.

DLP began as a device organisations bought to stop sensitive data leaving. Data can
leave in many ways — an employee emailing sensitive information to a personal
address, leaking it to the press, or an attacker copying data and sending it out.
DLP's job is to scan the environment for sensitive data on its way out and, ideally,
generate an alert for an investigator to follow up.

DLP is also deployed as part of an **insider threat program** — an initiative to
monitor for threats originating with employees. An upset employee wanting to cause
damage might take sensitive information and send it to the press or to a personal
email account, and DLP is one of the controls used to reduce that damage.

## Key concepts

| Concept | What it means | Why it matters in practice |
| --- | --- | --- |
| Data security | Broadly, the goal of all security; narrowly, encryption and DLP | Establish which meaning is in play before answering a question about it |
| Encryption | Scrambling data so only a key holder can read it | Reduces the **impact** of a breach, not its likelihood |
| Encryption key | The secret that makes decryption possible | The whole scheme's strength rests here |
| "Encrypted therefore safe" | A common executive misconception | Leads to under-investment in everything else |
| DLP | Controls detecting and blocking sensitive data leaving the organisation | Addresses exfiltration, which access control alone doesn't |
| Alerting and investigation | DLP raises alerts for a human to examine | The control is only as good as the response behind it |
| Insider threat program | Monitoring for threats originating inside the organisation | The context DLP is frequently bought for |

## Where this shows up in a real job

The encryption misconception has a version in the WordPress world: a site has an
SSL certificate, so the owner concludes the site is secure. The certificate is real
and does its job — protecting data in transit — and it says nothing about weak
admin passwords, unpatched plugins or an exposed database. Same shape of error,
smaller stakes.

The exfiltration problem is also familiar from support, where legitimate data
export exists as a feature. Customer data exports, database dumps for migration,
reports — the mechanism that lets someone do their job and the mechanism that lets
someone take the customer list are frequently the same mechanism.

I haven't worked with a DLP platform or an insider threat program, so this module
is new ground for me rather than something I can map onto prior experience.

## My take

The distinction worth carrying from this lesson is **which term of the risk each
control moves**, which goes back to module 2 lesson 3. Encryption doesn't make a
breach less likely — an attacker still gets in and still takes the data. It changes
what that data is worth once taken. DLP works on the other side: it's aimed at
detecting and stopping the data leaving in the first place. Two controls, two
different jobs, frequently discussed as though they were one topic.

Two things:

**The executive misconception has a precise correction, and it's more useful than
"that's not true".** Encryption protects data in specific *states* — at rest on a
disk, in transit over a network — and the data has to be decrypted to be used.
An application querying an encrypted database sees plaintext. A user opening a file
sees plaintext. So an attacker who compromises an account, or the application, or
the running server, is on the inside of the encryption and it protects nothing
against them. The honest summary: encryption defeats someone who steals the storage;
it doesn't defeat someone who steals the access. That's the version worth having
ready for a CIO, because it explains why identity controls still matter without
disputing that the encryption is real.

**DLP's hard part is knowing what's sensitive.** The lesson describes DLP scanning
for sensitive data leaving, which presumes the organisation has decided what
sensitive means and can recognise it in transit. That's data classification — and
that's why the next lessons are classification and labelling. A DLP deployment
without classification is a tool configured on guesses, which produces false
positives, which produces alerts nobody reads. Worth expecting the same pattern as
PAM: buying it is the easy part, coverage and use are the assessment.

**Insider threat programs raise questions that aren't technical.** Monitoring
employees is surveillance, and it carries legal and cultural weight — employee
privacy law, works council consultation in some jurisdictions, and the effect on
trust when people learn what is watched. The GRC role here isn't only "is the tool
configured correctly" but "is this proportionate, disclosed and lawful", which is
closer to the privacy assessment territory from module 2 than to a control review.
