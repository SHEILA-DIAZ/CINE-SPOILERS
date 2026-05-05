from django.contrib import admin
from .models import Genre

# NUEVO - registro simple y limpio
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering     = ['id']
