from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'password', 'first_name', 'last_name', 'profile_picture',)
        

    #overrides the init method to remove the password confirmation
    #keeps form similar to wireframe
    def __init__(self,*args, **kargs):
        super(CustomUserCreationForm, self).__init__(*args, **kargs)
        del self.fields['password2']
        
    def save(self,commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data["password"]
        user.set_password(password)
        if commit:
            user.save()
        return user