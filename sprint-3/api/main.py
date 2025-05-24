from fastapi import FastAPI
from .routes import router

app = FastAPI(title="OpsPilot-AI Drift Monitoring API", version="0.3.0")

app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Welcome to OpsPilot-AI Drift Monitoring API"}
