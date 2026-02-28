from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from services.logistics_service import analyze_logistics

router = APIRouter(prefix="/logistics", tags=["Logistics"])

@router.get("/analyze")
def logistics_analysis(db: Session = Depends(get_db)):
    return analyze_logistics(db)