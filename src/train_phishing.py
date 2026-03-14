import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from features import extract_features

# ==============================
# Load URL Dataset
# ==============================

DATASET_PATH = os.path.join("data", "url_dataset.csv")
df = pd.read_csv(DATASET_PATH)

print("Dataset Loaded Successfully ✅")
print(df.head())

X = []
y = []

print("Extracting Features...")

for index, row in df.iterrows():
    url = row["url"]
    label = row["label"]

    features = extract_features(url)
    X.append(features)
    y.append(label)

X = pd.DataFrame(X)
y = pd.Series(y)

print("Feature Extraction Complete ✅")
print("Feature Shape:", X.shape)

# ==============================
# Train/Test Split
# ==============================

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# ==============================
# Train Model
# ==============================

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)

print("Model Trained Successfully ✅")
print("Model Accuracy:", accuracy)

# ==============================
# Save Model
# ==============================

MODEL_PATH = os.path.join("models", "phishing_model.pkl")
joblib.dump(model, MODEL_PATH)

print("Model Saved Successfully ✅")
import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from features import extract_features

# ==============================
# Load URL Dataset
# ==============================

DATASET_PATH = os.path.join("data", "url_dataset.csv")
df = pd.read_csv(DATASET_PATH)

print("Dataset Loaded Successfully ✅")
print(df.head())

X = []
y = []

print("Extracting Features...")

for index, row in df.iterrows():
    url = row["url"]
    label = row["label"]

    features = extract_features(url)
    X.append(features)
    y.append(label)

X = pd.DataFrame(X)
y = pd.Series(y)

print("Feature Extraction Complete ✅")
print("Feature Shape:", X.shape)

# ==============================
# Train/Test Split
# ==============================

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# ==============================
# Train Model
# ==============================

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)

print("Model Trained Successfully ✅")
print("Model Accuracy:", accuracy)

# ==============================
# Save Model
# ==============================

MODEL_PATH = os.path.join("models", "phishing_model.pkl")
joblib.dump(model, MODEL_PATH)

print("Model Saved Successfully ✅")