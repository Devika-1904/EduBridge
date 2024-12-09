from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def Donate(request):
    return render(request, 'Donate.html')

def receive(request):
    return render(request, 'receive.html')


def alumini(request):
    return render(request, 'alumini.html')
