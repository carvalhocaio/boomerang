# Boomerang

Boomerang é um projeto Django para gerenciar receitas e pagamentos.

## Configuração

### Pré-requisitos

- Python 3.11
- Django 5.1.4
- Outros pacotes listados em `requirements.txt`

### Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/carvalhocaio/boomerang
    cd boomerang
    ```

2. Crie e ative um ambiente virtual:
    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

4. Configure as variáveis de ambiente:
    - Copie o arquivo `.env-sample` para `.env` e ajuste os valores conforme necessário.

5. Execute as migrações do banco de dados:
    ```sh
    python manage.py migrate
    ```

6. Inicie o servidor de desenvolvimento:
    ```sh
    make run
    ```

## Comandos Úteis

- Para rodar o servidor:
    ```sh
    make run
    ```

- Para verificar o linting:
    ```sh
    make lint
    ```

- Para formatar o código:
    ```sh
    make format
    ```

## Estrutura do Banco de Dados

O projeto possui dois modelos principais:

- `Income`: Representa uma receita com campos como valor, data, descrição e origem.
- `Payment`: Representa um pagamento com campos como nome, valor, data de vencimento, status de pagamento e data de pagamento.

---
