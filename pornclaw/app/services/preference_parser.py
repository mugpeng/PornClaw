from app.config import settings
from app.services.normalize import normalize_tags


def parse_free_text_intent(text: str | None) -> dict:
    if not text:
        return {"freshness_preference": None, "soft_preference_tags": [], "must_avoid_tags": []}
    lowered = text.lower()
    freshness = None
    for key, words in settings.freshness_keywords.items():
        if any(word.lower() in lowered for word in words):
            freshness = key
            break
    avoid_terms = []
    if "不要" in text or "avoid" in lowered or "no " in lowered:
        avoid_terms = normalize_tags([text])
    preferred = normalize_tags([text])
    return {
        "freshness_preference": freshness,
        "soft_preference_tags": preferred,
        "must_avoid_tags": avoid_terms,
    }
