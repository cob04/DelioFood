import factory


from ..models import (Product, Variation)


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
