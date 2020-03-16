from django.urls import path

from . import views

app_name = "moodFlip"
urlpatterns = [
    path("login", views.login, name="login")
]