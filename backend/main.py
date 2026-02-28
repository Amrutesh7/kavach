from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
import os
from dotenv import load_dotenv

from routers.soldier_router import router as soldier_router
from routers.cdr_router import router as cdr_router
from routers.logistics_router import router as logistics_router
from routers.legal_router import router as legal_router
from routers.report_router import router as report_router

load_dotenv()

app = FastAPI()

# ✅ CORS FIX
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Session Middleware
app.add_middleware(
    SessionMiddleware,
    secret_key=os.getenv("SECRET_KEY")
)

app.include_router(soldier_router)
app.include_router(cdr_router)
app.include_router(logistics_router)
app.include_router(legal_router)
app.include_router(report_router)

@app.get("/")
def root():
    return {"message": "IDC Backend Connected to Supabase"}