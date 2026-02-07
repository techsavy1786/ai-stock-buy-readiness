import pandas as pd
from business_score import calculate_business_score

df = pd.read_csv("data/sample_stock_data.csv")

for _, row in df.iterrows():
    score = calculate_business_score(row)
    print(row["ticker"], "→ Business Score:", score)
