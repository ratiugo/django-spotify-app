from django.urls import path

from . import views

app_name = "radioFromRecentlyPlayedTracks"
urlpatterns = [
    path("", views.IndexView, name="index")
]