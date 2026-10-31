from flask import Flask, render_template, request, jsonify
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.datasets import make_classification
from sklearn.preprocessing import MinMaxScaler

app = Flask(__name__)

# Generate a synthetic, inbuilt training dataset (not real patient data).
# Features are represented on a 0-10 scale for this demonstration.
rng = np.random.RandomState(42)
n_samples = 2000
X = rng.uniform(0, 10, size=(n_samples, 5))
stress, sleep, anxiety, workload, social_support = X.T

# Synthetic label rule: higher stress/anxiety/workload and lower sleep/support
# increase the chance of belonging to class 1. Noise prevents a perfect rule.
risk_score = (0.30 * stress + 0.30 * anxiety + 0.20 * workload
              - 0.15 * sleep - 0.15 * social_support
              + rng.normal(0, 1.5, n_samples))
y = (risk_score > 2.5).astype(int)

feature_names = ["Stress", "Sleep", "Anxiety", "Workload", "Social support"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

model = RandomForestClassifier(
    n_estimators=180, max_depth=9, min_samples_split=4,
    class_weight="balanced", random_state=42
)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
metrics = {
    "accuracy": round(accuracy_score(y_test, y_pred) * 100, 2),
    "precision": round(precision_score(y_test, y_pred, zero_division=0) * 100, 2),
    "recall": round(recall_score(y_test, y_pred, zero_division=0) * 100, 2),
    "f1": round(f1_score(y_test, y_pred, zero_division=0) * 100, 2),
}
cm = confusion_matrix(y_test, y_pred).tolist()

@app.route("/")
def home():
    return render_template("index.html", metrics=metrics, confusion=cm)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        values = [float(data[key]) for key in
                  ["stress", "sleep", "anxiety", "workload", "support"]]
        if any(value < 0 or value > 10 for value in values):
            return jsonify({"error": "All values must be between 0 and 10."}), 400

        prediction = int(model.predict([values])[0])
        probability = float(model.predict_proba([values])[0][1] * 100)
        return jsonify({
            "prediction": prediction,
            "probability": round(probability, 1),
            "message": ("The model identified a higher-risk pattern in these inputs."
                        if prediction == 1 else
                        "The model did not identify a higher-risk pattern in these inputs.")
        })
    except (TypeError, ValueError, KeyError):
        return jsonify({"error": "Please provide valid numeric values."}), 400

if __name__ == "__main__":
    app.run(debug=True)
