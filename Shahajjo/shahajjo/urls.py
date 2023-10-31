"""elearn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views as v
from HomePage import views as HP
from contact_application import views as CP
from donations import views
from link_app import views as LP


urlpatterns = [
    path('admin/', admin.site.urls),
    path('catAdmin/', v.index,name = 'catadmin'),
    path('insert/', v.insert,name='cat_insert'),
    path('', HP.homepage,name='HomePage.urls'),
    path('contact/', CP.cont_fun,name='contact.urls'),
    path('donations/', include('donations.urls')),
    path('link/', LP.index5,name = 'link.urls'),

]
