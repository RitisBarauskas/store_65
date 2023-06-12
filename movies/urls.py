from django.urls import path

from movies.views import (
    index,
    new_movies,
    movie_detail,
    movies_category,
    movies_director,
    stores,
    store_movies,
    create_movie,
    movie_to_store,
)

app_name='movies'

urlpatterns = [
    path('', index, name='main'),
    path('new_movies', new_movies, name='new_movies'),
    path('movie_detail/<int:movie_id>', movie_detail, name='movie_detail'),
    path('movies_category/<int:category_id>', movies_category, name='movies_category'),
    path('movies_director/<int:director_id>', movies_director, name='movies_director'),
    path('stores', stores, name='stores'),
    path('stores/<int:store_id>', store_movies, name='store_movies'),
    path('create_movie', create_movie, name='create_movie'),
    path('movie_to_store', movie_to_store, name='movie_to_store')
]