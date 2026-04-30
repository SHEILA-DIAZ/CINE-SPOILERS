from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, GenreViewSet, MovieViewSet

router = DefaultRouter()
router.register("categories", CategoryViewSet, basename="category")
router.register("genres", GenreViewSet, basename="genre")
router.register("movies", MovieViewSet, basename="movie")

urlpatterns = [
    path("", include(router.urls)),
]