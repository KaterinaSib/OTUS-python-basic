from django.test import TestCase
from django.urls import reverse, reverse_lazy

from addresses.models import Address
from meters.models import Category, Meter
from users.models import MyUser


class TestMeterView(TestCase):

    def setUp(self):
        self.admin = MyUser.objects.create(
            username='admin',
            email='admin@mail.com',
            password='admin12345!',
            is_superuser=True,
        )
        self.user = MyUser.objects.create_user(
            username='testuser',
            email='user@mail.com',
            password='12345',
        )

        self.address = Address.objects.create(
            street='Ленина',
            num_house=12,
            num_room=8,
            user=self.admin,
        )
        self.category = Category.objects.create(name='ГВС')
        self.meter = Meter.objects.create(
            address=self.address,
            category=self.category,
            type='Водомер',
            serial_num=12345,
        )

    def test_index_list_view(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

    def test_view_redirects_if_not_logged_in(self):
        url = reverse('meters:meter_list')
        response = self.client.get(url)
        success_url = f"{reverse('users:login')}?next={url}"
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, success_url)

    def test_view_for_non_super_user(self):
        self.client.force_login(self.user)
        url = reverse('meters:meter_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)

    def test_view_for_super_user(self):
        self.client.force_login(self.admin)
        response = self.client.get(reverse('meters:meter_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'meters/meter_list.html')

    def test_authenticated_user_access(self):
        self.client.force_login(self.admin)
        url = reverse('meters:meter_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_user_with_permissions_updates_meter_successfully(self):
        self.client.force_login(self.admin)
        url = reverse("meters:meter_update", kwargs={"pk": self.meter.pk})
        data = {
            "address": self.address.id,
            "category": self.category.id,
            "type": "Водомер",
            "serial_num": 67890,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.meter.refresh_from_db()
        self.assertEqual(self.meter.type, "Водомер")
        self.assertEqual(self.meter.serial_num, 67890)

    def test_user_without_permissions_cannot_update_meter(self):
        self.client.force_login(self.user)
        url = reverse("meters:meter_update", kwargs={"pk": self.meter.pk})
        data = {
            "address": self.address.id,
            "category": self.category.id,
            "type": "Водомер",
            "serial_num": 67890,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 403)

    def test_superuser_can_delete_meter(self):
        self.client.force_login(self.admin)
        url = reverse("meters:meter_delete", kwargs={"pk": self.meter.pk})
        success_url = reverse_lazy("meters:meter_list")
        response = self.client.post(url)
        self.assertFalse(Meter.objects.filter(pk=self.meter.pk).exists())
        self.assertRedirects(response, success_url)

    def test_regular_user_cannot_delete_meter(self):
        self.client.force_login(self.user)
        url = reverse("meters:meter_delete", kwargs={"pk": self.meter.pk})
        response = self.client.post(url)
        self.assertTrue(Meter.objects.filter(pk=self.meter.pk).exists())
        self.assertEqual(response.status_code, 403)
