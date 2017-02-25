from django import forms

from crispy_forms.bootstrap import Div
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, ButtonHolder

from .models import Order


class OrderCreationForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone', 'address',
                'directions']

    def __init__(self, *args, **kwargs):
        super(OrderCreationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'order'
        self.helper.form_class='form-horizontal'
        self.helper.label_class='col-sm-2'
        self.helper.field_class='col-sm-8'
        self.helper.layout = Layout(
            Field('first_name',
                placeholder='Your First name here',
                required=True),
            Field('last_name',
                placeholder='Your Last name here',
                required=True),
            Field('email',
                placeholder='Enter your email address',
                required=True),
            Field('phone', placeholder='Enter your phone number'),
            Field('address',
                placeholder='Name of your street, building',
                required=True),
            Field('directions',
                placeholder='Give us directions so we can find you'),
            Div(
                Submit('submit', 'Place Order',
                    css_class='btn btn-action btn-lg'
                ),
                css_class="col-sm-4 col-sm-offset-2"
            )
        )
        self.helper.form_method = 'post'
