from django.test import TestCase
from django.core.exceptions import ValidationError

from users.models import MyUser
from addresses.models import Address


class TestAddressModel(TestCase):
    def setUp(self):
        self.user = MyUser.objects.create(
            username='admin',
        )
        self.address = Address.objects.create(
            street='Ленина',
            num_house=12,
            num_room=8,
            user=self.user,
        )

    def test_address_str_method(self):
        self.assertEqual(
            str(self.address),
            "ул.Ленина, д.12, кв.8",
        )

    def test_address_num_room_positive(self):
        with self.assertRaises(ValidationError):
            address = Address(street='Main St', num_house='123', num_room=-1)
            address.full_clean()
