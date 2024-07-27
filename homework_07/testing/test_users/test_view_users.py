from django.test import TestCase
from django.urls import reverse

from addresses.models import Address
from users.models import MyUser


class TestUserView(TestCase):
    data = {
        "username": "TestUser",
        "first_name": "New",
        "last_name": "User",
        "email": "TestUser@example.com",
        "password1": "password12345!",
        "password2": "password12345!",
    }

    def setUp(self):
        self.user = MyUser.objects.create_user(
            username="newuser",
            first_name="New",
            last_name="User",
            email="newuser@example.com",
            password="password12345!",
        )
        self.address = Address.objects.create(
            street='Ленина',
            num_house=12,
            num_room=18,
            user=self.user,
        )

    def tearDown(self):
        self.user.delete()
        self.address.delete()

    def test_user_can_register_with_valid_data(self):
        url = reverse('users:register')
        response = self.client.post(url, self.data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(MyUser.objects.filter(username='TestUser').exists())

    def test_template_name(self):
        url = reverse('users:register')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'register.html')

    def test_success_url(self):
        url = reverse('users:register')
        response = self.client.post(
            url,
            data=self.data,
        )
        success_url = reverse("index")
        self.assertRedirects(response, success_url)

    def test_redirect_regular_users(self):
        url = reverse('users:login')
        response = self.client.post(
            url,
            data={"username": "newuser",
                  "password": "password12345!"}
        )
        success_url = reverse(
            "addresses:address_detail",
            kwargs={"pk": self.address.pk},
        )
        self.assertRedirects(response, success_url)
