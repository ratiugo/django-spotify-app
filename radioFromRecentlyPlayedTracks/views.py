from django.shortcuts import render
from django.urls import reverse
import requests
import sys
import spotipy
import spotipy.util as util
import json
from .models import User, Track, Playlist
from .services import SpotifyServices

def IndexView(request):
    return render(request, "radioFromRecentlyPlayedTracks/index.html")

def HomeView(request):

    return render(request, "radioFromRecentlyPlayedTracks/home.html")

def results(request):
    return render(request, "radioFromRecentlyPlayedTracks/results.html")

#Log in to Spotify, and grab all needed data about the User/playlists/tracks
def login(request):

    #create a SpotifyServices instance to create User/Playlist/Track models
    spotify = SpotifyServices()
    spotify.create_user_playlist_and_track_models()

    return render(request, 'radioFromRecentlyPlayedTracks/results.html')







