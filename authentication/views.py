from django.shortcuts import render
from .models import User   

# Create your views here.
def loginpage(request):
    if request.method == "POST":
        print(request.POST)

    return render(request, 'login.html')

def signup_page(request):
    if request.method == "POST":
        
        new_user = User( username= request.POST['username'],
                         first_name= request.POST['firstname'],
                         last_name=request.POST['lastname'],)
        new_user.set_password(request.POST['password'])
        new_user.save()
    return render(request, 'signup.html')