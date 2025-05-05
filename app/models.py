from pydantic import BaseModel
from typing import Optional, Dict

class ContentBasedRequest(BaseModel):
    song_title: str
    limit: int = 5
    weights: Optional[Dict[str, float]] = None

class GenreArtistRequest(BaseModel):
    genre: Optional[str] = None
    artist: Optional[str] = None
    limit: int = 5

class HybridRequest(BaseModel):
    song_title: str
    user_id: str
    content_weight: float = 0.7
    collab_weight: float = 0.3
    limit: int = 5
