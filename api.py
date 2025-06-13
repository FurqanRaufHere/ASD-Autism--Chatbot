from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from chatbot import generate_answer
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow CORS for frontend development server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this in production to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    query: str

class ChatResponse(BaseModel):
    response: str

import time
import logging

logging.basicConfig(level=logging.INFO)

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    logging.info(f"Received query: {request.query}")
    start_time = time.time()
    try:
        # Temporary dummy response for testing
        # answer = generate_answer(request.query)
        answer = "This is a dummy response for testing."
        elapsed = time.time() - start_time
        logging.info(f"Responding in {elapsed:.2f} seconds")
        return ChatResponse(response=answer)
    except Exception as e:
        logging.error(f"Error in chat_endpoint: {e}")
        raise HTTPException(status_code=500, detail=str(e))
