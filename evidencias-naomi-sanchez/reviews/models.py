from django.db import models
from movies.models import Movie

class Review(models.Model):
    # NUEVO - Reseña vinculada a una película
    movie       = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    reviewer    = models.CharField(max_length=100)
    comment     = models.TextField()
    rating      = models.IntegerField()  # IMPORTANTE - del 1 al 5
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"{self.reviewer} - {self.movie.title} ({self.rating}/5)"