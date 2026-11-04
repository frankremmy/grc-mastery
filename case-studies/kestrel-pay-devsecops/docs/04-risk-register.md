# 04 — Risk register entries and quantification

Code findings become risks once they're expressed as business impact. Risk owners are the business, not security.

## Register extract

| Risk ID | Risk | Linked findings | L × I (5×5) | Owner | Treatment | Due |
|---|---|---|---|---|---|---|
| R-01 | Card data exposed through logs and the log/SIEM pipeline | KP-05 | 4 × 5 = **20** | Head of Engineering | Mitigate: code fix, purge historic logs, detection rule for PAN patterns in logs | 14 days |
| R-02 | Fraudulent refunds through an unauthenticated or unlimited endpoint | KP-04, KP-06 | 3 × 5 = **15** | Head of Payments Ops | Mitigate: authentication, limits, dual approval above threshold | 7 days |
| R-03 | Cross-tenant card data disclosure | T2, KP-02, KP-03 | 3 × 5 = **15** | Head of Engineering | Mitigate: tenant binding, parameterised SQL, masking | 14 days |
| R-04 | Known-vulnerable components reach production | KP-09 | 4 × 3 = **12** | DevOps Lead | Mitigate: SCA gate, Dependabot, weekly re-scan | 30 days |
| R-05 | Credential compromise (hardcoded key, weak hashes) | KP-01, KP-07 | 3 × 4 = **12** | Head of Engineering | Mitigate: rotate key, vault, Argon2 with forced reset | 14 days |

## FAIR estimate for R-01 (card data in logs)

The method and spreadsheet are my [FAIR calculator](../../../deliverables/11-fair-calculator.xlsx). Every number below is an **illustrative assumption**, stated so it can be challenged.

| Factor | Assumption | Basis |
|---|---|---|
| Records exposed | ~50,000 PANs (12 months of refund traffic) | Refund volume × log retention |
| Loss event frequency | 0.15 per year (range 0.05–0.4) | Wide log access (developers, SIEM admins, support). Logs shipped to a third-party SIEM |
| Primary loss | €180k–€320k | Forensic investigation (PFI), engineering response, card reissue costs passed back by issuers |
| Secondary loss | €150k–€600k | Card-brand non-compliance assessments, customer contract penalties, possible loss of a bank customer |
| **Annualised loss exposure** | **≈ €95k** most likely (range €20k–€370k) | LEF × total loss magnitude |
| Cost to treat | ≈ €6k | 3 developer days, a log purge, one SIEM rule |

**What I'd tell the risk owner:** the fix costs about 6% of a single year's expected loss and removes the driver of a reportable card-data incident. This is a mitigate decision, not an accept. A residual-risk re-score is due after the log purge has been verified.
