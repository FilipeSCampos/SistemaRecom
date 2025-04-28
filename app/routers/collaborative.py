from fastapi import APIRouter, HTTPException
from app.data import user_likes, co_occurrence

router = APIRouter()

@router.get("/collaborative/{user_id}")
async def collaborative(user_id: str):
    if user_id not in user_likes:
        raise HTTPException(404, "Usuário não encontrado")
    liked = set(user_likes[user_id])
    scores = {}
    for s in liked:
        for other, cnt in co_occurrence.get(s, {}).items():
            if other in liked: continue
            scores[other] = scores.get(other, 0) + cnt
    recs = [{"title": t, "score": c} for t, c in sorted(scores.items(), key=lambda x: x[1], reverse=True)]
    return {"recommendations": recs}
