
# 🧠 OpsPilot-AI

> **A Production-Grade MLOps System** — Built for resilience, modularity, and real-time drift detection across the ML lifecycle.

---

## 🚀 Overview

`OpsPilot-AI` is a lightweight, end-to-end MLOps + AIOps platform designed to simulate and monitor machine learning pipelines in production. Built with modular sprints, this system combines:

- Model Training & Inference APIs
- Distributional & Performance Drift Detection
- FastAPI Microservices
- High Availability Principles
- Interview Pain Point Solutions Embedded ✨

---

## ✅ Sprint Summary

| Sprint | Features |
|--------|----------|
| **Sprint-1** | 🔧 Model Training, Inference API (FastAPI) with structured error handling |
| **Sprint-3** | 📊 PSI-based Drift Detection API for prediction distribution monitoring |
| **Sprint-4** | 📉 Model Performance Drift Monitor using statistical baselining & versioning |
| *(Sprint-2 skipped)* | *(Merged directly into later sprints for productivity)* |

> 💡 Interview Questions & Pain Points handled are embedded in each sprint module as inline comments and README snippets.

---

## 🛠️ Tech Stack

- `FastAPI`, `Uvicorn`
- `scikit-learn`, `joblib`, `pandas`
- `pydantic`, `PSI`, `json-logging`
- Designed to run on **WSL/Kubernetes-lite + Docker Desktop-free setups**

---

## 🧪 Running Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run model inference API (Sprint-1)
PYTHONPATH=. uvicorn sprint-1/api/main:app --reload

# Run PSI Drift API (Sprint-3)
PYTHONPATH=. uvicorn sprint-3/api/psi_drift:app --reload





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


## 🚀 Dockerized Deployment

We provide a pre-built Docker image with all Sprint-6 and Sprint-8 features integrated:

```bash
docker pull santy1504/opspilot-ai-1:v0.8.0
docker run -it --rm -p 8000:8000 santy1504/opspilot-ai-1:v0.8.0

