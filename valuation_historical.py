def calculate_valuation_score(row):
    score = 0

    pe_current = row["pe_current"]
    pe_avg = row["pe_5y_avg"]
    growth = row["profit_growth_3y"]
    margin = row["margin_trend"]

    # -----------------------------
    # 1. PE vs Historical Average (50)
    # -----------------------------
    if pe_current == "NA" or pe_avg == "NA":
        pe_score = 20  # uncertain valuation
    else:
        pe_current = float(pe_current)
        pe_avg = float(pe_avg)

        ratio = pe_current / pe_avg

        if ratio < 0.8:
            pe_score = 50   # undervalued
        elif ratio < 1.1:
            pe_score = 35   # fairly valued
        else:
            pe_score = 15   # expensive

    score += pe_score

    # -----------------------------
    # 2. Growth Justification (30)
    # -----------------------------
    if growth > 15:
        score += 30
    elif growth > 10:
        score += 20
    elif growth > 5:
        score += 10
    else:
        score += 5

    # -----------------------------
    # 3. Margin Trend (20)
    # -----------------------------
    if margin == "improving":
        score += 20
    elif margin == "stable":
        score += 10
    else:
        score += 5

    return score
