from django.db import models

class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    actors = models.ManyToManyField(Actor, related_name='movies')

    def __str__(self):
        return self.title

class Review(models.Model):
    grade = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return f"Review(s) pour {self.movie.title}"
