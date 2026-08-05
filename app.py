import streamlit as st

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="AI Fraud Detection System",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown("""
<style>

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

/* DO NOT HIDE HEADER */

.block-container{
padding-top:2rem;
padding-left:2rem;
padding-right:2rem;
padding-bottom:2rem;
}

.hero{
background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
padding:35px;
border-radius:15px;
color:white;
box-shadow:0 5px 20px rgba(0,0,0,.25);
}

.card{
background:#1f2937;
padding:20px;
border-radius:15px;
border:1px solid #374151;
text-align:center;
height:180px;
}

.card h3{
margin-bottom:15px;
}

.footer{
text-align:center;
padding-top:20px;
color:gray;
font-size:14px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# SIDEBAR
# ==========================================================

st.sidebar.title("🛡️ AI Fraud Detection")

st.sidebar.markdown("---")

st.sidebar.success("Enterprise ML Dashboard")

st.sidebar.write(
"""
Use the sidebar to navigate through:

- 🏠 Home
- 📊 Dashboard
- 🤖 Predict Fraud
- 📈 Model Performance
- 💰 Financial Impact
- 🧠 AI Investigator
- ℹ️ About
"""
)

st.sidebar.markdown("---")
st.sidebar.info("Built using Streamlit + Machine Learning")

# ==========================================================
# HERO
# ==========================================================

st.markdown("""
<div class='hero'>

# 🛡️ AI Fraud Detection System

### Real-Time Financial Fraud Analytics using Machine Learning

Predict fraudulent financial transactions using an enterprise-grade Random Forest model.

</div>
""", unsafe_allow_html=True)

st.write("")

# ==========================================================
# OVERVIEW
# ==========================================================

left,right=st.columns([2,1])

with left:

    st.header("📌 Project Overview")

    st.write("""

This application demonstrates a complete end-to-end Machine Learning
solution for Fraud Detection.

The project covers:

- Data Cleaning

- Exploratory Data Analysis

- Feature Engineering

- Model Training

- Hyperparameter Tuning

- Explainable AI

- Financial Impact Analysis

- Interactive Dashboard

- Real-Time Fraud Prediction

""")

with right:

    st.info("""

### 🚀 Technology Stack

- Python

- Streamlit

- Pandas

- NumPy

- Plotly

- Scikit-Learn

- Random Forest

- XGBoost

- SHAP

""")

st.divider()

# ==========================================================
# MODULES
# ==========================================================

st.header("✨ Application Modules")

c1,c2,c3=st.columns(3)

with c1:

    st.markdown("""
<div class='card'>

<h3>📊 Dashboard</h3>

Interactive KPIs

Fraud Analytics

Business Insights

</div>
""", unsafe_allow_html=True)

with c2:

    st.markdown("""
<div class='card'>

<h3>🤖 Predict Fraud</h3>

Real-Time Prediction

Risk Score

Probability

</div>
""", unsafe_allow_html=True)

with c3:

    st.markdown("""
<div class='card'>

<h3>🧠 AI Investigator</h3>

Executive Summary

Recommendations

Business Report

</div>
""", unsafe_allow_html=True)

st.divider()

# ==========================================================
# PROJECT PIPELINE
# ==========================================================

st.header("⚙️ Machine Learning Pipeline")

st.markdown("""

1. Business Understanding

2. Data Collection

3. Data Cleaning

4. Exploratory Data Analysis

5. Feature Engineering

6. Model Training

7. Hyperparameter Tuning

8. Model Evaluation

9. Explainable AI (SHAP)

10. Streamlit Deployment

""")

st.divider()

# ==========================================================
# PROJECT HIGHLIGHTS
# ==========================================================

st.header("🏆 Project Highlights")

k1,k2,k3,k4=st.columns(4)

with k1:
    st.metric("Best Model","Random Forest")

with k2:
    st.metric("Accuracy","99.95%")

with k3:
    st.metric("Precision","100%")

with k4:
    st.metric("ROC-AUC","0.9999")

st.divider()

# ==========================================================
# HOW TO USE
# ==========================================================

st.header("📖 How To Use")

st.write("""

1️⃣ Open Dashboard

2️⃣ Explore Analytics

3️⃣ Open Predict Fraud

4️⃣ Enter Transaction Details

5️⃣ Click Predict

6️⃣ Review Investigation Report

""")

st.divider()

st.markdown("""
<div class='footer'>

Developed by <b>Yash Kataria</b>

<br>

AI Fraud Detection Capstone Project

</div>
""", unsafe_allow_html=True)