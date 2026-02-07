def financial_stability(income, expenses):
    savings_rate = (income - expenses) / income
    if savings_rate >= 0.4:
        return 30
    elif savings_rate >= 0.25:
        return 24
    elif savings_rate >= 0.15:
        return 18
    elif savings_rate >= 0.05:
        return 10
    else:
        return 0


def emergency_fund_score(months):
    if months >= 12:
        return 25
    elif months >= 6:
        return 20
    elif months >= 3:
        return 12
    else:
        return 0


def horizon_score(years):
    if years >= 7:
        return 25
    elif years >= 5:
        return 20
    elif years >= 3:
        return 12
    else:
        return 5


def portfolio_score(existing, annual_income):
    ratio = existing / annual_income
    if ratio >= 3:
        return 20
    elif ratio >= 1.5:
        return 14
    elif ratio >= 0.5:
        return 8
    else:
        return 3


def personal_readiness(user):
    score = 0
    score += financial_stability(user["monthly_income"], user["monthly_expenses"])
    score += emergency_fund_score(user["emergency_months"])
    score += horizon_score(user["investment_horizon"])
    score += portfolio_score(user["existing_investments"], user["annual_income"])

    if score >= 75:
        profile = "HIGH"
    elif score >= 55:
        profile = "MEDIUM"
    else:
        profile = "LOW"

    return score, profile
