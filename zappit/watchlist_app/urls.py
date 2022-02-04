from django.urls import path, include
from .views import movi_list_v1

urlpatterns = [  # Api movie
    path('list/', movi_list_v1, name="movie-list-v1"),
]
