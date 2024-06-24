from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .models import MyUser
from .forms import RegisterForm


class RegisterView(CreateView):
    model = MyUser
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = 'index'


class AuthView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('meters:list')
