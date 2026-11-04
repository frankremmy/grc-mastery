#!/usr/bin/env python3
"""
Build an assessor-ready evidence pack from DevSecOps scanner output.

Reads Semgrep, Bandit and pip-audit JSON, normalises the findings, maps each one
to the control it evidences, and writes:
  evidence/findings.csv       - one row per finding, ready for the risk register
  evidence/evidence-index.md  - what each file proves, with SHA-256 and timestamp

Usage: python3 tools/evidence_pack.py <scan-dir> <out-dir> [--fail-on high]
"""
import argparse
import csv
import datetime as dt
import hashlib
import json
import pathlib
import sys

# Rule/test id -> (finding title, severity, control references)
CONTROL_MAP = {
    "pci-cvv-or-pan-in-logs":       ("Card data written to logs", "critical",
                                     "PCI DSS 3.3.1, 3.5.1; ISO 27001 A.8.11, A.8.15"),
    "sqli-string-concat":           ("SQL injection", "high",
                                     "PCI DSS 6.2.4; OWASP A03; ISO 27001 A.8.28"),
    "B608":                         ("SQL injection", "high",
                                     "PCI DSS 6.2.4; OWASP A03; ISO 27001 A.8.28"),
    "unauthenticated-money-endpoint": ("Unauthenticated refund endpoint", "critical",
                                     "PCI DSS 6.2.4, 7.2; OWASP A01; ISO 27001 A.8.3"),
    "hardcoded-live-api-secret":    ("Hardcoded secret", "high",
                                     "PCI DSS 6.2.4, 8.6.2; OWASP A07; ISO 27001 A.8.24"),
    "B105":                         ("Hardcoded secret", "high",
                                     "PCI DSS 6.2.4, 8.6.2; OWASP A07; ISO 27001 A.8.24"),
    "weak-password-hash":           ("Weak password hashing", "high",
                                     "PCI DSS 8.3.2; OWASP A02; ISO 27001 A.8.24"),
    "B324":                         ("Weak password hashing", "high",
                                     "PCI DSS 8.3.2; OWASP A02; ISO 27001 A.8.24"),
    "flask-debug-enabled":          ("Debug mode enabled", "medium",
                                     "PCI DSS 2.2.4; OWASP A05; ISO 27001 A.8.9"),
    "B201":                         ("Debug mode enabled", "medium",
                                     "PCI DSS 2.2.4; OWASP A05; ISO 27001 A.8.9"),
    "B104":                         ("Binds to all interfaces", "low",
                                     "PCI DSS 1.2.5; ISO 27001 A.8.20"),
}
SEV_ORDER = {"critical": 4, "high": 3, "medium": 2, "low": 1}


def sha256(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path):
    return json.loads(path.read_text()) if path.exists() else None


def from_semgrep(data):
    for r in data.get("results", []):
        rid = r["check_id"].split(".")[-1]
        yield "semgrep", rid, r["path"], r["start"]["line"]


def from_bandit(data):
    for r in data.get("results", []):
        yield "bandit", r["test_id"], r["filename"], r["line_number"]


def from_pip_audit(data):
    for dep in data.get("dependencies", []):
        ids = sorted({v["id"] for v in dep.get("vulns", [])})
        if ids:
            yield ("pip-audit", f'{dep["name"]}=={dep["version"]}', "requirements.txt",
                   f"{len(ids)} advisories: {', '.join(ids[:3])}{'...' if len(ids) > 3 else ''}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("scan_dir", type=pathlib.Path)
    ap.add_argument("out_dir", type=pathlib.Path)
    ap.add_argument("--fail-on", choices=SEV_ORDER, default=None,
                    help="exit 1 if any finding is at or above this severity (CI gate)")
    args = ap.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)

    sources = {
        "semgrep.json": from_semgrep,
        "bandit.json": from_bandit,
        "pipaudit.json": from_pip_audit,
    }
    rows, seen = [], set()
    for name, parser in sources.items():
        data = load(args.scan_dir / name)
        if data is None:
            continue
        for tool, rule, path, loc in parser(data):
            if tool == "pip-audit":
                title, sev, ctrl = ("Vulnerable dependency", "high",
                                    "PCI DSS 6.3.1, 6.3.3; OWASP A06; ISO 27001 A.8.8")
            else:
                title, sev, ctrl = CONTROL_MAP.get(rule, (rule, "medium", "triage required"))
            # de-duplicate the same issue reported by two tools (lines can differ by one)
            key = (title, path) if tool != "pip-audit" else (rule,)
            if key in seen:
                continue
            seen.add(key)
            rows.append({"id": "", "title": title, "severity": sev,
                         "tool": tool, "rule": rule, "location": f"{path}:{loc}",
                         "controls": ctrl})

    rows.sort(key=lambda r: -SEV_ORDER[r["severity"]])
    for i, r in enumerate(rows, 1):
        r["id"] = f"SC-{i:02d}"
    with (args.out_dir / "findings.csv").open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]) if rows else ["id"])
        w.writeheader()
        w.writerows(rows)

    now = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [f"# Evidence index\n\nGenerated {now} by `tools/evidence_pack.py`.\n",
             "| File | What it evidences | SHA-256 |", "|---|---|---|"]
    purpose = {
        "semgrep.json": "SAST with custom PCI rules (PCI DSS 6.2.4, 6.3.2; Secure SLC)",
        "bandit.json": "Python SAST (PCI DSS 6.2.4)",
        "pipaudit.json": "Software composition analysis (PCI DSS 6.3.1, 6.3.3)",
        "zap-report.html": "DAST baseline (PCI DSS 6.4.1, 11.3)",
        "gitleaks.json": "Secret scanning (PCI DSS 8.6.2)",
    }
    for name, why in purpose.items():
        p = args.scan_dir / name
        if p.exists():
            lines.append(f"| `{name}` | {why} | `{sha256(p)[:16]}…` |")
    counts = {s: sum(r["severity"] == s for r in rows) for s in SEV_ORDER}
    lines += ["", f"**Findings:** {len(rows)} unique "
              f"({', '.join(f'{v} {k}' for k, v in counts.items() if v)})."]
    (args.out_dir / "evidence-index.md").write_text("\n".join(lines) + "\n")
    print(f"{len(rows)} findings -> {args.out_dir}")

    if args.fail_on and any(SEV_ORDER[r["severity"]] >= SEV_ORDER[args.fail_on] for r in rows):
        print(f"Gate failed: findings at or above '{args.fail_on}'", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
