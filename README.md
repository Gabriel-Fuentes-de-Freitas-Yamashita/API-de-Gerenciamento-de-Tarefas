# API-de-Gerenciamento-de-Tarefas

## Descrição
Esta é uma API RESTful construída com Python e FastAPI para gerenciar uma lista de tarefas. O projeto implementa todas as operações fundamentais do CRUD (Create, Read, Update, Delete) para manipular tarefas.

## Funcionalidades
A API expõe os seguintes endpoints:

* GET /tarefas: Retorna uma lista com todas as tarefas.

* POST /tarefas: Cria uma nova tarefa. A API gera o ID automaticamente.

* PUT /tarefas/{id}: Atualiza uma tarefa existente com base no seu ID.

* DELETE /tarefas/{id}: Deleta uma tarefa com base no seu ID.

## Tecnologias Utilizadas
* Python 3

* FastAPI: O framework web para a construção da API.

* Uvicorn: O servidor ASGI para rodar a aplicação.

* Pydantic: Para validação e modelagem de dados.

## Como Rodar o Projeto
Clone este repositório.

Navegue até a pasta do projeto e crie um ambiente virtual:

python -m venv venv
Ative o ambiente virtual:

# No Windows
.\venv\Scripts\activate
Instale as dependências necessárias:


pip install fastapi uvicorn[standard]
Inicie o servidor da API:

uvicorn main:app --reload
A API estará disponível em http://127.0.0.1:8000. Você pode acessar a documentação interativa em http://127.0.0.1:8000/docs.

