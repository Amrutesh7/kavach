from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
from database import get_db
from services.legal_nlp_service import analyze_operation

router = APIRouter(prefix="/legal", tags=["Legal"])

@router.post("/analyze")
def legal_analysis(file: UploadFile = File(...), db: Session = Depends(get_db)):
    return analyze_operation(file, db)