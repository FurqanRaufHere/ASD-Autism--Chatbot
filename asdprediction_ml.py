import os
import json
import numpy as np
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sentence_transformers import SentenceTransformer
import faiss

def load_data(file_path):
    return pd.read_csv(file_path)

def preprocess_data(data):
    data = data.dropna()
    return data

def create_embeddings(data, model_name="all-MiniLM-L6-v2"):
    model = SentenceTransformer(model_name)
    embeddings = model.encode(data["text"].tolist(), show_progress_bar=True)
    return embeddings

def train_model(X_train, y_train):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    
    return y_pred

def save_model(model, model_path="model.joblib"):
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")

def main():
    data = load_data("data.csv")  # Replace with your dataset path
    data = preprocess_data(data)
    embeddings = create_embeddings(data)
    
    X_train, X_test, y_train, y_test = train_test_split(embeddings, data["target"], test_size=0.2, random_state=42)
    
    model = train_model(X_train, y_train)
    
    evaluate_model(model, X_test, y_test)
    
    save_model(model)

if __name__ == "__main__":
    main()
