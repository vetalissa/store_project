import uuid
from datetime import timedelta

from celery import shared_task
from django.utils.timezone import now

from users.models import EmailVerification, User


@shared_task
def send_create_message(user_id):
    user = User.objects.get(id=user_id)
    email_verification = EmailVerification.objects.filter(user=user)
    if email_verification.exists() and email_verification.last().is_expired():
        email_verification.last().send_email_verification()
    else:
        EmailVerification.objects.filter(user=user).delete()
        expiration = now() + timedelta(minutes=2)
        new_email_verification = EmailVerification.objects.create(code=uuid.uuid4(), user=user, expiration=expiration)
        new_email_verification.send_email_verification()
