import streamlit as st
import pandas as pd

# ---------- IMPORT ENGINES ----------
from personal_readiness import personal_readiness
from decision_engine import final_decision
from ml_decision_engine import ml_final_decision   # 👈 ML version
from stock_score import stock_business_score
from valuation_engine import calculate_valuation_score
from explainability_engine import explain_decision
from hold_decision import hold_decision
from allocation_engine import allocation_engine
from sip_engine import sip_or_lumpsum
from confidence_engine import confidence_score_engine


# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Am I Ready to Buy?",
    layout="centered"
)

st.title("📈 Am I Ready to Buy This Stock?")
st.caption("Readiness > Prediction | Rules + AI")


# =========================================================
# 👤 USER PROFILE INPUT
# =========================================================
st.header("👤 About You")

monthly_income = st.number_input("Monthly Income (₹)", min_value=1000, step=1000)
monthly_expenses = st.number_input("Monthly Expenses (₹)", min_value=500, step=500)
emergency_months = st.number_input("Emergency Fund (months)", min_value=0, step=1)
existing_investments = st.number_input("Existing Investments (₹)", min_value=0, step=10000)
investment_horizon = st.number_input("Investment Horizon (years)", min_value=1, step=1)

annual_income = monthly_income * 12

user = {
    "monthly_income": monthly_income,
    "monthly_expenses": monthly_expenses,
    "emergency_months": emergency_months,
    "existing_investments": existing_investments,
    "investment_horizon": investment_horizon,
    "annual_income": annual_income
}


# =========================================================
# 🏢 STOCK SELECTION
# =========================================================
st.header("🏢 Select Company")

df = pd.read_csv("dummy_stock_data.csv")
company = st.selectbox("Choose a company", df["company"].unique())

row = df[df["company"] == company].iloc[0]

business_score = stock_business_score(row)
valuation_score = calculate_valuation_score(row)


# =========================================================
# 📊 FUNDAMENTALS
# =========================================================
st.subheader("📊 Stock Fundamentals")

st.metric("Business Quality Score", business_score)
st.metric("Valuation Score", valuation_score)


# =========================================================
# 🤖 AI TOGGLE
# =========================================================
st.header("🤖 Decision Engine")

use_ml = st.checkbox("Use AI Model (Experimental)")


# =========================================================
# 📦 EXISTING HOLDING
# =========================================================
st.header("📦 Existing Holding (Optional)")

is_holding = st.checkbox("I already own this stock")
years_held = 0.0

if is_holding:
    years_held = st.number_input(
        "How many years have you held this stock?",
        min_value=0.0,
        step=0.5
    )


# =========================================================
# 🔍 MAIN DECISION
# =========================================================
if st.button("🔍 Check Readiness"):

    # ---------- PERSONAL READINESS ----------
    readiness_score, risk_profile = personal_readiness(user)

    # ---------- BUY DECISION (RULE vs ML) ----------
    if use_ml:
        decision = ml_final_decision(
            business_score,
            valuation_score,
            readiness_score
        )
        st.caption("🧠 Decision powered by AI model")
    else:
        decision = final_decision(
            business_score,
            valuation_score,
            readiness_score
        )
        st.caption("📏 Decision powered by rule engine")

    explanations = explain_decision(
        company,
        business_score,
        valuation_score,
        readiness_score,
        decision
    )

    # ---------- DISPLAY ----------
    st.subheader("🧠 Your Readiness")
    st.metric("Personal Readiness Score", readiness_score)
    st.write(f"**Risk Profile:** {risk_profile}")

    st.subheader("✅ Buy Decision")
    if decision == "BUY":
        st.success("🟢 BUY")
    elif decision == "WAIT":
        st.warning("🟠 WAIT")
    else:
        st.error("🔴 AVOID")

    st.subheader("🧾 Why this decision?")
    for e in explanations:
        st.write("•", e)


    # =====================================================
    # 💰 PORTFOLIO ALLOCATION
    # =====================================================
    st.subheader("💰 Portfolio Allocation")

    allocation_amount, allocation_reasons = allocation_engine(
        user,
        business_score,
        valuation_score,
        decision
    )

    if allocation_amount == 0:
        st.warning("No investable surplus available.")
    else:
        st.metric("Recommended Amount (₹)", allocation_amount)
        for r in allocation_reasons:
            st.write("•", r)


    # =====================================================
    # 🔁 SIP vs LUMP SUM
    # =====================================================
    st.subheader("🔁 SIP or Lump Sum")

    sip_type, sip_amount, sip_reasons = sip_or_lumpsum(
        decision,
        valuation_score,
        readiness_score,
        risk_profile,
        allocation_amount,
        investment_horizon
    )

    if sip_type == "LUMP SUM":
        st.success(f"💥 Lump Sum: ₹{sip_amount}")
    elif sip_type == "HYBRID":
        st.warning(f"🔀 Hybrid: SIP ₹{sip_amount}/month")
    elif sip_type == "SIP":
        st.info(f"📆 SIP: ₹{sip_amount}/month")

    for r in sip_reasons:
        st.write("•", r)


    # =====================================================
    # 🔐 CONFIDENCE SCORE
    # =====================================================
    st.subheader("🔐 Recommendation Confidence")

    confidence_score, confidence_level, confidence_reasons = confidence_score_engine(
        business_score,
        valuation_score,
        readiness_score,
        decision,
        sip_type
    )

    st.metric("Confidence Score", confidence_score)

    for r in confidence_reasons:
        st.write("•", r)


    # =====================================================
    # 📌 HOLD / EXIT (IF HOLDING)
    # =====================================================
    if is_holding:
        st.subheader("📌 Hold / Exit")

        hold_action, reasons, exit_signals, holding_period = hold_decision(
            row,
            business_score,
            valuation_score,
            years_held
        )

        st.write(f"**Action:** {hold_action}")
        st.write("⏳ Holding Period:", holding_period)

        for r in reasons:
            st.write("•", r)

        for e in exit_signals:
            st.write("⚠️", e)
