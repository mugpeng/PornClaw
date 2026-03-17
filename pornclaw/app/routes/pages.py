import json

from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.config import settings
from app.db import get_db
from app.services.ingest import AppError, ingest_source
from app.services.profile import create_or_update_profile


router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
def index(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        request,
        "index.html",
        {"tag_options": settings.standard_tags, "demo_url": "demo://seed"},
    )


@router.post("/start", response_class=HTMLResponse)
def start_flow(
    request: Request,
    source_url: str = Form(...),
    liked_tags: list[str] = Form(default=[]),
    disliked_tags: list[str] = Form(default=[]),
    free_text_intent: str = Form(default=""),
    db: Session = Depends(get_db),
):
    try:
        session = ingest_source(db, source_url)
        create_or_update_profile(db, session.id, liked_tags, disliked_tags, free_text_intent)
        return RedirectResponse(f"/candidate-feedback/{session.id}", status_code=303)
    except AppError as exc:
        return templates.TemplateResponse(
            request,
            "error.html",
            {"message": str(exc), "back_path": "/"},
            status_code=400,
        )
