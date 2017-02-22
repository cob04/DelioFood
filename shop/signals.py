from django.db.models.signals import post_save
from django.dispatch import receiver

from . import models

@receiver(post_save, sender=models.ProductImage)
def save_default_product_image(sender, instance, created, **kwargs):
    image = instance
    image.product.save()
