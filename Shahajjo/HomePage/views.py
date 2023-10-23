# HomePage/views.py
from django.shortcuts import HttpResponse, render


def homepage(request):
    
    return HttpResponse("Eta hocchey Home Page")
