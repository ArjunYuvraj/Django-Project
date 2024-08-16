from django.urls import path
from task import views
from .views import *


urlpatterns = [
   
    
    path('home/',views.base,name='base'),
    
]