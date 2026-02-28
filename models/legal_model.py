from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey
from database import Base

class LegalFramework(Base):
    __tablename__ = "legal_frameworks"

    id = Column(Integer, primary_key=True, index=True)
    law_name = Column(String(200))
    jurisdiction = Column(String(100))
    domain = Column(String(50))
    description = Column(Text)
    severity_level = Column(Integer)


class LegalKeywordMapping(Base):
    __tablename__ = "legal_keyword_mapping"

    id = Column(Integer, primary_key=True, index=True)
    keyword = Column(String(100))
    mapped_law_id = Column(Integer, ForeignKey("legal_frameworks.id"))
    risk_weight = Column(Float)