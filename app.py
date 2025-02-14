# Creating API using FastAPI and Uvicorn, Uvicorn is used along with FastAPI, it listens to the HTTP requests and routes them to the FastAPI application.
from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Loading model and vectorizer
model = joblib.load("classifier.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Defining category based on the source (incidents.csv)
category_mapping = {
    0: "Network Issue",
    1: "Server Issue",
    2: "Application Issue",
    3: "Security Issue",
    4: "Testing Issue"
}

# Defining the FastAPI app
app = FastAPI()

# Defining the request body
class Incident(BaseModel):
    description: str

# Defining the root endpoint
@app.post("/predict/")
async def predict(incident: Incident):
    # Transforming input with vectorizer
    transformed_description = vectorizer.transform([incident.description])
    # Predict the category
    prediction = model.predict(transformed_description)[0]
    # Mapping prediction to category
    category_mapping = {
        0: "Network Issue",
        1: "Server Issue",
        2: "Application Issue",
        3: "Security Issue",
        4: "Testing Issue"
    }
    predicted_category = category_mapping.get(prediction, "Unknown")
    return {"category": predicted_category}
