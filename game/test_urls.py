from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from category.models import GameCategory
from game.models import Game, GameReview


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

        self.GameReview = GameReview.objects.create(
            rating=4,
            comment='test comment',
            created_by=self.user,
            game=self.game,
        )

        self.user.save()
        self.category.save()
        self.game.save()
        self.user.set_password('testPass')
        self.client.login(username='testName', password='testPass')




    def tearDown(self):
        self.user.delete()
        self.category.delete()
        self.game.delete()
        self.GameReview.delete()
        #Clean up run after every test method.
        pass

    def test_search_url(self):
        response = self.client.get('/game/search/')
        self.assertEqual(response.status_code, 200)
    def test_new_game_url(self):
        response = self.client.get('/game/new/')
        self.assertEqual(response.status_code,200)

    def test_edit_url(self):
        url = reverse('editReview', kwargs={'review_id': self.GameReview.id})
        response = self.client.get(url)
        print(response)
        self.assertEqual(response.statu_code, 200)

    def test_view_url(self):
        url = reverse('viewGame', kwargs={'id': self.game.id})
        response = self.client.get(url)
        print(response)
        self.assertEqual(response.statu_code, 200)




