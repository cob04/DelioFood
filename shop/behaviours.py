from django.db import models


class Priced(models.Model):
    """
    Have a decimal field to represent some money value.
    """
    unit_price = models.DecimalField(max_digits=7, decimal_places=2)

    class meta:
        abstract = True
