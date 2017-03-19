from django.shortcuts import render
from django.views.generic import TemplateView

from .models import HomePage


class HomePageView(TemplateView):

    template_name = 'index.html'

