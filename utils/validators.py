import re


def clean_query(text: str) -> str:
    if not text:
        return ""
    text = text.strip()
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[\\/|<>]+", " ", text)
    return text.strip()


def is_valid_url(value: str) -> bool:
    return value.startswith(("http://", "https://"))
