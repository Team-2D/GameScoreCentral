
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import GameForm, GameReviewForm, GameSearchForm
from .models import Game, GameReview
from django.contrib.auth.models import AnonymousUser
from category.models import GameCategory
from django.db.models import Avg



# Create your views here.



def viewAllGames(request):
    game_list = Game.objects.all()
    context_dict = {'game_list': game_list}
    return render(request, 'game/viewAllGames.html', context_dict) # game/game/viewAllGames.html


def viewGame(request, id):
    game = get_object_or_404(Game,id=id)
    user_reviews = GameReview.objects.filter(game=game, created_by=request.user.id)
    other_reviews = GameReview.objects.filter(game=game).exclude(created_by=request.user.id)
    context_dict = {'game': game, 'other_reviews': other_reviews, 'user_reviews': user_reviews}
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
            print(form.errors)
    else:
        form = GameForm()
    return render(request, 'game/addNewGame.html', {'form': form})


def addReview(request, id):
    game = get_object_or_404(Game, id=id)
    
    if request.method == 'POST':
        form = GameReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            if isinstance(request.user, AnonymousUser):
                review.created_by = None
            else:
                review.created_by = request.user
            review.game = game

            review.save()
            game.average_review = game.avg_review()
            game.save()
            return redirect('game:viewGame', id=game.id)
    else:
        form = GameReviewForm()
    context_dict = {'form': form, 'game': game}
    return render(request, 'game/addReview.html', context_dict)

@login_required
def editReview(request, review_id):
    review = get_object_or_404(GameReview, id=review_id, created_by=request.user)
    game_id = review.game.id
    game = get_object_or_404(Game, id=game_id)  #get Game or return 404 error
    if request.method == 'POST':
        form = GameReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            game.average_review = game.avg_review()
            game.save()
            return redirect('game:viewGame',id=game.id)
    else:
        form = GameReviewForm(instance=review)
    context_dict = {'form': form, 'game': game}
    return render(request, 'game/editreview.html', context_dict)


@login_required
def deleteReview(request, review_id):
    review = get_object_or_404(GameReview, pk=review_id)
    if request.user == review.created_by or request.user.is_staff:  #allows staff to remove reviews
        game_id = review.game.id                                    #get game_id to allow redirect to game after review is deleted
        game = review.game
        review.delete()
        game.average_review = game.avg_review()
        game.save()
        return redirect('game:viewGame', id=game_id)
    else:
        return redirect('game:viewGame')                            #if doesn't have the authority to delete then redirect them to this
    


def searchGames(request):
    games = Game.objects.all()
    form = GameSearchForm()
    
    if 'search' in request.GET:
        form = GameSearchForm(request.GET)
        if form.is_valid():
            query = Q()
            if form.cleaned_data['title']:
                query &= Q(title__icontains=form.cleaned_data['title'])
            if form.cleaned_data['game_studio']:
                query &= Q(game_studio__icontains=form.cleaned_data['game_studio'])
            if form.cleaned_data['genre']:
                query &= Q(category__title__icontains=form.cleaned_data['genre'])
            games = games.filter(query)
        else:
            print("Form Errors:", form.errors) 

    
    return render(request, 'game/search_games.html', {'games': games})

