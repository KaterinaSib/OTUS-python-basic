from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Address, Category, Meter
from .forms import MeterForm, AddressForm


def index_list_view(request):
    return render(request, 'base.html')


class AddressListView(ListView):
    model = Address


class AddressDetailView(LoginRequiredMixin, DetailView):
    model = Address


class AddressCreateView(UserPassesTestMixin, CreateView):
    model = Address
    form_class = AddressForm
    success_url = reverse_lazy('meters:address_list')

    def test_func(self):
        user = self.request.user
        return self.request.user.is_staff or user.is_superuser


class AddressUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ["addresses.change_address"]
    model = Address
    fields = '__all__'
    success_url = reverse_lazy('meters:address_list')


class AddressDeleteView(DeleteView):
    model = Address
    success_url = reverse_lazy('meters:address_list')


class MeterListView(ListView):
    model = Meter


class MeterDetailView(LoginRequiredMixin, DetailView):
    model = Meter


class MeterCreateView(UserPassesTestMixin, CreateView):
    model = Meter
    form_class = MeterForm
    success_url = reverse_lazy('meters:meter_list')

    def test_func(self):
        user = self.request.user
        return self.request.user.is_staff or user.is_superuser


class MeterUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ["meters.change_meter"]  # view, add, change, delete
    model = Meter
    fields = ('indication',)
    success_url = reverse_lazy('meters:meter_list')


class MeterDeleteView(DeleteView):
    model = Meter
    success_url = reverse_lazy('meters:meter_list')
