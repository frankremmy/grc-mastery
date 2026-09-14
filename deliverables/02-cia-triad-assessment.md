# CIA triad assessment — Oscorp confidential formulation document

**Module:** 02 — Cyber Security Risk Management
**Type:** Practical assessment
**Status:** My own answer, written before watching the solution video.

---

## Scope

Oscorp is at an early stage of developing a new medication under high
confidentiality. The Chief Scientist, Harry Osborn, has compiled the candidate
ingredient list, and it currently exists as a Microsoft Word document.

The assessment covers that document — not the wider project, not the lab, not
Oscorp's estate. One file, three properties.

That narrowness is the point. It's also why proportionality matters: this is one
document at an early stage, and recommendations heavy enough to be ignored are
worse than lighter ones that get followed.

## Assumptions

Oscorp's profile is still thin (see
[`../capstone-nist-program/oscorp-profile.md`](../capstone-nist-program/oscorp-profile.md)).
Working assumptions for this assessment, to be corrected as facts arrive:

- The formulation is crown-jewel intellectual property; its loss to a competitor
  is the worst commercial outcome available to Oscorp at this stage.
- No patient or human-subject data is involved yet, so this is not a privacy
  assessment. That changes the moment trials are in scope.
- Oscorp has some managed IT estate available — email, file storage, identity —
  even if this document isn't currently in it.

---

## Questions for Harry

### Confidentiality — who can see it

1. Where does the document physically live right now — your laptop, a network
   share, a managed cloud location, a USB drive, a personal account?
2. Is that location managed by Oscorp IT, or is it yours?
3. Who has access to it today? Name them.
4. Has anyone *had* access who no longer needs it — a colleague you shared an
   early draft with, an assistant, anyone who has since left the project?
5. How has it been shared so far? Email attachment, a link, a copy handed over?
6. Are there any active sharing links, and do they expire?
7. Is the device it sits on encrypted, and is the document itself protected?
8. Do you access it from any personal device, or sync it to any personal cloud
   account?
9. Are there printed copies? Where are they kept?
10. Has any part of it been pasted into an external tool — a translation service,
    an AI assistant, an online converter?
11. Who *will* need it as the project grows — lab staff, procurement, suppliers?
    Does a supplier need the full list, or only individual items?
12. Does Oscorp have a data classification scheme, and has this been classified?

### Integrity — who can change it, and would you know

13. Who can edit the document, as opposed to read it?
14. Is there a single authoritative copy, or are there several versions in
    circulation?
15. Do you have version history, and can you see who changed what?
16. Are the accounts with access individual, or does anyone share a login?
17. If an ingredient name or a quantity were altered — deliberately or by
    accident — how would you find out, and how quickly?
18. Is there any review step before this list is acted on, such as ordering
    materials or beginning an experiment?
19. Is there an offline reference — a lab notebook, a signed copy — that the
    document could be checked against?

### Availability — what happens when it's gone

20. If the laptop were lost, stolen, or failed this afternoon, what would happen
    to the project?
21. Is the document backed up? Where, how often, and has a restore actually been
    performed and verified?
22. If the file were encrypted by ransomware, what's the recovery path and how
    long would it take?
23. Is there an offline or immutable backup copy, or would a backup connected to
    the same account be encrypted too?
24. If you were unavailable for two weeks, who else could reach this document?
25. How long could the project tolerate not having it — hours, days, weeks?

---

## Recommendations

Proportionate to an early-stage project and one document. Sequenced so the cheap,
high-value moves come first.

### Confidentiality

