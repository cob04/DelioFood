from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from mezzanine.core.models import TimeStamped

from shop.models import Product, Variation


@python_2_unicode_compatible
class Order(TimeStamped):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    directions = models.TextField()
    paid = models.BooleanField(default=False,
                    help_text="Checked if payment is complete and in full")

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return '{}: {}'.format(self.id, self.billing_name())

    def billing_name(self):
        """
        Contactenate the first and last names into one name.
        """
        return '{} {}'.format(self.first_name, self.last_name)

    def get_total_cost(self):
        """
        Calculate the cost of all items in an order.
        """
        return sum(item.get_cost() for item in self.items.all())

    @property
    def total_cost(self):
        """
        Prepend currency symbol on the total cost of the order.
        """
        return 'Ksh {}'.format(self.get_total_cost())


@python_2_unicode_compatible
class OrderItem(models.Model):
    order = models.ForeignKey('Order', related_name='items')
    product = models.ForeignKey(Product, related_name='order_items')
    variation = models.CharField(max_length=100)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    instructions = models.TextField(blank=True)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        """
        Calculate the cost of a single order item.
        """
        return self.unit_price * self.quantity
