from django.urls import path

from . import views

app_name = "radioFromRecentlyPlayedTracks"
urlpatterns = [
    path("", views.IndexView, name="index"),
    path("home", views.HomeView, name="home"),
    path("login", views.login, name="login"),
    path("results", views.results, name="results")
]