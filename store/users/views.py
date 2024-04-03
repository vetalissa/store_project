from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

from common.view import TitleMixin
from users.forms import UserLoginForm, UserProfileForm, UserRegisterForm
from users.models import User


class UserLoginView(TitleMixin, LoginView):
    template_name = 'users/login.html'
    title = 'Вход'
    form_class = UserLoginForm


class UserRegisterView(TitleMixin, CreateView):
    model = User
    template_name = 'users/register.html'
    title = 'Регистрация'
    form_class = UserRegisterForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        valid = super(UserRegisterView, self).form_valid(form)
        login(self.request, self.object)
        return valid


class UserProfileView(TitleMixin, UpdateView):
    template_name = 'users/profile.html'
    form_class = UserProfileForm
    model = User
    title = 'Профиль'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))
