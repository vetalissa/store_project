from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import (EmailVerificationView, UserLoginView, UserProfileView,
                         UserRegisterView, send_email)

app_name = 'users'

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', login_required(UserProfileView.as_view()), name='profile'),
    path('verification/<str:email>/<uuid:code>/', EmailVerificationView.as_view(), name='email_verification'),
    path('verification/send_email/<str:email>/', send_email, name='send_email'),
]
