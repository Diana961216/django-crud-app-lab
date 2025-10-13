from django.shortcuts import render
from .models import Artist


def home(request):
    return render(request, "home.html")


def artist_list(request):
    artists = Artist.objects.all()
    return render(request, "artists/artist_list.html", {"artists": artists})


def artist_detail(request, artist_id):
    artist = None
    try:
        artist = Artist.objects.get(id=artist_id)
    except Artist.DoesNotExist:
        pass
    return render(request, "artists/artist_detail.html", {"artist": artist})
