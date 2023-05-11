from pathlib import Path
from typing import Final

FIELDS: Final[set[str]] = {
    "TÍTULO DO ESTABELECIMENTO (NOME DE FANTASIA)",
    "NÚMERO DE INSCRIÇÃO",
    "DATA DE ABERTURA",
    "NOME EMPRESARIAL",
    "LOGRADOURO",
    "NÚMERO",
    "COMPLEMENTO",
    "CEP",
    "BAIRRO/DISTRITO",
    "MUNICÍPIO",
    "UF",
    "ENDEREÇO ELETRÔNICO",
    "TELEFONE",
    "ENTE FEDERATIVO RESPONSÁVEL (EFR)",
    "SITUAÇÃO CADASTRAL",
    "DATA DA SITUAÇÃO CADASTRAL",
    "MOTIVO DE SITUAÇÃO CADASTRAL",
    "SITUAÇÃO ESPECIAL",
    "DATA DA SITUAÇÃO ESPECIAL",
    "MOTIVO DA SITUAÇÃO CADASTRAL",
    "CÓDIGO E DESCRIÇÃO DA NATUREZA JURÍDICA",
}

ECONOMIC_ACTIVITIES: Final[set[str]] = "ATIVIDADE ECONÔMICA PRINCIPAL E SECUNDÁRIAS"

DIR_BROWSER_DATA: Path = Path(__file__).parent.parent / "browser_data"

BASE_URL: Final[
    str
] = "https://solucoes.receita.fazenda.gov.br/Servicos/cnpjreva/cnpjreva_solicitacao.asp"

# pattern to find the Pattern: 00.00-0-00 - Any text
ECONOMIC_PATTERN = r"\d{2}\.\d{2}-\d-\d{2}\s-\s.*$"

BASE_XPATH: str = "//*[@id='principal']"
TEXTS_XPATH: str = f"{BASE_XPATH}/table/tbody/tr/td/table/tbody/tr/td/font"
