from fastapi import APIRouter

from app.crawler.crawler_cnpj import crawler_search_cnpj
from app.models.error import ProblemOnDecode
from app.models.response_cnpj import ResponseCNPJ
from libs.validators import CNPJ

app = APIRouter(
    tags=["CNPJ"],
)


@app.get("/consultar")
def info(cnpj: CNPJ) -> ResponseCNPJ:
    cnpj_info: dict = crawler_search_cnpj(cnpj=cnpj)

    try:
        return ResponseCNPJ(**cnpj_info)

    except Exception as e:
        ProblemOnDecode(
            detail=f"Problem on decode: {e}",
            status_code=500,
        )
