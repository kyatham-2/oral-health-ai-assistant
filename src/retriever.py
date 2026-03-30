# retriever.py - load FAISS and retrieve relevant documents

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# Load embeddings model (same as before)
embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# Load saved FAISS index
vectorstore = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)

# Create retriever
retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

def get_relevant_docs(query):
    docs = retriever.invoke(query)
    print("\n🔍 Retrieved docs:\n")
    for d in docs:
        print(d.page_content[:200])
        print("------")
    return docs