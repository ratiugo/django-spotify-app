from django.http import HttpResponse
from .spotify_pipeline import Pipeline


#Log in to Spotify, and grab all needed data about the User/playlists/tracks
def home(request):

    pipeline = Pipeline()

    pipeline.run()

    return HttpResponse(status = 200)







