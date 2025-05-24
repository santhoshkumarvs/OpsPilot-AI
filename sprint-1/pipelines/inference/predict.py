import pandas as pd
import joblib  # ✅ Use joblib instead of pickle
from pydantic import BaseModel

class TransactionInput(BaseModel):
    age: int
    income: float
    transaction_count: int
    transaction_amount: float

def predict(input_data: TransactionInput):
    # Convert input to DataFrame with correct feature names
    data = input_data.model_dump()
    data["amount"] = data.pop("transaction_amount")
    data["user_id"] = "inference_user"  # dummy to match training schema
    df = pd.DataFrame([data])

    # Load model
    model = joblib.load("models/autopilot_clf.pkl")

    # Predict
    prediction = model.predict(df[["age", "income", "amount", "transaction_count"]])
    return {"prediction": int(prediction[0])}  # ✅ consistent return
