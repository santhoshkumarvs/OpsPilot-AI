import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
import os

def train():
    # Load data
    df = pd.read_csv("data/transactions.csv")

    # Rename to match inference schema
    if "transaction_amount" in df.columns:
        df.rename(columns={"transaction_amount": "amount"}, inplace=True)

    print("📄 Available columns:", df.columns.tolist())

    # Ensure schema consistency
    required_columns = ["age", "income", "amount", "transaction_count", "fraud_flag", "user_id"]
    assert all(col in df.columns for col in required_columns), "❌ Missing required columns!"

    # Prepare features and target
    X = df[["age", "income", "amount", "transaction_count"]]
    y = df["fraud_flag"]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    accuracy = model.score(X_test, y_test)

    # Save model
    os.makedirs("models", exist_ok=True)
    joblib.dump(model, "models/autopilot_clf.pkl")

    print("✅ Schema validated")
    print(f"✅ Model trained. Accuracy: {accuracy:.2f}")
    print("📦 Model saved to models/autopilot_clf.pkl")

if __name__ == "__main__":
    train()
