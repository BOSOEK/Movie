from django.urls import path
from MovieApp import views

urlpatterns = [
    path('', views.index),
]
