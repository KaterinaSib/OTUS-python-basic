from django.contrib import admin
from .models import Category, Meter, MeterData


admin.site.register(Category)
admin.site.register(Meter)
admin.site.register(MeterData)
