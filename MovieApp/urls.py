from django.urls import path
from .views import helloAPI, showMovie

urlpatterns = [
    path('hello/', helloAPI),
    path('Random/<int:id>/', showMovie),
]
