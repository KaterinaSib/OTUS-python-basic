from django.core.management.base import BaseCommand
from users.models import MyUser


class Command(BaseCommand):

    def handle(self, *args, **options):

        MyUser.objects.all().delete()

        MyUser.objects.create(
            username='IvanIvanov',
            first_name='Иван',
            last_name='Иванович',
            email='ivan@mail.com',
            password='Ivan123qwerty!',
        )
