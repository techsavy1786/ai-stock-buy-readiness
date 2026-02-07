def calculate_business_score(row):
    score = 0

    # Growth
    if row["revenue_growth_3y"] > 15:
        score += 40
    elif row["revenue_growth_3y"] > 10:
        score += 30
    elif row["revenue_growth_3y"] > 5:
        score += 20

    # Profitability
    if row["roe"] > 15:
        score += 30
    elif row["roe"] > 10:
        score += 20

    # Debt
    if row["debt_to_equity"] < 0.5:
        score += 30
    elif row["debt_to_equity"] < 1:
        score += 15

    return score
