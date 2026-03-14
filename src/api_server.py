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

app = Flask(__name__)
CORS(app)

model = joblib.load("models/phishing_model.pkl")


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

        # ===============================
        # HYBRID RISK SCORING SYSTEM
        # ===============================

        risk_score = 0

        # ML contribution
        if prediction == 1:
            risk_score += 50

        # VirusTotal contribution
        if vt_result["malicious"] > 0:
            risk_score += 40

        if vt_result["suspicious"] > 0:
            risk_score += 20

        # Domain age contribution
        if domain_age < 30:
            risk_score += 20

        # SSL contribution
        if ssl_status == "Invalid SSL":
            risk_score += 10

        # Final decision
        if risk_score >= 50:
            final_result = "PHISHING WEBSITE"
        else:
            final_result = "SAFE WEBSITE"

        result = {
            "final_result": final_result,
            "risk_score": risk_score,
            "probability": round(probability, 2),
            "ssl_status": ssl_status,
            "domain_age_days": domain_age,
            "vt_malicious": vt_result["malicious"],
            "vt_suspicious": vt_result["suspicious"]
        }

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)})

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)