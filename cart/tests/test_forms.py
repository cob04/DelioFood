from django.test import TestCase

from ..forms import CartAddProductForm

# Reuse model factories from shop app.
from shop.tests.model_factory import ProductFactory, VariationFactory


class CartProductAddFormTests(TestCase):

    def setUp(self):
        self._product = ProductFactory.create()
        self._product_var1 = VariationFactory.create(
            product=self._product)

    def test_form_with_valid_data(self):
        form = CartAddProductForm({
            'quantity': 2,
            'update': False,
            'instructions': 'hello There',
            'variation': self._product_var1,
        }, product=self._product)
        # confirm form is valid
        self.assertTrue(form.is_valid())
        cd = form.cleaned_data
        self.assertEqual(cd['quantity'], 2)
        self.assertEqual(cd['update'], False)
        self.assertEqual(cd['instructions'], "hello There")
        self.assertEqual(cd['variation'], self._product_var1)

    def test_form_with_blank_data(self):
        form = CartAddProductForm({}, product=self._product)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'quantity': ['This field is required.'],
            'variation': ['This field is required.'],
        })

    def test_dynamic_field_addition_with_product_instance(self):
        form = CartAddProductForm(product=self._product)
        self.assertTrue(form.fields['variation'])

    def test_dynamic_field_not_added_with_no_product_instance(self):
        form = CartAddProductForm()
        with self.assertRaises(KeyError):
            form.fields['variation']
