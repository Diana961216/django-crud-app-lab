from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    debut_year = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
