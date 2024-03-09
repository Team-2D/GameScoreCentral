from django.shortcuts import render
from game.models import Game


# Create your views here.



def viewAllGames(request):
    game_list = Game.objects.all()
    context_dict = {'game_list': game_list}
    return render(request, 'game/viewAllGames.html', context_dict)


def viewGame(request, id):
    context_dict = {'id': id}
    return render(request, 'game/viewGame.html', context_dict)


def addNewGame(request):
    return render(request, 'game/addNewGame.html')
