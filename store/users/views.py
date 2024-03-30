from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

from common.view import TitleMixin
from users.forms import UserLoginForm, UserRegisterForm
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
