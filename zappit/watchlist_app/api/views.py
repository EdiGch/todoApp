from django.shortcuts import render
from rest_framework import status
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


@api_view(['POST', 'GET'])
def movie_list_v2(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        movie_serializer = MovieSerializer(movies, many=True)

        return Response(movie_serializer.data)

    if request.method == 'POST':
        movie_serializer = MovieSerializer(data=request.data)
        if movie_serializer.is_valid():
            movie_serializer.save()
            return Response(movie_serializer.data)
        else:
            return Response(movie_serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_details_v2(request, pk):
    if request.method == 'GET':
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        movie_serializer = MovieSerializer(movie)
        return Response(movie_serializer.data, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        movie = Movie.objects.get(pk=pk)
        movie_serializer = MovieSerializer(movie, data=request.data)
        if movie_serializer.is_valid():
            movie_serializer.save()
            return Response(movie_serializer.data)
        else:
            return Response(movie_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)