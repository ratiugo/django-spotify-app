from rest_framework import serializers
from moodFlip.models import User, Playlist, Track

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ["belongs_to_playlist", "title", "artist", "artistID", "valence"]

class PlaylistSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True)

    class Meta:
        model = Playlist
        fields = ["owner", "name", "playlist_href", "image_url", "tracks"]

class UserSerializer(serializers.ModelSerializer):
    playlists = PlaylistSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["username", "playlists"]

