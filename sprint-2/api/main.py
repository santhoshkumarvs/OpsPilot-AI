from fastapi import FastAPI
from pydantic import BaseModel
from pipelines.inference.predict import predict
from pipelines.inference.predict import TransactionInput

app = FastAPI(title="OpsPilot-AI Inference API", version="0.1.0")

class InferenceResponse(BaseModel):
    prediction: int
    confidence: float

@app.get("/")
def read_root():
    return {"message": "Welcome to OpsPilot-AI Inference API"}

@app.post("/predict", response_model=InferenceResponse)
def get_prediction(input_data: TransactionInput):
    result = predict(input_data)
    return result
