import logging

from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView
from lionheart.decorators import render
from django.contrib import messages

logger = logging.getLogger(__name__)


@render
def home(request):
    return {}

class HomePageView(TemplateView):
    template_name = '../templates/test_home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        messages.info(self.request, 'hello http://example.com')
        return context
