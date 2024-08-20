from django.shortcuts import render, redirect
from .forms import *

# Create your views here.
def home(request):
    return render(request,'home.html')

def task(request):
    return render (request,'task.html')

def habits(request):
    return render(request,'habit.html')

def report(request):
    return render(request,'report.html')



def view_completed_task(request):
    return render(request, 'view_completed_task.html')    

def view_pending_task(request):
    return render(request, 'view_pending_task.html')    

def view_inprogress_task(request):
    return render(request, 'view_inprogress_task.html')

def add_task(request):
    if request.method == "POST":
        form = Taskform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Replace 'success_url' with your desired redirect
        
            
    else:
        form = Taskform()
    
    return render(request, 'add_task.html', {'form': form})
      

