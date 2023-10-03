from django.contrib import admin
from .models import Category, Studio, Episode, Anime, Quality, Genre

@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'sub_title',
        'slug',
        'description',
        'date_created',
        'duration',
    )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
    )

@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
    )

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
    )

@admin.register(Studio)
class StudioAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
    )

@admin.register(Quality)
class QualityAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
    )
