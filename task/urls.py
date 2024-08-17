from django.urls import path
from task import views
from .views import *


urlpatterns = [
   
    
    path('home/', base ,name='base'),
    path('task/', task ,name='base'),
    
]