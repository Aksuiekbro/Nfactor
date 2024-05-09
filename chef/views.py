from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import Http404
import requests

def home(request):
    return render(request, "chef/home.html")


def index(request, user_input):
    # Replace with your Edamam API key
    api_key = "f9cc26a944dbad90ab73e6782578cf6e"

    # Base URL for the API
    base_url = "https://api.edamam.com/api/recipes/v2?type=public&app_id=f3673165&app_key=58557ae2bb7beefab30f921e98ce42dc"

    # Example search parameters (modify as needed)
    params = {
        "q": user_input,  # Search query (e.g., ingredients, cuisine)
        "app_id": "f3673165",  # Your Edamam app ID (obtain from Edamam)
        "app_key": api_key,  # Replace with your API key
        "count": 1,  # Number of recipes to return (maximum 10)
    }

    # Send the GET request
    response = requests.get(base_url, params=params)
    list_of_recipes = []
    for i in response.json()['hits']:
        list_of_recipes.append((i['recipe']['label'], [j for j in i['recipe']['ingredientLines']]))
    return render(request, "chef/index.html", {"list_of_recipes": list_of_recipes})


