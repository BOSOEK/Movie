from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'genres', 'overview', 'popularity', 'adult', 'production', 'runtime', 'release', 'budget', 'voteAver', 'voteCount', 'tagLine', 'status', 'video', 'poster', 'backdrop', 'cast', 'director')