from django.urls import path
from .views import *

urlpatterns = [
    
    path('', loginpage, name='login'),
    path('signup/',signup_page),
]