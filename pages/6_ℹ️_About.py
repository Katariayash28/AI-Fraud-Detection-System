import streamlit as st

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="About Project",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ About This Project")
st.caption("End-to-End Machine Learning Fraud Detection System")

st.divider()

# =====================================================
# PROJECT OVERVIEW
# =====================================================

st.header("📌 Project Overview")

st.write("""
This project is an end-to-end Machine Learning solution developed to detect
fraudulent financial transactions in real time.

The solution combines exploratory data analysis, feature engineering,
supervised machine learning, explainable AI concepts, and an interactive
Streamlit dashboard to help financial institutions identify suspicious
transactions quickly and accurately.
""")

st.divider()

# =====================================================
# BUSINESS PROBLEM
# =====================================================

st.header("🏦 Business Problem")

st.info("""
Financial institutions process millions of transactions every day.

Traditional rule-based fraud detection systems often generate many false
positives and fail to detect evolving fraud patterns.

The objective of this project is to develop a Machine Learning model capable
of accurately distinguishing fraudulent transactions from legitimate ones,
thereby reducing financial losses and improving operational efficiency.
""")

st.divider()

# =====================================================
# DATASET
# =====================================================

st.header("📂 Dataset")

st.write("""

The dataset contains financial transaction information including:

• Transaction Type

• Transaction Amount

• Sender Balance

• Receiver Balance

• Fraud Label

Several additional engineered features were created to improve model
performance.

""")

st.divider()

# =====================================================
# MACHINE LEARNING PIPELINE
# =====================================================

st.header("⚙️ Machine Learning Pipeline")

st.markdown("""

1️⃣ Business Understanding

⬇️

2️⃣ Data Cleaning

⬇️

3️⃣ Exploratory Data Analysis

⬇️

4️⃣ Feature Engineering

⬇️

5️⃣ Data Preprocessing

⬇️

6️⃣ Model Training

⬇️

7️⃣ Hyperparameter Tuning

⬇️

8️⃣ Model Evaluation

⬇️

9️⃣ Explainable AI (SHAP)

⬇️

🔟 Streamlit Deployment

""")

st.divider()

# =====================================================
# MODELS
# =====================================================

st.header("🤖 Machine Learning Models")

st.success("""

Models Evaluated

✅ Logistic Regression

✅ Decision Tree

✅ Random Forest

✅ XGBoost

""")

st.divider()

# =====================================================
# PERFORMANCE
# =====================================================

st.header("📈 Final Model Performance")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Accuracy", "99.95%")

with c2:
    st.metric("Precision", "100%")

with c3:
    st.metric("Recall", "99.56%")

with c4:
    st.metric("ROC-AUC", "0.9999")

st.divider()

# =====================================================
# TECHNOLOGIES
# =====================================================

st.header("💻 Technologies Used")

st.write("""

Programming Language

• Python

Libraries

• Pandas

• NumPy

• Scikit-Learn

• Plotly

• Streamlit

• Joblib

• SHAP

Development Tools

• Google Colab

• VS Code

• GitHub

""")

st.divider()

# =====================================================
# PROJECT FEATURES
# =====================================================

st.header("🚀 Key Features")

st.success("""

✔ Executive Dashboard

✔ Interactive Visualizations

✔ Live Fraud Prediction

✔ AI Investigation Report

✔ Financial Impact Analysis

✔ Model Performance Dashboard

✔ Downloadable Reports

✔ Interactive User Interface

""")

st.divider()

# =====================================================
# FUTURE ENHANCEMENTS
# =====================================================

st.header("🔮 Future Enhancements")

st.info("""

• Deep Learning Models

• Real-Time API Integration

• Cloud Deployment

• Live Transaction Monitoring

• SHAP Visual Dashboard

• Email & SMS Fraud Alerts

• Database Integration

• User Authentication

""")

st.divider()

# =====================================================
# DEVELOPER
# =====================================================

st.header("👨‍💻 Developer")

st.write("""

**Yash Kataria**

Aspiring Data Analyst | Machine Learning Enthusiast | AI Developer

This project was developed as part of a Data Science & Generative AI
Capstone Project to demonstrate practical skills in:

• Data Analysis

• Machine Learning

• Feature Engineering

• Explainable AI

• Dashboard Development

• Streamlit Application Development

""")

st.divider()

st.success("🎉 Thank you for exploring the AI Fraud Detection System!")