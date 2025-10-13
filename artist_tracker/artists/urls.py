from django.urls import path
from . import views

urlpatterns = [
    path("", views.artist_list, name="artist_list"),  # list of artists
    path("<int:artist_id>/", views.artist_detail, name="artist_detail"),  # detail page
]
