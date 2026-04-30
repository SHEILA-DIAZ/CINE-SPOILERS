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
            "genres",
            "genres_detail",
            "created_at",
            "updated_at",
        )
        read_only_fields = (
            "id",
            "category_detail",
            "genres_detail",
            "created_at",
            "updated_at",
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