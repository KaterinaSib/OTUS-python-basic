from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Meter
from .forms import MeterForm


def index_list_view(request):
    return render(request, 'base.html')


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
