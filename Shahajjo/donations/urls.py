from django.contrib import admin
from django.urls import path, include
from . import views as v
from HomePage import views as HP
from contact_application import views as CP
from donations import views

urlpatterns = [
    path('subdonation/', views.index2 , name = 'donations'), 

]
