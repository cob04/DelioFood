from django.test import TestCase

from .model_factory import ProductFactory

class ProductMethodTests(TestCase):

    def setUp(self):
        self.product1 = ProductFactory.create()

    def test_product_string_representation(self):
        self.assertEqual(str(self.product1), 'Burger')
