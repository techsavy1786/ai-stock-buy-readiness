def confidence_score_engine(
    business_score,
    valuation_score,
    readiness_score,
    decision,
    sip_type
):
    score = 50
    reasons = []

    # Business consistency
    if business_score >= 75:
        score += 15
        reasons.append("Strong business fundamentals")

    if valuation_score >= 70:
        score += 15
        reasons.append("Valuation supports decision")

    if readiness_score >= 70:
        score += 10
        reasons.append("Investor readiness is strong")

    # Decision clarity
    if decision == "BUY":
        score += 5
    elif decision == "WAIT":
        score -= 5
        reasons.append("Timing uncertainty reduces confidence")

    # SIP logic alignment
    if sip_type in ["SIP", "HYBRID"]:
        score += 5
        reasons.append("Risk-managed investment approach")

    score = min(max(score, 0), 100)

    if score >= 75:
        level = "HIGH"
    elif score >= 55:
        level = "MEDIUM"
    else:
        level = "LOW"

    return score, level, reasons
