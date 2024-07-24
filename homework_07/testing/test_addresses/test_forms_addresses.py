from addresses.forms import AddressForm


class TestAddressForm:
    def test_form_includes_all_fields(self):
        form = AddressForm()
        expected_fields = ['street', 'num_house', 'num_room', 'user']
        assert list(form.fields.keys()) == expected_fields

    def test_form_validates_num_room(self):
        form_data = {
            'street': 'Ленина',
            'num_house': '123',
            'num_room': -1,
            'user': []
        }
        form = AddressForm(data=form_data)
        assert not form.is_valid()
        assert 'num_room' in form.errors

    def test_form_missing_required_field(self):
        form_data = {
            'street': 'Ленина',
            'num_house': '123',
            'num_room': 1
            # 'user' field is missing
        }
        form = AddressForm(data=form_data)
        assert not form.is_valid()
        assert 'user' in form.errors
