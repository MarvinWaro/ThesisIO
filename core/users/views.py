from django.shortcuts import render


def welcome_landing(request):
    return render(request, 'landingpage/index.html')


def admin_dashboard(request):
    return render(request, 'admin/dashboard.html')


def signin(request):
    return render(request, 'auth/signin.html')


def signup(request):
    return render(request, 'auth/signup.html')