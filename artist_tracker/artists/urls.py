from django.urls import path
from . import views

urlpatterns = [
    path("", views.artist_list, name="artist_list"),
    path("<int:artist_id>/", views.artist_detail, name="artist_detail"),
    path("create/", views.ArtistCreate.as_view(), name="artist_create"),
    path("<int:pk>/update/", views.ArtistUpdate.as_view(), name="artist_update"),
    path("<int:pk>/delete/", views.ArtistDelete.as_view(), name="artist_delete"),
    path(
        "<int:artist_id>/albums/create/",
        views.AlbumCreate.as_view(),
        name="album_create",
    ),
    path("albums/<int:pk>/", views.AlbumDetail.as_view(), name="album_detail"),
    path("albums/<int:pk>/update/", views.AlbumUpdate.as_view(), name="album_update"),
    path("albums/<int:pk>/delete/", views.AlbumDelete.as_view(), name="album_delete"),
    path("signup/", views.signup, name="signup"),
]
