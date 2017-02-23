from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404

from .models import Product


def product_detail(request, slug):
    """
    Detail page for a product.
    """
    queryset = Product.objects.published(for_user=request.user)
    product = get_object_or_404(queryset, slug=slug)
    context = {
        'product': product,
        }
    return render(request, 'shop/product/detail.html', context)
