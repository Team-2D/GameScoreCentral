from django.urls import path, include
from category import views
from unittest import TestCase
from django.contrib.auth import get_user_model
from category.models import GameCategory

class TestUrls(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testName',
            password='testPass'
        )

        self.GameCategory = GameCategory.objects.create(
            title='testTilte'
        )



    def tearDown(self):
        self.user.delete()
        self.GameCategory.delete()

    def test_game_category(self):
        exist = GameCategory.objects.filter(title='testTitle').exists()
        self.assertTrue(exist)
    def test_home_url(self):
        response = self.client.get('/category/')
        self.assertEqual(response.status_code, 200)