# 07 — Secure coding standard (one page) and training outline

## Kestrel secure coding standard v1.0 — the ten rules

1. **Every route is authenticated** through the shared decorator. Unauthenticated routes need ISO sign-off.
2. **Tenant identity comes from the credential,** never from request parameters.
3. **Parameterised queries only.** String-built SQL fails CI.
4. **Card data:** never accept, log or store CVV. Log PAN only through `mask_pan()`. Store PAN only as a token.
5. **Secrets come from the vault or environment.** A committed secret means immediate rotation and an incident ticket.
6. **Passwords are hashed with Argon2id.** MD5 or SHA-1 for credentials fails CI.
7. **Money-moving actions** have server-side limits and a structured audit event.
8. **No debug features** in non-local builds.
9. **Dependencies** run on supported versions. A high/critical advisory blocks the merge unless an exception has been risk-accepted.
10. **Changes touching auth, payments or card data** need a reviewer from the security champions list.

Each rule maps to a CI check or a review checklist item, so the standard can be enforced and not just read.

## Secure coding training (60 minutes, developers)

| Block | Content | Format |
|---|---|---|
| 10 min | Why it matters here: KP-05 and the FAIR estimate, in money not jargon | Talk |
| 20 min | Find the bug: the vulnerable `app.py`, in pairs | Hands-on |
| 15 min | Read your own scan output: walk through a failing pipeline and fix it | Live demo |
| 10 min | The ten rules and the security champion role | Talk |
| 5 min | Five-question check. The result is recorded in the LMS as competence evidence (A.6.3, PCI DSS 6.2.2) | Quiz |

The content is refreshed every year and whenever a new finding class appears in production.
