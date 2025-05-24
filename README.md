# Sprint 1: Transaction Fraud Classifier (Minimal Working Pipeline)

This is the first sprint of the **OpsPilot-AI** project, focused on building a minimal working ML pipeline with schema validation, model training, inference, and testing.

---

## ✅ Components

### 1. `scripts/generate_sample_data.py`
- Generates dummy transaction data with complete schema.
- Fields: `transaction_id`, `user_id`, `amount`, `timestamp`, `age`, `income`, `transaction_count`, `fraud_flag`.

### 2. `pipelines/training/train_model.py`
- Loads CSV data.
- Verifies required columns.
- Trains a simple `RandomForestClassifier`.
- Saves model to `models/autopilot_clf.pkl` using `joblib`.

### 3. `pipelines/inference/predict.py`
- Defines `TransactionInput` Pydantic model.
- Accepts input → converts to DataFrame → returns prediction from saved model.

### 4. `tests/test_inference.py`
- Unit test for `predict()` function using sample input.
- Verifies correct prediction structure.

---

## 🧪 To Run Locally

### Install dependencies
```bash
pip install -r requirements.txt
