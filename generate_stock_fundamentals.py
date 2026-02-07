import yfinance as yf
import pandas as pd

companies = {
    "TCS": "TCS.NS",
    "INFY": "INFY.NS",
    "HDFCBANK": "HDFCBANK.NS"
}

rows = []

for name, ticker in companies.items():
    stock = yf.Ticker(ticker)

    try:
        financials = stock.financials
        info = stock.info

        # -----------------------------
        # Revenue Growth (3Y)
        # -----------------------------
        revenue_growth_3y = (
            (financials.loc["Total Revenue"][0] - financials.loc["Total Revenue"][2])
            / financials.loc["Total Revenue"][2]
        ) * 100

        # -----------------------------
        # Profit Growth (3Y)
        # -----------------------------
        profit_growth_3y = (
            (financials.loc["Net Income"][0] - financials.loc["Net Income"][2])
            / financials.loc["Net Income"][2]
        ) * 100

        # -----------------------------
        # ROE & Debt
        # -----------------------------
        roe = info.get("returnOnEquity", 0) * 100
        debt_to_equity = info.get("debtToEquity", 0) / 100

        # -----------------------------
        # Margin Trend (proxy)
        # -----------------------------
        margins = info.get("profitMargins", 0)
        if margins > 0.15:
            margin_trend = "improving"
        elif margins > 0.08:
            margin_trend = "stable"
        else:
            margin_trend = "declining"

        # -----------------------------
        # Valuation Metrics
        # -----------------------------
        pe_current = info.get("trailingPE", None)
        pe_forward = info.get("forwardPE", None)

        # Approximate 5Y avg PE
        if pe_forward:
            pe_5y_avg = pe_forward
        else:
            pe_5y_avg = pe_current

        rows.append([
            name,
            round(revenue_growth_3y, 1),
            round(profit_growth_3y, 1),
            round(roe, 1),
            round(debt_to_equity, 2),
            margin_trend,
            round(pe_current, 1) if pe_current else None,
            round(pe_5y_avg, 1) if pe_5y_avg else None
        ])

    except Exception as e:
        print(f"Error for {name}: {e}")

df = pd.DataFrame(rows, columns=[
    "company",
    "revenue_growth_3y",
    "profit_growth_3y",
    "roe",
    "debt_to_equity",
    "margin_trend",
    "pe_current",
    "pe_5y_avg"
])

df.to_csv("stock_fundamentals.csv", index=False)
print("✅ stock_fundamentals.csv generated successfully!")
