from rest_framework import serializers
from genres.serializers import GenreSerializer  # NUEVO
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    # CAMBIO - géneros anidados en la respuesta JSON
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model  = Movie
        fields = ['id', 'title', 'description', 'release_year', 'genres']