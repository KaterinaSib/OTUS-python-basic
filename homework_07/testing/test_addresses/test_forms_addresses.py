from addresses.forms import AddressForm
from django.test import TestCase


class TestAddressForm(TestCase):
    def test_form_includes_all_fields(self):
        form = AddressForm()
        self.assertEqual(
            list(form.fields.keys()),
            ['street', 'num_house', 'num_room', 'user'],
        )

    def test_form_validates_num_room(self):
        form_data = {
            'street': 'Ленина',
            'num_house': '123',
            'num_room': -1,
            'user': []
        }
        form = AddressForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('num_room', form.errors)

    def test_form_missing_required_field(self):
        form_data = {
            'street': 'Ленина',
            'num_house': '123',
            'num_room': 1
        }
        form = AddressForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('user', form.errors)
