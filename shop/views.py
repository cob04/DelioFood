from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404

from .models import Product


def product_detail(request, slug):
    """
    Render the product's details.
    """
    queryset = Product.objects.published(for_user=request.user)
    product = get_object_or_404(queryset, slug=slug)
    context = {
        'product': product,
        }
    return render(request, 'shop/product/detail.html', context)


def product_list(request):
    """
    Render the product listing.
    """
    product_list = Product.objects.filter(available=True)
    context = {'product_list': product_list}
    return render(request, 'shop/product/list.html', context)
