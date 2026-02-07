def sip_or_lumpsum(
    decision,
    valuation_score,
    readiness_score,
    risk_profile,
    allocation_amount,
    investment_horizon
):
    reasons = []

    if allocation_amount == 0:
        return "NO INVEST", 0, ["No investable surplus available"]

    # WAIT → SIP only
    if decision == "WAIT":
        reasons.append("Market timing unclear — spreading risk via SIP")
        sip_amount = allocation_amount / 12
        return "SIP", round(sip_amount), reasons

    # Low readiness → SIP
    if readiness_score < 50:
        reasons.append("Low personal readiness — SIP reduces risk")
        sip_amount = allocation_amount / 12
        return "SIP", round(sip_amount), reasons

    # Valuation logic
    if valuation_score >= 75 and readiness_score >= 70:
        reasons.append("Attractive valuation and strong readiness")
        return "LUMP SUM", allocation_amount, reasons

    if 55 <= valuation_score < 75:
        reasons.append("Moderate valuation — split investment")
        sip_amount = allocation_amount / 12
        return "HYBRID", round(sip_amount), reasons

    # Default
    reasons.append("Valuation not cheap — SIP preferred")
    sip_amount = allocation_amount / 12
    return "SIP", round(sip_amount), reasons
