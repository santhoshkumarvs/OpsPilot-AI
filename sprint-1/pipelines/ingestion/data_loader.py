import os
import pandas as pd
import yaml
from pydantic import BaseModel, ValidationError

# INTERVIEW QUESTION (Nest Digital): Schema validation at ingestion
# Mature Answer: Use pydantic schema + fail-safe fallback

class Transaction(BaseModel):
    age: int
    income: float
    transaction_count: int
    fraud_flag: int

def load_config(path="config/config.yaml"):
    with open(path) as f:
        return yaml.safe_load(f)

def load_data(config):
    file_path = os.path.join(config['data_path'], "transactions.csv")
    df = pd.read_csv(file_path)

    if config["enable_schema_validation"]:
        try:
            _ = [Transaction(**row) for row in df.to_dict(orient="records")]
            print("✅ Schema validated")
        except ValidationError as e:
            print("❌ Schema validation failed:", e)
            raise e
    return df

if __name__ == "__main__":
    cfg = load_config()
    df = load_data(cfg)
    print(df.head())
