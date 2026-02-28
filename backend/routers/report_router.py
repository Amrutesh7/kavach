from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from services.report_summarizer_service import generate_intelligence_report

router = APIRouter(prefix="/report", tags=["Intelligence Report"])

@router.get("/summary")
def intelligence_summary(db: Session = Depends(get_db)):
    return generate_intelligence_report(db)