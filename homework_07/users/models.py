from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(unique=False, max_length=20)
    surname = models.CharField(unique=False, max_length=30)

    def __str__(self):
        return f'{self.name}/{self.surname}'