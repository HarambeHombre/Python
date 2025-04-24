import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID="CLIENT_ID"
CLIENT_SECRET="CLIENT_SECRET"
URL="https://www.billboard.com/charts/hot-100/"

# INITIALIZE CONNECTION WITH SPOTIFY---------------------
auth_manager = SpotifyOAuth(
    scope="playlist-modify-private",
    redirect_uri="http://localhost:9090",
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
)
sp = spotipy.Spotify(auth_manager=auth_manager)

user = sp.current_user()
ENDPOINT = f"https://api.spotify.com/v1/users/{user['id']}/playlists"


# INPUT FIELD FOR QUERIES---------------------------------
search_date = input("What year of music do you want to listen to? Enter in (YYYY-MM-DD: ")
split_date = (search_date.split("-"))


# CREATE PLAYLIST ----------------------------------------
sp_response = sp.user_playlist_create(user["id"], name=f"{search_date} Billboard 100", description="Top 100 Songs from this time period.", public=False)

# SONGLIST FROM TOP 100 BILLBOARD ------------------------
response = requests.get(f"{URL}{search_date}")
soup = BeautifulSoup(response.text, "html.parser")
song_list = soup.select("li ul li h3")
playlist = []
for song in song_list:
# Add top 100 songs from billboard 100 to created playlist on spotify
    artist_results = sp.search(f"track: {song.getText().strip()}, year: split_date[0]", limit=1)
    track_id = artist_results["tracks"]["items"][0]["id"]
    playlist.append(f"https://open.spotify.com/track/{track_id}")
sp_add_to_playlist = sp.playlist_add_items(sp_response["id"], playlist)