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
         'description': 'The Elder Scrolls V: Skyrim is sprawling fantasy RPG with intresting questlines, epic combat and dark mysteries to uncover',
         'release': 2011,
         'poster': os.path.join(media_url, 'game_posters', 'skyrim.jpg'),
         'game_studio': 'Bethesda',
         'posted_by':user1,
         'average_review': 9,
        },
        {'title': 'Balders Gate 3',
         'description': "Balders Gate three is a massive DnD inspired RPG that puts true choice in the hands of it's players",
         'release': 2023,
         'poster': os.path.join(media_url, 'game_posters', 'Baldurs.jpg'),
         'game_studio': 'Larian Studios',
         'posted_by':user2,
         'average_review': 0,
        },
        {'title': 'Pokemon Pearl',
         'description': "Pokémon Pearl Version is a role-playing video game developed by Game Freak and published by The Pokémon Company and Nintendo for the Nintendo DS in 2006. It is one of the first installments in the fourth generation of the Pokémon video game series.",
         'release': 2006,
         'poster': os.path.join(media_url, 'game_posters', 'Pearl.jpg'),
         'game_studio': 'Game Freak',
         'posted_by':user1,
         'average_review': 0,
        },
        
    ]

    fps_games = [
        {'title': 'Call of Duty: Modern Warfare 3',
         'description': 'Call of Duty: Modern Warfare 3 has fast paced modern shooting PVP, aswell as a gripping single-player campaign.',
         'release': 2011,
         'poster': os.path.join(media_url, 'game_posters', 'MW3.jpg'),
         'game_studio': 'Infinity Ward',
         'posted_by':user2,
         'average_review': 8,

        },
         {'title': 'Apex Legends',
         'description': 'Apex legends is a free-to-play, fastbased battle royale. Pick your favourite hero and fight for glory!',
         'release': 2019,
         'poster': os.path.join(media_url, 'game_posters', 'Apex.jpg'),
         'game_studio': 'Respawn Entertainment',
         'posted_by':user1,
         'average_review': 0,

        },
        {'title': 'Doom Eternal',
         'description': 'Doom Eternal is a first-person shooter straight from hell. slash, shoot and punch through demons in this engergetic sequal to the critically acclaimed Doom (2016)',
         'release': 2020,
         'poster': os.path.join(media_url, 'game_posters', 'Doom.jpg'),
         'game_studio': 'id Software',
         'posted_by':user1,
         'average_review': 0,

        },
        {'title': 'Overwatch',
         'description': 'Overwatch is a competative online hero shooter.',
         'release': 2016,
         'poster': os.path.join(media_url, 'game_posters', 'ItsSoOver.jpg'),
         'game_studio': 'Blizzard Entertainment',
         'posted_by':user2,
         'average_review': 0,

        },
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
        },
        {
         'title': 'Sonic The Hedgehog (2006)',
         'description': 'Sonic the Hedgehog (2006) was realeased as a celebration of the 15th aniversary of the sonic franchise, in the hope to reboot the series',
         'release': 2006,
         'poster': os.path.join(media_url, 'game_posters', 'Sonic.jpg'),
         'game_studio': 'Sonic Team',
         'posted_by':user2,
         'average_review': 0,
        },
        {
         'title': 'Celeste',
         'description': 'Celeste is a indie platforming game where you help the protagnist Madoline climb celeste mountain and battle her depresssion and anxiety',
         'release': 2018,
         'poster': os.path.join(media_url, 'game_posters', 'Celeste.jpg'),
         'game_studio': 'Maddy Makes Games',
         'posted_by':user1,
         'average_review': 0,
        }
        
    ]

    arcade_games = [
        {
         'title': 'Tetris',
         'description': 'Tetris is a arcade game where you are tasked with arraning falling blocks. Try and last as long as you can in this never ending classic',
         'release': 1985,
         'poster': os.path.join(media_url, 'game_posters', 'Tetris.jpg'),
         'game_studio': 'Alexey Paitnov',
         'posted_by':user2,
         'average_review': 10,

        },
        {
         'title': 'Space invaders',
         'description': 'Shoot down aliens and defend your planet in this classic sci-fi shooter game',
         'release': 1978,
         'poster': os.path.join(media_url, 'game_posters', 'Invaders.jpg'),
         'game_studio': 'Taito',
         'posted_by':user1,
         'average_review': 0,

        },
    ]

    fighting_games = [
        {
         'title': 'Street Fighter 6',
         'description': 'Street Fighters combat is as good at ever in this fresh modern take on the series',
         'release': 2023,
         'poster': os.path.join(media_url, 'game_posters', 'Street.jpg'),
         'game_studio': 'Capcom',
         'posted_by':user2,
         'average_review': 7,
        },
        {
         'title': 'Tekken 7',
         'description': 'Fight your way through Tekken 7s coulourful cast of characters in this awesome 3-d fighting game',
         'release': 2015,
         'poster': os.path.join(media_url, 'game_posters', 'Tekken.jpg'),
         'game_studio': 'Bandai Namco Entertainment',
         'posted_by':user1,
         'average_review': 0,
        },
        {
         'title': 'Super Smash Bros. Ultimate ',
         'description': 'Smash is as good as ever with its newest installment on the Nintendo Switch, hop on with up to 7 of your friends for awesome cross-over fighting madness',
         'release': 2018,
         'poster': os.path.join(media_url, 'game_posters', 'Smash.jpg'),
         'game_studio': 'Nintendo',
         'posted_by':user2,
         'average_review': 0,
        },
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
        },
        {'rating': 0,
         'comment': "It ruined my Life",
         'created_by':user2,
         'game': 'Sonic The Hedgehog (2006)',
         'created_at':'2024-03-11 12:00:00'
        },
         {'rating': 7,
         'comment': "I like this game, but I'm bad at it :(",
         'created_by':user1,
         'game': 'Street Fighter 6',
         'created_at':'2024-03-11 12:00:00'
        },
        {'rating': 10,
         'comment': "I love blocks!",
         'created_by':user2,
         'game':'Tetris',
         'created_at':'2024-03-11 12:00:00'
        },

    ]

    categories = {'RPG':{'games':rpg_games}, 'FPS':{'games': fps_games}, 'Platformers':{'games': platforming_games}, 'Arcade Games':{'games': arcade_games}, 'Fighting Games':{'games': fighting_games}}
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


    

        
