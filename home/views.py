from django.shortcuts import render
import requests
from django.http import HttpResponse

TMDB_API_KEY = "1f00b3f0d90a5ef0e263f5d2a04c4ac9"

def search(request):

    query = request.GET.get('q')
    print(query)

    results = []
    if query:
        data = requests.get(f"https://api.themoviedb.org/3/search/tv?api_key={TMDB_API_KEY}&language=en-US&page=1&include_adult=false&query={query}")

    else:
        return HttpResponse("Please enter a search query")
    
    return render(request, 'home/results.html', {
        "data": data.json(),
        "type": request.GET.get("type")
    })


def index(request):
    return render(request, 'home/index.html')