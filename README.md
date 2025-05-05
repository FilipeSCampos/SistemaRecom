# Music Recommender API

Um sistema de recomendação musical baseado em FastAPI, com múltiplas estratégias de recomendação: baseada em conteúdo, colaborativa, híbrida, popularidade e por gênero/artista.

## Como rodar o projeto

### 1. Clone o repositório

```sh
git clone <url-do-repositorio>
cd SistemaRecom
```

### 2. Crie o ambiente virtual e instale as dependências

```sh
python -m venv venv
# Ative o venv:
# No Windows:
.\venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Execute o servidor

```sh
# No diretório principal do projeto (onde está main.py):
uvicorn app.main:app --reload
```

A API estará disponível em: http://127.0.0.1:8000

Acesse a documentação interativa em: http://127.0.0.1:8000/docs

---

## Como testar cada endpoint da API

Use a interface `/docs` (Swagger UI) ou ferramentas como `curl` ou Postman.

### 1. Content-Based Recommendation

- **GET** `/recommendations/content-based/{song_title}?limit=5`
  - Exemplo: `/recommendations/content-based/Loca?limit=5`
  - Parâmetros opcionais: `limit` (1-5), `weights` (via query string, dicionário de features)
- **POST** `/recommendations/content-based/`
  - Body exemplo:
    ```json
    {
      "song_title": "Loca",
      "limit": 5,
      "weights": {
        "Beats.Per.Minute": 1,
        "Energy": 0.5,
        "Danceability": 2
      }
    }
    ```

### 2. Collaborative Recommendation

- **GET** `/recommendations/collaborative/{user_id}`
  - Exemplo: `/recommendations/collaborative/user1`

### 3. Hybrid Recommendation

- **POST** `/recommendations/hybrid`
  - Body exemplo:
    ```json
    {
      "song_title": "Loca",
      "user_id": "user1",
      "content_weight": 0.7,
      "collab_weight": 0.3,
      "limit": 5
    }
    ```

### 4. Popular Recommendation

- **GET** `/recommendations/popular?year=2010&genre=dance%20pop&limit=5`
  - Parâmetros opcionais: `year`, `genre`, `limit`

### 5. Genre/Artist Recommendation

- **POST** `/recommendations/genre-artist`
  - Body exemplo:
    ```json
    {
      "genre": "dance pop",
      "artist": "Katy Perry",
      "limit": 5
    }
    ```

---

## Exemplos de testes para o Try it out

Cole estes JSONs nos endpoints POST para testar diferentes cenários:

### Content-Based (POST)
```json
{
  "song_title": "Rock That Body",
  "limit": 5,
  "weights": {
    "Beats.Per.Minute": 1,
    "Energy": 0.5,
    "Danceability": 2
  }
}
```

### Hybrid (POST)
```json
{
  "song_title": "Loca",
  "user_id": "user1",
  "content_weight": 0.8,
  "collab_weight": 0.2,
  "limit": 5
}
```

### Genre/Artist (POST)
```json
{
  "genre": "dance pop",
  "artist": "Katy Perry",
  "limit": 5
}
```

---

## Observações

- O arquivo `top50MusicFrom2010-2019.csv` já está incluso e é carregado automaticamente.
- Os nomes das features para pesos (weights) são:
  - Beats.Per.Minute, Energy, Danceability, Loudness/dB, Liveness, Valence, Length, Acousticness, Speechiness, Popularity
- Para erros, a API retorna mensagens detalhadas (ex: feature inválida, música não encontrada).

---


