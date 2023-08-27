from django.shortcuts import HttpResponse, render
def index(request):
    return render(request,'admin/cat.html')
def insert(request):
    name = request.POST.get('name')
    gender = request.POST.get('gender')
    phn_number = request.POST.get('phn_number')
    occupation = request.POST.get('occupation')
    religion = request.POST.get('religion')
    gender = request.POST.get('gender')
    bank_no = request.POST.get('bank_no')

    
    return HttpResponse(name)
