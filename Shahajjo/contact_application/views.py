from django.shortcuts import HttpResponse, render


def cont_fun(request):
    
    return render(request,'contact_app/contact.html')