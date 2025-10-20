from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .models import Artist, Album


def home(request):
    return render(request, "home.html")


def artist_list(request):
    artists = Artist.objects.all()
    return render(request, "artists/artist_list.html", {"artists": artists})


def artist_detail(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)
    return render(request, "artists/artist_detail.html", {"artist": artist})


class ArtistCreate(CreateView):
    model = Artist
    fields = "__all__"
    template_name = "artists/artist_form.html"


class ArtistUpdate(UpdateView):
    model = Artist
    fields = "__all__"
    template_name = "artists/artist_form.html"


class ArtistDelete(DeleteView):
    model = Artist
    success_url = "/artists/"
    template_name = "artists/artist_confirm_delete.html"


class AlbumDetail(DetailView):
    model = Album
    template_name = "artists/album_detail.html"
    context_object_name = "album"


class AlbumCreate(CreateView):
    model = Album
    fields = ["title", "release_year", "notes"]
    template_name = "artists/album_form.html"

    def dispatch(self, request, *args, **kwargs):
        self.artist = get_object_or_404(Artist, pk=kwargs["artist_id"])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.artist = self.artist
        response = super().form_valid(form)
        return response

    def get_success_url(self):
        return reverse("artist_detail", args=[self.artist.id])

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["artist"] = self.artist
        return ctx


class AlbumUpdate(UpdateView):
    model = Album
    fields = ["title", "release_year", "notes"]
    template_name = "artists/album_form.html"

    def get_success_url(self):
        return reverse("artist_detail", args=[self.object.artist.id])


class AlbumDelete(DeleteView):
    model = Album
    template_name = "artists/album_confirm_delete.html"

    def get_success_url(self):
        return reverse_lazy("artist_detail", args=[self.object.artist.id])
