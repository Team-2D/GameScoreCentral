import os
from django.conf import settings
from django.core.files import File
from django.contrib.auth.models import User
from django.conf import settings
os.environ('DJANGO_SETTINGS_MODULE',
           'GameScoreCentral.settings')
import django
django.setup()
from game.models import Game, GameReview
from category.models import GameCategory

def populate():
    media_url = settings.MEDIA_URL
    user1 = User.objects.create_user(username='user1',password='password1')
    user2 = User.objects.create_user(username='user2',password='password2')

    rpg_games = [
        {'title': 'The Elder Scrols V: Skyrim',
         'description': 'The Elder Scrolls V: Skyrim is a fantasy action role-playing game, playable from either a first- or third-person perspective.',
         'release': 2011,
         'poster': os.path.join(media_url, 'game_posters', 'skyrim.jpg'),
         'game_studio': 'Bethesda',
         'posted_by':user1,
         'average_review': 9,
        }
    ]

    review_details = [
        {'rating': 9,
         'comment': "Its good",
         'created by':user2,
         'game': 'The Elder Scrols V: Skyrim',
         'created_at':'2024-03-11 12:00:00'
        }
    ]

    categories = {'RPG':{'games':rpg_games},}
    for cat, cat_data in categories.items():
        c = add_cat(cat)
        for g in cat_data['games']:
            game =add_game(g['title'],g['description'],g['release'],g['poster'],c,g['game_studio'],g['posted_by'],g['average_review'])
        
    for r in review_details:
        game_title = r['game']
        game = Game.Objects.get(title=game_title)
        add_review(r['rating'],r['comment'],r['created_by'],game,r['created_at'])

        
    
    

def add_game(title, description, release, poster,category,game_studio,posted_by,average_review):
    g = Game.objects.get_or_create(title=title, category=category)[0]
    g.description = description
    g.release = release
    g.poster = poster
    g.game_studio = game_studio
    g.posted_by = posted_by
    g.average_review = average_review
    g.save()
    return g

def add_review(rating,comment,created_by,game,created_at):
    r = GameReview.objects.get_or_create(game=game,created_by=created_by)[0]
    r.rating = rating
    r.comment = comment
    r.created_at = created_at
    r.save()

def add_cat(name):
    c = GameCategory.objects.get_or_create(title=name)[0]
    c.save()
    return c


    

        
