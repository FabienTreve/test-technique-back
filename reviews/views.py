from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Actor, Movie, Review
from .serializers import MovieSerializer, ReviewSerializer

@api_view(['GET'])
def movies(request):
    entries = Movie.objects.all()
    serializer = MovieSerializer(entries, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT'])
def movie_detail(request, id):
    if request.method == 'GET':
        try:
            movie = get_object_or_404(Movie, id=id)
            serializer = MovieSerializer(movie)
            return Response(serializer.data)
        except Movie.DoesNotExist:
            return Response({"message": "Movie not found"}, status=404)
    elif request.method == 'PUT':
        try:
            movie = get_object_or_404(Movie, id=id)
            serializer = MovieSerializer(movie, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Movie.DoesNotExist:
            return Response({"Error": f"Movie with id {id} does not exist"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST'])
def reviews(request):
    if request.method == 'GET':
        entries = Review.objects.all()
        serializer = ReviewSerializer(entries, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            movie_id = request.data.get('movie')
            try:
                movie_instance = Movie.objects.get(pk=movie_id)
                review = serializer.save(movie=movie_instance)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Movie.DoesNotExist:
                return Response({"Error": f"Movie with id {movie_id} does not exist"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)