from django.shortcuts import render

from cart.cart import Cart

from .forms import OrderCreationForm
from .models import OrderItem


def order_create(request):
    """
    Save the items in shopping cart to the database as an order.
    """
    context = {}
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreationForm(request.POST)
        if form.is_valid() and len(cart):
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    variation=item['variation'],
                    unit_price=item['unit_price'],
                    quantity=item['quantity'],
                    instructions=item['instructions'])
            # clear the cart
            cart.clear()
            context['order'] = order
        return render(request, 'orders/order/created.html', context)
    else:
        form = OrderCreationForm()
        context['form'] = form
        context['cart'] = cart
    return render(request, 'orders/order/create.html', context)
