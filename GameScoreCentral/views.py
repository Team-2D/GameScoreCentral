from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('/')  # redirect to homepage 
            else:
                return HttpResponse("Your account has been deactivated")
        else:
            error = "Invalid login details, please try again"
            context = {"error": error}
            return render(request, 'GameScoreCentral/signin.html', context)
    return render(request, 'GameScoreCentral/signin.html')


def signup(request):
    registered = False  
    if request.method == 'POST':
        # request.FILES is required to handle the profile_picture
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            registered = True
        else:
            context = {'user_form': form, 'registered': registered}
            return render(request, 'GameScoreCentral/signup.html', context)
    else:
        form = CustomUserCreationForm()

    context = {'user_form': CustomUserCreationForm, 'registered': registered}
    return render(request, 'GameScoreCentral/signup.html', context)