| # | Recommendation | What it does |
| --- | --- | --- |
| C1 | Move the document out of local or personal storage into a managed, access-controlled location owned by Oscorp | Reduces likelihood — puts the file where access can be granted, revoked and logged |
| C2 | Apply least privilege: an explicit, named access list limited to those who need it now, not those who might later | Reduces likelihood, and limits how far a single compromised account reaches |
| C3 | Individual accounts with multi-factor authentication; no shared logins or shared links | Reduces likelihood, and makes every access attributable |
| C4 | Revoke and expire any existing sharing links; confirm nothing is reachable by anyone outside the named list | Closes exposure that already exists |
| C5 | Classify and label the document under Oscorp's scheme, or agree a handling standard for it if no scheme exists yet | Makes the handling rules explicit rather than assumed |
| C6 | Encrypt at rest, and ensure full-disk encryption on any endpoint that holds a copy | Reduces impact of a lost or stolen device |
| C7 | Agree that the content goes into no external or personal service — personal cloud, personal email, third-party online tools | Closes the routes that bypass every other control |
| C8 | Consider splitting the formulation: ingredients in one document, quantities and process in another, with separate access | Reduces impact — a single leak yields an incomplete picture |
| C9 | Give suppliers only the individual items they need to fulfil, never the compiled list | Reduces impact as the project involves third parties |
| C10 | Schedule an access review as the project grows, and revoke on role change or departure | Keeps the access list from drifting |

### Integrity

| # | Recommendation | What it does |
| --- | --- | --- |
| I1 | Establish one authoritative copy and stop circulating the document by email attachment | Removes version ambiguity, which is where quiet errors survive |
| I2 | Enable version history and audit logging of access and edits | Makes change detectable and attributable after the fact |
| I3 | Separate read access from edit access; most people who need to see it don't need to change it | Reduces likelihood of both malicious and accidental modification |
| I4 | Require a second-person check on ingredient names and quantities before the list is used to order materials or run an experiment | Catches the error that a technical control cannot |
| I5 | Keep an independent reference — a signed or offline record — the document can be reconciled against | Gives you a known-good baseline to compare to |

### Availability

| # | Recommendation | What it does |
| --- | --- | --- |
| A1 | Automated backup of the managed location, with a restore that has actually been tested rather than assumed | Reduces impact of loss or corruption |
| A2 | At least one backup copy that is offline or immutable | Ensures ransomware can't encrypt the recovery path along with the original |
| A3 | Name a delegate with standing access so the project isn't blocked if Harry is unavailable | Removes the key-person single point of failure |
| A4 | Agree how long the project can tolerate losing the document, and check the backup arrangement actually meets it | Turns "we have backups" into a number that can be verified |

---

## Assessment notes

**Confidentiality dominates, but integrity carries the worst consequence.** The
obvious risk is the formula leaking to a competitor, and most of the effort
belongs there. But an altered ingredient or quantity, acted on without anyone
noticing, is a research failure at best and a safety event at worst — and unlike
a leak, it can happen without an attacker and without anyone realising for
months. Integrity is the leg most likely to be under-weighted here, which is why
recommendations I4 and I5 are human checks rather than technical controls.

**Availability is real but currently the smallest of the three.** At this stage
the ingredient list could plausibly be reconstructed by the person who wrote it.
That stops being true quickly as the work progresses, so the backup
recommendations are cheap now and expensive to retrofit later.

**Proportionality is itself a control decision.** A document this sensitive
invites an ambitious answer — DLP, rights management, monitoring. At this stage
that would be disproportionate, and worse, it would probably be circumvented: if
the managed location is painful, a copy ends up on the desktop and every control
above becomes theoretical. The recommendations are deliberately ones a working
scientist will accept.

**Out of scope, flagged rather than assessed.** Protection of the formulation as
intellectual property is a legal question as much as a security one — patent
timing, confidentiality agreements with staff and suppliers. No personal data is
in scope yet; that changes at the point trials involve human subjects, and a
privacy assessment would be needed then. Physical security of the lab and of
printed copies is adjacent and worth a separate look.

**A question this assessment can't answer.** Whether the confidential project has
different access rules from the rest of Oscorp, and who can grant an exception to
them, is a governance question that sits above this document. Given the project's
sponsor is also the person most invested in its progress, it's worth settling
early.
