from datetime import datetime
import os
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'GameScoreCentral.settings'
django.setup()
from django.conf import settings
from django.core.files import File
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
from game.models import Game, GameReview
from category.models import GameCategory
from account.models import CustomUser

def populate():
    media_url = settings.MEDIA_URL
    user1 = CustomUser.objects.create_user(username='user1',password='password1', profile_picture=os.path.join(media_url, 'profile_pictures', 'user1.jpg'))
    user2 = CustomUser.objects.create_user(username='user2',password='password2', profile_picture=os.path.join(media_url, 'profile_pictures', 'user2.jpg'))

    rpg_games = [
        {'title': 'The Elder Scrols V: Skyrim',
         'description': 'The Elder Scrolls V: Skyrim is a fantasy action role-playing game, playable from either a first- or third-person perspective.',
         'release': 2011,
         'poster': os.path.join(media_url, 'game_posters', 'skyrim.jpg'),
         'game_studio': 'Bethesda',
         'posted_by':user1,
         'average_review': 9,
        },
        {'title': 'Balders Gate 3',
         'description': "The game is the third main installment in the Baldur's Gate series, based on the tabletop fantasy role-playing system of Dungeons & Dragons.",
         'release': 2023,
         'poster': os.path.join(media_url, 'game_posters', 'Baldurs.jpg'),
         'game_studio': 'Larian Studios',
         'posted_by':user2,
         'average_review': 0,
        }
    ]

    fps_games = [
        {'title': 'Call of Duty: Modern Warfare 3',
         'description': 'Call of Duty: Modern Warfare 3 is a 2011 first-person shooter video game',
         'release': 2011,
         'poster': os.path.join(media_url, 'game_posters', 'MW3.jpg'),
         'game_studio': 'Infinity Ward',
         'posted_by':user2,
         'average_review': 8,

        }
    ]
    
    platforming_games = [
        {
         'title': 'Super Mario Bros. Wonder',
         'description': 'The player controls Mario, Luigi, and their friends as they attempt to stop Bowser, who plots to take over a new land known as the Flower Kingdom after using the magical Wonder Flower to fuse himself with the kingdoms castle.',
         'release': 2023,
         'poster': os.path.join(media_url, 'game_posters', 'SuperMarioWonder.jpg'),
         'game_studio': 'Nintendo',
         'posted_by':user1,
         'average_review': 10,
        } 
        
    ]



    review_details = [
        {'rating': 9,
         'comment': "Its good",
         'created_by':user2,
         'game': 'The Elder Scrols V: Skyrim',
         'created_at':'2024-03-11 12:00:00'
        },
        {'rating': 8,
         'comment': "Its pretty good, great shooting",
         'created_by':user1,
         'game': 'Call of Duty: Modern Warfare 3',
         'created_at':'2024-03-11 12:00:00'
        },
        {'rating': 10,
         'comment': "It changed my life",
         'created_by':user1,
         'game': 'Super Mario Bros. Wonder',
         'created_at':'2024-03-11 12:00:00'
        }

    ]

    categories = {'RPG':{'games':rpg_games}, 'FPS':{'games': fps_games}, 'Platformers':{'games': platforming_games}}
    for cat, cat_data in categories.items():
        c = add_cat(cat)
        for g in cat_data['games']:
            game =add_game(g['title'],g['description'],g['release'],g['poster'],c,g['game_studio'],g['posted_by'],g['average_review'])
        
    for r in review_details:
        game_title = r['game']
        game = Game.objects.get(title=game_title)
        add_review(r['rating'],r['comment'],r['created_by'],game,r['created_at'])

        
    
    

def add_game(title, description, release, poster,category,game_studio,posted_by,average_review):
    g = Game.objects.get_or_create(title=title, category=category, release_data=release,description = description,poster = poster, game_studio = game_studio, posted_by = posted_by, average_review = average_review)[0]
    g.save()
    return g

def add_review(rating,comment,created_by,game,created_at):
    created_at_datetime = datetime.strptime(created_at, '%Y-%m-%d %H:%M:%S')
    created_at_aware = timezone.make_aware(created_at_datetime)
    r = GameReview.objects.get_or_create(game=game,created_by=created_by, rating = rating, comment=comment, created_at=created_at_aware)[0]
    
    r.save()

def add_cat(name):
    c = GameCategory.objects.get_or_create(title=name)[0]
    c.save()
    return c

if __name__ == '__main__':
    print('Starting population script...')
    populate()


    

        
