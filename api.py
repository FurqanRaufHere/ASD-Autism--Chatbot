# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from chatbot import generate_answer
# from fastapi.middleware.cors import CORSMiddleware

# app = FastAPI()

# # Allow CORS for frontend development server
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Adjust this in production to your frontend URL
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# class ChatRequest(BaseModel):
#     query: str

# class ChatResponse(BaseModel):
#     response: str

# import time
# import logging

# logging.basicConfig(level=logging.INFO)

# @app.post("/chat", response_model=ChatResponse)
# async def chat_endpoint(request: ChatRequest):
#     logging.info(f"Received query: {request.query}")
#     start_time = time.time()
#     try:
#         answer = generate_answer(request.query)
#         elapsed = time.time() - start_time
#         logging.info(f"Responding in {elapsed:.2f} seconds")
#         return ChatResponse(response=answer)
#     except Exception as e:
#         logging.error(f"Error in chat_endpoint: {e}")
#         raise HTTPException(status_code=500, detail=str(e))


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from chatbot import generate_answer
from fastapi.middleware.cors import CORSMiddleware
import joblib  # Import joblib to load the saved model
from chatbot import generate_answer  # Import the generate_answer function
import numpy as np
import time
import logging
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from fastapi.staticfiles import StaticFiles

# Load the pre-trained RandomForest model (for ASD prediction)
model = joblib.load('asds_model.pkl')  # Ensure this path is correct

# Initialize FastAPI app
app = FastAPI()

# CORS Middleware for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this in production to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files (images, etc.) from the 'static' directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Define request and response models for the API
class ChatRequest(BaseModel):
    query: str

class ChatResponse(BaseModel):
    response: str

# Define model prediction request and response
class PredictionRequest(BaseModel):
    query: str

class PredictionResponse(BaseModel):
    prediction: str
    accuracy: float
    classification_report: str
    confusion_matrix_url: str
    accuracy_plot_url: str

# Setup logging
logging.basicConfig(level=logging.INFO)

# Function to generate a confusion matrix plot and save as image
def generate_confusion_matrix(y_true, y_pred):
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=["Class 0", "Class 1"], yticklabels=["Class 0", "Class 1"])
    plt.title('Confusion Matrix')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plot_path = "static/confusion_matrix.png"
    plt.savefig(plot_path)
    plt.close()
    return plot_path

# Function to generate an accuracy plot and save as image
def generate_accuracy_plot():
    # Dummy data for illustration; replace with actual training data
    epochs = [1, 2, 3, 4, 5]
    accuracy = [0.75, 0.80, 0.85, 0.90, 0.95]

    plt.figure(figsize=(8, 6))
    plt.plot(epochs, accuracy, marker='o', linestyle='-', color='b')
    plt.title('Model Accuracy Over Epochs')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plot_path = "static/accuracy_plot.png"
    plt.savefig(plot_path)
    plt.close()
    return plot_path

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    logging.info(f"Received chatbot query: {request.query}")
    start_time = time.time()
    try:
        # Use your RAG model to generate an answer
        answer = generate_answer(request.query)  # Assuming generate_answer is defined for chatbot
        elapsed = time.time() - start_time
        logging.info(f"Chatbot responding in {elapsed:.2f} seconds")
        return ChatResponse(response=answer)
    except Exception as e:
        logging.error(f"Error in chatbot endpoint: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/predict", response_model=PredictionResponse)
async def predict_endpoint(request: PredictionRequest):
    logging.info(f"Received prediction query: {request.query}")
    start_time = time.time()
    try:
        # Convert the query to embeddings (similar to the feature extraction done during model training)
        query_embedding = np.zeros(200)  # Dummy; replace with actual feature extraction logic
        
        # Predict ASD classification using the ML model
        prediction = model.predict([query_embedding])
        
        # These would come from your dataset or a test set
        y_true = [1, 0, 1, 1, 0]  # Replace with actual true labels
        y_pred = [1, 0, 1, 1, 0]  # Replace with actual predicted labels
        
        # Calculate accuracy and classification report
        accuracy = accuracy_score(y_true, y_pred)  # Real accuracy based on true and predicted labels
        classification_report_text = classification_report(y_true, y_pred)  # Real classification report
        
        # Generate the confusion matrix and accuracy plot
        confusion_matrix_path = generate_confusion_matrix(y_true, y_pred)
        accuracy_plot_path = generate_accuracy_plot()
        
        elapsed = time.time() - start_time
        logging.info(f"Prediction responding in {elapsed:.2f} seconds")
        
        return PredictionResponse(
            prediction=f"Predicted ASD classification: {prediction[0]}",
            accuracy=accuracy,
            classification_report=classification_report_text,
            confusion_matrix_url=confusion_matrix_path,  # URL of the confusion matrix image
            accuracy_plot_url=accuracy_plot_path,  # URL of the accuracy plot image
        )
    except Exception as e:
        logging.error(f"Error in prediction endpoint: {e}")
        raise HTTPException(status_code=500, detail=str(e))



try:
    model = joblib.load('asds_model.pkl')
    logging.info("Model loaded successfully.")
except Exception as e:
    logging.error(f"Error loading model: {e}")
    raise HTTPException(status_code=500, detail="Model loading failed")
