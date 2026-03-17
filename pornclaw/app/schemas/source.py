from pydantic import BaseModel, HttpUrl


class SourceIngestRequest(BaseModel):
    source_url: str


class SourceIngestResponse(BaseModel):
    session_id: int
    status: str
    raw_items_count: int
    series_count: int
    error_message: str | None = None
