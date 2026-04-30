from django.db import models
from movies.models import Movie  # IMPORTANTE


class Review(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name="reviews"
    )

    author = models.CharField(max_length=100)
    comment = models.TextField()
    rating = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.author} - {self.movie.title}"