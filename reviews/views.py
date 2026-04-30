from rest_framework.viewsets import ModelViewSet
from .models import Review
from .serializers import ReviewSerializer


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.all().order_by("id")