from rest_framework import serializers
from .models import Genre

# NUEVO
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Genre
        fields = ['id', 'name']