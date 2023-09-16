from django.shortcuts import render


def welcome_landing(request):
    return render(request, 'landingpage/index.html')


def signin(request):
    return render(request, 'auth/signin.html')


def signup(request):
    return render(request, 'auth/signup.html')
