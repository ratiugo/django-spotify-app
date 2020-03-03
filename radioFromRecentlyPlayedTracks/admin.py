from django.contrib import admin

from .models import User, Track, Playlist

class UserAdmin(admin.ModelAdmin):
    model = User

class TrackAdmin(admin.ModelAdmin):
    model = Track

class PlaylistAdmin(admin.ModelAdmin):
    model = Playlist

admin.site.register(User, UserAdmin)
admin.site.register(Track, TrackAdmin)
admin.site.register(Playlist, PlaylistAdmin)

