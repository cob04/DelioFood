from django.test import TestCase
from django.test import override_settings

from .model_factory import (ProductFactory, VariationFactory,
    ProductImageFactory, PackageFactory, PackageItemFactory)

MEDIA_ROOT = '/tmp/'


@override_settings(MEDIA_ROOT=MEDIA_ROOT)
class ProductMethodTests(TestCase):

    def setUp(self):
        self._product1 = ProductFactory.create()
        self._product_var1 = VariationFactory.create(
            product=self._product1)
        self._product_var2 = VariationFactory.create(
            product=self._product1)

    def test_product_string_representation(self):
        self.assertEqual(str(self._product1), 'Burger')

    def test_getting_abosolute_url(self):
        self.assertEqual(self._product1.get_absolute_url(),
            '/products/burger/'
        )

    def test_getting_product_default_variation(self):
        self.assertEqual(
            self._product1.default_variation,
            self._product_var1)

    def test_getting_product_default_variation_with_no_variations(self):
        product = ProductFactory.create()
        self.assertIsNone(product.default_variation)

    def test_getting_default_price_of_product(self):
        self.assertEqual(self._product1.price, 250)

    def test_getting_default_price_product_with_no_variations(self):
        product = ProductFactory.create()
        self.assertIsNone(product.price)

    def test_gettings_default_image_name(self):
        product = ProductFactory.create()
        img1 = ProductImageFactory(product=product)
        img2 = ProductImageFactory(product=product)
        self.assertEqual(product.get_default_image_name(), img1.image.name)


class VariationMethodTests(TestCase):

    def setUp(self):
        self._product1 = ProductFactory.create()
        self._variation1 = VariationFactory.create(
            product=self._product1)

    def test_variation_string_representation(self):
        self.assertEqual(
            str(self._variation1),
            'Medium: serves 5')


@override_settings(MEDIA_ROOT=MEDIA_ROOT)
class ProductImageMethodTests(TestCase):

    def setUp(self):
        self._product = ProductFactory.create()
        self._img1 = ProductImageFactory.create(
            product=self._product,
            caption='burger')
        self._img2 = ProductImageFactory.create(
            product=self._product)

    def test_product_image_string_representation(self):
        """
        Test product image string representation uses the caption
        when available or image filename otherwise.
        """
        self.assertEqual(str(self._img1), 'burger')
        self.assertEqual(str(self._img2), self._img2.image.name.split('/')[2])


@override_settings(MEDIA_ROOT=MEDIA_ROOT)
class PackageTests(TestCase):

    def setUp(self):
        self._package = PackageFactory.create()

    def test_package_string_representation(self):
        self.assertEqual(str(self._package), 'DelioRibs')


class PackageItemTests(TestCase):

    def setUp(self):
        self._package = PackageFactory.create()
        self._product = ProductFactory.create()
        self._package_item = PackageItemFactory(
            package=self._package,
            product=self._product)

    def test_package_item_string_representation(self):
        self.assertEqual(str(self._package_item), self._product.title)
