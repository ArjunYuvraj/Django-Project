from django.urls import path,include
from task import views
from .views import *


urlpatterns = [
   
    path('login',views.loginpage,name='login'),
    path('home/',views.base,name='base'),
    path('signup/',views.signup_page,name='signup'),
]