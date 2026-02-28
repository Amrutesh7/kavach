from sqlalchemy.orm import Session
from models.legal_model import LegalFramework, LegalKeywordMapping
from fastapi import UploadFile
from PyPDF2 import PdfReader
from docx import Document
import io


def extract_text_from_file(file: UploadFile):

    content = file.file.read()

    if file.filename.endswith(".pdf"):
        reader = PdfReader(io.BytesIO(content))
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text

    elif file.filename.endswith(".docx"):
        document = Document(io.BytesIO(content))
        return "\n".join([para.text for para in document.paragraphs])

    else:
        return ""


def analyze_operation(file: UploadFile, db: Session):

    text = extract_text_from_file(file)

    if not text:
        return {"error": "Could not extract text"}

    text = text.lower()

    mappings = db.query(LegalKeywordMapping).all()

    matched_laws = []
    total_risk_score = 0

    for mapping in mappings:
        keyword = mapping.keyword.lower()

        if keyword in text:
            law = db.query(LegalFramework).filter(
                LegalFramework.id == mapping.mapped_law_id
            ).first()

            if law:
                matched_laws.append({
                    "law_name": law.law_name,
                    "jurisdiction": law.jurisdiction,
                    "domain": law.domain,
                    "description": law.description,
                    "severity_level": law.severity_level,
                    "trigger_keyword": keyword
                })

                total_risk_score += mapping.risk_weight

    # Risk classification
    if total_risk_score < 2:
        risk_level = "FULLY COMPLIANT"
    elif total_risk_score < 5:
        risk_level = "REQUIRES LEGAL REVIEW"
    else:
        risk_level = "HIGH RISK OF VIOLATION"

    return {
        "matched_laws": matched_laws,
        "total_risk_score": round(total_risk_score, 2),
        "risk_classification": risk_level
    }