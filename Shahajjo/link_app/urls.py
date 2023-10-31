from django.contrib import admin
from django.urls import path, include
from . import views as v
from HomePage import views as HP
from link_app import views as LP

urlpatterns = [
    path('link', LP.index5,name = 'link.urls'),
    
]
