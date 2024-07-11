from django.db import models
from users.models import MyUser


class Address(models.Model):
    street = models.CharField(unique=False, max_length=30)
    num_house = models.CharField(unique=False, max_length=10)
    num_room = models.PositiveSmallIntegerField()
    user = models.ManyToManyField(MyUser)

    def __str__(self):
        return f'ул.{self.street}, д.{self.num_house}, кв.{self.num_room}'
