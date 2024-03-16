from django import forms
from .models import Game, GameReview
from category.models import GameCategory

class GameForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea, max_length=500)
    release_date = forms.IntegerField(min_value=1900, max_value=2100)
    class Meta:
        model = Game
        fields = ('title', 'description', 'release_date', 'poster', 'category', 'game_studio',)

class GameReviewForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea, max_length=2000)
    rating = forms.IntegerField(min_value=1, max_value=10)
    class Meta:
        model = GameReview
        fields = ('rating', 'comment',)


class GameSearchForm(forms.Form):
    title = forms.CharField(required=False)
    game_studio = forms.CharField(required=False)
    genre = forms.CharField(required=False)
    