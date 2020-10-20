#business logic
import sys
import spotipy
import spotipy.util as util
import json
from .models import User, Track, Playlist
from multiprocessing import Pool
import threading
from functools import partial


class Pipeline():

    def __init__(self):
        self.spotipyObject = None
        self.current_user = None
        self.playlist_objects = None

    #login to spotify using spotipy
    def login(self):

        scope = "user-library-read user-read-recently-played"
        username = "ratiugo"

        token = util.prompt_for_user_token(
            username,
            scope,
            client_id="d679ae3afd4f40268bd9dea2be269276",
            client_secret="32c40374e95f4b1b932fdbc4edc02de2",
            redirect_uri="http://localhost:3000/")

        self.spotipyObject = spotipy.Spotify(
                    auth=token,
                    requests_session = True
                    )
        return self

    def create_user(self):
        current_user = User.objects.create(
            username=self.spotipyObject.current_user()["display_name"])
        self.current_user = current_user
        current_user.save()

        return self

    def create_playlists(self):
        spotify = self.spotipyObject
        playlists = spotify.current_user_playlists(limit=50)["items"]
        playlist_objects = []

        for item in playlists:
            playlist_items = spotify.playlist_tracks(item["id"])["items"]
            playlist_tracks = []

            for playlist in playlist_items:
                if playlist["track"]:
                    playlist_tracks.append(playlist["track"])

            playlist_object = Playlist(
                owner = self.current_user,
                name = item["name"],
                playlist_href = item["id"],
                image_url = ("https://www.desicomments.com/wp-content/uploads/2018/09/Im-So-So-So-So-So-Sorry.jpg"
                             if spotify.playlist_cover_image(item["id"]) == []
                             else spotify.playlist_cover_image(item["id"])[0]["url"]),
                tracks = playlist_tracks)
            playlist_objects.append(playlist_object)

        self.playlist_objects = playlist_objects
        Playlist.objects.bulk_create(playlist_objects)

        return self

    def create_tracks(self):
        spotify = self.spotipyObject
        playlist_objects = self.playlist_objects

        for playlist in playlist_objects:
            print("\nAudio features:")
            print(playlist["tracks"])

        return self
#         if self.track["track"] is None:
#             pass
#         else:
#             audio_features = spotify.audio_features(self.track["track"]["id"])
#             if audio_features[0] is None:
#                 pass
#             else:
#                 valence = audio_features[0]["valence"]

#                 #creation of Track model with relevant data acquired above
#                 new_track = Track.objects.create(
#                     belongs_to_playlist=self.belongs_to_playlist,
#                     title=self.track["track"]["name"],
#                     artist=self.track["track"]["artists"][0]["name"],
#                     artistID=self.track["track"]["artists"][0]["id"],
#                     valence=valence
#                 )
#                 new_track.save()



    #run the pipeline
    def run(self):
        return(self.login()
               .create_user()
               .create_playlists()
               .create_tracks())


###################################OLD CODE BELOW##################################################

#middleware to ensure playlist data is a subscriptable type - becomes <class 'moodFlip.services.SpotifyServices'> if sent straight to 'create_playlist_and_track_model'
# def concurrent_track_model_middleware(playlist, track):

#     belongs_to_playlist = Playlist.objects.get(name=playlist["name"])
#     create_track = Create_Track(track, belongs_to_playlist)
#     create_track.create_track_model()

# class Create_User():

#     #create User model and Playlist models for each of the user's playlists, and Track objects for each track connected to a playlist
#     def login(self):

#         scope = "user-library-read user-read-recently-played"
#         username = "ratiugo"

#         token = util.prompt_for_user_token(
#             username,
#             scope,
#             client_id="d679ae3afd4f40268bd9dea2be269276",
#             client_secret="32c40374e95f4b1b932fdbc4edc02de2",
#             redirect_uri="http://localhost:3000/")

#         spotify = spotipy.Spotify(
#                     auth=token,
#                     requests_session = True
#                     )

#         current_user = User.objects.create(username=spotify.current_user()["display_name"])
#         current_user.save()

#         # create playlist objects for each playlist
#         playlists = spotify.current_user_playlists(limit=50)["items"]
#         playlists_name_image = []

#         for item in playlists:

#             # cover_image_obj = spotify.playlist_cover_image(item["id"])

#             # if cover_image_obj == []:
#             #     image_url = "https://www.desicomments.com/wp-content/uploads/2018/09/Im-So-So-So-So-So-Sorry.jpg"
#             # else:
#             #     image_url = cover_image_obj[0]["url"]
#             # name = item["name"]

#             # playlists_name_image.append({"name": name, "image_url": image_url})

#             cover_image_obj = spotify.playlist_cover_image(item["id"])

#             if cover_image_obj == []:
#                 image_url = "https://www.desicomments.com/wp-content/uploads/2018/09/Im-So-So-So-So-So-Sorry.jpg"
#             else:
#                 image_url = cover_image_obj[0]["url"]

#             created_playlist = Playlist.objects.create(
#             owner=current_user,
#             name=item["name"],
#             playlist_href=item["id"],
#             image_url=image_url
#             )
#             created_playlist.save()

#             playlist_items = spotify.playlist_tracks(item["id"])["items"]

#             with Pool(processes=4) as pool:
#                 playlist = item
#                 send_playlist_to_middleware = partial(concurrent_track_model_middleware, playlist)
#                 pool.map(send_playlist_to_middleware, playlist_items)

#         return playlists_name_image


#     # def
#     #     for item in playlists:

#     #         cover_image_obj = spotify.playlist_cover_image(item["id"])

#     #         if cover_image_obj == []:
#     #             image_url = "https://www.desicomments.com/wp-content/uploads/2018/09/Im-So-So-So-So-So-Sorry.jpg"
#     #         else:
#     #             image_url = cover_image_obj[0]["url"]

#     #         created_playlist = Playlist.objects.create(
#     #         owner=current_user,
#     #         name=item["name"],
#     #         playlist_href=item["id"],
#     #         image_url=image_url
#     #         )
#     #         created_playlist.save()

#     #         playlist_items = spotify.playlist_tracks(item["id"])["items"]

#     #         with Pool(processes=4) as pool:
#     #             playlist = item
#     #             send_playlist_to_middleware = partial(concurrent_track_model_middleware, playlist)
#     #             pool.map(send_playlist_to_middleware, playlist_items)

# class Create_Track():

#     def __init__(self, track, belongs_to_playlist):
#         self.track = track
#         self.belongs_to_playlist = belongs_to_playlist

#     def create_track_model(self):

#         scope = "user-library-read user-read-recently-played"
#         username = "ratiugo"

#         token = util.prompt_for_user_token(
#             username,
#             scope,
#             client_id="d679ae3afd4f40268bd9dea2be269276",
#             client_secret="32c40374e95f4b1b932fdbc4edc02de2",
#             redirect_uri="http://localhost:3000/")

#         spotify = spotipy.Spotify(
#                     auth=token,
#                     requests_session = True
#                     )
#         print(self.track["track"])
#         if self.track["track"] is None:
#             pass
#         else:
#             audio_features = spotify.audio_features(self.track["track"]["id"])
#             if audio_features[0] is None:
#                 pass
#             else:
#                 valence = audio_features[0]["valence"]

#                 #creation of Track model with relevant data acquired above
#                 new_track = Track.objects.create(
#                     belongs_to_playlist=self.belongs_to_playlist,
#                     title=self.track["track"]["name"],
#                     artist=self.track["track"]["artists"][0]["name"],
#                     artistID=self.track["track"]["artists"][0]["id"],
#                     valence=valence
#                 )
#                 new_track.save()


















