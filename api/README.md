# Helpdesk API

## Instalação e Configuração

### 1. Criar o ambiente virtual
```bash
py -m venv env
```

### 2. Ativar o ambiente
- **Windows**: `env\Scripts\activate`
- **Linux/macOS**: `source env/bin/activate`

### 3. Instalar as dependências
```bash
pip install -r requirements.txt
```

### 4. (Opcional) Salvar as dependências instaladas
```bash
pip freeze > requirements.txt
```

### 5. Configurar as variáveis do banco de dados (opcional)
```bash
cp .env.example .env
```

### 6. Criar o banco de dados e aplicar migrações
```bash
alembic upgrade head
```

### 7. Desativar o ambiente virtual
```bash
deactivate
```

## Fluxo de Desenvolvimento

Para começar com o projeto em uma máquina zerada:

```bash
# 1. Criar e ativar o ambiente virtual
py -m venv env
# Windows: env\Scripts\activate
# Linux/macOS: source env/bin/activate

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Configurar banco de dados (ajuste as credenciais)
cp .env.example .env

# 4. Criar tabelas no banco
alembic upgrade head

# 5. Executar o servidor
uvicorn app.main:app --reload
```

## Executando a Aplicação

### Comando padrão
```bash
uvicorn app.main:app --reload
```

### Ou execute diretamente
```bash
python -m app.main
```

A API será executada em `http://localhost:8000`

### Endpoints de verificação

- `GET /` - Página inicial
- `GET /health` - Status da aplicação

## Configuração do Banco de Dados

O projeto utiliza MySQL com SQLAlchemy e Alembic para migrações.

### Variáveis de ambiente necessárias (.env):
- `DATABASE_URL`: URL de conexão com MySQL (ex: `mysql+pymysql://user:password@localhost:3306/helpdesk_db`)
- Outras configurações: `APP_NOME`, `AMBIENTE`, etc.

## Estrutura do Projeto

- `app/` - Código da aplicação principal
  - `app/main.py` - Ponto de entrada FastAPI
  - `app/core/` - Configurações e utilitários
  - `app/models/` - Modelos SQLAlchemy
  - `app/controllers/` - Controladores de requisições
  - `app/repositories/` - Repositórios de dados
- `alembic/` - Migrações do banco de dados
- `uploads/` - Arquivos de anexo (se usado)
- `requirements.txt` - Dependências do projeto
- `.env.example` - Exemplo de arquivo .env
