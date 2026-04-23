# 🦷 Oral Health AI Assistant

## Overview

The Oral Health AI Assistant is an AI-powered web application that helps users, particularly elderly individuals and children, understand oral health in a simple and interactive manner.

The system uses **Retrieval-Augmented Generation (RAG)** to provide accurate, context-aware answers based on curated dental knowledge.

---

## 🚀 Live Demo

🔗 https://diaoral.streamlit.app/

---

## Features

* 🧠 AI-powered conversational assistant
* 📚 Retrieval-Augmented Generation (RAG) for accurate responses
* 👶 Age-aware responses (e.g., tailored for children)
* 💬 Interactive chat interface built with Streamlit
* 🔍 Context retrieval using FAISS vector database
* 🎯 Focused on oral health education and awareness

---

## Tech Stack

* **Frontend/UI:** Streamlit
* **Backend:** Python
* **AI/LLM Integration:** RAG architecture
* **Vector Database:** FAISS
* **Data Processing:** Custom preprocessing pipelines

---

## Project Structure

```id="c7k2tm"
.
├── app.py
├── requirements.txt
├── Data/
├── faiss_index/
├── assets/
├── src/
├── .streamlit/
└── README.md
```

---

## How It Works

1. User asks a question via the chat interface
2. The system retrieves relevant information from the FAISS vector database
3. Retrieved context is passed to the language model
4. The model generates a personalized, accurate response
5. Response is tailored based on user context (e.g., age group)

---

## How to Run Locally

### 1. Clone the repository

```id="hmz1l4"
git clone https://github.com/kyatham-2/oral-health-ai-assistant.git
```

### 2. Navigate to the project folder

```id="m7g39c"
cd oral-health-ai-assistant
```

### 3. Install dependencies

```id="j5v5xb"
pip install -r requirements.txt
```

### 4. Run the application

```id="9d9pbn"
streamlit run app.py
```

---

## Key Highlights

* Real-world application of **RAG architecture**
* Combines **AI + healthcare education**
* Designed for accessibility and ease of use
* Interactive and user-friendly interface
* Demonstrates vector search and LLM integration

---

## Future Improvements

* Add voice interaction for accessibility
* Expand dataset with more medical sources
* Improve personalization with user profiles
* Add multilingual support
* Deploy with scalable backend (AWS/GCP)

---

## Author

Vinay Kumar Kyatham
