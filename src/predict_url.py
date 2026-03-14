import joblib
import pandas as pd
import os
from features import extract_features

# Load model
MODEL_PATH = os.path.join("models", "phishing_model.pkl")
model = joblib.load(MODEL_PATH)

def predict_url(url):
    features = extract_features(url)

    # Convert directly to DataFrame
    df_input = pd.DataFrame([features])

    pred = model.predict(df_input)[0]
    proba = model.predict_proba(df_input)[0]

    phishing_prob = proba[1] * 100
    safe_prob = proba[0] * 100

    return int(pred), phishing_prob, safe_prob


if __name__ == "__main__":
    url = input("Enter a URL to check: ")

    result, phishing_prob, safe_prob = predict_url(url)

    print("\nResult:")
    if result == 1:
        print("⚠️ PHISHING")
    else:
        print("✅ LEGITIMATE")

    print(f"Phishing Probability: {phishing_prob:.2f}%")
    print(f"Safe Probability: {safe_prob:.2f}%")

import joblib
import pandas as pd
import os
from features import extract_features

# Load model
MODEL_PATH = os.path.join("models", "phishing_model.pkl")
model = joblib.load(MODEL_PATH)

def predict_url(url):
    features = extract_features(url)

    # Convert directly to DataFrame
    df_input = pd.DataFrame([features])

    pred = model.predict(df_input)[0]
    proba = model.predict_proba(df_input)[0]

    phishing_prob = proba[1] * 100
    safe_prob = proba[0] * 100

    return int(pred), phishing_prob, safe_prob


if __name__ == "__main__":
    url = input("Enter a URL to check: ")

    result, phishing_prob, safe_prob = predict_url(url)

    print("\nResult:")
    if result == 1:
        print("⚠️ PHISHING")
    else:
        print("✅ LEGITIMATE")

    print(f"Phishing Probability: {phishing_prob:.2f}%")
    print(f"Safe Probability: {safe_prob:.2f}%")
