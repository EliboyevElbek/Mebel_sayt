from idlelib.rpc import request_queue

from django.contrib.auth.password_validation import password_changed
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm

# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_msg = "Unday foydalanuvchi topilmadi, to'g'ri kiriting yoki ro'yxatdan o'ting"
            return render(request, 'login.html', {'error_message':error_msg})
    else:
        return render(request, 'login.html', {})

def signup_user(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        signup = CustomUserCreationForm(request.POST)
        if signup.is_valid():
            signup.save()
            username = signup.cleaned_data['username']
            password = signup.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
            return redirect('signup')
    else:
        return render(request, 'signup.html', {'form':form})

def logout_user(requests):
    logout(requests)
    return redirect('home')
