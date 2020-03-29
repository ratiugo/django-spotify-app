from django.shortcuts import render
from rest_framework.response import Response
from .services import Create_User, Playlist


#Log in to Spotify, and grab all needed data about the User/playlists/tracks
def login(request):

    #create a SpotifyServices instance to create User/Playlist/Track models
    user =User()
    playlists_name_image = user.login()

    return Response(status=status.HTTP_200_OK)







