from __future__ import unicode_literals

import os

from django.core. urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from mezzanine.core.fields import FileField
from mezzanine.core.managers import DisplayableManager
from mezzanine.core.models import (Displayable, Orderable, RichText,
    TimeStamped)
from mezzanine.pages.models import Page
from mezzanine.utils.models import AdminThumbMixin, upload_to

from .behaviours import Priced

@python_2_unicode_compatible
class Product(Displayable, RichText, AdminThumbMixin):
    """
    Product/Service being offered.
    """
    image = models.CharField(_("Image"), max_length=255, blank=True, null=True)
    available = models.BooleanField(default=True)

    objects = DisplayableManager()

    admin_thumb_field = 'image'

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title

    @property
    def default_variation(self):
        try:
            return self.variations.all().first()
        except AttributeError:
            pass
        return None

@python_2_unicode_compatible
class Variation(Orderable, Priced):
    """
    A variation on a product e.g. Size of meal.
    """
    title = models.CharField(max_length=255)
    product = models.ForeignKey('Product',
        related_name='variations',
        null=True,
        blank=True)
    no_of_servings = models.PositiveIntegerField(blank=True, null=True)
    stock = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        verbose_name = 'Product Variation'
        verbose_name_plural = 'Product Variations'

    def __str__(self):
        return "{}: serves {}".format(self.title, self.no_of_servings)
