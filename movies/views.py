from django.shortcuts import render, get_object_or_404
from .models import Movie
from django.http import Http404

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {"movies": movies}
    return render(request, "movies/list.html", context)

def details(request, movie_id:int):
    # movie = _check_does_not_exist(Movie, Movie.objects.get, pk=movie_id) # alternative way
    movie = get_object_or_404(Movie, pk=movie_id)
    context = {"movie": movie}
    return render(request, "movies/details.html", context)

def search(request):
    return render(request, "movies/search.html")

def _check_does_not_exist(obj, method, **kwargs):
    try:
        result = method(**kwargs)
    except Movie.DoesNotExist:
        raise Http404(f"Requested {obj.__name__} not found.")
    return result
