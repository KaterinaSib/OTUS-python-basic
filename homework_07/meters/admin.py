from django.contrib import admin

# Register your models here.

from .models import Address, Category, Meter

# Register your models here.
admin.site.register(Address)
admin.site.register(Category)
admin.site.register(Meter)
