from django import forms
from .models import Game

class GameForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea, max_length=500)
    release_date = forms.IntegerField(min_value=1900, max_value=2100)
    class Meta:
        model = Game
        fields = ('title', 'description', 'release_date', 'poster', 'category', 'game_studio',)