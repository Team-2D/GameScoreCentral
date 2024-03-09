from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import CustomUser
from game.models import GameReview

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
    user_info = get_object_or_404(CustomUser, username=username)
    user_reviews = GameReview.objects.filter(created_by=user_info)

    context_dict = {'user_info': user_info,
                    'user_reviews': user_reviews}

    return render(request, 'account/viewProfile.html', context_dict)


def editProfile(request):
    # editing own profile
    return render(request, 'account/editProfile.html')
