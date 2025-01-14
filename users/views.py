from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm

class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('catalog:home')


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('catalog:home')


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('catalog:home')
