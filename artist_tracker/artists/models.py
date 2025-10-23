from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    debut_year = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="albums")
    title = models.CharField(max_length=150)
    release_year = models.PositiveIntegerField(null=True, blank=True)
    notes = models.TextField(blank=True)
    genres = models.ManyToManyField(Genre, related_name="albums", blank=True)

    class Meta:
        ordering = ["-release_year", "title"]

    def __str__(self):
        return (
            f"{self.title} ({self.release_year})" if self.release_year else self.title
        )
