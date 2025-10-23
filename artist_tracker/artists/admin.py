from django.contrib import admin
from .models import Artist, Album, Genre


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ("name", "debut_year")
    search_fields = ("name",)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ("title", "artist", "release_year", "get_genres")
    list_filter = ("release_year", "artist")
    search_fields = ("title", "artist__name")

    def get_genres(self, obj):
        return ", ".join(g.name for g in obj.genres.all())

    get_genres.short_description = "Genres"
