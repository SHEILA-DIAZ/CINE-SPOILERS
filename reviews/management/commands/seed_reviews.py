from django.core.management.base import BaseCommand
from movies.models import Movie
from reviews.models import Review


class Command(BaseCommand):
    help = "Cargar reviews de prueba"

    def handle(self, *args, **kwargs):
        movies = Movie.objects.all()

        if not movies:
            self.stdout.write("No hay películas")
            return

        for movie in movies:
            Review.objects.create(
                movie=movie,
                author="Usuario 1",
                comment="Excelente película",
                rating=5
            )

            Review.objects.create(
                movie=movie,
                author="Usuario 2",
                comment="Muy buena pero un poco larga",
                rating=4
            )

        self.stdout.write(self.style.SUCCESS("Reviews creadas correctamente"))