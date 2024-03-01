from django.shortcuts import render

# Create your views here.


def viewAllGames(request):
    return render(request, 'game/viewAllGames.html')


def viewGame(request, id):
    context_dict = {'id': id}
    return render(request, 'game/viewGame.html', context_dict)


def addNewGame(request):
    return render(request, 'game/addNewGame.html')
