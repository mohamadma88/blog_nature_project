from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def user_login(request):
    if request.user.is_authenticated == True:
        return redirect('/')

    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/')
    return render(request, 'accounts_app/login.html')


def user_logout(request):
    logout(request)
    return redirect('/')
