from django.shortcuts import render, redirect,get_object_or_404
from .forms import *
from .models import *

# Create your views here.
def home(request):
    # Count tasks based on their status
    pending_count = Task.objects.filter(status='Pending').count()
    in_progress_count = Task.objects.filter(status='In Progress').count()
    completed_count = Task.objects.filter(status='Completed').count()

    # Pass the counts to the home template
    return render(request, 'home.html', {
        'pending_count': pending_count,
        'in_progress_count': in_progress_count,
        'completed_count': completed_count,
    })

def task(request):
    details = Task.objects.all()  # Fetch all tasks from the database
    return render(request, 'task.html', {'details': details})

def habits(request):
    return render(request,'habit.html')

def report(request):
    return render(request,'report.html')



def view_completed_task(request):
    details = Task.objects.filter(status='Completed')
    return render(request, 'view_completed_task.html', {
        'details': details,
        })    

def view_pending_task(request):
    details = Task.objects.filter(status='Pending')
    return render(request, 'view_pending_task.html', {
        'details': details,
        })   

def view_inprogress_task(request):
    details = Task.objects.filter(status='In Progress')
    return render(request, 'view_inprogress_task.html', {
        'details': details,
        })

def add_task(request):
    if request.method == "POST":
        form = Taskform(request.POST)
        if form.is_valid():
            form.save()
              # Replace 'success_url' with your desired redirect
        
            
    else:
        form = Taskform()
    
    return render(request, 'add_task.html', {'form': form})

def dashboard_view(request):
    total_tasks=Taskform.objects.count()
    context={
        'total_tasks': total_tasks
    }
    return render(request,'home.html')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.delete()
        return redirect('task')  # Redirect to the task list
    return render(request, 'delete_task.html', {'task': task})

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        form = Taskform(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task')  # Redirect to the task list
    else:
        form = Taskform(instance=task)
    return render(request, 'edit_task.html', {'form': form, 'task': task})

