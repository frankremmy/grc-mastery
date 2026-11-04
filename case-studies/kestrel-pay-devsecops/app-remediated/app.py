"""
Kestrel Pay - refunds & card-lookup API, remediated version.

Fictional company, training code. Each fix references the finding ID from
docs/03-code-review-findings.md.
"""
import logging
import os
import sqlite3
from functools import wraps
from hmac import compare_digest

from argon2 import PasswordHasher
from flask import Flask, g, jsonify, request

app = Flask(__name__)
logging.basicConfig(filename="api.log", level=logging.INFO)

API_SECRET = os.environ["KP_API_SECRET"]          # KP-01: secret from env/vault, not source
DB_PATH = os.environ.get("KP_DB_PATH", "kestrel.db")
MAX_REFUND = float(os.environ.get("KP_MAX_REFUND", "500"))
ph = PasswordHasher()                               # KP-07: Argon2id


def db():
    return sqlite3.connect(DB_PATH)


def mask_pan(pan: str) -> str:
    """KP-03: show at most first six and last four digits (PCI DSS Req 3.4.1)."""
    return pan[:6] + "*" * (len(pan) - 10) + pan[-4:] if pan and len(pan) >= 13 else "****"


def require_api_key(view):
    """KP-04: one decorator, applied to every route, constant-time compare."""
    @wraps(view)
    def wrapper(*args, **kwargs):
        key = request.headers.get("X-API-Key", "")
        if not compare_digest(key, API_SECRET):
            return jsonify(error="unauthorised"), 401
        g.merchant = request.headers.get("X-Merchant-Id")
        return view(*args, **kwargs)
    return wrapper


@app.route("/api/v1/cards/lookup")
@require_api_key
def card_lookup():
    rows = db().execute(                                       # KP-02: parameterised
        "SELECT pan, expiry FROM cards WHERE merchant_id = ?", (g.merchant,)
    ).fetchall()
    return jsonify([{"pan": mask_pan(r[0]), "expiry": r[1]} for r in rows])


@app.route("/api/v1/refunds", methods=["POST"])
@require_api_key
def refund():
    body = request.get_json(silent=True) or {}
    try:
        amount = round(float(body.get("amount", 0)), 2)
    except (TypeError, ValueError):
        return jsonify(error="invalid amount"), 400
    if not 0 < amount <= MAX_REFUND:                           # KP-06: server-side limit
        return jsonify(error="amount outside permitted range"), 422
    # KP-05: log the event, never PAN or CVV. CVV is not accepted at all.
    logging.info("refund queued merchant=%s pan=%s amount=%s",
                 g.merchant, mask_pan(str(body.get("pan", ""))), amount)
    db().execute("INSERT INTO refunds (merchant_id, pan_token, amount) VALUES (?, ?, ?)",
                 (g.merchant, body.get("pan_token"), amount))
    return jsonify(status="queued", amount=amount)


@app.route("/api/v1/merchants/register", methods=["POST"])
@require_api_key
def register_merchant():
    body = request.get_json(silent=True) or {}
    if not body.get("name") or len(body.get("password", "")) < 14:
        return jsonify(error="name and a 14+ character password are required"), 400
    db().execute("INSERT INTO merchants (name, pw) VALUES (?, ?)",
                 (body["name"], ph.hash(body["password"])))
    return jsonify(status="created")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)                       # KP-08: no debug, loopback
