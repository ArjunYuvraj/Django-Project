from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def task(request):
    return render (request,'tasks.html')

def habits(request):
    return render(request,'habit.html')
    

