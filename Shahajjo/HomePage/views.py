# HomePage/views.py
from django.shortcuts import HttpResponse, render


def homepage(request):
    
    return render(request,'homepage/about.html')
