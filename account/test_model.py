from unittest import TestCase
from .models import CustomUser

class TestAccountModel(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(username="testName",
                                                   password="testPass",
                                                   profile_picture='/profile_pictures/abc.jpg')

    def tearDown(self):
        self.user.delete()
        pass

    def test_accounttest_will_pass(self):
        self.assertFalse(False)
        self.assertEqual(self.user.username, "testName")
        self.assertEqual(self.user.profile_picture, '/profile_pictures/abc.jpg')
        pass
