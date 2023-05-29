from django.contrib import admin

from movies.models import Movie, Director, Category, Store

admin.site.register(Movie)
admin.site.register(Director)
admin.site.register(Category)
admin.site.register(Store)