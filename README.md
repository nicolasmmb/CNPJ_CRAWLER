# :scroll: Documentação :scroll:
# Instruções
Sigam as instruções abaixo para realizar rodar o projeto corretamente.

## Instalação
1. Instale o Python 3.11.2
   > Recomendo o uso do [PYENV](https://dev.to/womakerscode/instalando-o-python-com-o-pyenv-2dc7)

2. instale o Poetry com o comando:
   ```bash
    pip install poetry
    ```

3. Instale as dependências do projeto com o comando:
   ```bash
   # Cria o ambiente virtual no projeto
   poetry config virtualenvs.in-project true   
   ```
   ```bash
   # Instala as dependências de Produção
    poetry install --only=prod
    ```
   ```bash
   # Opcional - Instala as dependências de Desenvolvimento
    poetry install --with=prod,dev 
    ```

4. Ative o ambiente virtual com o comando:
   ```bash
    poetry shell
    ```

5. Rode instale o navegadores com o comando:
   ```bash
   playwright install firefox
   ```

6. Rode o projeto com o comando:
   ```bash
   python main.py
   ```

