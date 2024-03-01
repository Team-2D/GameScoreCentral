from django.shortcuts import render


def signin(request):
    return render(request, 'GameScoreCentral/signin.html')


def signup(request):
    return render(request, 'GameScoreCentral/signup.html')
