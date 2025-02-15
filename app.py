# Creating API using FastAPI and Uvicorn, Uvicorn is used along with FastAPI, it listens to the HTTP requests 
# and routes them to the FastAPI application.
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import os

# Defining the FastAPI app
app = FastAPI()

# Loading model and vectorizer
model_path = "classifier.pkl"
vectorizer_path = "vectorizer.pkl"

if not os.path.exists(model_path) or not os.path.exists(vectorizer_path):
    print("⚠️ Model or vectorizer file missing. Ensure both 'classifier.pkl' and 'vectorizer.pkl' are available.")
    model = None
    vectorizer = None
else:
    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)

# Defining category based on the source (incidents.csv)
category_mapping = {
    0: "Network Issue",
    1: "Server Issue",
    2: "Application Issue",
    3: "Security Issue",
    4: "Testing Issue"
}

# Defining the request body
class Incident(BaseModel):
    description: str

# Defining the health check endpoint for Kubernetes probes
@app.get("/health")
async def health_check():
    return {"status": "ok"}

# Defining the root endpoint
@app.post("/predict/")
async def predict(incident: Incident):
    # Ensure model and vectorizer are loaded
    if model is None or vectorizer is None:
        raise HTTPException(status_code=500, detail="Model or vectorizer not found. Please check deployment.")

    # Transforming input with vectorizer
    transformed_description = vectorizer.transform([incident.description])
    
    # Predict the category
    prediction = model.predict(transformed_description)[0]
    
    # Mapping prediction to category
    predicted_category = category_mapping.get(prediction, "Unknown")
    
    return {"category": predicted_category}