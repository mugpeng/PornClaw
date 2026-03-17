import re


def slugify_title(value: str) -> str:
    cleaned = re.sub(r"chapter\s*\d+|episode\s*\d+", "", value, flags=re.IGNORECASE)
    cleaned = re.sub(r"[^a-zA-Z0-9\u4e00-\u9fff]+", " ", cleaned)
    return re.sub(r"\s+", " ", cleaned).strip().lower()


def split_tags(value: str | list[str] | None) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [item.strip() for item in value if item and item.strip()]
    return [item.strip() for item in re.split(r"[,/|#]+", value) if item.strip()]
