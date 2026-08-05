import streamlit as st
from datetime import datetime
import random

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="AI Fraud Investigator",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 AI Fraud Investigation Assistant")
st.caption("Generate an executive fraud investigation report.")

st.divider()

# =====================================================
# USER INPUT
# =====================================================

col1, col2 = st.columns(2)

with col1:

    transaction_type = st.selectbox(
        "Transaction Type",
        [
            "CASH_OUT",
            "TRANSFER",
            "PAYMENT",
            "DEBIT"
        ]
    )

    amount = st.number_input(
        "Transaction Amount",
        min_value=0.0,
        value=500000.0
    )

with col2:

    probability = st.slider(
        "Fraud Probability (%)",
        0,
        100,
        95
    )

    risk = st.selectbox(
        "Risk Level",
        [
            "LOW",
            "MEDIUM",
            "HIGH"
        ]
    )

st.divider()

# =====================================================
# GENERATE REPORT
# =====================================================

if st.button("🧠 Generate Investigation Report", use_container_width=True):

    report_id = random.randint(100000, 999999)

    st.success("Investigation Report Generated Successfully")

    st.divider()

    st.subheader("📄 Executive Fraud Report")

    st.markdown(f"""
### Report Information

**Report ID:** FR-{report_id}

**Generated On:** {datetime.now().strftime('%d %B %Y %H:%M')}

**Transaction Type:** {transaction_type}

**Transaction Amount:** ₹ {amount:,.2f}

**Fraud Probability:** {probability}%

**Risk Level:** {risk}
""")

    st.divider()

    # =====================================================
    # RISK ANALYSIS
    # =====================================================

    if probability >= 80:

        st.error("🚨 High Fraud Risk")

        reasons = [
            "Large transaction amount.",
            "High probability score from the ML model.",
            "Transaction pattern resembles historical fraud.",
            "High sender balance reduction.",
            "Abnormal balance behaviour detected."
        ]

        recommendations = [
            "Temporarily hold the transaction.",
            "Perform customer identity verification.",
            "Escalate to Fraud Investigation Team.",
            "Require manual approval before processing.",
            "Continue monitoring the account."
        ]

    elif probability >= 40:

        st.warning("🟠 Medium Fraud Risk")

        reasons = [
            "Moderately suspicious transaction behaviour.",
            "Some fraud indicators are present.",
            "Transaction amount is higher than normal."
        ]

        recommendations = [
            "Request additional authentication.",
            "Monitor subsequent transactions.",
            "Flag account for observation."
        ]

    else:

        st.success("🟢 Low Fraud Risk")

        reasons = [
            "Transaction appears normal.",
            "No major fraud indicators detected.",
            "Customer behaviour is consistent."
        ]

        recommendations = [
            "Approve the transaction.",
            "Continue routine monitoring."
        ]

    st.subheader("🔍 Key Findings")

    for r in reasons:
        st.write("•", r)

    st.divider()

    st.subheader("📋 Recommended Actions")

    for r in recommendations:
        st.write("✅", r)

    st.divider()

    st.subheader("💼 Business Impact")

    if probability >= 80:

        st.info("""
Potential impact if ignored:

• Financial loss

• Regulatory compliance risk

• Customer trust issues

• Reputation damage

• Increased fraud exposure
""")

    elif probability >= 40:

        st.info("""
Potential impact:

• Moderate financial risk

• Increased monitoring required

• Customer verification recommended
""")

    else:

        st.info("""
Expected impact:

• Minimal business risk

• Standard transaction processing
""")

    st.divider()

    st.subheader("🤖 AI Summary")

    summary = f"""
The transaction has been classified as **{risk} RISK**
with an estimated fraud probability of **{probability}%**.

Based on the transaction characteristics,
the recommended action is to follow the investigation
steps listed above before processing the payment.
"""

    st.write(summary)

    st.divider()

    report = f"""
AI FRAUD INVESTIGATION REPORT

Report ID : FR-{report_id}

Transaction Type : {transaction_type}

Amount : {amount}

Fraud Probability : {probability}%

Risk Level : {risk}

Generated : {datetime.now()}
"""

    st.download_button(
        "📥 Download Investigation Report",
        report,
        file_name=f"Fraud_Report_{report_id}.txt"
    )