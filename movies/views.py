from rest_framework.viewsets import ModelViewSet

from .models import Category, Genre, Movie
from .serializers import CategorySerializer, GenreSerializer, MovieSerializer


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all().order_by("id")


# NUEVO
class GenreViewSet(ModelViewSet):
    serializer_class = GenreSerializer

    def get_queryset(self):
        return Genre.objects.all().order_by("id")


class MovieViewSet(ModelViewSet):
    serializer_class = MovieSerializer

    def get_queryset(self):
        return (
            Movie.objects
            .select_related("category")
            .prefetch_related("genres")  # NUEVO
            .all()
            .order_by("id")
        )