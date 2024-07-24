from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
    PermissionRequiredMixin,
)
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Meter, MeterData
from .forms import MeterForm, MeterDataForm


def index_list_view(request):
    return render(request, "base.html")


class MeterListView(UserPassesTestMixin, ListView):
    model = Meter

    def test_func(self):
        user = self.request.user
        return self.request.user.is_staff or user.is_superuser


class MeterDetailView(UserPassesTestMixin, DetailView):
    model = Meter

    def test_func(self):
        meter = self.get_object()
        return self.request.user or meter.user


class MeterCreateView(UserPassesTestMixin, CreateView):
    model = Meter
    form_class = MeterForm
    success_url = reverse_lazy("meters:meter_list")

    def test_func(self):
        user = self.request.user
        return self.request.user.is_staff or user.is_superuser


class MeterDataCreateView(LoginRequiredMixin, CreateView):
    model = MeterData
    # form_class = MeterDataForm
    fields = ("data",)
    permission_required = ["meters.add_meterdata"]

    def test_func(self):
        user = self.request.user
        address = self.get_object()
        return user in address.user.all().first()

    def get_success_url(self):
        return reverse("meters:meter_detail",
                       kwargs={"pk": self.object.meter.pk},
                       )

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.meter_id = self.kwargs["pk"]
        instance.save()
        return super().form_valid(form)


class MeterUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ["meters.change_meter"]
    model = Meter
    fields = '__all__'
    success_url = reverse_lazy("meters:meter_list")


class MeterDeleteView(UserPassesTestMixin, DeleteView):
    model = Meter

    def test_func(self):
        user = self.request.user
        return self.request.user.is_staff or user.is_superuser

    def get_success_url(self):
        return reverse_lazy("meters:meter_list")
