# HomePage/views.py
from django.shortcuts import HttpResponse, render

from shahajjo.models import Categories


def index5(request):

    data = Categories.objects.all()
    cat = {'all_cat':data}
    
    return render(request,'link_app/link_app.html', cat)
