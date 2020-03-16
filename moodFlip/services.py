#business logic
import sys
import spotipy
import spotipy.util as util
import json
from .models import User, Track, Playlist
from multiprocessing import Pool, TimeoutError
import threading
import ipdb

#functionality for interacting with the Spotify API through spotipy
class SpotifyServices():

    #create a playlist model and corresponding track models
    def create_playlist_and_track_model(playlist, self):

        print(playlist["id"])
        scope = "user-library-read user-read-recently-played"
        username = "ratiugo"


        token = util.prompt_for_user_token(
            username,
            scope,
            client_id="d679ae3afd4f40268bd9dea2be269276",
            client_secret="32c40374e95f4b1b932fdbc4edc02de2",
            redirect_uri="http://localhost:3000/")

        spotify = spotipy.Spotify(
                    auth=token,
                    requests_session = True
                    )


        image_url = spotify.playlist_cover_image(playlist["id"])[0]["url"]

        created_playlist = Playlist.objects.create(
            owner=current_user,
            name=playlist["name"],
            playlist_href=playlist["id"],
            image_url=image_url
        )
        created_playlist.save()

        #create Track models for each track in playlist just created

        #get playlist track objects
        playlist_items = spotify.playlist_tracks(playlist["id"])["items"]

        #get each track from playlist track object
        for item in playlist_items:

            #filter 'none' items to prevent crashing
            if item["track"] is None:
                continue

            #if the track object exists, grab the audio features of the track
            else:
                audio_features = spotify.audio_features(item["track"]["id"])

                #filter 'none' items to prevent crashing
                if audio_features[0] is None:
                    continue

                #if audio features exist, get the 'valence' i.e. mood of the track
                else:
                    valence = audio_features[0]["valence"]

                    #creation of Track model with relevant data acquired above
                    new_track = Track.objects.create(
                        belongs_to_playlist=created_playlist,
                        title=item["track"]["name"],
                        artist=item["track"]["artists"][0]["name"],
                        artistID=item["track"]["artists"][0]["id"],
                        valence=valence)
                    new_track.save()

    #create User model and Playlist models for each of the user's playlists, and Track objects for each track connected to a playlist
    def create_user_playlist_and_track_models(self):

        scope = "user-library-read user-read-recently-played"
        username = "ratiugo"

        token = util.prompt_for_user_token(
            username,
            scope,
            client_id="d679ae3afd4f40268bd9dea2be269276",
            client_secret="32c40374e95f4b1b932fdbc4edc02de2",
            redirect_uri="http://localhost:3000/")

        spotify = spotipy.Spotify(
                    auth=token,
                    requests_session = True
                    )

        current_user = User.objects.create(username=spotify.current_user()["display_name"])
        current_user.save()

        # create playlist objects for each playlist
        playlists = spotify.current_user_playlists(limit=50)["items"]
        # print(playlists)
        print(type(playlists))

        ipdb.set_trace()

        with Pool(processes=10) as pool:
            pool.map(self.create_playlist_and_track_model, playlists)




















