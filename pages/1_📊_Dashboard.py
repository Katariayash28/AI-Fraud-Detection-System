import streamlit as st
import pandas as pd
import plotly.express as px

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Executive Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Executive Dashboard")
st.caption("Real-Time Fraud Monitoring Dashboard")

# =====================================================
# LOAD DATA
# =====================================================

@st.cache_data
def load_data():

    df = pd.read_csv("data/Fraud_Analysis_Dataset.csv")

    feature = pd.read_csv("outputs/feature_importance.csv")

    comparison = pd.read_csv("outputs/model_comparison.csv")

    business = pd.read_csv("outputs/business_summary.csv")

    return df, feature, comparison, business


df, feature, comparison, business = load_data()

# =====================================================
# KPI CARDS
# =====================================================

total_transactions = len(df)

fraud_transactions = int(df["isFraud"].sum())

legitimate_transactions = total_transactions - fraud_transactions

fraud_rate = (fraud_transactions / total_transactions) * 100

best_model = comparison.iloc[0]["Model"]

c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    st.metric("Transactions", f"{total_transactions:,}")

with c2:
    st.metric("Fraud", f"{fraud_transactions:,}")

with c3:
    st.metric("Legitimate", f"{legitimate_transactions:,}")

with c4:
    st.metric("Fraud Rate", f"{fraud_rate:.2f}%")

with c5:
    st.metric("Best Model", best_model)

st.divider()

# =====================================================
# ROW 1
# =====================================================

left, right = st.columns(2)

with left:

    fig = px.histogram(
        df,
        x="type",
        color="isFraud",
        barmode="group",
        title="Fraud by Transaction Type"
    )

    fig.update_layout(height=450)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    fraud = df["isFraud"].value_counts().reset_index()

    fraud.columns = ["Type", "Count"]

    fraud["Type"] = fraud["Type"].replace(
        {
            0: "Legitimate",
            1: "Fraud"
        }
    )

    pie = px.pie(
        fraud,
        names="Type",
        values="Count",
        hole=0.45,
        title="Fraud Distribution"
    )

    pie.update_layout(height=450)

    st.plotly_chart(
        pie,
        use_container_width=True
    )

st.divider()

# =====================================================
# ROW 2
# =====================================================

left, right = st.columns(2)

with left:

    amount = px.histogram(
        df,
        x="amount",
        color="isFraud",
        nbins=60,
        title="Transaction Amount Distribution"
    )

    amount.update_layout(height=450)

    st.plotly_chart(
        amount,
        use_container_width=True
    )

with right:

    trend = px.line(
        df.groupby("step")["amount"].sum().reset_index(),
        x="step",
        y="amount",
        title="Transaction Trend"
    )

    trend.update_layout(height=450)

    st.plotly_chart(
        trend,
        use_container_width=True
    )

st.divider()

# =====================================================
# FEATURE IMPORTANCE
# =====================================================

st.subheader("🔥 Top Important Features")

feature = feature.sort_values(
    by="Importance",
    ascending=False
).head(10)

bar = px.bar(
    feature,
    x="Importance",
    y="Feature",
    orientation="h",
    color="Importance",
    title="Random Forest Feature Importance"
)

bar.update_layout(height=500)

st.plotly_chart(
    bar,
    use_container_width=True
)

st.divider()

# =====================================================
# MODEL COMPARISON
# =====================================================

st.subheader("🤖 Model Comparison")

st.dataframe(
    comparison,
    use_container_width=True,
    hide_index=True
)

st.divider()

# =====================================================
# BUSINESS SUMMARY
# =====================================================

st.subheader("💰 Business Summary")

st.dataframe(
    business,
    use_container_width=True,
    hide_index=True
)

st.divider()

# =====================================================
# EXECUTIVE SUMMARY
# =====================================================

st.success("""

### Executive Summary

✅ Total transactions processed successfully.

✅ Fraudulent transactions are concentrated in CASH_OUT and TRANSFER.

✅ Random Forest achieved the highest performance.

✅ Fraud detection rate exceeded 99%.

✅ Engineered features significantly improved prediction accuracy.

""")