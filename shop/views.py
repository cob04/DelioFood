from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404

from cart.forms import CartAddProductForm

from .models import Product


def product_detail(request, slug):
    """
    Render the product's details.
    """
    queryset = Product.objects.published(for_user=request.user)
    product = get_object_or_404(queryset, slug=slug)
    form = CartAddProductForm(product=product)
    form.helper.form_action = reverse('cart:add',
        kwargs={'product_id': product.id})
    context = {
        'product': product,
        'form': form,
        }

    return render(request, 'shop/product/detail.html', context)


def product_list(request):
    """
    Render the product listing.
    """
    product_list = Product.objects.filter(available=True)
    cart_add_form = CartAddProductForm()
    context = {
        'product_list': product_list,
        'cart_add_form': cart_add_form,
        }

    return render(request, 'shop/product/list.html', context)
