from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'genres', 'overview', 'adult', 'production', 'runtime', 'release', 'budget', 'voteAver', 'voteCount', 'status', 'video', 'poster', 'backdrop', 'cast', 'director')