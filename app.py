import streamlit as st
from multi_agent import run_agent

st.set_page_config(
    page_title="AI Email Agent",
    layout="wide"
)

st.title("📧 AI Email and Weather Assistant")
st.markdown("Send professional emails and check weather using AI")

# -------------------------
# Session Memory
# -------------------------

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# -------------------------
# Chat Interface
# -------------------------

user_input = st.chat_input("Ask AI to send an email...")

if user_input:

    st.session_state.chat_history.append(("user", user_input))

    with st.spinner("AI is working..."):
        response = run_agent(user_input)

    st.session_state.chat_history.append(("assistant", response))

# -------------------------
# Display Chat
# -------------------------

for role, message in st.session_state.chat_history:

    if role == "user":
        with st.chat_message("user"):
            st.write(message)

    else:
        with st.chat_message("assistant"):
            st.write(message)