def allocation_engine(user, business_score, valuation_score, decision):
    reasons = []

    # Annual savings
    annual_savings = (user["monthly_income"] - user["monthly_expenses"]) * 12

    # Risk-based base allocation
    if annual_savings <= 0:
        return 0, "No surplus available for investment."

    if user["investment_horizon"] >= 5:
        base_pct = 0.4
    else:
        base_pct = 0.3

    investable_amount = annual_savings * base_pct
    reasons.append(f"Base investable amount is ₹{round(investable_amount)}")

    # Stock confidence multiplier
    weight = 1.0

    if business_score >= 80:
        weight += 0.15
        reasons.append("Strong business fundamentals")

    if valuation_score >= 70:
        weight += 0.15
        reasons.append("Attractive valuation")

    if decision == "WAIT":
        weight -= 0.20
        reasons.append("Timing not ideal — reduced exposure")

    final_amount = investable_amount * weight

    # Cap allocation
    max_cap = investable_amount * 0.25
    final_amount = min(final_amount, max_cap)

    return round(final_amount), reasons
