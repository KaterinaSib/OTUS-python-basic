from django.contrib import admin
from .models import Address, Category, Meter


admin.site.register(Address)
admin.site.register(Category)
admin.site.register(Meter)
