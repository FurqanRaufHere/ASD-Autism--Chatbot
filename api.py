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

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    try:
        answer = generate_answer(request.query)
        return ChatResponse(response=answer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
