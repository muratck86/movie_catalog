from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username= username, password = password)
        if user is not None:
            auth.login(request, user)
            messages.add_message(request, messages.SUCCESS, "Login Successful")
            return redirect("index")
        else:
            messages.add_message(request, messages.ERROR, "Wrong username or password")
            return redirect("login")
    else:
        return render(request, "user/login.html")

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        if password != repassword:
            messages.add_message(request, messages.ERROR, "Passwords doesn't match.")
            return redirect("register")
        
        if User.objects.filter(username = username).exists():
            messages.add_message(request, messages.WARNING, "This username is already taken.")
            return redirect("register")
            
        if User.objects.filter(email = email).exists():
            messages.add_message(request, messages.WARNING, "This email already exists")
            return redirect("register")
      
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.add_message(request, messages.SUCCESS, "New user registered. ")
        return redirect("login")
    return render(request, "user/register.html")

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.add_message(request, messages.SUCCESS, "Logged out.")
    return redirect("index")