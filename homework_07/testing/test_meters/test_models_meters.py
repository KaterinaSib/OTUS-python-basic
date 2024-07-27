from django.core.exceptions import ValidationError
from django.db import IntegrityError, transaction
from django.test import TestCase
from django.utils import timezone

from meters.models import Category, Meter, Address, MeterData
from users.models import MyUser


class TestSetupBase(TestCase):
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


class TestCategoryModel(TestSetupBase):

    def test_create_category_with_valid_name(self):
        category = self.category
        self.assertEqual(str(category), 'ГВС')

    def test_create_category_with_empty_name(self):
        with self.assertRaises(ValidationError):
            category = Category.objects.create(name="")
            category.full_clean()
            category.save()


class TestMeterModel(TestSetupBase):

    def test_meter_str(self):
        expected_str = f'{self.category}/"Водомер"/12345'
        self.assertEqual(str(self.meter), expected_str)

    def test_clean_serial_num_unique(self):
        with self.assertRaises(IntegrityError):
            Meter.objects.create(
                address=self.address,
                category=self.category,
                type='ХВС',
                serial_num=12345
            )


class TestMeterDataModel(TestSetupBase):

    def test_meter_data_str_method(self):
        meter_data = MeterData.objects.create(
            meter=self.meter,
            data=100,
        )
        self.assertEqual(str(meter_data), f"{self.meter}: 100")

    def test_meter_data_foreign_key_constraint(self):
        meter_data = MeterData.objects.create(meter=self.meter, data=100)
        self.assertEqual(meter_data.meter, self.meter)

    def test_meter_data_auto_now_add(self):
        meter_data = MeterData.objects.create(meter=self.meter, data=100)
        self.assertLessEqual(meter_data.date_time, timezone.now())
