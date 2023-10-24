from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    
    path("", views.index , name='home'),

    path("about", views.about, name='about'),
    
    path("translator", views.translator, name='translator'),
    
    path('contact',views.contact,name='contact')
    
   
    



]