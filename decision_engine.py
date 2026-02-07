def final_decision(stock_score, valuation_score, readiness_score):
    combined = 0.5 * stock_score + 0.3 * valuation_score + 0.2 * readiness_score

    if combined >= 75:
        return "BUY"
    elif combined >= 55:
        return "WAIT"
    else:
        return "AVOID"
