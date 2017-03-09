from django.shortcuts import render
from django.views.generic import TemplateView

from .models import HomePage


class HomePageView(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        home_page = HomePage.objects.get(id=1)
        context['slides'] = home_page.slides.all()
        return context
