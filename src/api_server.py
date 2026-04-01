from flask import Flask, request, jsonify
from flask_cors import CORS
from features import (
    extract_features,
    check_domain_age,
    check_ssl_certificate,
    check_virustotal
)
import joblib
import pandas as pd
import os

app = Flask(__name__)
CORS(app)

model = joblib.load("models/phishing_model.pkl")
@app.route('/')
def home():
    return {"status": "JARVIS backend running"}

@app.route('/scan', methods=['POST'])
def scan():
    return {"final_result": "SAFE WEBSITE", "risk_score": 10}

@app.route('/scan', methods=['POST'])
def scan():
    return {
        "final_result": "SAFE WEBSITE",
        "risk_score": 12,
        "ssl": "Valid",
        "domain_age": 120
    }


# ✅ ROOT ROUTE (IMPORTANT FIX)
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "running",
        "message": "JARVIS-C Backend Live"
    })


@app.route("/scan", methods=["POST"])
def scan():
    try:
        data = request.json
        url = data.get("url")

        if not url or not url.startswith(("http://", "https://")):
            return jsonify({"error": "Invalid URL"})

        features = extract_features(url)
        feature_df = pd.DataFrame([features])

        prediction = model.predict(feature_df)[0]
        probability = model.predict_proba(feature_df)[0][1] * 100

        ssl_status = check_ssl_certificate(url)
        domain_age = check_domain_age(url)
        vt_result = check_virustotal(url)

        # Risk scoring
        risk_score = 0

        if prediction == 1:
            risk_score += 50

        if vt_result["malicious"] > 0:
            risk_score += 40

        if vt_result["suspicious"] > 0:
            risk_score += 20

        if domain_age < 30:
            risk_score += 20

        if ssl_status == "Invalid SSL":
            risk_score += 10

        final_result = "PHISHING WEBSITE" if risk_score >= 50 else "SAFE WEBSITE"

        return jsonify({
            "final_result": final_result,
            "risk_score": risk_score,
            "probability": round(probability, 2),
            "ssl_status": ssl_status,
            "domain_age_days": domain_age,
            "vt_malicious": vt_result["malicious"],
            "vt_suspicious": vt_result["suspicious"]
        })

    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)