import lyricsgenius
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")

genius = lyricsgenius.Genius(api_key, timeout=100)
artist = genius.search_artist("Michael Jackson", max_songs=160, sort="popularity")

for song in artist.songs:
    print(f"Fetching {song.title}")
    title = song.title
    if "/" in title:
        title = "".join(title.split("/"))
    with open(f"data/{title}.txt", "w", encoding="utf-8") as f:
        f.write(song.lyrics + "\n\n")
