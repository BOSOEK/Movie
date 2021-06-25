from django.urls import path
from .views import showMovie

urlpatterns = [
    path('Random/<int:id>/', showMovie),
]


