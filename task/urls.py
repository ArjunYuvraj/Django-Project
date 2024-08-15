from django.urls import path,include
from task import views


urlpatterns = [
    path('',views.homepage,name='homepage'),
]