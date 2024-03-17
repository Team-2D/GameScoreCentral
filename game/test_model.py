from django.test import TestCase

from category.models import GameCategory
from .models import Game
from django.contrib.auth import get_user_model


# Create your tests here.
class TestGameModel(TestCase):
    # 创建得时候执行的
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

    # 测试类销货执行的
    def tearDown(self):
        self.user.delete()
        self.category.delete()
        self.game.delete()
    #运行得时候执行的
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
        print("=======test Over==========")