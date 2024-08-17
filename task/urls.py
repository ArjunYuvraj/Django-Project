from django.urls import path
from task import views
from .views import *


urlpatterns = [
   
    
    path('habits/',habits ,name='habits'),
    path('tasks/',task ,name='tasks'),
    path('home/', home ,name='home'),
    
]