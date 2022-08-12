from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.context_processors import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView

from accounts.forms import SignupForm, ProfileForm


class SignupView(CreateView):
    form_class = SignupForm
    template_name = "form.html"
    success_url = settings.LOGIN_URL

class MyLoginView(LoginView):
    template_name = "form.html"

class MyLogoutView(LogoutView):
    next_page = settings.LOGIN_URL

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/profile.html"

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ProfileForm
    template_name = "form.html"
    success_url = reverse_lazy("accounts:profile")

    def get_object(self, queryset=None):
        return self.request.user

