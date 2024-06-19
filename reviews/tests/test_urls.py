from django.test import SimpleTestCase
from django.urls import reverse, resolve
from budget.views import movies, movie_detail, reviews

class TestUrls(SimpleTestCase):
    # Test
    #def test(self)
    #    assert 1 == 2

    # Test de l'URL pour movies
    def test_movies_url_is_resolved(self):
        url = reverse('movies')
        print(resolve(url))
        self.assertEquals(resolve(url).func, movies)

    # Test de l'URL pour reviews
    def test_reviews_url_is_resolved(self):
        url = reverse('reviews')
        print(resolve(url))
        self.assertEquals(resolve(url).func, reviews)
