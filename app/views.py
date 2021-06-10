from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Movie
from .serializer import MovieSerializer

# Create your views here.

@api_view(['GET'])
def helloAPI(request) :
    return Response('hello world!')