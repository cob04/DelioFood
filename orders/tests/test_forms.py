from django.test import TestCase

from shop.tests.model_factory import ProductFactory, VariationFactory

from ..forms import OrderCreationForm


class OrderCreationFormTests(TestCase):

    def setUp(self):
        self._product = ProductFactory.create()
        self._product_var1 = VariationFactory.create(
            product=self._product)

    def test_form_with_valid_data(self):
        form = OrderCreationForm({
            'first_name': 'James',
            'last_name': 'Bond',
            'email': 'bond@00.com',
            'phone': '0700007007',
            'address': 'classified',
            'directions': 'Cannot confirm or deny any knowledge',
        })
        # confirm form is valid
        self.assertTrue(form.is_valid())
        order = form.save()
        self.assertEqual(order.first_name, 'James')
        self.assertEqual(order.last_name, 'Bond')
        self.assertEqual(order.email, 'bond@00.com')
        self.assertEqual(order.phone, '0700007007')
        self.assertEqual(order.address, 'classified')
        self.assertEqual(order.directions, 'Cannot confirm or deny any knowledge')

    def test_form_with_blank_data(self):
        form = OrderCreationForm({})
        self.assertFalse(form.is_valid())
