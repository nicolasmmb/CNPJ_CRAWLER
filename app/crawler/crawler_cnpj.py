import re

from fastapi import status
from playwright.sync_api import Browser, Page, sync_playwright

from app.crawler.conts import (
    BASE_URL,
    DIR_BROWSER_DATA,
    ECONOMIC_ACTIVITIES,
    ECONOMIC_PATTERN,
    FIELDS,
    TEXTS_XPATH,
)
from app.crawler.utils import normalize_key, sanitize_text
from app.models.error import InfoNotFoundForCNPJ


def run_actions(page: Page, url: str) -> None:
    page.goto(url)

    page.wait_for_load_state("networkidle")

    checkbox: str = "hCaptcha. Selecione para acionar o desafio ou ignorá-lo se você tiver um cookie de acessibilidade."  # noqa
    iframe: str = 'iframe[title="Widget contendo caixa de seleção para desafio de segurança hCaptcha"]'  # noqa

    page.frame_locator(iframe).get_by_role("checkbox", name=checkbox).click()
    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(2500)
    page.get_by_role("button", name="Consultar").click()
    page.wait_for_load_state("networkidle")


def validate_correct_page(page: Page) -> None:
    if page.query_selector("div.alert-danger"):
        raise InfoNotFoundForCNPJ(
            detail="NÃO FORAM ENCONTRADAS INFORMAÇÕES PARA O CNPJ INFORMADO",
            status_code=status.HTTP_204_NO_CONTENT,
        )


def crawler_search_cnpj(cnpj):
    url_query_cnpj: str = f"{BASE_URL }?cnpj={cnpj}"

    with sync_playwright() as p:
        browser: Browser = p.firefox.launch_persistent_context(
            DIR_BROWSER_DATA,
            headless=False,
            viewport={"width": 1920 / 2.5, "height": 1080},
            devtools=True,
            timeout=59000,
        )

        page: Page = browser.new_page()

        run_actions(page, url_query_cnpj)

        validate_correct_page(page)

        texts: list[str] = []
        for item in page.query_selector_all(TEXTS_XPATH):
            text: str = item.text_content()
            text = sanitize_text(text)
            texts.append(text)

        fiels_data: dict = {}
        economic_activities: list[str] = []

        for index, text in enumerate(texts):
            if econimic_activity := re.findall(ECONOMIC_PATTERN, text):
                economic_activities.extend(econimic_activity)
                continue
            for key in FIELDS:
                if key == text:
                    fiels_data[key] = texts[index + 1]
                    continue

        fiels_data[ECONOMIC_ACTIVITIES] = economic_activities
        return {normalize_key(key): value for key, value in fiels_data.items()}
