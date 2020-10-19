from django.urls import path

from . import views

app_name = "moodFlip"
urlpatterns = [
    path("home", views.home, name="home")
]