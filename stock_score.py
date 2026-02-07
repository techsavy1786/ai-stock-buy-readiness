def stock_business_score(row):
    score = 0

    # Revenue Growth (25)
    if row["revenue_growth_3y"] >= 15:
        score += 25
    elif row["revenue_growth_3y"] >= 8:
        score += 18
    elif row["revenue_growth_3y"] >= 4:
        score += 10

    # Profit Growth (25)
    if row["profit_growth_3y"] >= 15:
        score += 25
    elif row["profit_growth_3y"] >= 8:
        score += 18
    elif row["profit_growth_3y"] >= 4:
        score += 10

    # ROE (20)
    if row["roe"] >= 20:
        score += 20
    elif row["roe"] >= 15:
        score += 14
    elif row["roe"] >= 10:
        score += 8

    # Debt to Equity (15)
    if row["debt_to_equity"] <= 0.5:
        score += 15
    elif row["debt_to_equity"] <= 1:
        score += 8

    # Margin Trend (15)
    if row["margin_trend"] == "improving":
        score += 15
    elif row["margin_trend"] == "stable":
        score += 8

    return score
