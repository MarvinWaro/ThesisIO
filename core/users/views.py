from django.shortcuts import render


def welcome_landing(request):
    return render(request, 'landingpage/index.html')
