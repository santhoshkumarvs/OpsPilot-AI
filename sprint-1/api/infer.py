from fastapi import FastAPI
from pipelines.inference.predict import TransactionInput, predict

app = FastAPI(title="AutoPilotOps Inference API")

@app.get("/")
def read_root():
    return {"message": "Welcome to AutoPilotOps Inference API"}

@app.post("/predict")
def get_prediction(input: TransactionInput):
    return predict(input)
