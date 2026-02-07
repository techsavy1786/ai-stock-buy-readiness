def explain_decision(
    company,
    business_score,
    valuation_score,
    readiness_score,
    decision
):
    explanations = []

    # -----------------------------
    # Business Explanation
    # -----------------------------
    if business_score >= 75:
        explanations.append(
            f"🏢 **{company}** has strong business fundamentals with healthy growth, returns, and balance sheet."
        )
    elif business_score >= 55:
        explanations.append(
            f"🏢 **{company}** has stable fundamentals but lacks strong competitive advantages."
        )
    else:
        explanations.append(
            f"🏢 **{company}** shows weak or risky business fundamentals."
        )

    # -----------------------------
    # Valuation Explanation
    # -----------------------------
    if valuation_score >= 75:
        explanations.append(
            "💰 The stock appears **undervalued** compared to its historical pricing and growth."
        )
    elif valuation_score >= 55:
        explanations.append(
            "💰 The stock is **fairly valued** at current levels."
        )
    else:
        explanations.append(
            "💰 The stock looks **expensive**, offering limited margin of safety."
        )

    # -----------------------------
    # Personal Readiness Explanation
    # -----------------------------
    if readiness_score >= 70:
        explanations.append(
            "👤 You are financially ready with sufficient emergency buffer and long-term horizon."
        )
    elif readiness_score >= 50:
        explanations.append(
            "👤 Your finances are stable, but some aspects (cash buffer / risk capacity) could improve."
        )
    else:
        explanations.append(
            "👤 You are **not financially ready** to take additional investment risk right now."
        )

    # -----------------------------
    # Final Guidance
    # -----------------------------
    if decision == "BUY":
        explanations.append(
            "✅ **Action:** You may consider investing gradually (SIP or phased buying) to manage risk."
        )
    elif decision == "WAIT":
        explanations.append(
            "⏳ **Action:** Wait for either a better price or improvement in personal readiness."
        )
    else:
        explanations.append(
            "🚫 **Action:** Avoid this stock for now and focus on strengthening fundamentals or finances."
        )

    return explanations
