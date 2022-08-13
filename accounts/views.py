from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.context_processors import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView, UpdateView, FormView

from accounts.forms import SignupForm, ProfileForm


class SignupView(FormView):
    form_class = SignupForm
    template_name = "form.html"
    # success_url = reverse("activities:list")

    def form_valid(self, form):
        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return HttpResponseRedirect(reverse("activities:list"))

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

