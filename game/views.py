from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import GameForm, GameReviewForm
from .models import Game, GameReview


# Create your views here.


def viewAllGames(request):
    return render(request, 'game/viewAllGames.html')


def viewGame(request, id):
    game = get_object_or_404(Game,id=id)
    reviews = GameReview.objects.filter(game=game)
    context_dict = {'game': game, 'reviews': reviews}
    return render(request, 'game/viewGame.html', context_dict)

@login_required
def addNewGame(request):
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            game = form.save(commit=False)
            game.posted_by = request.user   #posted_by is set to current user
            game.save()
            return redirect('game:viewGame', id=game.id)
    else:
        form = GameForm()
    return render(request, 'game/addNewGame.html', {'form': form})

@login_required 
def addReview(request):
    game_id = request.GET.get('game')   #get 'game' parameter from URL
    game = get_object_or_404(Game, id=game_id)  #get Game or return 404 error
    
    if request.method == 'POST':
        form = GameReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.game = game   #set game to one from url
            review.created_by = request.user
            #created_at is automatically set
            review.save()
            return redirect('game:viewGame', id=game.id)
    else:
        form = GameReviewForm()
    context_dict = {'form': form, 'game': game}
    return render(request, 'game/addReview.html', context_dict)

@login_required
def EditReview(request, review_id):
    game_id = request.GET.get('game')
    review = get_object_or_404(GameReview, id=review_id, created_by=request.user)
    game = get_object_or_404(Game, id=game_id)  #get Game or return 404 error
    if request.method == 'POST':
        form = GameReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('game:viewGame',id=game.id)
    else:
        form = GameReviewForm(instance=review)
    context_dict = {'form': form, 'game': game}
    return render(request, 'game/editreview.html', context_dict)