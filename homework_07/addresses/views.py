from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Address
from .forms import AddressForm


class AddressListView(ListView):
    model = Address


class AddressDetailView(LoginRequiredMixin, DetailView):
    model = Address


class AddressCreateView(UserPassesTestMixin, CreateView):
    model = Address
    form_class = AddressForm
    success_url = reverse_lazy('addresses:address_list')

    def test_func(self):
        user = self.request.user
        return self.request.user.is_staff or user.is_superuser


class AddressUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ["addresses.change_address"]
    model = Address
    fields = '__all__'
    success_url = reverse_lazy('addresses:address_list')


class AddressDeleteView(DeleteView):
    model = Address
    success_url = reverse_lazy('addresses:address_list')
