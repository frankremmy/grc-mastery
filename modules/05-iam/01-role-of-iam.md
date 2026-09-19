# The role of IAM in cyber security

> Module 05, lesson 1. A field large enough to be its own career — and what a GRC
> professional's part in it actually is.

## Summary

Identity and access management is a field in its own right. Some treat it as part
of cyber security; in practice it's a specialisation with sub-specialisations
inside it, and plenty of people spend entire careers on nothing else.

It still sits under the cyber security umbrella, because at its core IAM is about
verifying who someone is and giving them access to the right resource or device at
the right time. "Someone" is broader than it sounds — a person, a group, a device,
or an application. The constant is granting access to something, for a defined
period.

The everyday example carries the two halves of the name. You're given a username
and password, you log in, and you reach your email. Behind that, the system
verifies you are who you claim to be — only John is supposed to hold John's
password — and that verification is **authentication**. That's the identity
management half. Once your identity is established, you're granted access to your
mailbox and whatever applications your job requires, based on who you are and what
role you hold. That's **authorisation**, the access management half.

Managing all this is genuinely complex, with tools, people and processes at
several layers. Passwords: complexity rules, how credentials are issued, when they
expire. Stronger authentication: a password plus a code by SMS or an authenticator
app. And then the harder problem — what someone can reach once they're in.
Granting everyone access to everything is a recipe for disaster, because a single
compromised user then hands an attacker the whole organisation. So the level of
access has to be managed deliberately, and the detail runs deep. The accounting
department needs the accounting application, but does every accountant need full
administrative rights? Should every accountant be able to delete financial
records?

**Where GRC fits.** Not configuring the tools, and not adding or removing users.
The GRC contribution is writing the policies — password complexity, requirements
for two-factor or multi-factor authentication — and the security principles the
implementation has to honour, such as separation of duties and least privilege.
And as consultants, assessing maturity: checking the processes are designed
properly, that identity and access are genuinely being managed, and that there are
no gaps between the design and the execution.

So the standard to aim for is comfort with the principles, processes and the
outlines of the tooling, plus the ability to find gaps and help organisations use
what they have better.

## Key concepts

| Concept | What it means | Why it matters in practice |
| --- | --- | --- |
| Identity and access management | Verifying who someone is and granting appropriate access for a defined time | The control layer almost every other control depends on |
| Authentication | Establishing that the user is who they claim to be | Answers "who are you" — the identity half |
| Authorisation | Granting access to specific resources based on identity and role | Answers "what may you do" — the access half |
| Non-human identities | Devices and applications also hold identities and access | Often the least governed accounts in an organisation |
| Time-bounded access | Access granted for the period it's needed, not indefinitely | Turns a standing privilege into a temporary one |
| Blast radius | What a single compromised account can reach | The reason universal access is untenable |
| Granularity of rights | Not just which system, but which actions within it | Full admin versus the ability to read; delete rights are their own question |
| The GRC role | Policy, principles and assessment — not configuration or user administration | Defines where your judgement is wanted and where it isn't |

## Where this shows up in a real job

Support work sits on the operating end of this. Every access request and every
"can you give me admin on this" is an authorisation decision, and when the policy
is unclear the person on the ticket ends up making it. That's the same observation
I made in module 1: unclear governance turns into risk decisions taken by whoever
is holding the queue.

WordPress makes the granularity problem visible. The role system distinguishes
administrator, editor, author and contributor — a reasonable model — and in
practice a great many sites hand out administrator because it's the role that
definitely works. The accountant-with-delete-rights question in this lesson is the
same question as whether the person who writes blog posts needs the ability to
install plugins.

My home lab work on Active Directory and Entra ID is configuration experience, and
worth being precise about what that does and doesn't demonstrate. I can build the
thing. That's different from assessing whether an organisation's joiner-mover-
leaver process actually works at scale, which is what a GRC role would ask of me.

## My take

The clearest thing in this lesson is the boundary. GRC writes the policy, sets the
principles, and assesses the gap between design and execution — it doesn't
provision accounts. That's a narrower remit than it first appears, and a more
defensible one: the value is in asking whether the model is right and whether
reality matches it, which is a different skill from operating the tooling.

Two things I want to hold onto:

**The interesting failures are in the gap between design and execution, not in the
design.** Almost every organisation has a password policy and a role model that
reads correctly. What an assessment finds is the accounts that kept their access
after someone changed role, the service account with domain admin because a
migration needed it in 2019, the shared login the team uses because individual
accounts were slow to get. The policy is rarely the problem; the drift is. That's
where the questions should point.

**Non-human identities are the easy thing to under-weight.** The lesson mentions
devices and applications almost in passing, but service accounts and machine
identities tend to have broad standing privileges, no expiry, no obvious owner and
no one to notice when they stop being needed — because none of the processes built
around humans apply to them. Asking "who owns this service account and what would
break if we disabled it" is the IAM version of the server nobody dares turn off.

Having a lab helps here, and I should be careful about how I use it. Building
Active Directory and Entra ID teaches what the controls are and how they're
configured, which makes the vocabulary real. It doesn't teach what happens when
four hundred people change roles a year, which is where identity programmes
actually fail. The honest framing is that the lab gets me to competent questions
faster, not that it substitutes for operating at scale.
