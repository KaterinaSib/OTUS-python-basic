from django.test import TestCase
from django.urls import reverse

from addresses.models import Address
from users.models import MyUser


class TestAddressListView(TestCase):
    def setUp(self):
        self.admin = MyUser.objects.create(
            username='admin',
            email="admin@mail.com",
            password="admin12345!",
            is_superuser=True,
        )
        self.user = MyUser.objects.create(
            username='test_user',
            email="test_user@mail.com",
            password="test_user12345!",
        )
        self.address = Address.objects.create(
            street='Ленина',
            num_house=12,
            num_room=8,
            user=self.user,
        )

    def test_address_list_view_for_super_user(self):
        self.client.force_login(self.admin)
        response = self.client.get(reverse("addresses:address_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ленина")

    def test_address_list_view_for_non_super_user(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("addresses:address_list"))
        self.assertEqual(response.status_code, 403)

    def test_address_details_view_for_super_user(self):
        self.client.force_login(self.admin)
        url = reverse("addresses:address_detail", kwargs={"pk": self.address.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_user_without_login_cannot_view_address_details(self):
        url = reverse("addresses:address_detail", kwargs={"pk": self.address.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith(reverse('users:login')))

    def test_address_creation_by_super_user(self):
        self.client.force_login(self.admin)
        url = reverse("addresses:address_create")
        data = {
            "street": "Пушкина",
            "num_house": 2,
            "num_room": 12,
            "user": self.admin.id,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Address.objects.filter(street="Пушкина").exists())
        self.assertRedirects(response, reverse('addresses:address_list'))

    def test_address_creation_by_non_super_user(self):
        self.client.force_login(self.user)
        url = reverse("addresses:address_create")
        data = {
            "street": "Пушкина",
            "num_house": 2,
            "num_room": 12,
            "user": self.user.id,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 403)
        self.assertFalse(Address.objects.filter(street="Пушкина").exists())

    def test_updates_address_by_super_user(self):
        self.client.force_login(self.admin)
        url = reverse("addresses:address_update", kwargs={"pk": self.address.pk})
        data = {
            "street": "Пушкина",
            "num_house": 2,
            "num_room": 20,
            "user": self.user.id,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.address.refresh_from_db()
        self.assertEqual(self.address.street, "Пушкина")
        self.assertEqual(self.address.num_house, '2')
        self.assertEqual(self.address.num_room, 20)
        self.assertRedirects(response, reverse('addresses:address_list'))

    def test_updates_address_by_non_super_user(self):
        self.client.force_login(self.user)
        url = reverse("addresses:address_update", kwargs={"pk": self.address.pk})
        data = {
            "street": "Пушкина",
            "num_house": 2,
            "num_room": 20,
            "user": self.user.id,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 403)
        self.address.refresh_from_db()
        self.assertNotEqual(self.address.street, "Пушкина")

    def test_address_deleted_by_super_user(self):
        address = Address.objects.create(
            street="Пушкина",
            num_house="5",
            num_room=12,
            user=self.admin,
        )
        self.client.force_login(self.admin)
        url = reverse("addresses:address_delete", kwargs={"pk": address.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Address.objects.filter(pk=address.pk).exists())
        self.assertRedirects(response, reverse('addresses:address_list'))

    def test_address_deleted_by_non_super_user(self):
        self.client.force_login(self.user)
        url = reverse("addresses:address_delete", kwargs={"pk": self.address.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 403)
        self.assertTrue(Address.objects.filter(pk=self.address.pk).exists())
