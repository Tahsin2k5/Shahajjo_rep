# HomePage/views.py
from django.shortcuts import HttpResponse, render

from shahajjo.models import Categories


def homepage(request):

    data = Categories.objects.all()
    cat = {'all_cat':data}
    
    return render(request,'homepage/about.html', cat)
