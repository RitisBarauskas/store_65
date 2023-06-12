from django import forms

from movies.models import Movie, StoreMovie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'


class MovieToStoreForm(forms.ModelForm):
    class Meta:
        model = StoreMovie
        fields = '__all__'