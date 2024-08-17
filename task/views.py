from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def task(request):
    return render (request,'task.html')

def habits(request):
    return render(request,'habit.html')

def report(request):
    return render(request,'report.html')
    

