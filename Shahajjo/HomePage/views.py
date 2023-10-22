# HomePage/views.py
from django.shortcuts import HttpResponse


def homepage(request):
    
    return HttpResponse("Home er page eta")
