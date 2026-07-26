import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Load dataset
data = pd.read_json("data.json")

# Handle missing values
data['floor'] = data['floor'].fillna(0)
data['last_inspection'] = data['last_inspection'].fillna("2025-01-01")

# Convert date → numeric feature
data['last_inspection'] = pd.to_datetime(data['last_inspection'], errors='coerce')
data['days_since_last'] = (pd.Timestamp.today() - data['last_inspection']).dt.days

# Fill missing computed values
data['days_since_last'] = data['days_since_last'].fillna(200)

# Features (IMPORTANT: no leakage)
X = data[['floor', 'days_since_last']]
y = data['outcome']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Evaluate
accuracy = model.score(X_test, y_test)
print("Model Accuracy:", round(accuracy, 2))

# Example prediction
sample = [[3, 150]]  # floor=3, 150 days since inspection
prediction = model.predict(sample)

print("Prediction for sample:", "High Risk" if prediction[0] == 1 else "Safe")