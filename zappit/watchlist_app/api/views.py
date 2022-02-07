from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from watchlist_app.models import Movie, WatchList, StreamPlatform
from .serializers import MovieSerializer, WatchListSerializer, StreamPlatformSerializer
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


class MovieListAVV3(APIView):

    def get(self, request, format=None):
        movies = Movie.objects.all()
        movie_serializer = MovieSerializer(movies, many=True)

        return Response(movie_serializer.data)

    def post(self, request):
        movie_serializer = MovieSerializer(data=request.data)
        if movie_serializer.is_valid():
            movie_serializer.save()
            return Response(movie_serializer.data)
        else:
            return Response(movie_serializer.errors)


class MovieDetailsAVV3(APIView):

    def get(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        movie_serializer = MovieSerializer(movie)
        return Response(movie_serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        movie_serializer = MovieSerializer(movie, data=request.data)
        if movie_serializer.is_valid():
            movie_serializer.save()
            return Response(movie_serializer.data)
        else:
            return Response(movie_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, instance, pk):
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WatchListAVV4(APIView):

    def get(self, request, format=None):
        watch_list = WatchList.objects.all()
        watch_list_serializer = WatchListSerializer(watch_list, many=True)

        return Response(watch_list_serializer.data)

    def post(self, request):
        watch_list_serializer = WatchListSerializer(data=request.data)
        if watch_list_serializer.is_valid():
            watch_list_serializer.save()
            return Response(watch_list_serializer.data)
        else:
            return Response(watch_list_serializer.errors)


class WatchDetailsAVV4(APIView):

    def get(self, request, pk):
        try:
            watch_list = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        watch_list_serializer = WatchListSerializer(watch_list)
        return Response(watch_list_serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        watch_list_serializer = WatchListSerializer(movie, data=request.data)
        if watch_list_serializer.is_valid():
            watch_list_serializer.save()
            return Response(watch_list_serializer.data)
        else:
            return Response(watch_list_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, instance, pk):
        watch_list = WatchList.objects.get(pk=pk)
        watch_list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StreamPlatformListAVV4(APIView):

    def get(self, request, format=None):
        stream_platforms = StreamPlatform.objects.all()
        stream_platforms_list_serializer = StreamPlatformSerializer(stream_platforms, many=True)

        return Response(stream_platforms_list_serializer.data)

    def post(self, request):
        stream_platforms_list_serializer = StreamPlatformSerializer(data=request.data)
        if stream_platforms_list_serializer.is_valid():
            stream_platforms_list_serializer.save()
            return Response(stream_platforms_list_serializer.data)
        else:
            return Response(stream_platforms_list_serializer.errors)


class StreamPlatformDetailsAVV4(APIView):

    def get(self, request, pk):
        try:
            stream_platforms = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        stream_platforms_list_serializer = StreamPlatformSerializer(stream_platforms)
        return Response(stream_platforms_list_serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        stream_platforms = StreamPlatform.objects.get(pk=pk)
        stream_platforms_list_serializer = StreamPlatformSerializer(stream_platforms,
                                                                    data=request.data)
        if stream_platforms_list_serializer.is_valid():
            stream_platforms_list_serializer.save()
            return Response(stream_platforms_list_serializer.data)
        else:
            return Response(stream_platforms_list_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def delete(self, instance, pk):
        watch_list = StreamPlatform.objects.get(pk=pk)
        watch_list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
