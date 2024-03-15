from django.contrib.auth import get_user_model
from django.test import TestCase


class TestUrl(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testName',
            password='testPass'
        )



    def tearDown(self):
        self.user.delete()
        #Clean up run after every test method.
        pass

    def test_search_url(self):
        response = self.client.get('/game/search/')
        self.assertEqual(response.status_code, 200)

    def test_edit_url(self):
        self.client.login(username='testName', password='testPass')
        response = self.client.get('/game/edit/1')
        self.assertEqual(response.status_code, 200)


