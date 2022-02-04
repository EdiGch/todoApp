from django.urls import path, include
from .views import movi_list_v1, movie_details_v1, movie_list_v2, movie_details_v2

urlpatterns = [  # Api movie
    path('v1/list/', movi_list_v1, name="movie-list-v1"),
    path('v1/<int:pk>', movie_details_v1, name="movie-details-v1"),

    path('v2/list/', movie_list_v2, name="movie-list-v2"),
    path('v2/<int:pk>', movie_details_v2, name="movie-details-v2"),
]
