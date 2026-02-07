import pandas as pd
from valuation_score import calculate_valuation_score

df = pd.read_csv("data/sample_stock_data.csv")

for _, row in df.iterrows():
    val_score = calculate_valuation_score(row)
    print(row["ticker"], "→ Valuation Score:", val_score)
