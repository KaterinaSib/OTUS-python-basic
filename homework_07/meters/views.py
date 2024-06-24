from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Address, Category, Meter
from .forms import MeterForm


def index_list_view(request):
    # meters = Meter.objects.select_related('meters').prefetch_related('category').all()
    return render(request, 'base.html')


def addresses_list_view(request):
    addresses = Address.objects.all()
    return render(
        request,
        'addresses/list.html',
        {'addresses': addresses},
    )


def categoryes_list_view(request):
    categoryes = Category.objects.all()
    return render(
        request,
        'categoryes/list.html',
        {'categoryes': categoryes},
    )


def meters_list_view(request):
    meters = Meter.objects.all()
    return render(
        request,
        'meters/list.html',
        {'meters': meters},
    )


class MeterListView(ListView):
    model = Meter
    # paginate_by = 4


class MeterDetailView(LoginRequiredMixin, DetailView):
    model = Meter


class MeterCreateView(UserPassesTestMixin, CreateView):
    model = Meter
    # fields = '__all__'
    form_class = MeterForm
    success_url = reverse_lazy('meters:list')

    def test_func(self):
        user = self.request.user
        return (self.request.user.is_staff and user.username.endswith('2')) or user.is_superuser


class MeterUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ["meters.change_meter"]  # view, add, change, delete
    model = Meter
    # fields = '__all__'
    fields = ('indication',)
    success_url = reverse_lazy('meters:list')


class MeterDeleteView(DeleteView):
    model = Meter
    success_url = reverse_lazy('meters:list')
