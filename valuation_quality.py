def pe_vs_growth_score(pe, growth):
    if growth <= 0:
        return 0

    peg = pe / growth

    if peg <= 1:
        return 40
    elif peg <= 1.5:
        return 30
    elif peg <= 2:
        return 20
    elif peg <= 3:
        return 10
    else:
        return 0


def roce_score(roce):
    if roce >= 25:
        return 35
    elif roce >= 18:
        return 25
    elif roce >= 12:
        return 15
    elif roce >= 8:
        return 8
    else:
        return 0


def pe_sanity_score(pe):
    if pe <= 15:
        return 25
    elif pe <= 25:
        return 18
    elif pe <= 40:
        return 8
    else:
        return 0


def quality_valuation_score(pe, growth, roce):
    score = 0
    score += pe_vs_growth_score(pe, growth)
    score += roce_score(roce)
    score += pe_sanity_score(pe)
    return score
