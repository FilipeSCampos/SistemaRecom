
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.data import df, user_likes

client = TestClient(app)

# Variáveis para os testes
existing_song = df['title'].iloc[0]
nonexistent_song = "Song Not Found"
existing_user = list(user_likes.keys())[0]
nonexistent_user = "no_user"
existing_genre = df['genre'].iloc[0]
nonexistent_genre = "NoGenre"
existing_artist = df['artist'].iloc[0]

def test_content_based_success():
    response = client.get(f"/recommendations/content-based/{existing_song}")
    assert response.status_code == 200
    data = response.json()
    assert "recommendations" in data
    assert isinstance(data["recommendations"], list)
    assert len(data["recommendations"]) > 0

def test_content_based_not_found():
    response = client.get(f"/recommendations/content-based/{nonexistent_song}")
    assert response.status_code == 404

def test_genre_artist_success_by_genre():
    response = client.post("/recommendations/genre-artist", json={"genre": existing_genre, "limit": 3})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data["recommendations"], list)
    assert len(data["recommendations"]) <= 3

def test_genre_artist_success_by_artist():
    response = client.post("/recommendations/genre-artist", json={"artist": existing_artist, "limit": 3})
    assert response.status_code == 200

def test_genre_artist_not_found():
    response = client.post("/recommendations/genre-artist", json={"genre": nonexistent_genre, "artist": nonexistent_genre})
    assert response.status_code == 404

def test_collaborative_success():
    response = client.get(f"/recommendations/collaborative/{existing_user}")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data["recommendations"], list)

def test_collaborative_not_found():
    response = client.get(f"/recommendations/collaborative/{nonexistent_user}")
    assert response.status_code == 404

def test_hybrid_success():
    response = client.post("/recommendations/hybrid", json={
        "song_title": existing_song,
        "user_id": existing_user,
        "limit": 3
    })
    assert response.status_code == 200

def test_hybrid_song_not_found():
    response = client.post("/recommendations/hybrid", json={
        "song_title": nonexistent_song,
        "user_id": existing_user
    })
    assert response.status_code == 404

def test_hybrid_user_not_found():
    response = client.post("/recommendations/hybrid", json={
        "song_title": existing_song,
        "user_id": nonexistent_user
    })
    assert response.status_code == 404

def test_popular_success():
    existing_year = int(df['year'].iloc[0])
    response = client.get(f"/recommendations/popular?year={existing_year}&limit=3")
    assert response.status_code == 200

def test_popular_not_found():
    response = client.get("/recommendations/popular?year=9999&limit=3")
    assert response.status_code == 404
