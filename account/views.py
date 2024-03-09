from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from game.models import GameReview
from .forms import EditProfileFrom

# Create your views here.

@login_required
def profilePage(request):
    #viewing own profile
    user_info = request.user
    user_reviews = GameReview.objects.filter(created_by=request.user)

    context_dict = {
        'user_info': user_info,
        'user_reviews': user_reviews,
    }

    return render(request, 'account/profile.html', context_dict)


def viewProfile(request, username):
    #viewing other profiles
    user_info = get_object_or_404(CustomUser, username=username)
    user_reviews = GameReview.objects.filter(created_by=user_info)

    context_dict = {'user_info': user_info,
                    'user_reviews': user_reviews}

    return render(request, 'account/viewProfile.html', context_dict)

@login_required
def editProfile(request):
    if request.method == 'POST':
        form = EditProfileFrom(request.POST, request.FILES, instance=request.user)
        if form.us_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileFrom(instance=request.user)
    return render(request, 'account/editProfile.html', {'form':form})
