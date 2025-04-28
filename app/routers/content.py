from fastapi import APIRouter, Query
from typing import Optional, Dict
import numpy as np

from app.data import df, similarity_matrix, features
from app.utils import get_song_index

router = APIRouter()

@router.get("/content-based/{song_title}")
async def content_based(
    song_title: str,
    limit: int = Query(5, ge=1, le=20),
    weights: Optional[Dict[str, float]] = None
):
    idx = get_song_index(song_title)
    sims = similarity_matrix[idx].copy()
    # se vierem pesos, aplica multiplicação direta (exemplo simplificado)
    if weights:
        for feat, w in weights.items():
            if feat not in features:
                raise HTTPException(status_code=400, detail=f"Feature inválida: {feat}")
            sims = sims * w
    # ordena e filtra
    order = np.argsort(sims)[::-1]
    recs = []
    for i in order:
        if df.iloc[i]['title'].lower() == song_title.lower():
            continue
        recs.append({
            "title": df.iloc[i]['title'],
            "score": float(sims[i])
        })
        if len(recs) >= limit:
            break
    return {"recommendations": recs}
