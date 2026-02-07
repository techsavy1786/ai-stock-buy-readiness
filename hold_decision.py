def hold_decision(
    row,
    business_score,
    valuation_score,
    years_held,
):
    reasons = []
    exit_signals = []

    # ---------------- Business strength ----------------
    if business_score >= 75:
        reasons.append("Business fundamentals are strong with healthy growth and profitability.")
    elif business_score >= 60:
        reasons.append("Business fundamentals are stable but need monitoring.")
    else:
        exit_signals.append("Business fundamentals have weakened.")

    # ---------------- Growth ----------------
    if row["revenue_growth_3y"] > 10 and row["profit_growth_3y"] > 10:
        reasons.append("Revenue and profit are growing consistently.")
    elif row["profit_growth_3y"] < 5:
        exit_signals.append("Profit growth has slowed.")

    # ---------------- Debt ----------------
    if row["debt_to_equity"] > 1:
        exit_signals.append("Debt levels are rising and risky.")
    else:
        reasons.append("Debt levels are under control.")

    # ---------------- Margins ----------------
    if row["margin_trend"] == "declining":
        exit_signals.append("Margins are declining.")
    else:
        reasons.append("Margins are stable or improving.")

    # ---------------- Valuation ----------------
    if valuation_score >= 70:
        reasons.append("Valuation is reasonable compared to fundamentals.")
    elif valuation_score < 50:
        exit_signals.append("Valuation looks stretched.")

    # ---------------- FINAL DECISION LOGIC ----------------

    # Strong compounder
    if business_score >= 75 and valuation_score >= 70 and len(exit_signals) <= 1:
        decision = "ADD MORE"
        holding_period = "Hold for 3–5+ years while fundamentals remain strong."

    # Good but not cheap
    elif business_score >= 70 and valuation_score >= 50:
        decision = "HOLD"
        holding_period = "Continue holding; review annually."

    # Warning zone
    elif len(exit_signals) >= 2 and years_held < 3:
        decision = "REDUCE"
        holding_period = "Reduce exposure and reassess in next 2 quarters."

    # Exit zone
    elif len(exit_signals) >= 2 and years_held >= 3:
        decision = "EXIT"
        holding_period = "Exit and redeploy capital into stronger opportunities."

    else:
        decision = "HOLD"
        holding_period = "No strong action required. Monitor fundamentals quarterly."

    return decision, reasons, exit_signals, holding_period
