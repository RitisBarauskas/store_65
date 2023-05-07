from django.urls import path

from movies.views import index, new_movies, movie_detail

urlpatterns = [
    path('', index, name='main'),
    path('new_movies', new_movies, name='new_movies'),
    path('movie_detail/<int:movie_id>', movie_detail, name='movie_detail'),
]