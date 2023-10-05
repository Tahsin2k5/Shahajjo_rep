from django.shortcuts import HttpResponse, render, redirect
from django.contrib import messages

from .models import Categories

def index(request):
    return render(request,'admin/cat.html')
def insert(request):
    cat_name = request.POST.get('name')

    if cat_name:
        cat_obj = Categories()
        cat_obj.name = cat_name
        cat_obj.save()
        messages.success(request, "Data inserted successfully")

        
    else:
        messages.success(request, "The field cannot be empty")
        


    # gender = request.POST.get('gender')
    # phn_number = request.POST.get('phn_number')
    # occupation = request.POST.get('occupation')
    # religion = request.POST.get('religion')
    # gender = request.POST.get('gender')
    # bank_no = request.POST.get('bank_no')

    # cat_obj = Categories()
    # cat_obj.name = cat_name
    # cat_obj.save()
    # messages.success(request, "Data inserted successfully")
    return redirect('catadmin')

    
    return HttpResponse(name)
