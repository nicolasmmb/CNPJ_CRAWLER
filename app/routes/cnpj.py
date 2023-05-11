from fastapi import APIRouter

from app.crawler.crawler_cnpj import crawler_search_cnpj
from libs.validators import CNPJ

app = APIRouter(
    tags=["CNPJ"],
)


@app.get("/consultar")
def info(cnpj: CNPJ) -> dict:
    cnpj_info: dict = crawler_search_cnpj(cnpj=cnpj)

    return cnpj_info
