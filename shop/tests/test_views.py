from django.core.urlresolvers import reverse
from django.test import TestCase

from .model_factory import ProductFactory


class ProductDetailViewTests(TestCase):

    def setUp(self):
        self._product1 = ProductFactory.create()

    def test_get_response(self):
        response = self.client.get(self._product1.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['product'], self._product1)

    def test_product_detail_template_is_used(self):
        response = self.client.get(self._product1.get_absolute_url())
        self.assertTemplateUsed(response, 'shop/product/detail.html')


class ProductListViewTests(TestCase):

    def setUp(self):
        self._product1 = ProductFactory.create()

    def test_get_response(self):
        response = self.client.get(reverse('shop:product:list'))
        self.assertEqual(response.status_code, 200)
        product_list = response.context['product_list']
        self.assertEqual(
            [repr(product) for product in product_list],
            ['<Product: Burger>']
        )

    def test_product_list_template_is_used(self):
        response = self.client.get(reverse('shop:product:list'))
        self.assertTemplateUsed(response, 'shop/product/list.html')
