from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import json

from auth.dependencies import get_current_user
from db.database import get_db
from db.models import ResearchResult
from scraping.service import scrape_website
from scraping.extractor import extract_all
from llm.gemini import generate_structured_output

router = APIRouter(
    prefix="/research",
    tags=["Research"]
)


@router.post("/")
def research_website(
    payload: dict,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    website_url = payload.get("website_url")
    if not website_url:
        raise HTTPException(status_code=400, detail="website_url is required")

    # 1. Scrape website
    pages = scrape_website(website_url)

    # 2. Extract contacts
    extracted = extract_all(pages)

    # 3. Generate structured output (LLM or fallback)
    try:
        structured = generate_structured_output(
            website=website_url,
            pages=pages,
            extracted=extracted
        )
    except Exception:
        structured = {
            "company_name": website_url,
            "website": website_url,
            "summary": "LLM unavailable",
            "emails": extracted.get("emails", []),
            "phone_numbers": extracted.get("phones", []),
            "socials": extracted.get("socials", []),
            "sources": [p["url"] for p in pages]
        }

    # 4. Save to DB — ONLY result_json
    db_entry = ResearchResult(
        website=website_url,
        result_json=json.dumps(structured)
    )

    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)

    return {
        "id": db_entry.id,
        "website": website_url,
        "structured_result": structured
    }
