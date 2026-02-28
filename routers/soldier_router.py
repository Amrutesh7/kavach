from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from services.soldier_ai_service import get_all_soldiers_with_risk

router = APIRouter(prefix="/soldiers", tags=["Soldiers"])

@router.get("/")
def fetch_soldiers(db: Session = Depends(get_db)):
    return get_all_soldiers_with_risk(db)