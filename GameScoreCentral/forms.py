from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        #automatically handles passwords
        model = User
        fields = ('username', 'email', 'first_name', 'last_name','profile_picture',)
