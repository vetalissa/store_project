from users.models import EmailVerification


class TitleMixin:
    title = None

    def get_context_data(self, **kwargs):
        context = super(TitleMixin, self).get_context_data()
        context['title'] = self.title

        return context


class EmailAgainSendMixin:

    def get_context_data(self, **kwargs):
        context = super(EmailAgainSendMixin, self).get_context_data()
        email_again_send = EmailVerification.objects.filter(user=self.request.user)
        context['email_again_send'] = False if not email_again_send.exists() else email_again_send.first().is_expired()
        return context
