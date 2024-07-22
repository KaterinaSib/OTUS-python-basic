from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(unique=False, max_length=20)
    last_name = models.CharField(unique=False, max_length=30)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} / {self.username}"
