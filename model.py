import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
data = pd.read_json("data.json")

# Handle missing values
data['floor'] = data['floor'].fillna(0)
data['last_inspection'] = data['last_inspection'].fillna("2025-01-01")

# Convert date → numeric
data['last_inspection'] = pd.to_datetime(data['last_inspection'], errors='coerce')
data['days_since_last'] = (pd.Timestamp.today() - data['last_inspection']).dt.days

# Fill missing computed values
data['days_since_last'] = data['days_since_last'].fillna(200)

# Features (NO data leakage)
X = data[['floor', 'days_since_last']]
y = data['outcome']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)

# 🔥 CHANGE 2: Confidence threshold
threshold = 0.95  # high threshold to force "Not Sure"

final_predictions = []

for i in range(len(y_pred)):
    confidence = max(y_prob[i])

    if confidence < threshold:
        final_predictions.append("Not Sure")
    else:
        final_predictions.append(y_pred[i])

# 🔥 PRINT RESULTS WITH CONFIDENCE
print("\nPredictions with Confidence:\n")

for i in range(len(final_predictions)):
    print(
        f"Actual: {y_test.iloc[i]} | "
        f"Predicted: {final_predictions[i]} | "
        f"Confidence: {max(y_prob[i]):.2f}"
    )

# 🔥 CHANGE 1: Accuracy + Classification Report
print("\nModel Accuracy:", round(model.score(X_test, y_test), 2))
print("Accuracy:", accuracy_score(y_test, y_pred))

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# 🔥 FORCE BORDERLINE CASE (IMPORTANT FOR VIDEO)
print("\n--- Borderline Case Test ---")

sample = [[2, 90]]  # moderate case
prob = model.predict_proba(sample)
confidence = max(prob[0])

if confidence < threshold:
    print("Prediction: Not Sure | Confidence:", round(confidence, 2))
else:
    pred = model.predict(sample)
    print("Prediction:", pred[0], "| Confidence:", round(confidence, 2))
