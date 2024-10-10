# YouTube URL CRUD - Backend

## Descrição

Este projeto consiste em uma API que permite armazenar, listar, editar e deletar URLs de vídeos do YouTube. A API foi desenvolvida utilizando **Python**, **Django**, e **PostgreSQL** como banco de dados. O projeto também utiliza práticas de desenvolvimento, como **Testes Unitários**, **SOLID**, **Arquitetura Hexagonal**, e está **Dockerizado** para facilitar a execução em diferentes ambientes.

## Funcionalidades

- Inserir e armazenar uma URL do YouTube.
- Listar URLs armazenadas.
- Recuperar e tocar o vídeo via URL salva.
- Editar o nome e/ou a URL do vídeo.
- Deletar uma URL.
- Autenticação de usuários via **JWT** (JSON Web Token).
- Testes unitários.
- Arquitetura baseada em **SOLID** e **Hexagonal**.

## Testes Unitários

Este projeto utiliza o **pytest** para a implementação.
Para executar os testes:

```bash
pytest
```

## Pré-requisitos

- Docker e Docker Compose instalados.

## Instruções de Configuração

### 1. Clonar o repositório

```bash
git clone https://github.com/tdoval/youtube-url-crud-backend
cd youtube-url-crud-backend
```

### 2. Variáveis de Ambiente

Certifique-se de que o arquivo .env esteja configurado corretamente. Você pode usar o .env.example como modelo:

```bash
cp .env.example .env
```

Atualize as seguintes variáveis no arquivo .env:

```makefile
# .env

# Configurações do Django
SECRET_KEY=<sua_chave_secreta>

# Configurações do Banco de Dados
DB_NAME=<seu_nome_de_banco_de_dados>
DB_USER=<seu_usuario_de_banco_de_dados>
DB_PASSWORD=<sua_senha_de_banco_de_dados>
DB_HOST=<seu_host_db>
DB_PORT=<seu_port>
```

### 3 Build e Execução

Pode ser feito com Docker ou sem docker

#### 3.1 Build e execução com Docker

1. Execute o comando:

```bash
docker-compose up --build
```

Isso irá:

- Construir a imagem Docker para o backend Django.
- Configurar e executar o banco de dados PostgreSQL dentro de um contêiner Docker.
- Executar o servidor Django.

2. Executar Migrações

Após os serviços estarem em execução, você precisará rodar as migrações do Django para criar as tabelas necessárias no banco de dados PostgreSQL:

```bash
docker-compose exec web python manage.py migrate
```

3. Acessar o Backend

Uma vez que os contêineres estiverem em execução, o backend estará disponível em:

```bash
http://localhost:8000
```

4. Testar o Backend

Depois de executar o backend, você pode testar sua funcionalidade utilizando ferramentas como Postman ou cURL, direcionando para `http://localhost:8000` para fazer requisições à API.

5. Parar os Contêineres

Para parar os contêineres em execução:

```bash
docker-compose down
```

Isso irá parar e remover os contêineres, mas seus dados de banco de dados serão persistidos no volume do Docker.

#### 3.2 Como rodar o projeto localmente, sem Docker

1. Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate      # Windows
```

2. Instale as dependências

```bash
pip install -r requirements.txt
```

3. Execute as migrações do banco de dados

```bash
python manage.py migrate
```

4. O servidor estará disponível em `http://localhost:8000`

## Melhorias Futuras

1. Implementação de Cache

- Melhorar a performance utilizando um sistema de cache (como Redis) para armazenar respostas de URLs frequentemente acessadas ou dados que não mudam com frequência.

2. Paginação e Busca Otimizadas

- Busca eficiente e paginação nas listas de URLs, principalmente se o volume de dados crescer.

3. Monitoramento e Logs Avançados

- Integrar uma ferramenta de monitoramento e logs (como ELK Stack, Grafana, ou Prometheus)

4. Rate Limiting e Proteção contra Abuso

- Rate limiting por usuário ou IP

5. Melhoria na Validação das URLs do YouTube

- Implementar uma validação mais robusta das URLs do YouTube

6. Deploy Automatizado com CI/CD

- Automatizar o processo de deploy utilizando pipelines de CI/CD

7. Documentação da API

- Ferramentas como Swagger ou Redoc

8. Teste de Performance e Stress Testing

- testar como o sistema se comporta sob carga (Locust ou JMeter)
