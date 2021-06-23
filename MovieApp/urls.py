from django.urls import path
from .views import helloAPI, showMovie, choseMovie

urlpatterns = [
    path('hello/', helloAPI),
    path('Random/<int:id>/', showMovie),
    path('<int:id>/', choseMovie)
]
