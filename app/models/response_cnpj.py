from pydantic import BaseModel


class ResponseCNPJ(BaseModel):
    numero_de_inscricao: str
    data_de_abertura: str
    nome_empresarial: str
    titulo_do_estabelecimento_nome_de_fantasia: str
    codigo_e_descricao_da_natureza_juridica: str
    logradouro: str
    numero: str
    complemento: str
    cep: str
    bairro_distrito: str
    municipio: str
    uf: str
    endereco_eletronico: str
    telefone: str
    ente_federativo_responsavel_efr: str
    situacao_cadastral: str
    data_da_situacao_cadastral: str
    motivo_de_situacao_cadastral: str
    situacao_especial: str
    data_da_situacao_especial: str
    atividade_economica_principal_e_secundarias: list[str]
