from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=150)
    synopsis = models.TextField()
    release_year = models.PositiveIntegerField()
    duration_minutes = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.title