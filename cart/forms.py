from django import forms
from django.core.urlresolvers import reverse

from crispy_forms.bootstrap import InlineField, Div, StrictButton
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

from shop.models import Product

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 4)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
                choices=PRODUCT_QUANTITY_CHOICES,
                coerce=int)
    update = forms.BooleanField(
                required=False,
                initial=False,
                widget=forms.HiddenInput)

    instructions = forms.CharField(
            required=False,
            widget=forms.Textarea(attrs={'row':'4'}))

    def __init__(self, *args, **kwargs):
        self._product = kwargs.pop('product', None)
        super(CartAddProductForm, self).__init__(*args, **kwargs)
        if self._product:
            self.fields['variation'] = forms.ModelChoiceField(
                queryset=self._product.variations.all()
            )
            self.fields['variation'].label="Select Option"
        self.fields['quantity'].label="No of Platters."
        self.fields['instructions'].label="Additional information"
        self.helper = FormHelper()
        self.helper.form_id='cart_add'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-sm-4'
        self.helper.field_class = 'col-sm-6'
        self.helper.layout = Layout(
            Div(
                Field('variation'),
                css_class='row',
            ),
            Div(
                Field('quantity'),
                css_class='row',
            ),
            Div(
                Field('instructions',
                    placeholder="Indicate any addtional instructions and"
                        " dietary restrictions here.",
                    rows=4),
                css_class="row",
            ),
            Submit('Submit', 'Order Now', css_class='btn btn-lg btn-action'),
        )
        self.helper.form_method = 'post'
