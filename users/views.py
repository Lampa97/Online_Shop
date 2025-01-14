from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.contrib.auth import login
from django.views.generic.edit import FormView
from .forms import CustomUserCreationForm
from django.conf import settings

class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('catalog:home')


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('catalog:home')


class RegisterView(FormView):
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = 'Поздравляем с регистрацией!'
        message = "Примите наши поздравления с регистрацией в нашем сервисе! Теперь вы можете просматривать продукты и управлять ими"
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list)