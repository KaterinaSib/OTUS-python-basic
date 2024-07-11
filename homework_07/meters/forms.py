from django import forms
from .models import Meter, Address


class MeterForm(forms.ModelForm):
    class Meta:
        model = Meter
        fields = '__all__'


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'
