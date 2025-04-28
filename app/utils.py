from fastapi import HTTPException
from app.data import df, features

def get_song_index(title: str) -> int:
    """Retorna o índice no DataFrame ou lança 404 se não existir."""
    mask = df['title'].str.lower() == title.lower()
    if not mask.any():
        raise HTTPException(status_code=404, detail="Música não encontrada")
    return int(df[mask].index[0])

def normalize_scores(scores: dict) -> dict:
    """Divide todos os valores pelo maior para escala [0,1]."""
    if not scores:
        return {}
    mx = max(scores.values())
    return {k: v/mx for k, v in scores.items()}
