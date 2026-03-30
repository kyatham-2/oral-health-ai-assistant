from src.retriever import get_relevant_docs
from google import genai
import streamlit as st
import os

client = genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])

# 🔹 classify query
def is_dental_query(query):
    keywords = ["tooth", "teeth", "gum", "oral", "dental",
    "brush", "floss", "cavity", "mouth",
    "tongue", "bleeding", "pain", "patches"]
    return any(word in query.lower() for word in keywords)


def needs_follow_up(query):
    # if user question is too short → we need more info
    if len(query.split()) < 5:
        return True
    return False

def generate_answer(query, age_group, chat_history, summary):

    history_text = ""
    for msg in chat_history[-6:]:
       history_text += f"{msg['role']}: {msg['content']}\n"


    # if not is_dental_query(query):
    #     answer = handle_general_query(query,age_group)
    #     return answer,summary

    # 🔹 DENTAL → RAG + Gemini
    docs = get_relevant_docs(query)

    if not docs:
        return "I don’t have enough information about that. Please consult a dentist."

    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are a friendly and intelligent dental assistant.

User age group: {age_group}

Summary:
{summary}

Conversation so far:
{history_text}

Instructions:
- This is a CONTINUOUS conversation
- Understand user intent based on previous messages

Behavior:
1. If user asks a new dental question → answer using context
2. If user asks follow-up (like "why", "explain", "simplify") →
   → continue previous answer naturally
3. If user asks unrelated question →
   → say politely: "I can only help with oral and dental health questions"
4. If user message is unclear →
   → ask clarification


Guidelines:
- For children:
  Focus on hygiene habits, diet, sugar intake, and brushing practices
  Explain if the issue may be due to poor habits or nutrition

- For adults:
  Consider lifestyle factors such as stress, smoking, irregular dental care, and early-stage diseases

- For elderly:
  Consider age-related factors such as gum recession, tooth wear, medication side effects, dry mouth, or long-term habits like smoking

- Always:
  1. Explain possible causes based on the user’s age
  2. Give simple and practical advice
  3. Suggest when to see a dentist if needed
  4. Do NOT assume — guide carefully

Context:
{context}

Question:
{query}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    answer = response.text
    summary_prompt = f"""
Summarize the conversation briefly.

Previous summary:
{summary}

New interaction:
User: {query}
Assistant: {answer}

Updated summary:
"""  
    summary_response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=summary_prompt
    )

    new_summary = summary_response.text

    return answer, new_summary


# 🔹 General questions
def handle_general_query(query, age_group):

    prompt = f"""
You are a dental assistant specialized ONLY in oral and dental health.


STRICT RULES:
- Answer ONLY questions related to oral health, teeth, gums, mouth, or dental care
- If the question is NOT related to oral health, DO NOT answer it
- Instead, say: "I can only help with oral and dental health questions."

User age group: {age_group}

User:
{query}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text