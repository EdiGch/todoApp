from django.shortcuts import render
from .models import Movie
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
