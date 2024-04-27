from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView

from common.view import TitleMixin
from users.forms import UserLoginForm, UserProfileForm, UserRegisterForm
from users.models import EmailVerification, User
from users.tasks import send_create_message


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
        login(self.request, self.object, backend='django.contrib.auth.backends.ModelBackend')
        send_email(self.request, self.object.id)
        return valid


class UserProfileView(TitleMixin, UpdateView):
    template_name = 'users/profile.html'
    form_class = UserProfileForm
    model = User
    title = 'Профиль'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data()
        email_verify = EmailVerification.objects.filter(user=self.object)
        context['email_verify'] = False if not email_verify.exists() else email_verify.first().is_expired()
        return context


class EmailVerificationView(TitleMixin, TemplateView):
    template_name = 'users/email_verification.html'
    title = 'Подтверждение почты'

    def get(self, request, *args, **kwargs):
        code = kwargs['code']
        user = User.objects.get(email=kwargs['email'])
        email_verification = EmailVerification.objects.filter(code=code, user=user)

        if email_verification.exists() and email_verification.first().is_expired():
            user.if_verified_email = True
            user.save()
            return super(EmailVerificationView, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('home'))


def send_email(request, user_id):
    send_create_message.delay(user_id)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
