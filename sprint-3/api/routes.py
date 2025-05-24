from fastapi import APIRouter
from .schemas import DriftInput, DriftResponse
from monitoring.drift import check_drift

router = APIRouter()

@router.post("/check-drift", response_model=DriftResponse)
def detect_drift(data: DriftInput):
    result = check_drift(data.reference, data.current)
    return DriftResponse(**result)
