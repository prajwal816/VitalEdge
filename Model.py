import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

# Sample Dataset: Symptoms → Disease Mapping
data = {
    "fever": [1, 1, 0, 0, 1, 1],
    "cough": [1, 0, 1, 0, 0, 1],
    "fatigue": [1, 1, 1, 0, 1, 1],
    "body_pain": [0, 1, 1, 0, 1, 0],
    "sore_throat": [0, 1, 1, 0, 0, 1],
    "runny_nose": [1, 0, 0, 0, 1, 1],
    "disease": ["Flu", "Cold", "COVID-19", "Healthy", "Dengue", "Bronchitis"]
}

df = pd.DataFrame(data)

# Features and Labels
X = df.drop(columns=["disease"])  # Symptoms
y = df["disease"]  # Target (Disease)

# Train the Decision Tree model
model = DecisionTreeClassifier()
model.fit(X, y)

# Save the trained model
joblib.dump(model, "healthcare_model.pkl")

print("✅ Model training complete and saved as 'healthcare_model.pkl'")
