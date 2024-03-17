from unittest import TestCase

from django.contrib.auth import get_user_model

from category.models import GameCategory


class TestCategory(TestCase):
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
        GameCategory = self.GameCategory.objects.filter(tilte='testTilte')


