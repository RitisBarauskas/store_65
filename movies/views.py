from datetime import date

from django.shortcuts import render, get_object_or_404

from .models import Movie, Category, Director, Store
from .helpers import query_debugger


@query_debugger
def index(request):
    """Главная страница."""
    movies = Movie.objects.select_related('director', 'category')
    context = {
        'movies': movies,
    }

    return render(request, 'index.html', context)


@query_debugger
def new_movies(request):
    """Отображение новых фильмов."""
    current_year = date.today().year
    movies = Movie.objects.filter(year=current_year)
    context = {
        'movies': movies,
        'year': current_year,
    }

    return render(request, 'movies/new_movies.html', context)


@query_debugger
def movie_detail(request, movie_id):
    """Отображение детальной информации о фильме."""
    movie = get_object_or_404(Movie, id=movie_id)
    context = {
        'movie': movie,
    }

    return render(request, 'movies/movie_detail.html', context)


@query_debugger
def movies_category(request, category_id):
    """Отображение фильмов по категориям."""
    category = get_object_or_404(Category, id=category_id)
    movies = category.movies.select_related('director')
    context = {
        'category': category,
        'movies': movies,
    }

    return render(request, 'movies/movies_category.html', context)


@query_debugger
def movies_director(request, director_id):
    """Отображение фильмов по режиссерам."""
    director = get_object_or_404(Director, id=director_id)
    movies = director.movies.select_related('category')
    context = {
        'director': director,
        'movies': movies,
    }

    return render(request, 'movies/movies_director.html', context)


@query_debugger
def stores(request):
    """Отображение магазинов."""
    stores = Store.objects.prefetch_related('movies__category', 'movies__director')
    context = {
        'stores': stores,
    }

    return render(request, 'movies/stores.html', context)


@query_debugger
def store_movies(request, store_id):
    """Отображение фильмов в магазине."""
    store = get_object_or_404(Store, id=store_id)
    movies = store.movies.select_related('director', 'category')
    context = {
        'store': store,
        'movies': movies,
    }

    return render(request, 'movies/store_movies.html', context)
