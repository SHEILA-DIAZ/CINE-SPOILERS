from django.db import models
from genres.models import Genre  # NUEVO

class Movie(models.Model):
    title       = models.CharField(max_length=200)
    description = models.TextField()
    release_year = models.IntegerField()
    genres      = models.ManyToManyField(Genre, blank=True)  # NUEVO - relación muchos a muchos

    class Meta:
        ordering = ['id']  # IMPORTANTE 

    def __str__(self):
        return self.title
