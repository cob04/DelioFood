from django.conf.urls import include, url

from . import views


product_urls = [
    url(r'^(?P<slug>[-\w]+)/$', views.product_detail, name='detail'),
]

urlpatterns = [
    url(r'products/', include(product_urls, namespace='product')),
]
