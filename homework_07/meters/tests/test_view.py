from django.test import TestCase
from django.urls import reverse

from meters.models import Address, Category, Meter
from users.models import MyUser


class TestViews(TestCase):

    def setUp(self):
        self.admin = MyUser.objects.create_superuser(
            username="admin",
            email="admin@mail.com",
            password="admin12345!",
        )
        self.address = Address.objects.create(
            street="Main Street",
            num_house=5,
            num_room=12,
        )
        self.category = Category.objects.create(
            name="ГВС",
        )
        self.meter = Meter.objects.create(
            address=self.address,
            category=self.category,
            serial_num=12345,
        )

    def tearDown(self):
        self.admin.delete()
        self.address.delete()
        self.category.delete()
        self.meter.delete()

    def test_address_detail_view_for_auth_user(self):
        self.client.force_login(self.admin)
        url = reverse("addresses:address_detail", kwargs={"pk": self.address.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_address_detail_view_for_unauth_user(self):
        url = reverse("addresses:address_detail", kwargs={"pk": self.address.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_address_list_view(self):
        self.client.force_login(self.admin)
        url = reverse("addresses:address_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_meter_list_view(self):
        self.client.force_login(self.admin)
        url = reverse("meters:meter_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_address_detail_view_context(self):
        self.client.force_login(self.admin)
        url = reverse("addresses:address_detail", kwargs={"pk": self.address.pk})
        response = self.client.get(url)
        print(response)
        self.assertContains(response, self.address.street)
        self.assertContains(response, self.address.num_house)
        self.assertContains(response, self.address.num_room)

    def test_meter_detail_view_context(self):
        self.client.force_login(self.admin)
        url = reverse("meters:meter_detail", kwargs={"pk": self.meter.pk})
        response = self.client.get(url)
        self.assertContains(response, self.meter.serial_num)

    def test_address_delete_view_context(self):
        self.client.force_login(self.admin)
        url = reverse("addresses:address_delete", kwargs={"pk": self.address.pk})
        response = self.client.get(url)
        self.assertContains(response, "Удалить?", html=True)
