from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from addresses.views import AddressListView
from addresses.models import Address
from users.models import MyUser


class TestAddressListView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = MyUser.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='password',
        )
        self.staff_user = MyUser.objects.create_user(
            username='staffuser',
            email='staff@example.com',
            password='password',
            is_staff=True,
        )
        self.superuser = MyUser.objects.create_superuser(
            username='superuser',
            email='super@example.com',
            password='password',
            is_superuser=True,
        )

    def tearDown(self):
        self.user.delete()
        self.staff_user.delete()
        self.superuser.delete()

    def test_non_privileged_user_access(self):
        request = self.factory.get('/addresses/')
        request.user = self.user
        view = AddressListView.as_view()
        with self.assertRaises(PermissionDenied):
            response = view(request)

    def test_staff_user_access(self):
        request = self.factory.get('/addresses/')
        request.user = self.staff_user
        view = AddressListView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_superuser_access(self):
        request = self.factory.get('/addresses/')
        request.user = self.superuser
        view = AddressListView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, 200)
