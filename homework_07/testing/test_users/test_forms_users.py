from django.test import TestCase

from users.forms import RegisterForm


class TestUserForm(TestCase):

    def test_form_initializes_with_all_fields(self):
        form = RegisterForm()
        self.assertEqual(
            list(form.fields.keys()),
            ["username", "first_name", "last_name", "email", "password1", "password2"],
        )

    def test_form_handles_missing_required_fields(self):
        form_data = {
            'username': None,
            'first_name': None,
            'last_name': None,
            'email': None,
            'password1': None,
            'password2': None,
        }
        form = RegisterForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)
        self.assertIn('first_name', form.errors)
        self.assertIn('last_name', form.errors)
        self.assertIn('email', form.errors)
        self.assertIn('password1', form.errors)
        self.assertIn('password2', form.errors)
