from django.shortcuts import render
from django.http import HttpResponse
from json_api import templates
from django.shortcuts import get_object_or_404

#index page
def index(request):
    return render(request, "index.html", context = None)
