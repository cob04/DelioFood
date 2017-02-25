from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.cache import never_cache
from django.views.decorators.http import require_POST
from django.template.response import TemplateResponse

from shop.models import Product, Variation

from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    queryset = Product.objects.published()
    product = get_object_or_404(queryset, id=product_id)

    # check if variation field is in form.
    if request.POST.get('variation'):
        form = CartAddProductForm(request.POST, product=product)
    else:
        form = CartAddProductForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        try:
            variation = cd['variation']
        except KeyError:
            variation = None
        cart.add(product=product,
                    variation=variation,
                    quantity=cd['quantity'],
                    update_quantity=cd['update'],
                    instructions=cd['instructions'])
    return redirect('cart:detail')


def cart_remove(request, variation_id):
    cart = Cart(request)
    variation = get_object_or_404(Variation, id=variation_id)
    cart.remove(variation)
    return redirect('cart:detail')


@never_cache
def cart_detail(request, template='cart/detail.html'):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={'quantity': item['quantity'],
            'update': True})
    context= {'cart': cart}
    return TemplateResponse(request, template, context)
