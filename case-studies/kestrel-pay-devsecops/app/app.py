"""
Kestrel Pay - refunds & card-lookup API (DELIBERATELY VULNERABLE TRAINING CODE).

Fictional company. Seeded with realistic flaws for a secure-code-review and
DevSecOps exercise. Do not deploy. All card numbers are PCI test PANs.
"""
import hashlib
import logging
import sqlite3

from flask import Flask, jsonify, request

app = Flask(__name__)
logging.basicConfig(filename="api.log", level=logging.INFO)

# KP-01: hardcoded credential committed to source control
API_SECRET = "kp_live_9f8a7c6b5d4e3f2a1b0c9d8e7f6a5b4c"
DB_PATH = "kestrel.db"


def db():
    return sqlite3.connect(DB_PATH)


def check_key(req):
    return req.headers.get("X-API-Key") == API_SECRET


@app.route("/api/v1/cards/lookup")
def card_lookup():
    if not check_key(request):
        return jsonify(error="unauthorised"), 401
    merchant = request.args.get("merchant_id", "")
    # KP-02: SQL injection - user input concatenated into the query
    rows = db().execute(
        "SELECT pan, expiry, cardholder FROM cards WHERE merchant_id = '" + merchant + "'"
    ).fetchall()
    # KP-03: full PAN returned without masking
    return jsonify([{"pan": r[0], "expiry": r[1], "name": r[2]} for r in rows])


@app.route("/api/v1/refunds", methods=["POST"])
def refund():
    # KP-04: no authentication or authorisation on a money-moving endpoint
    body = request.get_json(force=True)
    # KP-05: full PAN and CVV written to application log
    logging.info("refund request pan=%s cvv=%s amount=%s",
                 body.get("pan"), body.get("cvv"), body.get("amount"))
    amount = float(body.get("amount", 0))
    # KP-06: no server-side limit or validation on refund amount
    db().execute("INSERT INTO refunds (pan, amount) VALUES (?, ?)", (body.get("pan"), amount))
    return jsonify(status="queued", amount=amount)


@app.route("/api/v1/merchants/register", methods=["POST"])
def register_merchant():
    body = request.get_json(force=True)
    # KP-07: weak, unsalted hash for merchant passwords
    pw_hash = hashlib.md5(body["password"].encode()).hexdigest()
    db().execute("INSERT INTO merchants (name, pw) VALUES (?, ?)", (body["name"], pw_hash))
    return jsonify(status="created")


if __name__ == "__main__":
    # KP-08: debug mode exposes the Werkzeug console
    app.run(host="0.0.0.0", port=5000, debug=True)
