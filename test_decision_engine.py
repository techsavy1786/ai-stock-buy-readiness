import pandas as pd
from business_score import calculate_business_score
from valuation_score import calculate_valuation_score
from decision_engine import final_decision

# Dummy personal readiness (for now)
PERSONAL_READINESS_SCORE = 70

df = pd.read_csv("data/sample_stock_data.csv")

print("FINAL DECISIONS:\n")

for _, row in df.iterrows():
    business = calculate_business_score(row)
    valuation = calculate_valuation_score(row)
    decision, reason = final_decision(business, valuation, PERSONAL_READINESS_SCORE)

    print(row["ticker"])
    print(" Business Score:", business)
    print(" Valuation Score:", valuation)
    print(" Decision:", decision)
    print(" Reason:", reason)
    print("-" * 40)
