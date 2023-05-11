from dataclasses import dataclass, field

from fastapi import HTTPException


@dataclass
class InfoNotFoundForCNPJ(HTTPException):
    detail: str = "CNPJ not found"
    status_code: int = 204
    headers: dict[str, str] = field(default_factory=dict)


@dataclass
class ProblemOnDecode(HTTPException):
    detail: str = "Problem on decode"
    status_code: int = 500
    headers: dict[str, str] = field(default_factory=dict)
