from django.urls import path
from task import views
from .views import *


urlpatterns = [
   
    
    path('habits/',habits ,name='habits'),
    path('report/',report ,name='report'),
    path('task/',task ,name='task'),
    path('home/', home ,name='home'),
    
]