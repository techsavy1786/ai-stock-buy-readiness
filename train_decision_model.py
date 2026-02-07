import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
import joblib

df = pd.read_csv("decision_training_data.csv")

X = df[["business_score", "valuation_score", "readiness_score"]]
y = df["decision"]

encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)
print("Model accuracy:", accuracy)

joblib.dump(model, "decision_model.pkl")
joblib.dump(encoder, "decision_encoder.pkl")
