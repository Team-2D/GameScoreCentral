from django.contrib.auth import get_user_model
from django.test import TestCase

from category.models import GameCategory
from game.models import Game


class TestGamesUrls(TestCase):

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
        self.user.save()
        self.category.save()
        self.game.save()
        self.user.set_password('testPass')
        self.client.login(username='testName', password='testPass')




    def tearDown(self):
        self.user.delete()
        #Clean up run after every test method.
        pass

    def test_search_url(self):
        response = self.client.get('/game/search/')
        self.assertEqual(response.status_code, 200)
    def test_new_game_url(self):
        response = self.client.get('/game/new/')
        self.assertEqual(response.status_code,200)

    def test_edit_url(self):
        response = self.client.get('/game/editReview/1/')
        print(response)
        self.assertEqual(response.status_code, 200)




