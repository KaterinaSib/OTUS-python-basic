from django.test import TestCase
from django.core.exceptions import ValidationError

from meters.models import Category, Meter
from users.models import MyUser
from addresses.models import Address


class TestAddressModel(TestCase):
    def setUp(self):
        self.user = MyUser.objects.create_user(
            username='testuser',
            email='user@mail.com',
            password='12345',
        )
        self.admin = MyUser.objects.create_superuser(
            username='superuser',
            email='admin@mail.com',
            password='12345',
            is_superuser=True,
        )

        self.address = Address.objects.create(
            street='Test Street',
            num_house=12,
            num_room=8,
            user=self.user,
        )
        self.category = Category.objects.create(name='Test Category')

        self.meter = Meter.objects.create(
            address=self.address,
            category=self.category,
            type='Test Type',
            serial_num=123456,
        )

    def test_address_str_method(self):
        self.assertEqual(str(self.address), "ул.Test Street, д.12, кв.8")

    def test_address_num_room_positive(self):
        with self.assertRaises(ValidationError):
            address = Address(street='Main St', num_house='123', num_room=-1)
            address.full_clean()
