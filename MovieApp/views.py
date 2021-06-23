from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Movie
from .serializers import MovieSerializer
import random

# Create your views here.

@api_view(['GET'])
def helloAPI(request):
    return Response('hello world!')

@api_view(['GET'])
def showMovie(request, id):
    totalMovie = Movie.objects.all()
    randomMovie = random.sample(list(totalMovie), id)
    serializer = MovieSerializer(randomMovie, many=True)
    return Response(serializer.data)
