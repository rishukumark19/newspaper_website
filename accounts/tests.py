from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse # new
class UsersManagersTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="normal", email="normal@user.com", password="foo", age=33
        )
        self.assertEqual(user.username, "normal")
        self.assertEqual(user.email, "normal@user.com")
        self.assertEqual(user.age, 33)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="super", email="super@user.com", password="foo", age=44
        )
        self.assertEqual(admin_user.username, "super")
        self.assertEqual(admin_user.email, "super@user.com")
        self.assertEqual(admin_user.age, 44)
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

class SignupPageTests(TestCase): # new
    def test_url_exists_at_correct_location_signupview(self):
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)
    def test_signup_view_name(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")
    def test_signup_form(self):
        response = self.client.post(
            reverse("signup"),
                {
                "username": "testuser",
                "email": "testuser@email.com",
                "password1": "testpass123",
                "password2": "testpass123",
                "age": 33,
                },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, "testuser")
        self.assertEqual(
            get_user_model().objects.all()[0].email, "testuser@email.com"
        )

        self.assertEqual(get_user_model().objects.all()[0].age, 33)
