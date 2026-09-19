# Managing passwords in the real world

> Module 05, lesson 4. The conversation you'll have most often, and how much of
> the received wisdom is out of date.

## Summary

Passwords aren't going away, even as MFA spreads, so the questions keep coming.
How long? How short? Capital letters, special characters? How often should users
change them? Can they reuse one from six months ago?

**First, split the question in two.** Before answering anything, establish whether
the conversation is about **end-user passwords** — what employees use day to day —
or **privileged and system accounts**: admin credentials, the passwords used to
configure systems, especially systems holding critical data. Completely different
problems, completely different rules. Privileged credentials should be
substantially more demanding than user ones, which isn't licence for users to have
weak passwords, but the distinction has to be explicit before any useful advice
can follow.

**Second, most of the familiar rules are obsolete.** Minimum lengths dressed up
with mandatory capitals, lower case and special characters are twenty-year-old
practice still in wide use. Current NIST guidance says something different:

- **Length is what matters.** Short passwords are far easier to guess; longer is
  better.
- **Use passphrases.** A sentence — "this GRC course is the best course ever and I
  learned so much" — is long, memorable, and harder to guess than a short password
  bristling with special characters.
- **Don't force periodic changes.** Only require a change where there's evidence
  the password has been compromised. Forced rotation drives users to recycle
  passwords they already use for Facebook or LinkedIn, and once one of those is
  breached the work account follows — particularly since people list their employer
  on those profiles. A unique long password that hasn't been compromised doesn't
  need changing.

**Third, expect resistance and legacy constraints.** Not every organisation
receives this well; some users don't know what a passphrase is, and educating them
falls jointly to IT and security. And longer passwords surface a practical
obstacle: legacy applications that cap passwords at 16 or 25 characters. That cap
is a red flag in its own right — an application that old is likely vulnerable in
other ways too, and the real recommendation is to plan its decommissioning rather
than to design the password standard around its limitations.

## What the current NIST guidance actually says

The authoritative source is **NIST SP 800-63B-4, Digital Identity Guidelines:
Authentication and Authenticator Management**. It calls passwords "memorized
secrets" and states requirements as SHALL / SHALL NOT:

| Requirement | Wording |
| --- | --- |
| Minimum length, single factor | **SHALL** require a minimum of **15 characters** where a password is the only factor |
| Minimum length, within MFA | **SHALL** require a minimum of **8 characters** |
| Maximum length | **SHOULD** permit at least **64 characters** |
| Composition rules | **SHALL NOT** impose composition rules such as requiring mixtures of character types |
| Periodic change | **SHALL NOT** require periodic password changes; **SHALL** force a change on evidence of compromise |
| Blocklists | Compare the proposed password against a blocklist of common, expected or compromised passwords |
| Password hints | **SHALL NOT** allow a hint retrievable by anyone not yet authenticated |
| Security questions | **SHALL NOT** prompt for knowledge-based authentication — "what was the name of your first pet" — when choosing passwords |

Two of these are worth noticing. The **15-character single-factor minimum** is
higher than most organisations enforce and higher than most practitioners expect.
And the blocklist requirement is the part that does the real work: length alone
doesn't help if the chosen phrase is one of the million most common.

## Key concepts

| Concept | What it means | Why it matters in practice |
| --- | --- | --- |
| End-user vs privileged passwords | Two separate problems with separate rules | Answering without establishing which produces bad advice |
| Passphrase | A long memorable sentence used as a credential | Reconciles length with human memory |
| Composition rules | Mandatory character-type mixtures | Now advised against — they add little and push users to predictable patterns |
| Forced rotation | Requiring periodic change regardless of compromise | Advised against; drives reuse of personal passwords |
| Change on compromise | The one trigger that does warrant a reset | Replaces rotation as the rule |
| Password blocklist | Screening against known-compromised and common passwords | Where most of the actual protection comes from |
| Credential reuse | Same password on work and personal accounts | The mechanism that turns someone else's breach into yours |
| Legacy length caps | Applications refusing passwords over 16–25 characters | A symptom of a system with wider problems |

## Where this shows up in a real job

Password resets are routine support work, and the reuse pattern the lesson
describes is visible from that seat. People do not invent a new password each time;
they iterate one they already have, or they fall back to the one they use
everywhere. Any policy that ignores this is designing for a user who doesn't exist.

The legacy cap point matches the WordPress ecosystem, where a plugin or a hosting
panel silently truncating or rejecting a long password is a real occurrence — and
it's always a signal about the rest of the codebase rather than an isolated
quirk.

The distinction between user and privileged credentials is also where my home lab
is genuinely relevant: setting up Active Directory makes the difference concrete,
because domain admin and a standard user account are visibly different objects with
different consequences, not just different entries in a policy document.

## My take

The most useful habit in this lesson is refusing to answer the question as asked.
"What should our password policy be" is unanswerable until you know whether it's
about staff or about administrative access to critical systems. That's a small
reframe that immediately makes the advice better, and it's the same move as asking
what business this is before writing an asset list.

Three things:

**The blocklist is the control that matters most, and it's the least discussed.**
Length rules assume attackers guess character by character. They mostly don't —
they try passwords that have already appeared in breaches. A fifteen-character
passphrase that happens to be a song lyric is long and already in the wordlists.
Screening proposed passwords against known-compromised sets addresses the actual
attack, and it's the requirement people skip because it needs a service rather than
a settings change.

**Dropping rotation is right and it needs a replacement, not just a removal.**
"Never change passwords" only holds if you can detect compromise, which means
monitoring credentials against breach data, watching for anomalous sign-ins, and
having a process to force a reset quickly when something surfaces. An organisation
that removes rotation without building detection hasn't modernised — it has simply
stopped doing the one thing it was doing. Worth stating explicitly when
recommending the change, because the old control was at least visible.

**The legacy cap is a finding about the application, not about passwords.** A
system that rejects a 30-character password is telling you how it stores
credentials, and the answer is rarely reassuring — truncation implies fixed-width
storage and often predates modern hashing entirely. The right move in an assessment
is to treat the cap as evidence and ask what else is true of that system, rather
than negotiating the policy down to fit it.

One connection back to the previous lessons: NIST explicitly says **not** to use
security questions. That sits awkwardly beside the earlier framing of a mother's
maiden name or a favourite city as a legitimate additional check. Knowledge-based
answers are guessable, findable and unchangeable once exposed, which is why current
guidance rules them out rather than treating them as a weaker option.

## Reference

- NIST SP 800-63B-4, Digital Identity Guidelines: Authentication and Authenticator
  Management — <https://pages.nist.gov/800-63-4/sp800-63b.html>
