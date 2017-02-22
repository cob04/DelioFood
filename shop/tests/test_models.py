from django.test import TestCase

from .model_factory import ProductFactory, VariationFactory

class ProductMethodTests(TestCase):

    def setUp(self):
        self._product1 = ProductFactory.create()
        self._product_var1 = VariationFactory.create(
            product=self._product1)
        self._product_var2 = VariationFactory.create(
            product=self._product1)

    def test_product_string_representation(self):
        self.assertEqual(str(self._product1), 'Burger')

    def test_gettings_default_variation(self):
        self.assertEqual(
            self._product1.default_variation,
            self._product_var1)

    def test_getting_default_variation_with_no_variations(self):
        product = ProductFactory.create()
        self.assertIsNone(product.default_variation)

class VariationMethodTests(TestCase):

    def setUp(self):
        self._product1 = ProductFactory.create()
        self._variation1 = VariationFactory.create(
            product=self._product1)

    def test_variation_string_representation(self):
        self.assertEqual(
            str(self._variation1),
            'Medium: serves 5')
