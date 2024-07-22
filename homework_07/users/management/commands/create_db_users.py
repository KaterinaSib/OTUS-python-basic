from django.core.management.base import BaseCommand
from users.models import MyUser


class Command(BaseCommand):

    def handle(self, *args, **options):

        MyUser.objects.all().delete()

        MyUser.objects.create_superuser(
            username="admin",
            email="admin@mail.com",
            password="admin12345!",
        )
