from django.conf.urls import include, url

from . import views


product_urls = [
    url(r'^$', views.product_list, name='list'),
    url(r'^(?P<slug>[-\w]+)/$', views.product_detail, name='detail'),
]

urlpatterns = [
    url(r'products/', include(product_urls, namespace='product')),
]
