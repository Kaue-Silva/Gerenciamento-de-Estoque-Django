from django.test import TestCase
from django.urls import reverse


class UsersTestModels(TestCase):
    def test_user_views_signup_return_status_code_200(self):
        response = self.client.get(reverse("register"))
        self.assertEquals(response.status_code, 200)

    def test_user_views_login_return_status_code_200(self):
        response = self.client.get(reverse("login"))
        self.assertEquals(response.status_code, 200)

    def test_user_views_logout_return_status_code_302(self):
        response = self.client.get(reverse("logout"))
        self.assertEquals(response.status_code, 302)
