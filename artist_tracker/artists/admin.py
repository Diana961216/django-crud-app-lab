from django.contrib import admin
from .models import Artist, Album


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ("name", "debut_year")
    search_fields = ("name",)


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ("title", "artist", "release_year")
    list_filter = ("release_year", "artist")
    search_fields = ("title", "artist__name")
