import factory
import tempfile

from django.core.files import File

from ..models import (Product, ProductImage, Variation, Package, PackageItem)


class ProductFactory(factory.DjangoModelFactory):

    class Meta:
        model = Product

    title = 'Burger'
    description = 'Cheese Burger'


class VariationFactory(factory.DjangoModelFactory):

    class Meta:
        model = Variation

    product = factory.SubFactory(ProductFactory)
    title = 'Medium'
    no_of_servings = 5
    unit_price = 250
    stock = 5

# generate temporary file for testing.
def get_test_image_file():
    from django.core.files.images import ImageFile
    file = tempfile.NamedTemporaryFile(suffix='.jpg')
    return ImageFile(file, name=file.name)

class ProductImageFactory(factory.DjangoModelFactory):

    class Meta:
        model = ProductImage

    image = get_test_image_file()
    product = factory.SubFactory(ProductFactory)

class PackageFactory(factory.DjangoModelFactory):

    class Meta:
        model = Package

    title = 'DelioRibs'
    description = 'ribs ribs ribs'
    cover_image = get_test_image_file()

class PackageItemFactory(factory.DjangoModelFactory):

    class Meta:
        model = PackageItem

    product = factory.SubFactory(ProductFactory)
    package = factory.SubFactory(PackageFactory)
