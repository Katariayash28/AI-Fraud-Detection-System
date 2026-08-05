import streamlit as st
import pandas as pd
import plotly.express as px

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Model Performance",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Machine Learning Model Performance")
st.caption("Comparison of all trained Machine Learning models")

# =====================================================
# LOAD DATA
# =====================================================

@st.cache_data
def load_data():
    return pd.read_csv("outputs/model_comparison.csv")

comparison = load_data()

# =====================================================
# BEST MODEL
# =====================================================

best = comparison.iloc[0]

c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    st.metric("🏆 Best Model", best["Model"])

with c2:
    st.metric("Accuracy", f"{best['Accuracy']:.4f}")

with c3:
    st.metric("Precision", f"{best['Precision']:.4f}")

with c4:
    st.metric("Recall", f"{best['Recall']:.4f}")

with c5:
    st.metric("ROC-AUC", f"{best['ROC AUC']:.4f}")

st.divider()

# =====================================================
# TABLE
# =====================================================

st.subheader("📋 Complete Model Comparison")

st.dataframe(
    comparison,
    use_container_width=True,
    hide_index=True
)

st.divider()

# =====================================================
# ACCURACY
# =====================================================

fig = px.bar(
    comparison,
    x="Model",
    y="Accuracy",
    color="Accuracy",
    text="Accuracy",
    title="Accuracy Comparison"
)

fig.update_traces(texttemplate='%{text:.4f}')

st.plotly_chart(
    fig,
    use_container_width=True
)

# =====================================================
# PRECISION
# =====================================================

fig = px.bar(
    comparison,
    x="Model",
    y="Precision",
    color="Precision",
    text="Precision",
    title="Precision Comparison"
)

fig.update_traces(texttemplate='%{text:.4f}')

st.plotly_chart(
    fig,
    use_container_width=True
)

# =====================================================
# RECALL
# =====================================================

fig = px.bar(
    comparison,
    x="Model",
    y="Recall",
    color="Recall",
    text="Recall",
    title="Recall Comparison"
)

fig.update_traces(texttemplate='%{text:.4f}')

st.plotly_chart(
    fig,
    use_container_width=True
)

# =====================================================
# F1 SCORE
# =====================================================

fig = px.bar(
    comparison,
    x="Model",
    y="F1 Score",
    color="F1 Score",
    text="F1 Score",
    title="F1 Score Comparison"
)

fig.update_traces(texttemplate='%{text:.4f}')

st.plotly_chart(
    fig,
    use_container_width=True
)

# =====================================================
# ROC AUC
# =====================================================

fig = px.bar(
    comparison,
    x="Model",
    y="ROC AUC",
    color="ROC AUC",
    text="ROC AUC",
    title="ROC-AUC Comparison"
)

fig.update_traces(texttemplate='%{text:.4f}')

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# =====================================================
# RADAR CHART
# =====================================================

st.subheader("📊 Performance Radar")

metrics = ["Accuracy","Precision","Recall","F1 Score","ROC AUC"]

radar = comparison.set_index("Model")[metrics].T

st.line_chart(radar)

st.divider()

# =====================================================
# EXECUTIVE INSIGHTS
# =====================================================

st.success("""

### 📈 Executive Insights

• Random Forest achieved the highest overall performance.

• XGBoost delivered nearly identical performance.

• Logistic Regression provides a strong baseline while remaining computationally efficient.

• Decision Tree performed well but is more susceptible to overfitting.

• Random Forest is recommended for deployment due to its excellent balance of accuracy, precision, recall and robustness.

""")

st.info("""

### Business Impact

✅ High Precision minimizes false fraud alerts.

✅ High Recall ensures most fraudulent transactions are detected.

✅ High ROC-AUC indicates strong separation between legitimate and fraudulent transactions.

""")