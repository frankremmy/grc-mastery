# Privileged Access Management (PAM)

> Module 05, lesson 7. Controlling the accounts that can do anything — and
> checking whether the control is actually being used.

## Summary

PAM is the management of highly privileged accounts — admin and root accounts with
effectively absolute access. Compromise of one is catastrophic, so they warrant
disproportionate attention.

Every application and system has an admin account with full control: provisioning
access, creating and deleting users, and in a financial records system, adding or
deleting records. Those capabilities are needed. They aren't needed by everyone.

**Restrict the number.** The first PAM measure is keeping admin accounts to an
absolute minimum. One is good. Zero standing admin accounts is achievable — harder
to implement, but it exists. Many admin accounts is the red flag: a sign the system
is mismanaged and the attack surface is larger than it needs to be.

**Control how they're accessed.** MFA on admin accounts is non-negotiable. An
admin account reachable with a password alone is a disaster waiting to happen.

**Demand strong passwords on them.** Admin credentials must be significantly more
complex than user ones. The cautionary story from the lesson: years ago, `qwerty`
was used as the root password on systems at major airports and financial
institutions — because nobody expected to use the root account, so nobody thought
about the password. That was a world where those systems weren't internet-facing.
It isn't this one. Expect to find dormant admin accounts with trivially guessable
passwords.

**Dedicated tooling, for mature organisations.** Specialist products exist solely
to manage privileged accounts — CyberArk is a commonly seen example. The pattern:
the root or admin account is disabled entirely, and access requires a special
password and token split across several people, who together can provision access.
The requester receives a temporary password valid for perhaps ten or twenty
minutes, performs the task, and the account locks again. Highly effective, and
common in mature organisations.

**Then the caveats, which are the real content of the lesson.** Organisations
asked about privileged access will say they have CyberArk and it's under control.
Two follow-up questions matter:

*Is it deployed everywhere?* An organisation may have hundreds or thousands of
applications. A tool implemented somewhere is not a tool implemented everywhere,
and coverage is what you're assessing.

*Is it actually being used?* This one takes longer to find. The lesson's example:
system administrators who correctly lock the main account behind CyberArk, and then
maintain a separate self-created account with full admin rights, outside the tool,
because it's faster. That account has a weak password and no oversight — and it's
how some organisations get breached. The vaulted account is safe; the shadow one
isn't.

So: a tool being implemented doesn't mean it's configured properly, and it
certainly doesn't mean everyone is using it as intended.

## Key concepts

| Concept | What it means | Why it matters in practice |
| --- | --- | --- |
| Privileged account | Admin or root — effectively unlimited access to a system | The highest-consequence credential in any environment |
| Minimising admin accounts | Keeping the count as low as the work allows | Fewer accounts, less to attack and less to monitor |
| Zero standing privilege | No permanently privileged accounts; access is granted when needed | The strongest model, and the hardest to implement |
| MFA on privileged accounts | Non-negotiable additional factor | Password-only admin access is indefensible |
| Credential vaulting | The privileged password held by a tool, not by people | Removes the shared password everyone knows |
| Split approval | Multiple people required to release access | Separation of duties applied to privilege itself |
| Just-in-time access | Temporary credential valid for minutes, then revoked | Turns standing privilege into a bounded event |
| Coverage | Whether the tool reaches every system, not just some | The first question after "do you have a PAM tool" |
| Bypass accounts | Self-created admin accounts outside the tool | The finding that matters most, and the hardest to see |

## Where this shows up in a real job

The bypass pattern is the one I recognise most clearly, because the motivation is
familiar rather than malicious. When the sanctioned route is slow and the work is
urgent, people build a faster route. In WordPress terms it's the extra
administrator account created "temporarily" for a migration and never removed, or
FTP credentials shared because the proper process took two days. Nobody in that
story is acting in bad faith, and the outcome is an unmanaged privileged
credential either way.

My home lab is useful for the mechanics here but genuinely limited: I can create
privileged accounts and apply policies to them, and there's nobody in the lab with
an incentive to work around me. The human half of PAM — which is most of it — isn't
reproducible on your own hardware.

The support parallel is that elevated access is often granted informally and
temporarily, and the temporary part is the bit that decays. "Just for today" is a
sentence that survives for years.

## My take

The strongest idea in this lesson isn't the tooling — it's that **a control's
existence and a control's coverage are different findings, and its actual use is a
third.** That maps exactly onto the audit ladder from module 3: the control
exists, it's designed correctly, it covers the estate, it operates, and something
happens when it fires. PAM is where those distinctions become concrete, because an
organisation can truthfully say "we have CyberArk" while two of the five rungs are
missing.

Three things:

**The bypass account is the finding, and it's found by asking sysadmins, not by
reading configuration.** No dashboard lists accounts that exist outside the
dashboard. What surfaces them is reconciling the directory's full list of
privileged accounts against the PAM tool's inventory and asking about every
difference — plus spending enough time with the team that someone mentions the
account they use when the vault is slow. That second route is why the lesson says
it only emerged during longer engagements.

**Bypasses are a usability signal before they're a discipline problem.** If
administrators are routing around the tool, the sanctioned path is too slow for
real work. Reporting "administrators are bypassing PAM" gets defensiveness;
reporting "administrators bypass PAM because checkout takes twenty minutes during
an incident, and here's the shadow account that resulted" gets a fixable problem.
Same finding, and only one version leads anywhere.

**Zero standing privilege is worth understanding as the direction of travel.** The
lesson mentions organisations with zero admin accounts almost in passing, and
that's the model modern PAM aims at: nobody holds privilege permanently, access is
requested, approved and time-bound, and every use is recorded. It reframes the
question from "how few admins can we have" to "why does anyone hold this
permanently" — and the just-in-time pattern described with CyberArk is already that
idea, just applied to one account rather than as a principle.

On the `qwerty` story: the underlying reasoning is what's worth keeping. The
password was weak precisely *because* nobody used the account, and an account
nobody uses attracts no attention, no monitoring and no rotation. Dormant
privileged accounts are more dangerous than busy ones for exactly that reason, and
"show me every privileged account that hasn't been used in ninety days" is a
question with an uncomfortable answer in most organisations.
