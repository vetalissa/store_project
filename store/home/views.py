from django.views.generic.base import TemplateView

from common.view import TitleMixin


class HomeView(TitleMixin, TemplateView):
    template_name = 'home/index.html'
    title = 'Roselissa'
