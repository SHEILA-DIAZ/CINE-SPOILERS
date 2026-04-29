from django.contrib import admin

from .models import Category, Genre, Movie


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    ordering = ("id",)


# NUEVO
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    ordering = ("id",)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "release_year",
        "duration_minutes",
        "is_available",
        "category",
    )
    list_filter = ("is_available", "release_year", "category", "genres")
    search_fields = ("title",)
    filter_horizontal = ("genres",)  # NUEVO
    ordering = ("id",)