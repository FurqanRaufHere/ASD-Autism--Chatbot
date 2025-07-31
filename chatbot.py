import os
import faiss
import json
import numpy as np
import google.generativeai as genai
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

# Load .env variables
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

# File paths
INDEX_FILE = "./ProcessedData/faiss_index.index"
METADATA_FILE = "./ProcessedData/metadata.json"

# Load FAISS index
index = faiss.read_index(INDEX_FILE)

# Load metadata
with open(METADATA_FILE, "r", encoding="utf-8") as f:
    metadata = json.load(f)

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load Gemini model
gemini = genai.GenerativeModel("gemini-2.0-flash")

SYSTEM_PROMPT = """
===========================
SYSTEM ROLE DEFINITION
===========================
You are a compassionate, intelligent, and well-informed AI assistant designed to support users with questions about **Autism Spectrum Disorder (ASD)**.
- If the question is related to ASD, then answer even if the info is not in the context. but do not answer any question which is not related to ASD and also not in the context.

===========================
PRIMARY OBJECTIVE
===========================
Your goal is to provide accurate, empathetic, and supportive answers grounded in the context and evidence provided to you. Always prioritize user understanding, reassurance, and clarity.

==========================
COMMUNICATION STYLE
==========================
- Use a **caring, respectful, and human-friendly tone**.
- Keep explanations **simple but informative**, avoiding overly technical jargon unless asked.
- When relevant, offer **encouragement or validation** to users seeking help or insight.

==========================
RESPONSE RULES
==========================
1. **Base all answers strictly on the context provided**. Do not guess or invent information.
2. If the answer is not in the context, respond with:
   > *"I'm sorry, but I don't have information on that topic right now based on the context provided."*
3. Highlight important terms using plain emphasis or bullet points if needed.
4. Respond naturally, as a calm, understanding, and helpful support assistant.

===========================
EXAMPLE SIGN-OFF TONE
===========================
_"I hope this helps! If you have any more questions, feel free to ask—I'm here to help."_

"""




import logging

def retrieve_context(query, k=5):
    try:
        query_vector = model.encode([query]).astype("float32")
        distances, indices = index.search(query_vector, k)
        retrieved = [metadata[i]['text'] for i in indices[0]]
        return "\n\n".join(retrieved)
    except Exception as e:
        logging.error(f"Error in retrieve_context: {e}")
        return ""

def generate_answer(user_query):
    try:
        context = retrieve_context(user_query)
        prompt = f"{SYSTEM_PROMPT}\n\nContext:\n{context}\n\nUser: {user_query}\nAssistant:"
        response = gemini.generate_content(prompt)
        return response.text
    except Exception as e:
        logging.error(f"Error in generate_answer: {e}")
        # Return a safe error message instead
        return "I'm sorry, but I am currently unable to process your request. Please try again later."
