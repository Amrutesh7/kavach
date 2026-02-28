from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from services.cdr_graph_service import analyze_cdr_network

router = APIRouter(prefix="/cdr", tags=["CDR"])

@router.get("/analyze")
def analyze_cdr(db: Session = Depends(get_db)):
    return analyze_cdr_network(db)