from django.urls import path,include
from task import views
from .views import *


urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('base/',views.base,name='base'),
]