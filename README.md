# Como Funciona Uma API: Métodos HTTP e Seus Status Codes

Neste vídeo, eu explico como funcionam os métodos e status codes HTTP mais comuns utilizados em APIs, com uma aplicação prática desenvolvida em FastAPI. A aplicação simula uma API de produtos, permitindo operações básicas como listar todos os produtos (**GET**), criar um novo produto (**POST**), atualizar um produto existente (**PUT**) e remover um produto (**DELETE**). Além disso, demonstro o comportamento dos principais status codes HTTP, como o **200 OK** para requisições bem-sucedidas, **201 Created** para recursos criados com sucesso, **400 Bad Request** para requisições inválidas e **500 Internal Server Error**, simulando erros internos do servidor. Esse conteúdo é perfeito para quem deseja entender os fundamentos de APIs de forma prática e didática.

Esta aplicação em FastAPI simula uma API de produtos, permitindo executar operações básicas como:

- **GET**: Listar todos os produtos.
- **POST**: Criar um novo produto.
- **PUT**: Atualizar um produto existente.
- **DELETE**: Remover um produto.

A aplicação também demonstra o funcionamento dos seguintes **Status Codes HTTP**:

- **200 OK**: Requisição bem-sucedida.
- **201 Created**: Recurso criado com sucesso.
- **400 Bad Request**: Requisição inválida, geralmente devido a dados ausentes ou incorretos.
- **500 Internal Server Error**: Erro interno simulado para demonstração.

<!--
https://www.youtube.com/@renato-coelho
-->

## Apresentação em vídeo

<p align="center">
  <a href="https://youtu.be/viE7zOKoFOU" target="_blank"><img src="imagens/thumbnail/metodos-status-codes-http.png" alt="Vídeo de apresentação"></a>
</p>

### Requisitos

+ ![Docker](https://img.shields.io/badge/Docker-23.0.3-E3E3E3)

+ ![Docker-compose](https://img.shields.io/badge/Docker--compose-1.25.0-E3E3E3)

+ ![Git](https://img.shields.io/badge/Git-2.25.1%2B-E3E3E3)

+ ![Ubuntu](https://img.shields.io/badge/Ubuntu-20.04-E3E3E3)

## Métodos HTTP Implementados

### **GET /produtos**

Retorna a lista de todos os produtos.

#### Exemplo de Resposta (200):
```json
[
    {
        "id": 1,
        "nome": "Produto A",
        "descricao": "Descrição do Produto A"
    },
    {
        "id": 2,
        "nome": "Produto B",
        "descricao": "Descrição do Produto B"
    }
]
```

### **POST /produtos**

Cria um novo produto.

#### Parâmetros:
- `nome` (string): Nome do produto.
- `descricao` (string): Descrição do produto.

#### Exemplo de Resposta (201):
```json
{
    "id": 3,
    "nome": "Produto C",
    "descricao": "Descrição do Produto C"
}
```

### **PUT /produtos/{produto_id}**

Atualiza as informações de um produto existente.

#### Parâmetros:

- `produto_id` (int): ID do produto.
- `nome` (string): Nome atualizado.
- `descricao` (string): Descrição atualizada.

#### Exemplo de Resposta (200):
```json
{
    "id": 1,
    "nome": "Produto A Atualizado",
    "descricao": "Descrição do Produto A Atualizada"
}
```

### **DELETE /produtos/{produto_id}**

Remove um produto pelo ID.

#### Parâmetros:

- `produto_id` (int): ID do produto a ser removido.

#### Exemplo de Resposta (200):

```json
{
    "mensagem": "Produto deletado com sucesso."
}
```

### **GET /simular-erro-500**

Simula um erro interno do servidor.

#### Exemplo de Resposta (500):

```json
{
    "detail": "Erro interno do servidor simulado."
}
```

## Executando a Aplicação com Docker Compose

### Passos

1. Clone este repositório:
   ```bash
   git clone https://github.com/Renatoelho/metodos-status-codes.git metodos-status-codes
   cd metodos-status-codes
   ```

2. Ative Aplicação:
   ```bash
   docker compose -p api-aula -f docker-compose.yaml up -d --build
   ```

3. Acesse a documentação interativa da API no navegador:
   [http://localhost:8000/docs](http://localhost:8000/docs)

### Finalizando Aplicação

Para parar os containers, pressione `Ctrl+C` ou execute:

```bash
docker compose -p api-aula -f docker-compose.yaml down
```

### Referências

Request Methods, ***datatracker***. Disponível em: <https://datatracker.ietf.org/doc/html/rfc7231#section-4>. Acesso em: 31 Dez. 2024.

Métodos de requisição HTTP, ***developer.mozilla.org***. Disponível em: <https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Methods>. Acesso em: 31 Dez. 2024.

Lista de códigos de estado HTTP, ***Wikipedia***. Disponível em: <https://pt.wikipedia.org/wiki/Lista_de_c%C3%B3digos_de_estado_HTTP>. Acesso em: 31 Dez. 2024.
