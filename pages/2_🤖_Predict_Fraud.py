import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go

# ===========================================================
# PAGE CONFIG
# ===========================================================

st.set_page_config(
    page_title="Predict Fraud",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Fraud Detection System")
st.caption("Predict whether a financial transaction is fraudulent.")

# ===========================================================
# LOAD MODEL
# ===========================================================

@st.cache_resource
def load_model():
    return joblib.load("models/fraud_detection_model.pkl")

model = load_model()

# ===========================================================
# INPUT FORM
# ===========================================================

left, right = st.columns(2)

with left:

    step = st.number_input(
        "Step",
        min_value=1,
        value=1
    )

    transaction_type = st.selectbox(
        "Transaction Type",
        [
            "CASH_OUT",
            "DEBIT",
            "PAYMENT",
            "TRANSFER"
        ]
    )

    amount = st.number_input(
        "Transaction Amount",
        min_value=0.0,
        value=1000.0
    )

    oldbalanceOrg = st.number_input(
        "Sender Balance Before",
        min_value=0.0,
        value=10000.0
    )

    newbalanceOrig = st.number_input(
        "Sender Balance After",
        min_value=0.0,
        value=9000.0
    )

with right:

    oldbalanceDest = st.number_input(
        "Receiver Balance Before",
        min_value=0.0,
        value=0.0
    )

    newbalanceDest = st.number_input(
        "Receiver Balance After",
        min_value=0.0,
        value=1000.0
    )

    receiver = st.selectbox(
        "Receiver Type",
        [
            "Customer",
            "Merchant"
        ]
    )

st.write("")

# ===========================================================
# PREDICT BUTTON
# ===========================================================

if st.button("🚀 Predict Transaction", use_container_width=True):

    sender_balance_change = oldbalanceOrg - newbalanceOrig

    receiver_balance_change = newbalanceDest - oldbalanceDest

    amount_to_balance_ratio = (
        amount / oldbalanceOrg
        if oldbalanceOrg != 0 else 0
    )

    isMerchant = 1 if receiver == "Merchant" else 0

    large_transaction = 1 if amount > 200000 else 0

    input_df = pd.DataFrame({

        "step":[step],

        "amount":[amount],

        "oldbalanceOrg":[oldbalanceOrg],

        "newbalanceOrig":[newbalanceOrig],

        "oldbalanceDest":[oldbalanceDest],

        "newbalanceDest":[newbalanceDest],

        "sender_balance_change":[sender_balance_change],

        "receiver_balance_change":[receiver_balance_change],

        "amount_to_balance_ratio":[amount_to_balance_ratio],

        "isMerchant":[isMerchant],

        "large_transaction":[large_transaction],

        "type_CASH_OUT":[1 if transaction_type=="CASH_OUT" else 0],

        "type_DEBIT":[1 if transaction_type=="DEBIT" else 0],

        "type_PAYMENT":[1 if transaction_type=="PAYMENT" else 0],

        "type_TRANSFER":[1 if transaction_type=="TRANSFER" else 0]

    })

    prediction = model.predict(input_df)[0]

    probability = model.predict_proba(input_df)[0][1]

    st.divider()

    c1, c2 = st.columns([1, 2])

    # ===========================================================
    # GAUGE
    # ===========================================================

    with c1:

        gauge = go.Figure(go.Indicator(

            mode="gauge+number",

            value=probability*100,

            title={"text":"Fraud Probability"},

            gauge={
                "axis":{"range":[0,100]},
                "bar":{"color":"red"},
                "steps":[
                    {"range":[0,40],"color":"green"},
                    {"range":[40,70],"color":"orange"},
                    {"range":[70,100],"color":"red"}
                ]
            }

        ))

        gauge.update_layout(height=350)

        st.plotly_chart(
            gauge,
            use_container_width=True
        )

    # ===========================================================
    # RESULT
    # ===========================================================

    with c2:

        if prediction == 1:

            st.error("🚨 FRAUD DETECTED")

        else:

            st.success("✅ LEGITIMATE TRANSACTION")

        st.metric(
            "Fraud Probability",
            f"{probability*100:.2f}%"
        )

        st.progress(float(probability))

        if probability > 0.80:

            risk = "🔴 HIGH"

        elif probability > 0.40:

            risk = "🟠 MEDIUM"

        else:

            risk = "🟢 LOW"

        st.info(f"### Risk Level : {risk}")

        st.divider()

        st.subheader("📄 AI Investigation Report")

        if prediction == 1:

            st.markdown(f"""

**Summary**

The transaction has been classified as **Fraudulent**.

**Confidence**

{probability*100:.2f}%

### Possible Reasons

• Large transaction amount

• Significant sender balance reduction

• High amount-to-balance ratio

• Suspicious transaction behaviour

### Recommended Action

✅ Hold transaction

✅ Verify customer

✅ Manual approval

✅ Notify Fraud Team

""")

        else:

            st.markdown(f"""

**Summary**

The transaction appears to be **Legitimate**.

**Confidence**

{(1-probability)*100:.2f}%

### Recommendation

Approve transaction.

Continue routine monitoring.

""")

    st.divider()

    with st.expander("📊 Engineered Features Used"):

        st.dataframe(
            input_df,
            use_container_width=True,
            hide_index=True
        )

    report = f"""

AI Fraud Detection Report

Prediction : {"Fraud" if prediction==1 else "Legitimate"}

Fraud Probability : {probability*100:.2f}%

Risk Level : {risk}

Transaction Amount : {amount}

Transaction Type : {transaction_type}

Generated using AI Fraud Detection System

"""

    st.download_button(
        "📥 Download Report",
        report,
        file_name="Fraud_Report.txt"
    )