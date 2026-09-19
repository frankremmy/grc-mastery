# Active Directory

> Module 05, lesson 6. The system almost every organisation runs identity on, and
> what a GRC professional asks about it.

## Summary

Active Directory is Microsoft's domain controller, and it's the de facto standard
for managing usernames, passwords and access to systems, email and applications.
Security, network engineering, system administration, help desk — there's no role
that avoids it.

**Why groups exist.** Take a company of 500 people across accounting, marketing,
HR and IT. One option is granting each employee access individually, which would
consume unlimited time and effort. The other is Active Directory: create a group
per department, and assign each new joiner to the appropriate group, which carries
the access the role requires. A new accountant is added to the accounting group and
has the accounting application. Someone leaving marketing is removed from the
marketing group and loses those applications.

**On-premises or cloud.** The server can be physical and on-site, or the cloud
service — referred to in the lesson as Azure Active Directory. Conceptually the
same job, different hosting.

**Who owns it.** Not the security team. Active Directory belongs to system
administrators, systems engineers, Windows admins — the people who know it deeply
and keep it configured correctly. Security's involvement is in the *process* of
assigning users to groups and the level of access they get, plus the principles
that get implemented inside it: least privilege, MFA, separation of duties through
role-based access control.

**The assessment questions.** When reaching identity and access in an assessment:
How is Active Directory configured? Who looks after it? Then speak to those
people, and start with **how many admin accounts exist**. Tens or hundreds is a
serious red flag — it signals admin accounts aren't being managed, and it enlarges
the attack surface, because every additional privileged account is another chance
of compromise.

Then: do you implement least privilege, and how? The answer tells you a lot. If IT
says it has no idea how the marketing department is managed and simply creates
users when asked, that's a gap — those requests should be reviewed and approved,
with access limited to the minimum needed.

The GRC role here is to be an independent assessor, or an adviser to the Active
Directory team and other departments, holding them to what the security policy
requires. The lesson's closing argument: this work is what separates organisations
that get breached badly from those that don't. Where identity is managed well, one
compromised user means a password reset and little damage. Where it isn't, one
compromise can reach an admin account and take the business down.

## Key concepts

| Concept | What it means | Why it matters in practice |
| --- | --- | --- |
| Active Directory | Microsoft's domain controller and directory service | The identity backbone of most organisations |
| Domain controller | The server authenticating and authorising within a domain | Compromise it and you effectively own the environment |
| Groups | Collections of users carrying access appropriate to a function | Makes access manageable at scale; assign once, not per application |
| Joiner and leaver by group | Add to a group on joining, remove on departure | The mechanism that makes access changes fast and reversible |
| On-premises vs cloud directory | A local server, or the Microsoft cloud equivalent | Same function; different exposure, tooling and controls |
| Ownership | System administrators own and configure it, not security | Sets where your questions go and what you can reasonably ask for |
| Admin account count | How many privileged accounts exist | The fastest diagnostic available in an identity assessment |
| Unreviewed access requests | Access granted on request without approval | Where least privilege quietly stops being true |

## Where this shows up in a real job

This is the most directly familiar lesson in the module for me, because I've built
the thing. Running Windows Server and Active Directory in the home lab — and Entra
ID alongside it — makes groups, organisational units and group policy concrete
rather than abstract. When the lesson talks about assigning a user to a group and
the access following, I've watched that happen.

I want to be accurate about what that does and doesn't mean. Building a domain for
a handful of test users teaches the mechanics and the vocabulary. It doesn't teach
what an AD environment looks like after fifteen years of mergers, leavers who were
never removed, and groups nobody can explain — which is what an assessment actually
encounters. The lab gets me to informed questions faster; it isn't operational
experience.

The support parallel is real too: help desk work is often the front end of this
system. Password resets, account lockouts and access requests are Active Directory
operations, and being the person who processes an access request without any
approval step is exactly the gap the lesson describes.

## My take

**Terminology to keep current:** Microsoft renamed Azure Active Directory to
**Microsoft Entra ID**. Same service, and plenty of people still say Azure AD, but
the current name is what appears in documentation and job adverts now. Worth using
the new name and recognising the old one.

It's also worth being precise that the two aren't simply the same product in
different places. On-premises AD and Entra ID use different protocols and have
different attack surfaces — one is a domain on your network, the other an
internet-facing identity service. Most organisations run both, synchronised, and
the synchronisation between them is its own area of risk. For assessment purposes,
"we have Active Directory" and "we use Entra ID" describe different exposures and
deserve different questions.

Three things:

**The admin count is the best opening question in the module.** It's a single
number, quickly produced, immediately comparable against headcount, and it tells
you whether anything else in the identity programme is likely to hold. Worth
sharpening further by asking *which kinds* of admin — domain admins are the ones
that matter most, and an organisation with a handful of domain admins and many
local or application admins is in a very different position from one with fifty
domain admins.

**The most dangerous accounts are frequently not people.** Service accounts running
applications and scheduled tasks tend to hold high privilege, have passwords that
never change because something would break, belong to nobody in particular, and
are invisible to every process built around employees. "How many admin accounts"
should explicitly include them, and the follow-up — who owns this one and what
breaks if we disable it — is where the uncomfortable silences happen.

**Ownership sitting outside security is the point, not an obstacle.** The lesson
is clear that sysadmins own AD, and that's the right arrangement — but it means
every finding must be delivered to a team that doesn't report to you and that
knows the system far better than you do. Turning up with "you have too many admin
accounts" invites a reasonable defence about operational necessity. Turning up with
"here are the twelve accounts with domain admin, here's what each was created for,
and here are the four nobody can account for" is a conversation the other team can
actually act on. Specificity is what makes an external finding land, and it's also
what stops you sounding like someone who has only read about the system.
