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


def get_by_query(element: ElementHandle, query: str) -> str:
    text: ElementHandle | None = element.query_selector(query)
    if text:
        text: str = text.text_content()

    text = sanitize_text(text)

    return text


def get_list_by_query(element: ElementHandle, query: str, subquery: str) -> list[str]:
    tables: list[ElementHandle] = element.query_selector_all(query)
    texts: list[str] = []
    for item in tables:
        rows: list[ElementHandle] = item.query_selector_all(subquery)
        texts.extend(sanitize_text(row.text_content()) for row in rows)
    return texts
