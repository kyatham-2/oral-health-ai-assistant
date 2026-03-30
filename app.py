import streamlit as st
from src.chatbot import generate_answer

st.title("🦷 Oral Health AI Assistant")

if "summary" not in st.session_state:
    st.session_state.summary = ""

if "age_group" not in st.session_state:
    st.subheader("Welcome 👋")
    st.write("Please select your age group to continue:")

    age_group = st.selectbox(
        "Select age group:",
        ["Child", "Adult", "Elderly"]
    )

    if st.button("Continue"):
        st.session_state.age_group = age_group
        st.session_state.messages = []  # reset chat
        st.success(f"Age group selected: {age_group}")
        st.rerun()

    st.stop()  # stop app until age is selected

# 🔹 Show selected age
st.write(f"👤 Age group: {st.session_state.age_group}")
st.info("💡 Answers will be tailored based on your age group.")

# 🔹 Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# 🔹 Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# 🔹 User input
user_input = st.chat_input("Ask your question here...")

if user_input:
    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.write(user_input)

    # Generate response
    answer, new_summary = generate_answer(
        user_input,
        st.session_state.age_group,
        st.session_state.messages,
        st.session_state.summary
    )

    st.session_state.summary = new_summary

    # Save assistant message
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    with st.chat_message("assistant"):
        st.write(answer)