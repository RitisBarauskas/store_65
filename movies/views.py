from datetime import date

from django.shortcuts import render

from .constants import MOVIES


def index(request):
    """Главная страница."""
    context = {
        'movies': MOVIES,
    }

    return render(request, 'index.html', context)


def new_movies(request):
    """Отображение новых фильмов."""
    current_year = date.today().year
    new_movies = []
    for movie in MOVIES:
        if movie.get('year') == current_year:
            new_movies.append(movie)

    context = {
        'movies': new_movies,
        'year': current_year,
    }

    return render(request, 'movies/new_movies.html', context)


def movie_detail(request, movie_id):
    for movie in MOVIES:
        if movie.get('id') == movie_id:
            context = {
                'movie': movie,
            }
            return render(request, 'movies/movie_detail.html', context)
