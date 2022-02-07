from django.urls import path, include
from .views import movi_list_v1, movie_details_v1, movie_list_v2, movie_details_v2, MovieListAVV3, \
    MovieDetailsAVV3, WatchListAVV4, WatchDetailsAVV4, StreamPlatformListAVV4, \
    StreamPlatformDetailsAVV4

urlpatterns = [  # Api movie
    path('v1/list/', movi_list_v1, name="movie-list-v1"),
    path('v1/<int:pk>', movie_details_v1, name="movie-details-v1"),

    path('v2/list/', movie_list_v2, name="movie-list-v2"),
    path('v2/<int:pk>', movie_details_v2, name="movie-details-v2"),

    path('v3/list/', MovieListAVV3.as_view(), name="movie-list-v3"),
    path('v3/<int:pk>', MovieDetailsAVV3.as_view(), name="movie-details-v3"),

    path('v4/list/', WatchListAVV4.as_view(), name="movie-list-v4"),
    path('v4/<int:pk>', WatchDetailsAVV4.as_view(), name="movie-details-v4"),

    path('v4/stream-platform/list/', StreamPlatformListAVV4.as_view(), name="stream-platform-v4"),
    path('v4/stream-platform/<int:pk>', StreamPlatformDetailsAVV4.as_view(),
         name="stream-platform--details-v4"),
]
