# :scroll: Documentação :scroll:
# Instruções
Sigam as instruções abaixo para rodar o projeto corretamente.

## Instalação
1. Instale o Python 3.11
   > Recomendo o uso do [PYENV](https://dev.to/womakerscode/instalando-o-python-com-o-pyenv-2dc7)
   - Caso não tenha a versão 3.11 instalada, ao instalar as dependências do projeto, o Poetry irá bloquear a instalação das dependências.
   Para resolver, basta instalar a versão 3.11

2. Instalação Simplificada
   ```bash
   # Execute no terminal em alguma distribuicão Linux - De Preferência Ubuntu

   make install
   ```

3. Rodando o projeto
   ```bash
   # Execute no terminal em alguma distribuicão Linux - De Preferência Ubuntu

   make run
   ```

---
## Instalação Manual
1. Instale o Poetry com o comando:
   ```bash
    pip install poetry
   ```

2. Instale as dependências do projeto com o comando:
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

3. Ative o ambiente virtual com o comando:
   ```bash
    poetry shell
    ```

4. Rode instale o navegadores com o comando:
   ```bash
   playwright install firefox
   ```

5. Rode o projeto com o comando:
   ```bash
   python main.py
   ```

