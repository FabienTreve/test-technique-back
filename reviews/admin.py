from django.contrib import admin
from .models import Actor, Movie, Review

models = [Actor, Movie, Review]
admin.site.register(models)