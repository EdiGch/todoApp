from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from watchlist_app.models import Movie
from .serializers import MovieSerializer
from django.http import JsonResponse


def movi_list_v1(request):
    movies = Movie.objects.all()
    print(movies.values())
    data = {
        'movies': list(movies.values())
    }

    return JsonResponse(data)


def movie_details_v1(request, pk):
    movie = Movie.objects.get(pk=pk)
    data = {
        'name': movie.name,
        'description': movie.description,
        'active': movie.active,
    }
    return JsonResponse(data)


@api_view(['GET'])
def movie_list_v2(request):
    movies = Movie.objects.all()
    movie_serializer = MovieSerializer(movies, many=True)

    return Response(movie_serializer.data)


@api_view(['POST', 'GET'])
def movie_details_v2(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie_serializer = MovieSerializer(movie)
    return Response(movie_serializer.data)
