import streamlit as st
from groq import Groq

# ==============================
# PAGE CONFIG
# ==============================
st.set_page_config(
    page_title="AI Fraud Detection System",
    page_icon="🛡️",
    layout="wide"
)

# ==============================
# CUSTOM CSS (UI IMPROVEMENT)
# ==============================
st.markdown("""
<style>
.main {
    background-color: #0E1117;
}
h1, h2, h3 {
    color: #ffffff;
}
.stButton>button {
    background-color: #00C9A7;
    color: white;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

# ==============================
# GROQ SETUP
# ==============================
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

def get_ai_response(prompt):
    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are a fraud detection expert assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

# ==============================
# SIDEBAR
# ==============================
st.sidebar.title("🛡️ Fraud System")
page = st.sidebar.radio(
    "Navigate",
    ["🏠 Dashboard", "🔍 Predict Fraud", "📊 Model Info", "💬 AI Assistant"]
)

# ==============================
# DASHBOARD
# ==============================
if page == "🏠 Dashboard":
    st.title("Fraud Detection Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric("Transactions", "120K", "+5%")
    col2.metric("Frauds Detected", "2,340", "+12%")
    col3.metric("Accuracy", "94.8%", "+1.2%")

    st.markdown("### 📈 Overview")
    st.info("This system uses Machine Learning to detect fraudulent transactions in real-time.")

# ==============================
# PREDICT FRAUD (PLACEHOLDER)
# ==============================
elif page == "🔍 Predict Fraud":
    st.title("Fraud Prediction")

    amount = st.number_input("Transaction Amount")
    time = st.number_input("Transaction Time")

    if st.button("Predict"):
        st.success("Prediction: Not Fraud (Demo)")
        # 👉 Replace with your ML model logic

# ==============================
# MODEL INFO
# ==============================
elif page == "📊 Model Info":
    st.title("Model Information")

    st.write("""
    - Model: Random Forest / XGBoost  
    - Dataset: Credit Card Transactions  
    - Features: Time, Amount, V1-V28  
    - Accuracy: 94%+  
    """)

# ==============================
# AI CHATBOT
# ==============================
elif page == "💬 AI Assistant":
    st.title("AI Fraud Assistant 🤖")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    prompt = st.chat_input("Ask about fraud detection, data, or your project...")

    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

        response = get_ai_response(prompt)

        st.session_state.messages.append({"role": "assistant", "content": response})
        st.chat_message("assistant").write(response)
