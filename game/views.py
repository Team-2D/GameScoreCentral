from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import GameForm


# Create your views here.


def viewAllGames(request):
    return render(request, 'game/viewAllGames.html')


def viewGame(request, id):
    context_dict = {'id': id}
    return render(request, 'game/viewGame.html', context_dict)

@login_required 
def addNewGame(request):
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            game = form.save(commit=False)
            game.posted_by = request.user   #posted_by is set to current user
            game.save()
            return redirect('')
    else:
        form = GameForm()
    return render(request, 'game/addNewGame.html', {'form': form})
