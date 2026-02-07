from valuation_historical import calculate_valuation_score
from valuation_quality import quality_valuation_score


def final_valuation_score(row):
    """
    Final valuation = Historical + Quality-Growth
    """

    # Historical valuation (0–100)
    historical_score = calculate_valuation_score(row)

    # Quality valuation (0–100)
    quality_score = quality_valuation_score(
        pe=row["pe_current"],
        growth=row["profit_growth_3y"],
        roce=row["roce"]
    )

    # Weighted merge
    final_score = int(0.6 * historical_score + 0.4 * quality_score)

    return final_score, historical_score, quality_score
