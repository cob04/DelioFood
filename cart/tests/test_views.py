from django.contrib.sessions.middleware import SessionMiddleware
from django.conf import settings
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import RequestFactory
from django.test import Client

from shop.tests.model_factory import ProductFactory, VariationFactory

from ..cart import Cart


class CartViewTests(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self._product1 = ProductFactory.create()
        self._product2 = ProductFactory.create()
        self._product_var1 = VariationFactory.create(
            product=self._product1)
        self._product_var2 = VariationFactory.create(
            product=self._product2)

    def test_mobile_template_used_for_cart_detail_for_mobile_devices(self):
        request = self.factory.get(reverse('home'))
        middleware = SessionMiddleware()
        middleware.process_request(request)
        cart = Cart(request)
        cart.add(product=self._product1,
                variation=self._product_var1,
                instructions='Hello There')
        self.assertEqual(cart.cart['1'], {
            'quantity':1,
            'unit_price': '250',
            'instructions': 'Hello There',
            }
        )
        client = Client(HTTP_USER_AGENT='iPhone')
        client.get(reverse('cart:detail'))
        self.assertTemplateUsed('/mobile/cart/detail.html')
