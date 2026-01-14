from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import json

from db.database import get_db
from db.models import ResearchResult
from auth.dependencies import get_current_user

router = APIRouter(
    prefix="/history",
    tags=["History"]
)


@router.get("/")
def get_history(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    results = db.query(ResearchResult).order_by(
        ResearchResult.created_at.desc()
    ).all()

    response = []
    for r in results:
        data = json.loads(r.result_json)
        response.append({
            "id": r.id,
            "website": r.website,
            "company_name": data.get("company_name"),
            "created_at": r.created_at
        })

    return response


@router.get("/{research_id}")
def get_history_by_id(
    research_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    r = db.query(ResearchResult).filter(
        ResearchResult.id == research_id
    ).first()

    if not r:
        raise HTTPException(status_code=404, detail="Record not found")

    return {
        "id": r.id,
        "website": r.website,
        "result": json.loads(r.result_json),
        "created_at": r.created_at
    }
