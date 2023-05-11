from playwright.sync_api import ElementHandle
from unidecode import unidecode


def sanitize_text(text: str) -> str:
    if isinstance(text, str):
        text = text.replace("\n", "")
        text = text.replace("\t", "")
        text = text.replace("\r", "")
        text = text.replace("  ", "")
        return text.strip()

    return text


def normalize_key(text: str) -> str:
    text: str = text.strip()
    text = text.lower()
    text = text.replace(" ", "_")
    text = text.replace("/", "_")
    text = text.replace("-", "_")
    text = text.replace("(", "")
    text = text.replace(")", "")
    text = text.replace(".", "")
    text = text.replace(",", "")

    return unidecode(text)
