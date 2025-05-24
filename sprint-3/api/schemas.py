from pydantic import BaseModel
from typing import List

class DriftInput(BaseModel):
    reference: List[float]
    current: List[float]

class DriftResponse(BaseModel):
    drift_detected: bool
    details: str
