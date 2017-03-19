from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.FAQListView.as_view(), name='faqs'),
]
