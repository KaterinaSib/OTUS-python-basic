from django.core.management.base import BaseCommand
from users.models import MyUser


class Command(BaseCommand):

    def handle(self, *args, **options):

        MyUser.objects.all().delete()

        MyUser.objects.create(
            name='Admin',
            surname='Admin',
            email='admin@mail.com',
            username='AdminAdminovich',
            password='Admin123qwerty!',
            is_staff=True,
        )

        MyUser.objects.create(
            name='Иван',
            surname='Иванович',
            email='ivan@mail.com',
            username='IvanIvanovich',
            password='Ivan123qwerty!',
        )
