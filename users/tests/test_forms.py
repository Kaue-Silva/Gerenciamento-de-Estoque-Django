from django.test import TestCase
from ..forms import UserRegisterForm


class UsersTestForms(TestCase):
    def test_form_is_valid(self):
        form = UserRegisterForm(
            data={
                "username": "kauesil",
                "email": "kauesilva940@gmail.com",
                "first_name": "kaue",
                "last_name": "silva",
                "password1": "test12345@#",
                "password2": "test12345@#",
            }
        )

        self.assertTrue(form.is_valid())

    def test_form_is_not_valid(self):
        form = UserRegisterForm(data={})

        self.assertFalse(form.is_valid())
