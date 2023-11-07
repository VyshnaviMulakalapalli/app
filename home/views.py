from django.shortcuts import render
import requests
from django.http import HttpResponse,JsonResponse

TMDB_API_KEY = "1f00b3f0d90a5ef0e263f5d2a04c4ac9"

def search(request):

    query = request.GET.get('q')
    

    results = []
    if query:
        data = requests.get(f"https://api.themoviedb.org/3/search/{request.GET.get('type')}?api_key={TMDB_API_KEY}&language=en-US&page=1&include_adult=false&query={query}")

    else:
        return HttpResponse("Please enter a search query")
    
    return render(request, 'home/results.html', {
        "data": data.json(),
        "type": request.GET.get("type")
    })


def index(request):
    return render(request, 'home/index.html')

def view_tv_detail(request, tv_id):
    data = requests.get(f"https://api.themoviedb.org/3/tv/{tv_id}?api_key={TMDB_API_KEY}&language=en-US")
    recommendations = requests.get(f"https://api.themoviedb.org/3/tv/{tv_id}/recommendations?api_key={TMDB_API_KEY}&language=en-US")
    return render(request, "home/tv_detail.html", {
        "data": data.json(),
        "recommendations": recommendations.json(),
        "type": "tv"
    })

def view_movie_detail(request, movie_id):
    data = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US")
    recommendations = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key={TMDB_API_KEY}&language=en-US")
    return render(request, "home/movie_detail.html", {
        "data": data.json(),
        "recommendations": recommendations.json(),
        "type": "movie"
    })

def view_trendings_results(request):
    type = request.GET.get("media_type")
    time_window = request.GET.get("time_window")

    trendings = requests.get(f"https://api.themoviedb.org/3/trending/{type}/{time_window}?api_key={TMDB_API_KEY}&language=en-US")
    return JsonResponse(trendings.json())