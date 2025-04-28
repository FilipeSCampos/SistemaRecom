from fastapi import APIRouter, HTTPException
from app.data import df
from app.models import GenreArtistRequest

router = APIRouter()

@router.post("/genre-artist")
async def by_genre_artist(req: GenreArtistRequest):
    sub = df
    if req.genre:
        sub = sub[sub['genre'].str.lower() == req.genre.lower()]
    if req.artist:
        sub = sub[sub['artist'].str.lower() == req.artist.lower()]
    if sub.empty:
        raise HTTPException(404, "Nenhuma música encontrada")
    sub = sub.sort_values('Popularity', ascending=False)
    recs = sub.head(req.limit)[['title','artist','genre','Popularity']] \
               .to_dict(orient='records')
    return {"recommendations": recs}
