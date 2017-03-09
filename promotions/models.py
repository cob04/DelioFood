from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from mezzanine.core.models import Orderable
from mezzanine.core.fields import FileField

from mezzanine.utils.models import upload_to


class HomePage(models.Model):
    """
    The website homepage content to be saved in the database.
    """
    class Meta:
        verbose_name = 'Home Page'
        verbose_name_plural = 'Home Page'

    pass


class Slide(Orderable):
    """
    A carousel slide
    """
    image = FileField(_("Image"), max_length=255, format="Image",
        upload_to=upload_to("promotions.Slide.file", "promotions"))
    page = models.ForeignKey('HomePage', related_name='slides')

    class Meta:
        verbose_name = 'slide'

    @property
    def index(self):
        return self._order or 0
