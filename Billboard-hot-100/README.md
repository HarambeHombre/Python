# Billboard 100 Playlist Generator ![Python](https://img.shields.io/badge/Python-3.x-blue)

The **Billboard 100 Playlist Generator** is a Python application that automatically creates a Spotify playlist from the Billboard Hot 100 songs for a user-specified date. By combining the power of web scraping with the Spotify Web API, the script fetches Billboard's top 100 songs and adds them to a newly created private playlist on the user's Spotify account.

---

## Features

- **Date Selection**: Users can input a specific date (in `YYYY-MM-DD` format) to fetch the Billboard Hot 100 chart from that time.
- **Spotify Playlist Creation**: Automatically creates a private Spotify playlist for the selected date.
- **Song Fetching**: Scrapes song titles from Billboard and searches for them on Spotify.
- **Automated Playlist Population**: Adds the top 100 songs from Billboard to the generated Spotify playlist.

---

## Requirements

### Python Libraries
The script requires the following Python libraries:
- `requests`: For making HTTP requests to the Billboard website.
- `BeautifulSoup` (from `bs4`): For scraping song data from Billboard.
- `spotipy`: For interfacing with the Spotify Web API.

Install the required libraries with:
```bash
pip install requests beautifulsoup4 spotipy
```

### Spotify Setup
To use this script, you need a `Spotify Developer` account. Follow these steps:
1. Go to the  `Spotify Developer Dashboard` and create a new application.
2. Note down the **Client ID** and **Client Secret** provided by Spotify.
3. Set the Redirect URI to `http://localhost:9090` in your app settings.
4. Replace the placeholders `CLIENT_ID` and `CLIENT_SECRET` in the script with your Spotify app's credentials.

---

## How to Use
1. **Run the Script**:
```bash
main.py
```

2. **Provide Input**: The script will prompt you to enter a date in the `YYYY-MM-DD` format:
```
What year of music do you want to listen to? Enter in (YYYY-MM-DD):
```

3. Playlist Creation:
   - The script will scrape the Billboard Hot 100 for the entered date.
   - It will search for the top 100 songs on Spotify and create a private playlist in your account with the songs.

---

## Code Breakdown
### Spotify API Initialization
The script uses the `spotipy` library for authentication and playlist management:
```Python
auth_manager = SpotifyOAuth(
    scope="playlist-modify-private",
    redirect_uri="http://localhost:9090",
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
)
sp = spotipy.Spotify(auth_manager=auth_manager)
```

### Billboard Web Scraping
The `BeautifulSoup` library extracts song titles from the Billboard Hot 100 page:
```Python
response = requests.get(f"{URL}{search_date}")
soup = BeautifulSoup(response.text, "html.parser")
song_list = soup.select("li ul li h3")
```

### Playlist Creation
Creates a Spotify playlist with the specified date as its title:
```Python
sp_response = sp.user_playlist_create(
    user["id"], name=f"{search_date} Billboard 100", description="Top 100 Songs from this time period.", public=False
)
```

### Adding Songs to Playlist
Searches for each song on Spotify and adds the found tracks to the playlist:
```Python
for song in song_list:
    artist_results = sp.search(f"track: {song.getText().strip()}, year: split_date[0]", limit=1)
    track_id = artist_results["tracks"]["items"][0]["id"]
    playlist.append(f"https://open.spotify.com/track/{track_id}")
sp_add_to_playlist = sp.playlist_add_items(sp_response["id"], playlist)
```

---

## Example Workflow
1. User Input:
```
What year of music do you want to listen to? Enter in (YYYY-MM-DD): 2000-01-01
```
2. Spotify Playlist: The script creates a playlist named "2000-01-01 Billboard 100" containing the top 100 songs from the Billboard chart of that date.

---

## Notes
- Error Handling:
  - Ensure the entered date has a corresponding Billboard chart; otherwise, scraping may fail.
  - Songs not found on Spotify will be skipped.

- Private Playlist:
  - The playlist is created as private by default. You can modify this in the `user_playlist_create()` function.




