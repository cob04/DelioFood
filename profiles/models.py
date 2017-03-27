from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Profile(models.Model):
    """
    User profile for additional user related information.
    """
    user = models.OneToOneField("auth.User")
    phone = models.CharField(_("Phone number"), max_length=10)


class Address(models.Model):
    """
    A saved for delivery to made.
    Preferrably for frequent deliveries.
    """
    user = models.ForeignKey("auth.User", related_name="addresses")
    name = models.CharField(_("Name"), max_length=30)
    address = models.CharField(_("Address"), max_length=255,
        help_text="Your physical address.")
    directions = models.TextField(_("Directions"), blank=True,
        help_text="Directions so we can easily find you.")

    class Meta:
        verbose_name = "Delivery Address"
        verbose_name_plural = "Delivery Addresses"
