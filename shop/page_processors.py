from mezzanine.pages.page_processors import processor_for

from cart.forms import CartAddProductForm

from .models import Menu

@processor_for(Menu)
def cart_form(request, page):
    cart_add_form = CartAddProductForm()
    context = {'cart_add_form': cart_add_form}
    return context
