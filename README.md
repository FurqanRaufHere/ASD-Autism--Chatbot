# ASD Chatbot 🤖

**ASD Chatbot** is an AI-powered assistant designed to provide informative, empathetic, and accurate answers related to **Autism Spectrum Disorder (ASD)**. It is a RAG based Chatbot that uses **Google Gemini Flash 2.0** for response generation and **FAISS** for efficient retrieval of relevant information from a knowledge base. 

---

## Features

- **Conversational AI:** Provide insightful and personalized answers regarding Autism Spectrum Disorder.
- **Empathetic Tone:** Responses are designed to be understanding and sensitive to the needs of users seeking ASD-related information.
- **Contextual Knowledge Retrieval:** Uses **FAISS** (Facebook AI Similarity Search) to efficiently retrieve relevant data from a vectorized knowledge base.
- **Responsive Interface:** Built with **Streamlit** to ensure the chatbot works seamlessly across all devices (mobile, tablet, desktop).
- **Dark Mode:** Toggle between dark and light mode for a better user experience.

---

## Main Dependencies

- **PDF Extraction:** pdfplumber – Extracts text from PDF documents.
- **Text Chunking & Utility:** langchain, tqdm – Chunks large text and tracks progress.
- **Embedding Model:** sentence-transformers, numpy – Converts text into vector embeddings.
- **Vector Search:** faiss-cpu – Enables fast similarity-based search.
- **LLM Integration:** google-generativeai – Communicates with Gemini Flash 2.0. Used for custom responses.
- **Frontend UI:** streamlit – Builds an interactive and user-friendly web interface.
- **Environment Management:** python-dotenv – Loads secure API keys from .env file.

---

## How It Works
### **1. Extracts text from ASD-related PDF files using pdfplumber.**
- Chunks large texts into smaller passages using LangChain’s RecursiveCharacterTextSplitter.

### **2. Embedding and Indexing**
- Converts chunks into vector embeddings via SentenceTransformers.
- Stores and indexes them using FAISS for efficient retrieval.

### **3. Context Retrieval and Answer Generation**
- On each user query, retrieves the top-matching chunks from FAISS.



## Requirements

Before running the application, you’ll need to install the following dependencies. You can install all of them by running:

```bash
pip install -r requirements.txt
