from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import UserPassesTestMixin, PermissionRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.views import LoginView, LogoutView
from addresses.models import Address
from .models import MyUser
from .forms import RegisterForm


class RegisterView(CreateView):
    model = MyUser
    form_class = RegisterForm
    template_name = "register.html"
    success_url = reverse_lazy("index")


class AuthView(LoginView):
    template_name = "login.html"

    def get_success_url(self):
        user = self.request.user
        if user.is_staff or user.is_superuser:
            return reverse_lazy("index")
        address = get_object_or_404(Address, user=user)
        return reverse("addresses:address_detail", kwargs={"pk": address.pk})


class ReAuthView(LogoutView):
    template_name = "login.html"


class UserListView(UserPassesTestMixin, ListView):
    model = MyUser

    def test_func(self):
        user = self.request.user
        return user.is_staff or user.is_superuser


class UserDetailView(DetailView):
    model = MyUser


class UserCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ["users.change_user"]
    model = MyUser
    form_class = RegisterForm
    success_url = reverse_lazy("users:list")


class UserUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ["users.change_user"]  # view, add, change, delete
    model = MyUser
    fields = "__all__"
    success_url = reverse_lazy("users:list")


class UserDeleteView(DeleteView):
    model = MyUser
    success_url = reverse_lazy("users:list")
