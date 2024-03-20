from django.test import TestCase

from category.models import GameCategory
from .models import Game, GameReview
from django.contrib.auth import get_user_model


# Create your tests here.
class TestGameModel(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testName',
            password='testPass'
        )

        self.category = GameCategory.objects.create(
            title='testCategory'
        )

        self.game = Game.objects.create(
            title='testcategory',
            description='description',
            release_data=123,
            poster='testposter/',
            game_studio='testStudio',
            category=self.category,
            posted_by=self.user,
        )

        self.GameReview = GameReview.objects.create(
            rating=4,
            comment='test comment',
            created_by=self.user,
            game=self.game,
        )

    def tearDown(self):
        self.user.delete()
        self.category.delete()
        self.game.delete()
        self.GameReview.delete()

    def test_game_model(self):
        print("=======test Start==========")
        game = Game.objects.filter(title='testcategory').first()
        print(game.release_data)
        self.assertEqual(game.title,'testcategory')
        self.assertEqual(game.description,'description')
        self.assertEqual(game.release_data,123)
        self.assertEqual(game.posted_by.username,'testName')
        self.assertEqual(game.poster,'testposter/')
        self.assertEqual(game.game_studio,'testStudio')
        self.assertEqual(game.average_review,0)
        self.assertEqual(self.GameReview.rating,4)
        self.assertEqual(self.GameReview.comment,'test comment')
        self.assertEqual(self.GameReview.created_by,self.user)
        self.assertEqual(self.GameReview.game,self.game)
        print("=======test Over==========")