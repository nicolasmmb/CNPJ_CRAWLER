from dataclasses import dataclass

from fastapi import HTTPException


@dataclass
class InfoNotFoundForCNPJ(HTTPException):
    detail: str = "CNPJ not found"
    status_code: int = 404
