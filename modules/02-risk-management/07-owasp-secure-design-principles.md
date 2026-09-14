# The OWASP secure design principles

> Module 02, lesson 7. Eleven principles that apply well beyond web applications,
> and the reasoning behind each one.

## Summary

OWASP is best known for the **Top Ten**, a list of the most significant web
application security risk categories, which is a separate thing from what this
lesson covers and which I read separately as an assignment. This lesson is about
the **secure design principles** — general principles that apply to designing and
securing systems, and that scale up to how an organisation manages security
risk overall.

They're worth learning as a set rather than individually, because a lot of
security products and strategies are built around one or another of them, and
because they give you a vocabulary for saying *why* a design is weak rather than
just that it feels wrong.

## The principles

| Principle | What it means | The reasoning |
| --- | --- | --- |
| **Defence in depth** | More than one layer of protection, and the layers must be *different* — firewall, proxy, IDS/IPS, anti-malware, DLP | If an attacker gets past one layer, a different kind of control has a chance to stop or detect them. Duplicating the same control isn't depth — two identical firewalls in series fail to the same bypass |
| **Fail safe / fail secure** | When something goes wrong, the system should end up in a safe state rather than an open one — deny by default | A failure shouldn't hand out access. The lesson's emphasis is the related discipline: when a security issue is found, fix it properly and re-test to confirm the fix — rescan after remediation rather than assuming |
| **Least privilege** | A person or process gets the minimum access needed for the task, and only for as long as the task requires | The backup engineer gets a `backup` role that can only run backups, active only in the Friday 22:00–22:30 window. If those credentials are stolen, the attacker can't log in outside the window and can't do anything but back up. It caps the impact of a compromise |
| **Separation of duties** | No single person holds enough rights to abuse a critical system alone | Splits Active Directory admin into maintaining the directory, creating and deleting users, and applying updates. Removes both the abuse path and the single point of failure — one compromised account no longer means the whole estate |
| **Economy of mechanism** | Keep the design as simple as it can be — "keep it simple" | Complex security designs are hard to operate, and unmanageable controls are where the gaps appear. Simplicity is a security property, not just an engineering preference |
| **Complete mediation** | Every action gets checked against whether it's allowed, every time | Implemented organisationally as change management: an engineer can't just install updates, they raise a change, someone reviews it, it's approved and tracked. An attacker with the engineer's account still has to get an unusual request past a reviewer |
| **Open design** | Security must not depend on the design being secret | You wouldn't publish the network design, but if it leaked it shouldn't reveal a way in. Assume it becomes public one day and make sure that changes nothing |
| **Least common mechanism** | Minimise mechanisms shared between users — don't share the means of access | A shared password for the backup account means no accountability and a much wider blast radius. Individual credentials keep the compromise of one from being the compromise of all |
| **Psychological acceptability** | Security shouldn't be so burdensome that users work around it | Password rules onerous enough that people write them on a note by the keyboard have made things worse. There's always a trade to strike between security and usability |
| **Weakest link** | Your security is only as strong as its weakest point | Elaborate encryption and token handling still comes down to a four-character password if that's what guards the front door. Look for the weak point deliberately rather than reinforcing what's already strong |
| **Leverage existing components** | Reuse tested, trusted components rather than building from scratch | New code carries unknown bugs and vulnerabilities. Something proven in the field has had the obvious problems found already |

## Where this shows up in a real job

Several of these describe things I've watched go wrong in the WordPress world.

**Leveraging existing components** is the entire plugin ecosystem — nobody writes
their own contact form, and that's correct. It's also where the vulnerabilities
come from, which is the tension I work with directly in my CVE detection lab: the
reused component is the tested one *and* the one with the published advisory.

**Least privilege** maps onto WordPress roles, and the gap between the model and
reality is wide. The role system distinguishes administrator, editor, author and
contributor; a lot of sites hand out administrator because it's the one that
definitely works. The support equivalent is the access I hold to do my job, which
is broad because the job is broad.

**Least common mechanism** is the shared admin login — one set of credentials that
the agency, the freelancer and the client all use. When something changes, nobody
can say who did it.

**Psychological acceptability** is visible in every support conversation about
two-factor authentication. The control is right and the friction is real, and
users who find it intolerable find a way around it.

## My take

The one I'll remember is defence in depth meaning *different*, not *more*. Layers
of the same control fail to the same bypass, so a design with five identical
checks has one check. The same logic applies to the weakest link principle from
the other direction: adding strength where you're already strong buys nothing.

Three threads worth holding:

**Least privilege has a time axis.** Restricting what an account can do is the
half everyone knows. Restricting *when* it can do it is the half that gets
skipped, and it's most of the value in the backup example — stolen credentials
are useless for 167 hours of the week.

**Complete mediation is why change management exists.** I'd previously filed change
approval as bureaucracy. Framed as "every action is checked against whether it's
allowed", it's the same principle as an access check in code, applied to humans —
and the reviewer is the control, which means a rubber-stamp reviewer removes it.

**Reuse is both a principle and a risk.** Leverage existing components says use the
tested thing. The current OWASP Top 10 puts software supply chain failures in its
top three. Both are true: the component you didn't write is safer than the one you
would have written badly, *and* it's an inherited dependency you don't control.
The principle is about not reinventing; it isn't permission to skip knowing what
you've pulled in.

There's also a neat symmetry between these principles and the Top Ten — insecure
design and mishandling of exceptional conditions are both, in effect, what these
principles look like when they're absent.
