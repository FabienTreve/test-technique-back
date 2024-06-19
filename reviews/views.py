from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Actor, Movie, Review
from .serializers import MovieSerializer

@api_view(['GET'])
def movies(request):
    entries = Movie.objects.all()
    serializer = MovieSerializer(entries, many=True)
    return Response(serializer.data)
