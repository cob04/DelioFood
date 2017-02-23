from django.db.models.signals import post_save
from django.dispatch import receiver

from . import models


@receiver(post_save, sender=models.ProductImage)
def save_default_product_image(sender, instance, created, **kwargs):
    """
    Save the product afresh each time a product image is saved in case
    its the first image on the images list who's filename is saved on the
    product image field and needs updating
    (TODO: limit this to the only the first on the list).
    """
    image = instance
    image.product.save()
