from django.contrib import admin

# Register your models here.
from .models import Movie


class MovieAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ('title', 'genres', 'overview', 'popularity', 'adult', 'production', 'runtime', 'release', 'budget', 'voteAver', 'voteCount', 'tagLine', 'status', 'video', 'poster', 'backdrop', 'cast', 'director')


admin.site.register(Movie, MovieAdmin)
