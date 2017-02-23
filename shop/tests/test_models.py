from django.test import TestCase

from .model_factory import ProductFactory, VariationFactory

class ProductMethodTests(TestCase):

    def setUp(self):
        self._product1 = ProductFactory.create()

    def test_product_string_representation(self):
        self.assertEqual(str(self._product1), 'Burger')

class VariationMethodTests(TestCase):

    def setUp(self):
        self._product1 = ProductFactory.create()
        self._variation1 = VariationFactory.create(
            product=self._product1)

    def test_variation_string_representation(self):
        self.assertEqual(
            str(self._variation1),
            'Medium: serves 5')
