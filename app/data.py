# app/data.py

from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity

BASE_DIR = Path(__file__).parent
CSV_PATH = BASE_DIR / "top50MusicFrom2010-2019.csv"

df = pd.read_csv(CSV_PATH)

df = df.rename(columns={
    'the genre of the track': 'genre',
    'Beats.Per.Minute -The tempo of the song': 'Beats.Per.Minute',
    'Energy- The energy of a song - the higher the value, the more energtic': 'Energy',
    'Danceability - The higher the value, the easier it is to dance to this song': 'Danceability',
    'Loudness/dB - The higher the value, the louder the song': 'Loudness/dB',
    'Liveness - The higher the value, the more likely the song is a live recording': 'Liveness',
    'Valence - The higher the value, the more positive mood for the song': 'Valence',
    'Length - The duration of the song': 'Length',
    'Acousticness - The higher the value the more acoustic the song is': 'Acousticness',
    'Speechiness - The higher the value the more spoken word the song contains': 'Speechiness',
    'Popularity- The higher the value the more popular the song is': 'Popularity'
})

#Lista de features numéricas para similaridade
features = [
    'Beats.Per.Minute', 'Energy', 'Danceability', 'Loudness/dB',
    'Liveness', 'Valence', 'Length', 'Acousticness', 'Speechiness', 'Popularity'
]

#Normaliza features para [0,1]
scaler = MinMaxScaler()
df[features] = scaler.fit_transform(df[features])

#Matriz de similaridade (cosine entre as features)
similarity_matrix = cosine_similarity(df[features])

#Pedi pro querido GPT gerar isso aqui 
likes_history = [
    {"user_id": "user7",  "song_title": "One Call Away (feat. Tyga) - Remix"},
    {"user_id": "user8",  "song_title": "Meet Me Halfway"},
    {"user_id": "user7",  "song_title": "International Love"},
    {"user_id": "user3",  "song_title": "Rude"},
    {"user_id": "user8",  "song_title": "7 Years"},
    {"user_id": "user4",  "song_title": "Turn Up the Music"},
    {"user_id": "user6",  "song_title": "Up"},
    {"user_id": "user2",  "song_title": "Ghosttown"},
    {"user_id": "user6",  "song_title": "Confident"},
    {"user_id": "user5",  "song_title": "Kiss You"},
    {"user_id": "user10", "song_title": "Whataya Want from Me"},
    {"user_id": "user9",  "song_title": "This Town"},
    {"user_id": "user10", "song_title": "The Cure"},
    {"user_id": "user3",  "song_title": "Ferrari"},
    {"user_id": "user4",  "song_title": "Water Under the Bridge"},
    {"user_id": "user3",  "song_title": "OK - Spotify Version"},
    {"user_id": "user3",  "song_title": "Meet Me Halfway"},
    {"user_id": "user9",  "song_title": "Feel This Moment (feat. Christina Aguilera)"},
    {"user_id": "user2",  "song_title": "Roses"},
    {"user_id": "user9",  "song_title": "Here"},
    {"user_id": "user2",  "song_title": "Bloodstream"},
    {"user_id": "user5",  "song_title": "See You Again (feat. Charlie Puth)"},
    {"user_id": "user7",  "song_title": "True Colors"},
    {"user_id": "user8",  "song_title": "Try Sleeping with a Broken Heart"},
    {"user_id": "user1",  "song_title": "Girls (feat. Cardi B, Bebe Rexha & Charli XCX)"},
    {"user_id": "user8",  "song_title": "Roses"},
    {"user_id": "user2",  "song_title": "Me Too"},
    {"user_id": "user6",  "song_title": "Locked Out of Heaven"},
    {"user_id": "user4",  "song_title": "How Far I'll Go - From \"Moana\""},
    {"user_id": "user2",  "song_title": "Wait"}
]

from collections import defaultdict

user_likes = defaultdict(list)
for ev in likes_history:
    user_likes[ev["user_id"]].append(ev["song_title"])


#Co-ocorrência entre músicas
co_occurrence: dict[str, dict[str, int]] = {}
for user, likes in user_likes.items():
    for song in likes:
        co_occurrence.setdefault(song, {})
        for other in likes:
            if other == song:
                continue
            co_occurrence[song][other] = co_occurrence[song].get(other, 0) + 1
