from fastapi import FastAPI
from app.routers import content, genre_artist, collaborative, hybrid, popular

app = FastAPI(title="Music Recommender")

# todos sob o prefixo /recommendations
app.include_router(content.router,       prefix="/recommendations")
app.include_router(genre_artist.router, prefix="/recommendations")
app.include_router(collaborative.router, prefix="/recommendations")
app.include_router(hybrid.router,        prefix="/recommendations")
app.include_router(popular.router,       prefix="/recommendations")
