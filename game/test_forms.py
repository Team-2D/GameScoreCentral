from django.test import TestCase
from game.forms import GameForm

# 1. 测试表单的有效性
# 2. 测试字段验证
# 3. 测试表单与数据库model交互


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
        self.assertTrue(form.is_valid)
    def test_game_form_invalid(self):
        form_data = {
            'title':'FormTile',
            'description':'FormFes',
            'releas_data':11
        }
        form = GameForm(form_data)
        self.assertFalse(form.is_valid())

class