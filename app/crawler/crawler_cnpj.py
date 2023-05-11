import re

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
            status_code=200,
        )


def crawler_search_cnpj(cnpj):
    url_query_cnpj: str = f"{BASE_URL }?cnpj={cnpj}"

    with sync_playwright() as p:
        browser: Browser = p.firefox.launch_persistent_context(
            DIR_BROWSER_DATA,
            headless=True,
            viewport={"width": 1920 / 2.5, "height": 1080},
            devtools=True,
            timeout=59000,
        )

        page: Page = browser.new_page()

