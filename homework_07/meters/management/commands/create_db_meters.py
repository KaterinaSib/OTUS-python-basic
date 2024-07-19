import datetime

from django.core.management.base import BaseCommand
from addresses.models import Address
from meters.models import Category, Meter, MeterData


class Command(BaseCommand):

    def handle(self, *args, **options):

        Address.objects.all().delete()
        Category.objects.all().delete()
        Meter.objects.all().delete()

        address_1 = Address.objects.create(
            street='Мира',
            num_house=2,
            num_room=15,
        )

        address_2 = Address.objects.create(
            street='Ленина',
            num_house=20,
            num_room=5,
        )

        gvs = Category.objects.create(
            name='ГВС',
        )

        hvs = Category.objects.create(
            name='ХВС',
        )

        meter_1 = Meter.objects.create(
            address=address_1,
            category=gvs,
            type='Тайпит',
            serial_num=45678,
        )

        data_meter_1 = MeterData.objects.create(
            meter=meter_1,
            data=65,
        )

        meter_2 = Meter.objects.create(
            address=address_2,
            category=hvs,
            type='Тайпит',
            serial_num=54321,
        )

        data_meter_2 = MeterData.objects.create(
            meter=meter_2,
            data=123,
        )
