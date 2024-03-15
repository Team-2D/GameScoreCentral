from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve


class TestView(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testName',
            password='testPass'
        )



    def tearDown(self):
        self.user.delete()
        #Clean up run after every test method.
        pass

    def test_search_view(self):
        path = reverse('/search')
        assert resolve(path).view_name == 'searchGames'

