import pandas as pd
from business_score import calculate_business_score
from valuation_score import calculate_valuation_score
from hold_decision import hold_decision

df = pd.read_csv("data/sample_stock_data.csv")

# Example: user holds TCS
row = df[df["ticker"] == "TCS"].iloc[0]

business = calculate_business_score(row)
valuation = calculate_valuation_score(row)

decision, reasons, exit_signals, period = hold_decision(row, business, valuation)

print("Decision:", decision)
print("\nWhy Hold:")
for r in reasons:
    print("-", r)

print("\nExit Signals to Watch:")
for e in exit_signals:
    print("-", e)

print("\nSuggested Holding Period:")
print(period)
