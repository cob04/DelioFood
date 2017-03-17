from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


class Location(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    overview = models.TextField(_("Overview"))

    class Meta:
        verbose_name = "Delivery Location"
        verbose_name_plural = "Delivery Locations"

    def __str__(self):
        return self.name
