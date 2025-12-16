import os
from flask import Flask, redirect, request, session, url_for, render_template, Response
from werkzeug.wrappers import Response as WerkzeugResponse
from typing import Union, Dict, Any
import requests
import json
from urllib.parse import quote
from api import (
    get_user_profile,
    get_user_top_tracks,
    get_user_top_artists,
    get_recently_played,
    SPOTIFY_AUTH_URL,
    SPOTIFY_TOKEN_URL,
    REDIRECT_URI,
    CLIENT_ID,
    CLIENT_SECRET,
    PORT,
    auth_query_parameters
)

RouteResponse = Union[Response, WerkzeugResponse, str]

# Use this guide for reference: https://developer.spotify.com/web-api/authorization-guide/

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'random_secret_key')

# -- User route authentication --
@app.route("/")
def index() -> RouteResponse:
    url_args: str = "&".join(["{}={}".format(key, quote(val)) for key, val in auth_query_parameters.items()])
    auth_url: str = "{}/?{}".format(SPOTIFY_AUTH_URL, url_args)
    return redirect(auth_url)

# -- Authorization code -> Access token --
@app.route("/callback/q")
def callback() -> RouteResponse:
    auth_token = request.args['code']

    token_data: Dict[str, str | int] = {
        "grant_type": "authorization_code",
        "code": str(auth_token),
        "redirect_uri": REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    }

    post_request = requests.post(SPOTIFY_TOKEN_URL, data=token_data)
    response_data: Dict[str, Any] = json.loads(post_request.text)

    if "access_token" not in response_data:
        return "Error retrieving access token", 400

    access_token: str = response_data["access_token"]

    # -- Token exchange --

    refresh_token = response_data.get("refresh_token")
    token_type = response_data["token_type"]
    expires_in = response_data["expires_in"]

    session['access_token'] = access_token
    session.setdefault('time_range', 'medium_term')

    return redirect(url_for('dashboard'))

@app.route("/dashboard")
def dashboard() -> RouteResponse:
    access_token: str | None = session.get("access_token")

    if not access_token:
        return redirect(url_for("index"))
    
    time_range: str = session.get("time_range", "medium_term")

    user_profile = get_user_profile(access_token)
    recently_played = get_recently_played(access_token)
    top_tracks = get_user_top_tracks(access_token, time_range=time_range)
    top_artists = get_user_top_artists(access_token, time_range=time_range)

    return render_template(
        "dashboard.html",
        user_profile=user_profile,
        recently_played=recently_played,
        top_tracks=top_tracks,
        top_artists=top_artists
    )

@app.route("/set_time_range", methods=["POST"])
def set_time_range() -> RouteResponse:
    selected_range: str = request.form.get("time_range", "medium_term")
    session["time_range"] = selected_range
    return redirect(url_for("dashboard"))


if __name__ == "__main__":
    app.run(debug=True, port=PORT)
