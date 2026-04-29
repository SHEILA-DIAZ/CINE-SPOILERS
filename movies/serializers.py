from datetime import datetime

from rest_framework import serializers

from .models import Category, Genre, Movie


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
        )
        read_only_fields = ("id",)


# NUEVO
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = (
            "id",
            "name",
        )
        read_only_fields = ("id",)


class MovieSerializer(serializers.ModelSerializer):
    category_detail = CategorySerializer(source="category", read_only=True)

    # NUEVO
    genres_detail = GenreSerializer(source="genres", many=True, read_only=True)

    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "synopsis",
            "release_year",
            "duration_minutes",
            "is_available",
            "category",
            "category_detail",
            "genres",          # NUEVO: recibe IDs
            "genres_detail",   # NUEVO: muestra información completa
            "created_at",
            "updated_at",
        )
        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
            "category_detail",
            "genres_detail",
        )

    def validate_release_year(self, value):
        current_year = datetime.now().year

        if value > current_year:
            raise serializers.ValidationError(
                "El año no puede ser en el futuro."
            )

        return value

    def validate_duration_minutes(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "La duración debe ser mayor a 0."
            )

        return value

    def validate(self, data):
        title = data.get("title")
        release_year = data.get("release_year")

        queryset = Movie.objects.filter(
            title__iexact=title,
            release_year=release_year,
        )

        if self.instance:
            queryset = queryset.exclude(id=self.instance.id)

        if queryset.exists():
            raise serializers.ValidationError(
                "Esta película ya existe."
            )

        return data