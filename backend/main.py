from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from auth.routes import router as auth_router
from api.research import router as research_router
from api.history import router as history_router
from db.database import engine
from db import models

app = FastAPI(
    title="Internal Website Intelligence & Contact Discovery Tool"
)

# ✅ CORS FIX (THIS IS THE KEY)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create DB tables
models.Base.metadata.create_all(bind=engine)

# Routers
app.include_router(auth_router)
app.include_router(research_router)
app.include_router(history_router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
