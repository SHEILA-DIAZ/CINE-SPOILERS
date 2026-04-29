from django.contrib import admin

from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "release_year",
        "duration_minutes",
        "is_available",
    )
    list_filter = ("is_available", "release_year")
    search_fields = ("title",)
    ordering = ("id",)