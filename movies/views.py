from rest_framework.viewsets import ModelViewSet

from .models import Category, Movie
from .serializers import CategorySerializer, MovieSerializer


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all().order_by("id")


class MovieViewSet(ModelViewSet):
    serializer_class = MovieSerializer

    def get_queryset(self):
        return Movie.objects.select_related("category").all().order_by("id")