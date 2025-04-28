from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from app.data import df

router = APIRouter()

@router.get("/popular")
async def popular(
    year: Optional[int]   = Query(None),
    genre: Optional[str]  = Query(None),
    limit: int            = Query(5, ge=1, le=50)
):
    sub = df
    if year is not None:
        sub = sub[sub['year'] == year]
    if genre:
        sub = sub[sub['genre'].str.lower() == genre.lower()]
    if sub.empty:
        raise HTTPException(404, "Nenhuma música encontrada")
    sub = sub.sort_values('Popularity', ascending=False)
    recs = sub.head(limit)[['title','artist','genre','year','Popularity']] \
               .to_dict(orient='records')
    return {"recommendations": recs}
