import streamlit as st
import pandas as pd
import plotly.express as px
from groq import Groq

# ================================
# CONFIG
# ================================
st.set_page_config(page_title="AI Fraud Detection", layout="wide")

# ================================
# GROQ SETUP
# ================================
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

def get_ai_response(prompt):
    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",  # ✅ updated working model
            messages=[
                {"role": "system", "content": "You are an expert fraud detection assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# ================================
# SIDEBAR
# ================================
st.sidebar.title("🛡️ Fraud System")

page = st.sidebar.radio(
    "Navigation",
    ["🏠 App"]
)

# ================================
# 🏠 MAIN APP (CHATBOT + INFO)
# ================================
if page == "🏠 App":
    st.title("🛡️ AI Fraud Detection System")

    st.markdown("## 🤖 AI Fraud Assistant")

    # Chat memory
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    # Input
    prompt = st.chat_input("Ask anything about fraud, your model, or insights...")

    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

        response = get_ai_response(prompt)

        st.session_state.messages.append({"role": "assistant", "content": response})
        st.chat_message("assistant").write(response)

    st.markdown("---")

    # INFO SECTION
    st.markdown("## 📌 About This Project")

    st.info("""
    This AI-powered Fraud Detection System uses Machine Learning to detect suspicious transactions 
    and prevent financial fraud. It also includes an AI chatbot that helps explain fraud patterns 
    and model insights in real-time.
    """)

    st.markdown("## ⚙️ Tech Stack")

    col1, col2 = st.columns(2)

    with col1:
        st.success("""
        - Python  
        - Pandas, NumPy  
        - Scikit-learn  
        """)

    with col2:
        st.success("""
        - Streamlit  
        - Plotly  
        - Groq API (LLM)  
        """)

    st.markdown("## 🚀 Features")

    st.write("""
    - Fraud Prediction using ML  
    - Interactive Dashboard  
    - AI Chat Assistant  
    - Real-time Insights  
    """)





