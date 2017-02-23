from django.db import models


class Priced(models.Model):
    """
    Abstract model with unit price
    """
    unit_price = models.DecimalField(max_digits=7, decimal_places=2)

    class meta:
        abstract = True
