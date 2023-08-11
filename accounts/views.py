from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate




def login_(request):
    return render(request,"accounts/index-sign-in-up_.html")


from django.contrib.auth import authenticate, login ,logout


def logout_user(request):
    logout(request)
    return redirect('home')

def login_user(request):
    if request.method == 'POST':
        username1 = request.POST.get('username1')
        password1 = request.POST.get('password1')

        user = authenticate(request, username=username1, password=password1)

        if user is not None:
            login(request, user)  # Log in the user using the login function
            return redirect("home")
        else:
            return HttpResponse("Invalid Crediential")
    else:
        return HttpResponse("Not Found - 404")


def signup_user(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        if User.objects.filter(username=username).exists():
            return HttpResponse("Username already exists. Please choose a different username.")
        # errors:=
        myuser=User.objects.create_user(username,email,password)
        # myuser.first_name=username
        # d={"name":username}
        myuser.save()
        return render(request,"accounts/index-sign-in-up_.html")
    else:
        return HttpResponse("Not Found - 404")