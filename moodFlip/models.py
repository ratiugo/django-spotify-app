from django.db import models


class User(models.Model):
    username = models.CharField(max_length = 100)

    def __str__(self):
        return self.username or ''


class Playlist(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length = 200)
    playlist_href = models.CharField(max_length = 200, default = "")
    image_url = models.CharField(max_length = 500, null=True)

    def __str__(self):
        return self.name or ''


class Track(models.Model):
    belongs_to_playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length = 200, null=True)
    artist = models.CharField(max_length = 100, null=True)
    artistID = models.CharField(max_length = 100, null=True)
    valence = models.DecimalField(decimal_places=3, max_digits=5, null=True)

    def __str__(self):
        return self.title or ''




