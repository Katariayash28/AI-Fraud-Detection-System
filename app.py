import streamlit as st
import os
from groq import Groq

# ==============================
# PAGE CONFIG
# ==============================
st.set_page_config(page_title="AI Fraud Detection System", layout="wide")

# ==============================
# SIDEBAR NAVIGATION
# ==============================
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Fraud Detection", "💬 Chat Assistant"])

# ==============================
# GROQ SETUP
# ==============================
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_ai_response(prompt):
    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": "You are a fraud detection expert assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.content


# ==============================
# FRAUD PAGE (KEEP YOUR OLD CODE HERE)
# ==============================
if page == "Fraud Detection":
    st.title("Fraud Detection Dashboard")

    st.write("Your existing fraud detection code here...")

# ==============================
# CHATBOT PAGE
# ==============================
if page == "💬 Chat Assistant":
    st.title("AI Fraud Assistant 🤖")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    # Input box
    if prompt := st.chat_input("Ask about fraud, data, or your project..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

        response = get_ai_response(prompt)

        st.session_state.messages.append({"role": "assistant", "content": response})
        st.chat_message("assistant").write(response)
