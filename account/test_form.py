from django.test import TestCase
from account.forms import EditProfileForm

class EditProfileFormTest(TestCase):
    def test_edit_profile_form_valid(self):
        form_data = {
            'username':'test_name',
            'email':'<EMAIL>',
            'first_name':'firstname',
            'last_name':'lastname',
            'profile_picture':'abc.txt'
        }
        form = EditProfileForm(form_data)
        self.assertTrue(form.is_valid())

    def test_edit_profile_form_invalid(self):
        form_data = {
            'username':1.2,
            'email':'<EMAIL>',
            'first_name':'firstname',
            'last_name':'lastname',
            'profile_picture':12
        }
        form = EditProfileForm(form_data)
        self.assertFalse(form.is_valid())