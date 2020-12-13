from django.http import HttpResponse
from .spotify_pipeline import SpotifyPipeline


#Log in to Spotify, and grab all needed data about the User/playlists/tracks
def home(request):

    Spotify = SpotifyPipeline()

    Spotify.run()

    return HttpResponse(status = 200)







