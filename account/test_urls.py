from django.test import TestCase
from .models import CustomUser

class TestAccountUrls(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(username="testName",
                                                   password="testPass",
                                                   profile_picture='/profile_pictures/abc.jpg')
        self.user.set_password('testPass')
        loginSuccess = self.client.login(username='testName', password='testPass')
        print(loginSuccess)


    def tearDown(self):
        self.user.delete()
        pass

    def test_accounttest_will_pass(self):
        self.assertFalse(False)
        self.assertEqual(self.user.username, "testName")
        self.assertEqual(self.user.profile_picture, '/profile_pictures/abc.jpg')
        pass

    def test_profile_url(self):
        response = self.client.get('/account/profile/')
        self.assertEqual(response.status_code, 200)

    def test_edit_profile_url(self):
        response = self.client.get('/account/edit/')
        self.assertEqual(response.status_code,200)

    def test_view_profile_url(self):
        response = self.client.get('/account/view/testName')
        self.assertEqual(response.status_code,200)

    def test_logout_url(self):
        self.client.login(username='testName', password='testPass')
        response = self.client.get('/account/logout/')
        self.assertEqual(response.status_code,302)
        self.assertEqual(response['location'],'/')
