# 03 — Secure code review and scan results

Target: `app/app.py` and `app/requirements.txt`, the vulnerable baseline. Method: a manual review led by the threat model, then the automated tools. The output of every tool is in [`../scans/`](../scans/), and the normalised list is in [`../evidence/findings.csv`](../evidence/findings.csv).

## Findings

| ID | Finding | OWASP / CWE | Severity | Found by | Fix (in `app-remediated/`) |
|---|---|---|---|---|---|
| KP-01 | Live API secret hardcoded in source | A07 / CWE-798 | High | Semgrep (custom), Bandit B105 | Loaded from the environment or a vault. Rotate the leaked key |
| KP-02 | SQL injection in card lookup | A03 / CWE-89 | High | Semgrep (custom), Bandit B608 | Parameterised query |
| KP-03 | Full PAN returned in the API response | A02 / CWE-359 | High | **Manual only** | `mask_pan()`: first 6 and last 4 digits at most |
| KP-04 | Refund endpoint has no authentication | A01 / CWE-306 | Critical | Semgrep (custom rule) | `@require_api_key` on every route, constant-time compare |
| KP-05 | PAN and CVV written to the application log | A09 / CWE-532 | Critical | Semgrep (custom PCI rule) | CVV no longer accepted. PAN masked. Existing logs purged |
| KP-06 | No server-side refund limit | A04 / CWE-840 | High | **Manual only** | Range check, configurable ceiling |
| KP-07 | Unsalted MD5 for merchant passwords | A02 / CWE-916 | High | Semgrep (custom), Bandit B324 | Argon2id |
| KP-08 | Flask debug console enabled, binds 0.0.0.0 | A05 / CWE-489 | Medium | Semgrep, Bandit B201/B104 | Debug off, binds to loopback behind the gateway |
| KP-09 | Outdated dependencies: **27 unique advisories** across Flask, Werkzeug, Requests and transitive packages | A06 / CWE-1104 | High | pip-audit | Supported versions. Dependabot and a weekly scheduled re-scan |
| — | Cross-tenant read (merchant ID from query string) | A01 / CWE-639 | High | **Manual (threat model T2)** | Merchant ID bound to the authenticated key |

## Before and after

| | Vulnerable `app/` | Remediated `app-remediated/` |
|---|---|---|
| Semgrep (6 custom PCI/OWASP rules) | 6 findings | 0 |
| Bandit | 5 findings (2 high, 2 medium, 1 low) | 0 |
| pip-audit | 27 unique advisories in 5 packages | 0 |
| Normalised by `evidence_pack.py` | 12 unique (2 critical, 8 high, 1 medium, 1 low) | 0 → gate passes |

## What the exercise taught

1. **Three of the ten issues were found only by a person.** Unmasked PAN in responses, a missing business limit, and the cross-tenant read are logic problems. Scanners cover the known patterns, and review effort should go where scanners can't reach. That's why the threat model came first.
2. **Generic rulesets miss payment-specific risk.** No off-the-shelf rule knows that `cvv` in a log line is a PCI violation, so I wrote custom Semgrep rules ([`.semgrep/pci-rules.yml`](../.semgrep/pci-rules.yml)). A payments company should own a small rule pack like this.
3. **Rules need tuning, or developers stop trusting the gate.** My first version of `unauthenticated-money-endpoint` flagged the *fixed* refund route, because it didn't recognise the decorator. I added an exclusion for `@require_api_key` and re-ran both apps (6 → 6 on vulnerable, 1 → 0 on remediated). Every rule change gets the same before/after check.
4. **Dependencies dominate the count but not the risk.** 27 advisories came from a single stale pin. The two critical findings came from code the team wrote. Triage weighs exposure and data impact, not the volume of findings.

## Developer-facing write-up (example, KP-05)

> **Card data in application logs (critical).** `refund()` logs the request PAN and CVV at INFO level (app.py line 47). Anyone with access to `api.log` or the SIEM can read full card data, and storing CVV after authorisation is never permitted (PCI DSS 3.3.1). **Fix:** stop accepting CVV on this endpoint, and log `mask_pan(pan)` only (see `app-remediated/app.py`). **Also needed:** purge historic logs and SIEM indexes, and confirm the retention copies are gone. I can pair on this today.

The tone is deliberate: what's wrong, where it is, why it matters, how to fix it, and an offer of help. The standard gets cited once, not lectured.
