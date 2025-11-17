import streamlit as st

st.set_page_config(page_title="AI Chatbot", layout="centered")

st.title("🤖 AI Chatbot")

st.write("Ask me anything...")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display old messages
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").markdown(msg["content"])
    else:
        st.chat_message("assistant").markdown(msg["content"])

# Input box
user_input = st.chat_input("Type your message...")

if user_input:
    # Show user message
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Simple dummy AI response (replace with real model later)
    ai_response = f"Your question was: **{user_input}**. I'll answer using AI soon!"

    # Show bot response
    st.chat_message("assistant").markdown(ai_response)
    st.session_state.messages.append({"role": "assistant", "content": ai_response})
