from pathlib import Path
import os
import requests
import json
from urllib.parse import quote
from dotenv import load_dotenv

# Use this guide for reference: https://developer.spotify.com/web-api/authorization-guide/

# --Spotify URLs--
SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
SPOTIFY_API_BASE_URL = "https://api.spotify.com"
API_VERSION = "v1"
SPOTIFY_API_URL = f"{SPOTIFY_API_BASE_URL}/{API_VERSION}"

# --Client Keys--

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
           
# --Server-side Parameters--
CLIENT_SIDE_URL = "http://127.0.0.1"
PORT = 8081
REDIRECT_URI = "{}:{}/callback/q".format(CLIENT_SIDE_URL, PORT)
SCOPE = "user-read-recently-played user-top-read user-read-private user-read-currently-playing user-read-playback-state"


auth_query_parameters = {
    "response_type": "code",
    "client_id": CLIENT_ID,
    "scope": SCOPE,
    "redirect_uri": REDIRECT_URI
}

# --- REQUEST DATA FROM SPOTIFY ---

def get_user_profile(access_token):
    url = f"{SPOTIFY_API_URL}/me"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json()

def get_recently_played(access_token, limit=50):
    url = f"{SPOTIFY_API_URL}/me/player/recently-played"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers, params={'limit': limit})
    return response.json()

time_range = "medium_term"

def get_user_top_tracks(access_token, time_range=time_range, limit=5):
    url = f"{SPOTIFY_API_URL}/me/top/tracks"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers, params={'time_range': time_range, 'limit': limit})
    return response.json()

def get_user_top_artists(access_token, time_range=time_range, limit=5):
    url = f"{SPOTIFY_API_URL}/me/top/artists"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers, params={'time_range': time_range, 'limit': limit})
    return response.json()


