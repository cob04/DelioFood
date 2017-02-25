from decimal import Decimal

from django.conf import settings

from shop.models import Product, Variation


class Cart(object):
    """
    Shopping cart object.
    """

    def __init__(self, request):
        """
        Initialize the shopping cart.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session.
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products and
        product variations from the database
        """
        variation_ids = self.cart.keys()
        variations = Variation.objects.filter(id__in=variation_ids)

        for variation in variations:
            self.cart[str(variation.id)]['product'] = variation.product
            self.cart[str(variation.id)]['variation'] = variation

        for item in self.cart.values():
            item['unit_price'] = Decimal(item['unit_price'])
            item['total_price'] = item['unit_price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Sum the quantity of all the items in the shopping cart.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def add(self, product, variation=None, quantity=1,
        update_quantity=False, instructions=None):
        """
        Add a product to the cart or update its quantity.
        """
        variation = variation or product.default_variation
        variation_id = str(variation.id)
        if variation_id not in self.cart:
            self.cart[variation_id] = {
                                    'quantity': 0,
                                    'unit_price': str(variation.unit_price),
                                    'instructions': instructions}
        if update_quantity:
            self.cart[variation_id]['quantity'] = quantity
        else:
            self.cart[variation_id]['quantity'] += quantity
            self.cart[variation_id]['instructions'] = instructions

        self.save()

    def get_total_price(self):
        """
        Calculate the total price of all the items in the shopping cart.
        """
        return sum(Decimal(item['unit_price']) * item['quantity'] for item in
            self.cart.values())

    def remove(self, variation):
        """
        Remove a product (product variation)  from the shopping cart.
        """
        variation_id = str(variation.id)
        if variation_id in self.cart:
            del self.cart[variation_id]
            self.save()

    def clear(self):
        """
        Remove cart from session.
        """
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    def save(self):
        """
        Update the session cart by marking the session as "modified" to
        make sure its saved.
        """
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True
