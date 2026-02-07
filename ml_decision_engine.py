import joblib

model = joblib.load("decision_model.pkl")
encoder = joblib.load("decision_encoder.pkl")

def ml_final_decision(business, valuation, readiness):
    pred = model.predict([[business, valuation, readiness]])
    return encoder.inverse_transform(pred)[0]
