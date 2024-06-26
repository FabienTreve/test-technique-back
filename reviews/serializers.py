from rest_framework import serializers
from .models import Actor, Movie, Review
from django.db.models import Avg

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    actors_display = serializers.SerializerMethodField()
    average_grade = serializers.SerializerMethodField()
    actors = ActorSerializer(many=True, required=False)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'actors', 'actors_display', 'average_grade']

    def get_actors_display(self, obj):
        if obj.actors.exists():
            return [f"{actor.first_name} {actor.last_name}" for actor in obj.actors.all()]
        else:
            return []

    def get_average_grade(self, obj):
        reviews = Review.objects.filter(movie=obj)
        if reviews.exists():
            return reviews.aggregate(average_grade=Avg('grade'))['average_grade']
        return None

    def update(self, instance, validated_data):
        actors_data = validated_data.pop('actors', None)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.save()

        if actors_data is not None:
            for actor_data in actors_data:
                actor, created = Actor.objects.get_or_create(**actor_data)
                instance.actors.add(actor)

        return instance

class ReviewSerializer(serializers.ModelSerializer):
    movie = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all())

    class Meta:
        model = Review
        fields = ('id', 'grade', 'movie')

    def get_movie(self, obj):
        movie = obj.movie
        if movie:
            return f"{movie.title}"
        return None

    def create(self, validated_data):
        movie_id = validated_data.pop('movie').id
        review = Review.objects.create(movie_id=movie_id, **validated_data)
        return review
