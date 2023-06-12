from django.db import models

from core.models import TimeStampModel


class Director(TimeStampModel):
    name = models.CharField(max_length=200, verbose_name='Имя')
    age = models.IntegerField(verbose_name='Возраст')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Режиссер'
        verbose_name_plural = 'Режиссеры'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name}, которому сейчас {self.age} лет, о котором думают: {self.description}'


class Category(TimeStampModel):
    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Movie(TimeStampModel):
    title = models.CharField(max_length=200, verbose_name='Название')
    year = models.IntegerField(verbose_name='Год выхода')
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies', verbose_name='Режиссер')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='movies', verbose_name='Категория')

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
        ordering = ('id',)

    def __str__(self):
        return self.title


class Store(TimeStampModel):
    name = models.CharField(max_length=200, verbose_name='Название')
    address = models.CharField(max_length=200, verbose_name='Адрес')
    movies = models.ManyToManyField(Movie, related_name='stores', verbose_name='Фильмы', through='StoreMovie')

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'
        ordering = ('name',)

    def __str__(self):
        return self.name


class StoreMovie(TimeStampModel):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='store_movies', verbose_name='Магазин')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='store_movies', verbose_name='Фильм')
    quantity = models.IntegerField(verbose_name='Количество')

    class Meta:
        verbose_name = 'Фильм в магазине'
        verbose_name_plural = 'Фильмы в магазинах'
        ordering = ('id',)

    def __str__(self):
        return f'{self.movie} в {self.store} в количестве {self.quantity}'
