from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from mezzanine.core.models import Displayable, Orderable


class FAQ(Orderable):
    question = models.CharField(_("Question"), max_length=255)
    answer = models.TextField(_("Answer"))
