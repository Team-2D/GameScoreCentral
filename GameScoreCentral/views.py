from django.shortcuts import render


def home(request):
    return render(request, 'GameScoreCentral/home.html')


def signin(request):
    return render(request, 'GameScoreCentral/signin.html')


def signup(request):
    return render(request, 'GameScoreCentral/signup.html')
