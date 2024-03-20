from django.test import TestCase
from game.forms import GameForm, GameReviewForm, GameSearchForm


# 1. Testing form validation
# 2. testing field validation
# 3. Testing Form Interaction with Database Models


class GameFormTest(TestCase):

    def test_game_form_valid(self):
        form_data = {
            'title':'FormTile',
            'description':'FormFes',
            'releas_data':123,
            'poster':'/static/img',
            'category':1,
            'game_studio':'test studio'
        }
        form = GameForm(form_data)
        self.assertTrue(form.is_valid())
    def test_game_form_invalid(self):
        form_data = {
            'title':'FormTile',
            'description':'FormFes',
            'releas_data':11
        }
        form = GameForm(form_data)
        self.assertFalse(form.is_valid())

class GameReviewFormTest(TestCase):

    def test_game_form_valid(self):
        form_data = {
            'ratting':'1',
            'comment':'test comment'
        }
        form = GameReviewForm(form_data)
        self.assertTrue(form.is_valid())

    def test_game_form_invalid(self):
        form_data = {
            'ratting':'123',
            'comment':'test comment'
        }
        form = GameReviewForm(form_data)
        self.assertFalse(form.is_valid())

class GameSearchFormTest(TestCase):

    def test_search_form_valid(self):
        form_data = {
            'title':'FormTitle',
            'game_studio':'test studio',
            'genre':'test genre'
        }
        form = GameSearchForm(form_data)
        self.assertTrue(form.is_valid())

    def test_search_form_invalid(self):
        form_data = {
            'title':123,
            'game_studio':'test studio',
            'genre':1.2
        }
        form = GameSearchForm(form_data)
        self.assertFalse(form.is_valid())