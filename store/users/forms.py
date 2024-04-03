from django import forms
from django.contrib.auth.forms import (AuthenticationForm, UserChangeForm,
                                       UserCreationForm)

from users.models import User


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-title'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-title'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-title'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-title'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-title'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-title'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-title'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-title'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserProfileForm(UserChangeForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-title', 'style': 'border:none;'}),
                             required=False)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-title'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-title'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-title', 'readonly': True}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-title', 'readonly': True}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image', 'username', 'email')
