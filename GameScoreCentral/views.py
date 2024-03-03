from django.shortcuts import render
from .forms import UserForm, UserProfile

def signin(request):
    return render(request, 'GameScoreCentral/signin.html')


def signup(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfile(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            password = user_form.cleaned_data['password']
            user.set_password(password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfile()

    # Render the template with context variables
    return render(request, 'GameScoreCentral/signup.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered
    })