from django.db import models

from django.db import models

class Genre(models.Model):
    # NUEVO 
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['id']  # IMPORTANTE 

    def __str__(self):
        return self.name
