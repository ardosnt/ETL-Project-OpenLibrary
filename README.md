# ETL-Project-OpenLibrary

Pipeline de ETL (Extract, Transform, Load) que consome a API pública do [Open Library](https://openlibrary.org/), trata os dados com Pandas e carrega o resultado em um banco PostgreSQL.

## 🎯 O que o projeto faz

O pipeline busca livros por assunto na API do Open Library (por padrão, o assunto **"cinema"**), limpa e estrutura os dados relevantes e os persiste em uma tabela PostgreSQL, pronta para consultas e análises.

## 🛠️ Tecnologias

- **Python 3**
- **Requests** — consumo da API do Open Library
- **Pandas** — transformação e limpeza dos dados
- **SQLAlchemy + psycopg** — conexão e carga no PostgreSQL
- **python-dotenv** — gerenciamento de variáveis de ambiente
- **Docker / Docker Compose** — sobe o banco PostgreSQL localmente

## 📂 Estrutura do projeto

```
ETL-Project-OpenLibrary/
├── extract.py                 # Extração dos dados da API do Open Library
├── transform.py                # Limpeza e transformação dos dados com Pandas
├── load.py                     # Carga dos dados no PostgreSQL
├── main.py                     # Orquestra o pipeline (extract → transform → load)
├── transform_in_notebook.ipynb # Notebook para explorar as transformações
├── docker-compose.yml          # Sobe o container do PostgreSQL
├── .env.example                # Modelo das variáveis de ambiente
└── .gitignore
└── requirements

```

## 🔄 Como o pipeline funciona

1. **Extract** (`extract.py`)
   Faz uma requisição à API do Open Library no formato `subjects/{assunto}.json` (ex.: `subjects/cinema.json`) e retorna o JSON bruto.

2. **Transform** (`transform.py`)
   Converte o JSON em um DataFrame do Pandas, seleciona as colunas relevantes (`key`, `title`, `first_publish_year`, `edition_count`, `authors`), extrai o nome do primeiro autor de cada obra e limpa o campo `key` (removendo o prefixo `/works/`).

3. **Load** (`load.py`)
   Carrega o DataFrame tratado em uma tabela do PostgreSQL (por padrão `tb_livros_cinema`), substituindo a tabela existente a cada execução.

4. **main.py**
   Orquestra as três etapas em sequência, executando o pipeline de ponta a ponta.

## 🚀 Como rodar o projeto

### Pré-requisitos

- Python 3.10+
- Docker e Docker Compose

### 1. Clone o repositório

```bash
git clone https://github.com/ardosnt/ETL-Project-OpenLibrary.git
cd ETL-Project-OpenLibrary
```

### 2. Configure as variáveis de ambiente

Copie o arquivo de exemplo e preencha com suas credenciais:

```bash
cp .env.example .env
```

### 3. Suba o banco de dados PostgreSQL

```bash
docker-compose up -d
```

O banco ficará disponível em `localhost:5433`.

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

> 💡 Se o repositório tiver um `requirements.txt`, use `pip install -r requirements.txt` no lugar do comando acima.

### 5. Execute o pipeline

```bash
python main.py
```

Ao final, os dados estarão disponíveis na tabela configurada dentro do PostgreSQL.

## 📋 Variáveis de ambiente

| Variável | Descrição |
|---|---|
| `POSTGRES_USER` | Usuário do banco PostgreSQL |
| `POSTGRES_PASSWORD` | Senha do banco PostgreSQL |
| `POSTGRES_DB` | Nome do banco de dados |

## 📓 Notebook

O arquivo `transform_in_notebook.ipynb` pode ser usado para explorar e testar as transformações dos dados de forma interativa, antes de rodar o pipeline completo.

