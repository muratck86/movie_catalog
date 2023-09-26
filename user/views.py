from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username= username, password = password)
        if user is not None:
            auth.login(request, user)
            print("login successful")
            return redirect("index")
        else:
            print("fail")
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
            print("passwords doesn't match")
            return redirect("register")
        
        if User.objects.filter(username = username).exists():
            print ("this username is already taken")
            return redirect("register")
            
        if User.objects.filter(email = email).exists():
            print ("this email is already exists")
            return redirect("register")
      
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        print("User registered")
        return redirect("login")
    return render(request, "user/register.html")

def logout(request):
    return render(request, "user/logout.html")