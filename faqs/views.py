from django.shortcuts import render
from django.views.generic.list import ListView

from .models import FAQ


class FAQListView(ListView):
    """
    Listing FAQs.
    """
    model = FAQ
    template_name = 'faq_list.html'
