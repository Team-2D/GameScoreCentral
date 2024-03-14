from django.shortcuts import render
from game.models import Game
from category.models import GameCategory
from django.db.models import Max


def home(request):
    # Get all categories
    category_list = GameCategory.objects.all()
    category_dict = {}

    # Query popular games based on last uploaded time
    popular_games = Game.objects.order_by('-id')[:4]

    # Query highest rated games based on average review score
    highest_rated_games = Game.objects.annotate(
        max_review=Max('average_review')).order_by('-max_review')[:4]

    for category in category_list:
        games_in_category = Game.objects.filter(category=category)
        category_dict[category] = games_in_category

    context_dict = {
        'category_dict': category_dict,
        'popular_games': popular_games,
        'highest_rated_games': highest_rated_games
    }

    return render(request, 'GameScoreCentral/home.html', context_dict)
