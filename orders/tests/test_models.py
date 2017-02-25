from django.test import TestCase

from shop.models import Product
from shop.tests.model_factory import ProductFactory, VariationFactory

from .model_factory import OrderFactory, OrderItemFactory


class OrderTests(TestCase):

    def setUp(self):
        self._product1 = ProductFactory.create()
        self._product2 = ProductFactory.create(
            title='Fish Fillet',
            description="Tilapia")
        self._product_var1 = VariationFactory.create(
            product=self._product1)
        self._product_var2 = VariationFactory.create(
            product=self._product2)

        self._order = OrderFactory.create()

        self._order_item1 = OrderItemFactory.create(
            order=self._order)

        self._order_item2 = OrderItemFactory.create(
            order=self._order,
            product=self._product2)

    def test_string_representation(self):
        self.assertEqual(str(self._order), '1: James Bond')

    def test_billing_name(self):
        self.assertEqual(self._order.billing_name(), 'James Bond')

    def test_calculating_order_total_cost(self):
        self.assertEqual(self._order.get_total_cost(), 500.00)

    def test_order_total_cost_property(self):
        self.assertEqual(self._order.total_cost, 'Ksh 500.00')

    def test_calculating_order_item_cost(self):
        self.assertEqual(self._order_item1.get_cost(), 250.00)

    def test_order_item_string_representation(self):
        self.assertEqual(str(self._order_item1), '1')
        self.assertEqual(str(self._order_item2), '2')

