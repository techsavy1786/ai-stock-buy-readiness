import random
import pandas as pd
from decision_engine import final_decision

rows = []

for _ in range(1000):
    business = random.randint(30, 90)
    valuation = random.randint(30, 90)
    readiness = random.randint(30, 90)

    decision = final_decision(business, valuation, readiness)

    rows.append([
        business,
        valuation,
        readiness,
        decision
    ])

df = pd.DataFrame(rows, columns=[
    "business_score",
    "valuation_score",
    "readiness_score",
    "decision"
])

df.to_csv("decision_training_data.csv", index=False)
print("Training data generated!")
