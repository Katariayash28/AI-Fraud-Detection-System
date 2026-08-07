import streamlit as st
from groq import Groq

# ==============================
# PAGE CONFIG
# ==============================
st.set_page_config(page_title="AI Fraud Detection System", layout="wide")

# ==============================
# GROQ CLIENT (SECURE)
# ==============================
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

def get_ai_response(prompt):
    try:
        completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": "You are a fraud detection expert assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message.content

    except Exception as e:
        return f"⚠️ Error: {str(e)}"

# ==============================
# SIDEBAR NAVIGATION
# ==============================
st.sidebar.title("Navigation")
page = st.sidebar.selectbox(
    "Go to",
    ["Fraud Detection", "💬 Chat Assistant"]
)

# ==============================
# FRAUD DETECTION PAGE
# ==============================
if page == "Fraud Detection":
    st.title("Fraud Detection Dashboard")

    st.write("🚀 Your fraud detection system is running successfully!")

    # 👉 You can paste your old fraud model/dashboard code here


# ==============================
# CHATBOT PAGE
# ==============================
elif page == "💬 Chat Assistant":
    st.title("AI Fraud Assistant 🤖")

    # Store chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display previous messages
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    # Chat input
    prompt = st.chat_input("Ask about fraud, transactions, or data...")

    if prompt and prompt.strip() != "":
        # Show user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

        # Get AI response
        response = get_ai_response(prompt)

        # Show AI message
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.chat_message("assistant").write(response)
