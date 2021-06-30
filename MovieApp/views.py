from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from .models import Movie
from .serializers import MovieSerializer
import random

# Create your views here.

class randMovieView(APIView):
    def get(self, request):
        page = int(request.GET['page'])
        totalMovie = Movie.objects.all()
        randomMovie = random.sample(list(totalMovie), page * 20)
        serializer = MovieSerializer(randomMovie, many=True)
        return Response(serializer.data)

class populMovieView(APIView):
    def get(self, request):
        page = int(request.GET['page'])
        totalMovie = Movie.objects.all().order_by('-release', '-voteAver')
        MovieData = totalMovie[:page * 20]
        serializer = MovieSerializer(MovieData, many=True)
        return Response(serializer.data)

class userGoodView(APIView):
    def get(self, request):
        user = request.GET['user']
