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

    def save(self, *args, **kwargs):
        self.image = self.get_default_image_name()
        super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('shop:product:detail', kwargs={'slug': self.slug})

    @property
    def default_variation(self):
        """
        Return the first variation related to a product.
        """
        try:
            return self.variations.all().first()
        except AttributeError:
            pass
        return None

    @property
    def price(self):
        """
        Return the price of the default variation
        (the first variation in the list).
        """
        if self.default_variation:
            return self.default_variation.unit_price
        return None

    def get_default_image_name(self):
        """
        Return the name of the first image in the images list.
        """
        try:
            image = self.images.all().first().image
            return image.name
        except AttributeError:
            pass
        return ''


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


@python_2_unicode_compatible
class ProductImage(TimeStamped, Orderable):
    """
    Product photos.
    """
    image = FileField(_("Image"), max_length=255, format="Image",
        upload_to=upload_to("shop.ProductImage.file", "products"))
    caption = models.CharField(_("Caption"), max_length=255, blank=True)
    product = models.ForeignKey("Product", related_name="images")

    class Meta:
        verbose_name = _("Image")
        verbose_name_plural = _("Images")

    def __str__(self):
        value = self.caption
        if not value:
            path = self.image.name
            _other_part, value = os.path.split(path)
        return value


@python_2_unicode_compatible
class Menu(Page):
    """
    Grouping Products together under a package.
    """
    cover_image = FileField(_("Cover image"), max_length=255, format="Image",
        upload_to=upload_to("shop.Menu.cover_image", "cover_images"))

    class Meta:
        verbose_name = 'Delio Menu'
        verbose_name_plural = 'Delio Menus'

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class MenuItem(Orderable):
    """
    A product listed in a Menu.
    """
    product = models.ForeignKey('Product', related_name='products')
    menu = models.ForeignKey('Menu', related_name='items')

    def __str__(self):
        return self.product.title
