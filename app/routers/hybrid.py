from fastapi import APIRouter
from app.models import HybridRequest
from app.utils import normalize_scores
from app.routers.content import content_based
from app.routers.collaborative import collaborative

router = APIRouter()

@router.post("/hybrid")
async def hybrid(req: HybridRequest):
    # content-based (pega mais do que o limit pra combinar)
    cb = (await content_based(req.song_title, limit=50))['recommendations']
    cr = (await collaborative(req.user_id))['recommendations']
    cb_scores = normalize_scores({r['title']: r['score'] for r in cb})
    cr_scores = normalize_scores({r['title']: r['score'] for r in cr})
    combined = {}
    for t, s in cb_scores.items():
        combined[t] = combined.get(t, 0) + s * req.content_weight
    for t, s in cr_scores.items():
        combined[t] = combined.get(t, 0) + s * req.collab_weight
    top = sorted(combined.items(), key=lambda x: x[1], reverse=True)[:req.limit]
    return {"recommendations": [{"title": t, "score": sc} for t, sc in top]}
