from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    name = models.CharField(unique=False, max_length=20)
    surname = models.CharField(unique=False, max_length=30)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.name} {self.surname}'
