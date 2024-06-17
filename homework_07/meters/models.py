from django.db import models

from users.models import User


# Create your models here.


class Address(models.Model):
    street = models.CharField(unique=False, max_length=30)
    num_house = models.CharField(unique=False, max_length=10)
    num_room = models.PositiveSmallIntegerField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f'ул.{self.street}, д.{self.num_house}, кв.{self.num_room}'


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Meter(models.Model):
    address = models.ManyToManyField(Address)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.CharField(max_length=30)
    serial_num = models.PositiveIntegerField(unique=True)
    indication = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.category}/"{self.type}"/{self.serial_num}'
