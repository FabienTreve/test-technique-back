# serializers.py
from rest_framework import serializers
from .models import Actor, Movie, Review
from django.db.models import Avg

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__' 

class MovieSerializer(serializers.ModelSerializer):
    actors = serializers.SerializerMethodField()
    average_grade = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'actors', 'average_grade')

    # Permet l'affichage des noms des acteurs dans l'API, au lieu de leurs id
    def get_actors(self, obj):
        if obj.actors.exists():
            return [f"{actor.first_name} {actor.last_name}" for actor in obj.actors.all()]
        else:
            return []

    def get_average_grade(self, obj):
        reviews = Review.objects.filter(movie=obj)
        if reviews.exists():
            return reviews.aggregate(average_grade=Avg('grade'))['average_grade']
        return None

class ReviewSerializer(serializers.ModelSerializer):
    movie = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ('id', 'grade', 'movie')

    def get_movie(self, obj):
        movie = obj.movie
        if movie:
            return f"{movie.title}"
        return None

    def create(self, validated_data):
        return Review.objects.create(movie=validated_data['movie'], grade=validated_data['grade'])
