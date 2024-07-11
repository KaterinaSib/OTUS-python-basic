from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from .models import MyUser
from .forms import RegisterForm


class RegisterView(CreateView):
    model = MyUser
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('meters:list')


class AuthView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('meters:list')


class UserListView(ListView):
    model = MyUser


class UserDetailView(LoginRequiredMixin, DetailView):
    model = MyUser


class UserCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ["users.change_user"]
    model = MyUser
    form_class = RegisterForm
    success_url = reverse_lazy('users:list')


class UserUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ["users.change_user"]  # view, add, change, delete
    model = MyUser
    fields = '__all__'
    success_url = reverse_lazy('users:list')


class UserDeleteView(DeleteView):
    model = MyUser
    success_url = reverse_lazy('users:list')