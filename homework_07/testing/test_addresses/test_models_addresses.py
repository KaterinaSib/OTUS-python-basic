import pytest
from django.core.exceptions import ValidationError
from users.models import MyUser
from addresses.models import Address


class TestAddressModel:
    @pytest.fixture
    def user(self, db):
        return MyUser.objects.create(
            username='testuser',
            first_name='Test',
            last_name='User',
            email='testuser@example.com',
        )

    @pytest.fixture
    def address(self, db, user):
        address = Address.objects.create(
            street='Main St',
            num_house='123',
            num_room=1,
        )
        address.user.add(user)
        return address

    def test_address_str_method(self, address):
        assert str(address) == "ул.Main St, д.123, кв.1"

    def test_address_num_room_positive(self, db):
        with pytest.raises(ValidationError):
            address = Address(street='Main St', num_house='123', num_room=-1)
            address.full_clean()  # This will trigger the validation

    def test_address_user_many_to_many(self, db, user):
        address = Address.objects.create(
            street='Main St',
            num_house='123',
            num_room=1,
        )
        user2 = MyUser.objects.create(
            username='testuser2',
            first_name='Test2',
            last_name='User2',
            email='testuser2@example.com',
        )
        address.user.add(user, user2)
        assert address.user.count() == 2
        assert user in address.user.all()
        assert user2 in address.user.all()
