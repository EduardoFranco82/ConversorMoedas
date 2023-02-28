# ConversorMoedas API

Construção de uma API para conversão de valores monetários. 
Valores aceitos : USD BRL EUR BTC ETH

Inserindo dois valores de moedas monetárias listados acima, acrescentando o valor a ser transformado,
a API retorna a conversão.

Motivação de construir a API com  FastAPI.
Framework assíncrono, que permite com sua documentação Swagger fazer as requisições requeridas.


## Pré-requisitos

- Python 3.9: `https://www.python.org/downloads/`
- Docker: `https://www.docker.com/`
- Criação do ambiente virtual: `https://docs.python.org/pt-br/3/library/venv.html`


## Necessário

Criar um arquivo `.secrets.toml` dentro do diretório app/.
Estrutura do arquivo:

[default]\
API_KEY = "" \
Valor enviado por email

### Rodar via containeer Docker
- Ativação do Docker
    - `docker build -t micro-python .`
    - `docker run -it micro-python`
    

- Ativação do Docker-compose
    - `docker-compose build`
    - `docker-compose up -d`

- Acessar url 
   - `http://127.0.0.1/docs` 

### Rodar localmente

- Ativação do ambiente virtual:
  - `$ source ./venv/bin/activate`
- Instalar todas as dependências necessárias:
  - `$ pip install -r requirements_dev.txt`
- Rodar no terminal:
    - `uvicorn app.main:app --host 0.0.0.0 --port 8081`


### Rodar test

    - pytest -v


