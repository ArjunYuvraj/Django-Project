from django.urls import path
from .views import *

urlpatterns = [
    path('habits/', habits, name='habits'),
    path('report/', report, name='report'),
    path('task/', task, name='task'),
    path('home/', home, name='home'),
    path('add_task/', add_task, name='add_task'),
    path('view_completed_task/', view_completed_task, name='view_completed_task'),
    path('view_inprogress_task/', view_inprogress_task, name='view_inprogress_task'),
    path('view_pending_task/', view_pending_task, name='view_pending_task'),
    path('edit_task/<int:task_id>/', edit_task, name='edit_task'),
    path('delete_task/<int:task_id>/', delete_task, name='delete_task'),
]
