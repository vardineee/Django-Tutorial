from django.shortcuts import render
from movieFormApp import forms
from movieFormApp import models

# Create your views here.
def index(request):
    return render(request, 'movieApp/index.html')



def addMovie(request):
    form = forms.MovieForm()
    if request.method == "POST":
        form = forms.MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
    return render(request, 'movieApp/addMovie.html', {'form': form})



def listMovie(request):
    movies = models.Movie.objects.all()
    return render (request, 'movieApp/listMovie.html', {'movies': movies})
