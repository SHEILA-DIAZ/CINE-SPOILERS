from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["id"]
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


# NUEVO
class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["id"]
        verbose_name = "Genre"
        verbose_name_plural = "Genres"

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=150)
    synopsis = models.TextField()
    release_year = models.PositiveIntegerField()
    duration_minutes = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="movies",
        null=True,
        blank=True,
    )

    # NUEVO
    genres = models.ManyToManyField(
        Genre,
        related_name="movies",
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.title