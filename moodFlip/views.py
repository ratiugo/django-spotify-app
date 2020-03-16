from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.urls import reverse
import requests
import sys
import spotipy
import spotipy.util as util
import json
from .models import User, Track, Playlist
from .services import SpotifyServices
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

@api_view(('GET',))
#Log in to Spotify, and grab all needed data about the User/playlists/tracks
def login(request):

    #create a SpotifyServices instance to create User/Playlist/Track models
    spotify = SpotifyServices()
    spotify.create_user_playlist_and_track_models()

    return Response(status=status.HTTP_200_OK)







