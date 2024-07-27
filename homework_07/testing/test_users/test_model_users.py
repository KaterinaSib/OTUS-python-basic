from django.test import TestCase

from users.models import MyUser


class TestUserModel(TestCase):
    def setUp(self):
        self.user = MyUser.objects.create_user(
            username='testuser',
            first_name='test_first_name',
            last_name='test_last_name',
            email='user@mail.com',
            password='12345',
        )

    def test_user_str(self):
        expected_str = f"{self.user.first_name} {self.user.last_name} / {self.user.username}"
        self.assertEqual(str(self.user), expected_str)

    def test_create_user_with_valid_data(self):
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.first_name, "test_first_name")
        self.assertEqual(self.user.last_name, "test_last_name")
        self.assertEqual(self.user.email, "user@mail.com")

    def test_create_user_with_duplicate_username(self):
        with self.assertRaises(Exception):
            MyUser.objects.create_user(
                username="testuser",
                first_name="Second",
                last_name="User",
                email="seconduser@example.com",
                password="54321"
            )

    def test_create_user_with_duplicate_email(self):
        with self.assertRaises(Exception):
            MyUser.objects.create_user(
                username="new_user",
                first_name="Second",
                last_name="User",
                email="user@mail.com",
                password="54321"
            )
