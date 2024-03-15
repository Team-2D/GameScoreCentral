from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
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
                messages.error(request, 'Invalid username or password')
    else:
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
            print(form.errors)
            context = {'user_form': form, 'registered': registered}
            return render(request, 'GameScoreCentral/signup.html', context)
    else:
        form = CustomUserCreationForm()

    context = {'user_form': CustomUserCreationForm, 'registered': registered}
    return render(request, 'GameScoreCentral/signup.html', context)
