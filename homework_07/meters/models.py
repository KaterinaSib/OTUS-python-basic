from django.db import models


class Address(models.Model):
    street = models.CharField(unique=False, max_length=30)
    num_house = models.CharField(unique=False, max_length=10)
    num_room = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'ул.{self.street}, д.{self.num_house}, кв.{self.num_room}'


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Meter(models.Model):
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.CharField(max_length=30)
    serial_num = models.PositiveIntegerField(unique=True)
    indication = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.category}/"{self.type}"/{self.serial_num}'