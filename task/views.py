from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,'homepage.html')

def base(request):
    return render(request, 'base.html')

def loginpage(request):
    return render(request, 'login.html')

def signup_page(request):
    return render(request, 'signup.html')