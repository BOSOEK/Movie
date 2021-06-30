from django.urls import path
from .views import randMovieView, populMovieView

urlpatterns = [
    path('Random', randMovieView.as_view()),
    path('populMovie', populMovieView.as_view())
]


