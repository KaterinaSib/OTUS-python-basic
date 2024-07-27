from django.test import TestCase

from users.models import MyUser
from addresses.models import Address
from meters.forms import MeterForm, MeterDataForm
from meters.models import Category, Meter


class TestSetupBase(TestCase):
    def setUp(self):
        self.admin = MyUser.objects.create(
            username='admin',
            is_superuser=True,
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


class TestMeterForm(TestSetupBase):
    def test_form_initializes_with_all_fields(self):
        form = MeterForm()
        self.assertEqual(
            list(form.fields.keys()),
            ['address', 'category', 'type', 'serial_num'],
        )

    def test_form_handles_missing_required_fields(self):
        form_data = {
            'address': None,
            'category': None,
            'type': '',
            'serial_num': ''
        }
        form = MeterForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('address', form.errors)
        self.assertIn('category', form.errors)
        self.assertIn('type', form.errors)
        self.assertIn('serial_num', form.errors)

    def test_form_unique_serial_num(self):
        form_data = {
            'address': self.address.id,
            'category': self.category.id,
            'type': 'Water',
            'serial_num': 12345
        }
        form = MeterForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('serial_num', form.errors)
        self.assertEqual(
            first=form.errors['serial_num'],
            second=form.errors['serial_num'],
            msg=['Счетчик с этим серийным номером уже зарегистрирован.'],
        )


class TestMeterDataForms(TestSetupBase):
    def test_form_initializes_with_valid_data(self):
        meter = self.meter
        form_data = {'meter': meter.id, 'data': 100}
        form = MeterDataForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_initializes_with_missing_required_fields(self):
        form_data = {'data': 100}
        form = MeterDataForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('meter', form.errors)
