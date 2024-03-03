from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class UserFrom(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'password', 'first_name', 'last_name', 'profile_picture')