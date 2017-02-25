from django.contrib.sessions.middleware import SessionMiddleware
from django.conf import settings
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import RequestFactory

from shop.tests.model_factory import ProductFactory, VariationFactory

from ..cart import Cart


class CartMethodsTests(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self._product1 = ProductFactory.create()
        self._product2 = ProductFactory.create()
        self._product_var1 = VariationFactory.create(
            product=self._product1)
        self._product_var2 = VariationFactory.create(
            product=self._product2)

    def test_add_to_cart_method(self):
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

    def test_add_to_with_update_quantity_option(self):
        request = self.factory.get(reverse('home'))
        middleware = SessionMiddleware()
        middleware.process_request(request)
        cart = Cart(request)
        cart.add(product=self._product1,
                variation=self._product_var1,
                quantity=2,
                update_quantity=True,
                instructions='Hello There')
        self.assertEqual(len(cart), 2)

    def test_getting_quantity_of_entire_cart(self):
        request = self.factory.get(reverse('home'))
        middleware = SessionMiddleware()
        middleware.process_request(request)
        cart = Cart(request)
        cart.add(product=self._product1,
                variation=self._product_var1,
                quantity=3,
                update_quantity=False,
                instructions='Hello There')
        cart.add(product=self._product2,
                variation=self._product_var2,
                quantity=4,
                update_quantity=False,
                instructions='Hello There')
        self.assertEqual(len(cart), 7)

    def test_getting_cart_items_total_price(self):
        request = self.factory.get(reverse('home'))
        middleware = SessionMiddleware()
        middleware.process_request(request)
        cart = Cart(request)
        cart.add(product=self._product1,
                variation=self._product_var1,
                quantity=1,
                update_quantity=False,
                instructions='Hello There')
        self.assertEqual(cart.get_total_price(), 250)

    def test_removing_item_from_cart(self):
        request = self.factory.get(reverse('home'))
        middleware = SessionMiddleware()
        middleware.process_request(request)
        cart = Cart(request)
        cart.add(product=self._product1,
                variation=self._product_var1,
                quantity=1,
                update_quantity=False,
                instructions='Hello There')
        cart.add(product=self._product2,
                variation=self._product_var2,
                quantity=1,
                update_quantity=False,
                instructions='Hello There')
        cart.remove(self._product1)
        with self.assertRaises(KeyError):
            cart.cart['1']

    def test_removing_item_thats_not_in_cart(self):
        request = self.factory.get(reverse('home'))
        middleware = SessionMiddleware()
        middleware.process_request(request)
        cart = Cart(request)
        cart.add(product=self._product1,
                variation=self._product_var1,
                quantity=1,
                update_quantity=False,
                instructions='Hello There')
        cart.remove(self._product2)
        self.assertEqual(cart.cart['1'], {
            'quantity':1,
            'unit_price': '250',
            'instructions': 'Hello There',
            }
        )

    def test_iterating_over_cart_items(self):
        request = self.factory.get(reverse('home'))
        middleware = SessionMiddleware()
        middleware.process_request(request)
        cart = Cart(request)
        cart.add(product=self._product1,
                variation=self._product_var1,
                quantity=1,
                update_quantity=False,
                instructions='Hello There')
        cart.add(product=self._product2,
                variation=self._product_var2,
                quantity=1,
                update_quantity=False,
                instructions='Hello There')
        count = 0
        for item in cart.cart:
           count += 1
        self.assertEqual(count, 2)

    def test_having_multiple_variations_of_them_producr_in_cart(self):
        request = self.factory.get(reverse('home'))
        middleware = SessionMiddleware()
        middleware.process_request(request)
        product_var2 = VariationFactory.create(
            product=self._product1)
        cart = Cart(request)
        cart.add(product=self._product1,
                variation=self._product_var1,
                quantity=3,
                update_quantity=False,
                instructions='Variation 1')
        cart.add(product=self._product1,
                variation=product_var2,
                quantity=4,
                update_quantity=False,
                instructions='Variation 2')
        products = [{
                'instructions': 'Variation 1',
                'unit_price': '250',
                'quantity': 3
            },
            {
                'instructions': 'Variation 2',
                'unit_price': '250',
                'quantity': 4
            }]
        # test obove two variations are added
        for key, value in cart.cart.items():
            self.assertIn(value, products)
        # test total quantity
        self.assertEqual(len(cart), 7)
