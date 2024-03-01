from django.shortcuts import render

# Create your views here.


def profilePage(request):
    # viewing own profile
    return render(request, 'account/profile.html')


def viewProfile(request, id):
    # viewing other user's profile

    context_dict = {'id': id}

    return render(request, 'account/viewProfile.html', context_dict)


def editProfile(request):
    # editing own profile
    return render(request, 'account/editProfile.html')
