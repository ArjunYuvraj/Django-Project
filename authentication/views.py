from django.shortcuts import render,redirect
from .models import User 
from django.contrib.auth import authenticate, login,logout  

# Create your views here.
def loginpage(request):
    if request.method == "POST":
    
        user=authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request,user)
            return redirect ('task/home/')

    return render(request, 'login.html')

def signup_page(request):
    if request.method == "POST":
        
        new_user = User( username= request.POST['username'],
                         first_name= request.POST['firstname'],
                         last_name=request.POST['lastname'],)
        new_user.set_password(request.POST['password'])
        new_user.save()
    return render(request, 'signup.html')
    return redirect('login')