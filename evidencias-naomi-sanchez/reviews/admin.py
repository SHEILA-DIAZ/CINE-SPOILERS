from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'movie', 'reviewer', 'rating', 'created_at']
    ordering     = ['id']