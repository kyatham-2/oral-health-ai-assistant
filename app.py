import streamlit as st
import os
from src.chatbot import generate_answer


st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #EAF7F3, #F8FBFA);
}
</style>
""", unsafe_allow_html=True)

user_avatar = os.path.join("assets", "User.png")
bot_avatar = os.path.join("assets", "Doctor.png")

st.markdown("""
<h1 style='text-align: center; color: #2E8B57;'>
🦷 Oral Health AI Assistant
</h1>
""", unsafe_allow_html=True)
st.markdown("""
<div style="
background-color:#E6F4EA;
padding:12px;
border-radius:10px;
border:1px solid #B7E4C7;
text-align:center;
">
🩺 Welcome! This assistant helps you understand oral health in a simple and friendly way.
</div>
""", unsafe_allow_html=True)
st.markdown("""
<style>

/* Remove default box feel */
[data-testid="stChatMessage"] {
    background: transparent !important;
    border: none !important;
    padding: 8px 0px !important;
}

/* User bubble (right side) */
[data-testid="stChatMessage"][data-testid*="user"] > div {
    background-color: #E8F5E9;
    border-radius: 16px;
    padding: 12px 16px;
    max-width: 70%;
    margin-left: auto;
}

/* Bot bubble (left side) */
[data-testid="stChatMessage"][data-testid*="assistant"] > div {
    background-color: #FFFFFF;
    border-radius: 16px;
    padding: 12px 16px;
    max-width: 70%;
    margin-right: auto;
    border: 1px solid #E0E0E0;
}

</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>
.stTextInput input {
    border-radius: 10px;
    border: 1px solid #95D5B2;
}
</style>
""", unsafe_allow_html=True)

if "summary" not in st.session_state:
    st.session_state.summary = ""

if "age_group" not in st.session_state:
    # st.write("Please select your age group to continue:")
    age_group = st.selectbox(
        # st.write("Please select your age group:"),
        # "Select age group:",
        "Please select your age group to continue:",
        ["Child", "Adult", "Elderly"]
    )

    if st.button("Continue"):
        st.session_state.age_group = age_group
        st.session_state.messages = []  # reset chat
        st.success(f"Age group selected: {age_group}")
        st.rerun()

    st.stop()  # stop app until age is selected

# 🔹 Show selected age
# st.write(f"👤 Age group: {st.session_state.age_group}")
st.markdown(f"""
<div style="
padding:12px;
border-radius:10px;
text-align:left; color:#2E8B57;
">
💡 Answers will be tailored based on {st.session_state.age_group} age group
</div>
""", unsafe_allow_html=True)
# st.write("💡 Answers will be tailored based on your age group.")

# 🔹 Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# 🔹 Display previous messages
for msg in st.session_state.messages:
    avatar = user_avatar if msg["role"] == "user" else bot_avatar
    with st.chat_message(msg["role"], avatar=avatar):
        st.write(msg["content"])

# 🔹 User input
user_input = st.chat_input("Ask your question here...")

if user_input:
    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user", avatar=user_avatar):
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

    with st.chat_message("assistant",  avatar=bot_avatar):
        st.write(answer)