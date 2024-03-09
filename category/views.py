from django.shortcuts import render
from game.models import Game
from category.models import GameCategory

# Create your views here.

def home(request):
    category_list = GameCategory.objects.all()
    category_dict = {}

    for category in category_list:
        games_in_category = Game.objects.filter(category=category)
        category_dict[category] = games_in_category

    context_dict = {'category_dict': category_dict}

    return render(request, 'GameScoreCentral/home.html', context_dict)
