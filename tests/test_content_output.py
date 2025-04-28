import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_content_based_hey_soul_sister_top5():
    # Chama o endpoint com Hey, Soul Sister e limit=5
    response = client.get(
        "/recommendations/content-based/Hey, Soul Sister",
        params={"limit": 5}
    )
    assert response.status_code == 200
    data = response.json()
    assert "recommendations" in data
    
    recs = data["recommendations"]
    # Deve retornar exatamente 5 recomendações
    assert isinstance(recs, list)
    assert len(recs) == 5
    
    # Títulos esperados na ordem correta
    expected_titles = [
        "Happier",
        "Love Runs Out",
        "The Heart Wants What It Wants",
        "Cake By The Ocean",
        "One More Night"
    ]
    returned_titles = [r["title"] for r in recs]
    assert returned_titles == expected_titles
    
    # Verifica que os scores estão em ordem decrescente e acima de 0.99
    scores = [r["score"] for r in recs]
    assert scores == sorted(scores, reverse=True)
    assert all(score > 0.99 for score in scores)