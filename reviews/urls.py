from rest_framework.routers import DefaultRouter
from django.urls import path,include
from . import views

router = DefaultRouter()
router.register(r'movies', views.MovieViewSet)
router.register(r'reviews', views.ReviewViewSet)
router.register(r'actors', views.ActorViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
