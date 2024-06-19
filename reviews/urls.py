from django.urls import path
from . import views

urlpatterns = [
    #path("", views.home, name="home"),
    path("api/movies/", views.movies, name="movies"),
    path('api/movies/<int:id>/', views.movie_detail, name='movie-detail'),
    path("api/reviews/", views.reviews, name="reviews"),
]#